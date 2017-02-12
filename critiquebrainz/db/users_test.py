from critiquebrainz.data.testing import DataTestCase
from critiquebrainz.db.user import User
from critiquebrainz.data import db
import critiquebrainz.db.users as db_users
from critiquebrainz.db.users import gravatar_url, get_many_by_mb_username
from critiquebrainz.data.model.review import Review
from critiquebrainz.data.model.license import License
import critiquebrainz.db.vote as db_vote
from datetime import datetime, date, timedelta
from uuid import UUID

class UserTestCase(DataTestCase):
    def setUp(self):
        super(UserTestCase, self).setUp()
        self.user1 = User(db_users.get_or_create("test", musicbrainz_id='tester_1'))
        self.user2 = User(db_users.get_or_create("test1", musicbrainz_id="тестер"))
        self.author = User(db_users.get_or_create("Author1", musicbrainz_id="author1"))
        license = License(id='Test', full_name='Test License')
        db.session.add(license)
        db.session.commit()
        self.review = Review.create(release_group='e7aad618-fa86-3983-9e77-405e21796eca',
                               text="Testing!",
                               user_id=self.author.id,
                               is_draft=False,
                               license_id=license.id)
        vote = db_vote.submit(self.user1.id, self.review.last_revision.id, True)
        self.review_created = self.review.last_revision.timestamp
        self.review_id = self.review.id

    def test_get_many_by_mb_username(self):
        users = [self.user1.musicbrainz_id, self.user2.musicbrainz_id]
        dbresults = get_many_by_mb_username(users)
        dbresults = [user["musicbrainz_id"] for user in dbresults]
        self.assertEqual(users, dbresults)
        self.assertEqual(get_many_by_mb_username([]), [])

    def test_avatar(self):
        self.assertEqual(
            gravatar_url("test2"),
            "https://gravatar.com/avatar/ad0234829205b9033196ba818f7a872b?d=identicon&r=pg"
        )

    def test_get_by_id(self):
        user = db_users.get_by_id(self.user1.id)
        self.assertEqual(user['display_name'], "test")
        self.assertEqual(user['musicbrainz_id'], "tester_1")

    def test_users_list(self):
        users = db_users.list()
        self.assertEqual(len(users), 3)

        users = db_users.list(0, 10)
        self.assertEqual(len(users), 0)

        user3 = db_users.get_or_create("test2", "user_1")
        users = db_users.list(1, 1)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['display_name'], "test1")

    def test_get_count(self):
        count = db_users.get_count()
        self.assertEqual(count, 3)

        user3 = db_users.get_or_create("test2", "user_1")
        count = db_users.get_count()
        self.assertEqual(count, 4)

    def test_get_by_mbid(self):
        user = db_users.get_by_mbid("tester_1")
        self.assertEqual(user['display_name'], "test")

    def test_create(self):
        user = db_users.create("test_user", email="foo@foo.com", musicbrainz_id="tester2")
        self.assertEqual(user['email'], "foo@foo.com")
        self.assertEqual(type(user['id']), UUID)
        self.assertEqual(user['is_blocked'], False)

    def test_vote(self):
        voted = db_users.has_voted(self.user1.id, self.review.id)
        self.assertEqual(voted, True)
        voted = db_users.has_voted(self.user2.id, self.review.id)
        self.assertEqual(voted, False)

    def test_karma(self):
        karma = db_users.karma(self.author.id)
        self.assertEqual(karma, 1)
        karma = db_users.karma(self.user2.id)
        self.assertEqual(karma, 0)

    def test_reviews(self):
        review = db_users.reviews(self.author.id)[0]
        self.assertEqual(review['license_id'], 'Test')
        self.assertEqual(type(review['user_id']), UUID)
        self.assertEqual(str(review['user_id']), self.author.id)

    def test_votes_since(self):
        votes = db_users.get_votes(self.user1.id)
        self.assertEqual(len(votes), 1)
        two_days_from_now = date.today() + timedelta(days=2)
        votes = db_users.get_votes(self.user1.id, two_days_from_now)
        self.assertEqual(len(votes), 0)

    def test_review_since(self):
        reviews = db_users.get_reviews(self.author.id)
        self.assertEqual(len(reviews), 1)
        self.review.update(text="Testing Again")
        reviews = db_users.get_reviews(self.author.id)
        self.assertEqual(len(reviews), 1)
        self.assertEqual(reviews[0]['creation_time'], self.review_created)
        two_days_from_now = date.today() + timedelta(days=2)
        reviews = db_users.get_reviews(self.author.id, two_days_from_now)
        self.assertEqual(len(reviews), 0)

    def test_update(self):
        db_users.update(self.user1, email='foo@foo.com')
        user1 = db_users.get_by_id(self.user1.id)
        self.assertEqual(user1['email'], 'foo@foo.com')

    def test_delete(self):
        db_users.delete(self.author.id)
        # Review should not exist
        reviews = db_users.get_reviews(self.author.id)
        self.assertEqual(len(reviews), 0)
        db_users.delete(self.user1.id)
        # Votes should be deleted as well
        votes = db_users.get_votes(self.user1.id)
        self.assertEqual(len(votes), 0)


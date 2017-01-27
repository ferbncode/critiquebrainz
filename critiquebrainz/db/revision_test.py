from critiquebrainz.data.testing import DataTestCase
from critiquebrainz.data import db
from critiquebrainz.data.model.revision import Revision
from critiquebrainz.data.model.review import Review
from critiquebrainz.data.model.license import License
from critiquebrainz.db import exceptions
from critiquebrainz.db import revision
from datetime import datetime
from uuid import UUID


class RevisionTestCase(DataTestCase):

    def setUp(self):
        super(RevisionTestCase, self).setUp()

        self.user = User(dispaly_name=u'Tester')
        db.session.add(self.user)
        db.session.commit()

        self.license = Liscense(id=u'TEST', full_name=u"Test License")
        db.session.add(self.license)
        db.session.commit()

        self.review = Review.create(user=self.user,
                                    release_group='e7aad618-fa86-3983-9e77-405e21796eca',
                                    text=u"Testing!",
                                    is_draft=False,
                                    license_id=self.license.id)

        def test_get(self):
            """Test the get function that gets revisions for the test review, optionally ordered by the timestamp"""

            review_id = self.review.id
            first_revision = revision.get(review_id)[0]
            self.assertEqual(first_revision.text, "Testing!")
            self.assertEqual(first_revision.review_id, self.review.id)
            self.assertEqual(type(first_revision.timestamp, datetime))
            self.assertEqual(type(first_revision.id, int))






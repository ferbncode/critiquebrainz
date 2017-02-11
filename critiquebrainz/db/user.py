from critiquebrainz.data.model.mixins import DeleteMixin, AdminMixin
import critiquebrainz.db.users as db_user
import hashlib
from critiquebrainz.data.constants import user_types
import critiquebrainz.db.users as db_user
# def has_voted(user_id, review_id):
# def review_limit_exceeded(user) # def vote_limit_exceeded(user)
# get_karma() understand
# de


class User(AdminMixin, DeleteMixin):

    def __init__(self, user):
        self.id = str(user.get('id'))
        self.display_name = user.get('display_name')
        self.email = user.get('email')
        self.created = user.get('created')
        self.musicbrainz_id = user.get('musicbrainz_id')
        self.show_gravatar = user.get('show_gravatar')
        self.is_blocked = user.get('is_blocked')

    @property
    def avatar(self):
        """Link to user's avatar image."""
        if self.show_gravatar and self.email:
            return "https://gravatar.com/avatar/" + hashlib.md5(self.mail.encode("utf-8")).hexdigest() + "?d=identicon&r=pg"
        else:
            return "https://gravatar.com/avatar/" + hashlib.md5(self.id.encode("utf-8")).hexdigest() + "?d=identicon"


    @property
    def karma(self):
        if hasattr(self, '_karma') is False:
            self._karma = db_user.karma(self.id)
        return self._karma


    @property
    def user_type(self):
        def get_user_type(user):
            for user_type in user_types:
                if user_type.is_instance(user):
                    return user_type
        if hasattr(self, '_user_type') is False:
            self._user_type = get_user_type(self)
        return self._user_type

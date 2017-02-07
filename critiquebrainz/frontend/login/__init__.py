"""
Package login provides authentication functionality for CritiqueBrainz.

It is based on OAuth2 protocol. MusicBrainz is the only supported provider.
"""
from flask import redirect, url_for
from flask_login import LoginManager, current_user
from flask_babel import lazy_gettext, gettext
# from critiquebrainz.data.model.user import User
from critiquebrainz.data.model.mixins import AnonymousUser, AdminMixin, DeleteMixin
import critiquebrainz.db.users as db_user
from werkzeug.exceptions import Unauthorized
from functools import wraps

mb_auth = None

login_manager = LoginManager()
login_manager.login_view = 'login.index'
login_manager.login_message = gettext("Please sign in to access this page.")
login_manager.localize_callback = gettext
login_manager.anonymous_user = AnonymousUser

class User(AdminMixin, DeleteMixin):
    def __init__(self, user):
        self.id = user['id']
        self.display_name = user['display_name']
        self.email = user['email']
        self.created = user['created']
        self.musicbrainz_id = user['musicbrainz']

    @classmethod
    def from_dbrow(cls, user):
        return User(user)


@login_manager.user_loader
def load_user(user_id):
    user = db_user.get(user_id)
    if user:
        return User.from_dbrow(user)
    else:
        return None

def login_forbidden(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if current_user.is_anonymous is False:
            return redirect(url_for('frontend.index'))
        return f(*args, **kwargs)

    return decorated


def admin_view(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_admin():
            raise Unauthorized(lazy_gettext('You must be an administrator to view this page.'))
        return f(*args, **kwargs)

    return decorated

from flask import Blueprint, render_template, request
from flask_login import current_user
from flask_babel import gettext
import critiquebrainz.frontend.external.musicbrainz_db.place as mb_place
import critiquebrainz.frontend.external.musicbrainz_db.exceptions as mb_exceptions
import critiquebrainz.db.review as db_review
from werkzeug.exceptions import NotFound

place_bp = Blueprint('place', __name__)


@place_bp.route('/<uuid:id>')
def entity(id):
    id = str(id)
    try:
        place = mb_place.get_place_by_id(id)
    except mb_exceptions.NoDataFoundException:
        raise NotFound(gettext("Sorry, we couldn't find a place with that MusicBrainz ID."))

    if current_user.is_authenticated:
        my_reviews, my_count = db_review.list_reviews(entity_id=id, entity_type='place', user_id=current_user.id)
        if my_count != 0:
            my_review = my_reviews[0]
        else:
            my_review = None
    else:
        my_review = None

    limit = int(request.args.get('limit', default=10))
    offset = int(request.args.get('offset', default=0))
    reviews, count = db_review.list_reviews(entity_id=id, entity_type='place', sort='rating', limit=limit, offset=offset)

    return render_template('place/entity.html', id=id, place=place, reviews=reviews,
                           my_review=my_review, limit=limit, offset=offset, count=count)

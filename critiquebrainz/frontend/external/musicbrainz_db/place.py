from mbdata.models import Place
from critiquebrainz.frontend.external.musicbrainz_db import mb_session
from critiquebrainz.frontend.external.musicbrainz_db.includes import check_includes
from brainzutils import cache


DEFAULT_CACHE_EXPIRATION = 12 * 60 * 60 # seconds (12 hours)
THREAD_POOL_PROCESSES = 10


def get_place_by_id(id):
    key = cache.gen_key(id)
    place = cache.get(key)
    place = None
    if not place:
        place = _get_place_by_id(
            id, ['artist-rels', 'place-rels', 'release_group-rels', 'url-rels'],
        )
    place = place.name
    # Work to convert into dict so that it can go into cache
    cache.set(key=key, val=place, time=DEFAULT_CACHE_EXPIRATION)
    return place


def _get_place_by_id(id, includes=[]):

    # Validate includes
    check_includes('place', includes)
    with mb_session() as session:
        place = session.query(Place).filter_by(gid=id).first()
    # rest of the work
    return place

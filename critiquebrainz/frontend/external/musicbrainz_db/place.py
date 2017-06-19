import critiquebrainz.frontend.external.musicbrainz_db as mb
from critiquebrainz.frontend.external.musicbrainz_db.includes import check_includes
from critiquebrainz.frontend.external.musicbrainz_db.helpers import entity_relation_helper
import critiquebrainz.frontend.external.musicbrainz_db.exceptions as mb_exceptions
from brainzutils import cache
from critiquebrainz.utils import dict_uuids_to_str
import sqlalchemy
from ast import literal_eval as make_tuple


DEFAULT_CACHE_EXPIRATION = 12 * 60 * 60 # seconds (12 hours)
THREAD_POOL_PROCESSES = 10


def get_place_by_id(id):
    """Get information related to place using ID."""
    key = cache.gen_key(id)
    place = cache.get(key)
    if not place:
        place = _get_place_by_id(
            id, ['artist-rels', 'place-rels', 'release-group-rels', 'url-rels'],
        )
    cache.set(key=key, val=place, time=DEFAULT_CACHE_EXPIRATION)
    return place


def _get_place_by_id(id, includes=[]):
    """Get place info from MusicBrainz database"""

    # Validate includes
    check_includes('place', includes)
    place = {}
    with mb.engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("""
            SELECT place.gid AS id,
                   pt.name AS type,
                   place.name,
                   coordinates,
                   address,
                   area.id AS area_id,
                   area.name AS area_name
              FROM place
         LEFT JOIN area
                ON area.id = place.area
         LEFT JOIN place_type pt
                ON place.type = pt.id
             WHERE place.gid = :id
        """), {
            'id': id,
        })
        place = result.fetchone()
    if not place:
        raise mb_exceptions.NoDataFoundException("Can't find a place with ID: {id}".format(id=id))
    place = dict_uuids_to_str(dict(place))
    place['coordinates'] = make_tuple(place['coordinates'])

    if 'artist-rels' in includes:
        place['artist-rels'] = entity_relation_helper(
            id, 'artist-rels', relationship='l_artist_place', entity_type='place', is_linked_entity_first=True
        )
    if 'place-rels' in includes:
        place['place-rels'] = entity_relation_helper(
            id, 'place-rels', relationship='l_place_place', entity_type='place', is_linked_entity_first=True
        )
    if 'url-rels' in includes:
        place['url-rels'] = entity_relation_helper(
            id, 'url-rels', relationship='l_place_url', entity_type='place', is_linked_entity_first=False
        )
    return place

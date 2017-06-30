from mbdata import models
from mbdata.utils import get_something_by_gid
from critiquebrainz.frontend.external.musicbrainz_db import mb_session
from critiquebrainz.frontend.external.musicbrainz_db.includes import check_includes
import critiquebrainz.frontend.external.musicbrainz_db.exceptions as mb_exceptions
from critiquebrainz.frontend.external.musicbrainz_db.serialize import to_dict_places
from critiquebrainz.frontend.external.musicbrainz_db.helpers import entity_relation_helper
from brainzutils import cache


DEFAULT_CACHE_EXPIRATION = 12 * 60 * 60 # seconds (12 hours)


def get_release_group_by_id(mbid):
    """Get release group with the MusicBrainz ID"""
    key = cache.gen_key(id)
    release_group = cache.get(key)
    if not release_group:
        release_group = _get_release_group_by_id(
            mbid, ['artists', 'releases', 'release-group-rels', 'url-rels', 'work-rels', 'tags'],
        )
    cache.set(key=key, val=release_group, time=DEFAULT_CACHE_EXPIRATION)
    return release_group


def _get_release_group_by_id(release_group_id, includes=[]):
    includes_data = {}
    check_includes('release_group', includes)
    with mb_session() as db:
        query = db.query(models.ReleaseGroup)
        release_group = get_something_by_gid(query, models.ReleaseGroupGIDRedirect, release_group_id)
        if release_group:
            raise mb_exceptions.NoDataFoundException("Couldn't find a release group with id: {release_group_id}".format(release_group_id=release_group_id))
    print(release_group)
    return release_group

from critiquebrainz.frontend.external.musicbrainz_db.testing import MBDatabaseTestCase
from critiquebrainz.frontend.external.musicbrainz_db import release_group as mb_release_group


class ReleaseGroupTestCase(MBDatabaseTestCase):

    def test_get_by_id(self):
        release_group = mb_release_group.get_release_group_by_id(
            'baca4e84-aa67-3ef9-adbe-0dfebe7b6a82'
        )
        print(release_group)
        self.assertEqual(release_group["id"], "baca4e84-aa67-3ef9-adbe-0dfebe7b6a82")
        self.assertEqual(release_group["title"], "Trentemøller: The Pølar Mix")


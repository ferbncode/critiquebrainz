from critiquebrainz.frontend.external.musicbrainz_db.testing import MBDatabaseTestCase
from critiquebrainz.frontend.external.musicbrainz_db import place as mb_place


class PlaceTestCase(MBDatabaseTestCase):

    def test_get_by_id(self):

        place = mb_place.get_place_by_id(
            'd71ffe38-5eaf-426b-9a2e-e1f21bc84609',
        )
        self.assertEqual(place['name'], 'Suisto')
        self.assertEqual(place['type'], 'Venue')
        self.assertDictEqual(place['coordinates'], {
            'latitude': 60.997758,
            'longitude': 24.477142
        })
        self.assertDictEqual(place["area"], {
            'id': '4479c385-74d8-4a2b-bdab-f48d1e6969ba',
            'name': 'Hämeenlinna',
        })

    def test_fetch_multiple_places(self):
        places = mb_place.fetch_multiple_places(
            mbids=['d71ffe38-5eaf-426b-9a2e-e1f21bc84609', 'bd55aeb7-19d1-4607-a500-14b8479d3fed'],
            includes=['artist-rels', 'place-rels', 'release-group-rels', 'url-rels'],
        )
        self.assertEqual(len(places), 2)
        self.assertEqual(places['bd55aeb7-19d1-4607-a500-14b8479d3fed']['name'], 'Abbey Road Studios')
        self.assertEqual(places['d71ffe38-5eaf-426b-9a2e-e1f21bc84609']['name'], 'Suisto')

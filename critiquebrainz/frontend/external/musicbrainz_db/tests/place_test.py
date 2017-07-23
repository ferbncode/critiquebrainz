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
        # Check if the place-rels are fetched (Part of)
        self.assertEqual(place["place-rels"][0]["direction"], "backward")
        self.assertEqual(place["place-rels"][0]["place"]["name"], "Verkatehdas")


    def test_fetch_multiple_places(self):
        places = mb_place.fetch_multiple_places(
            mbids=['d71ffe38-5eaf-426b-9a2e-e1f21bc84609', 'f9587914-8505-4bd1-833b-16a3100a4948'],
            includes=['artist-rels', 'place-rels', 'release-group-rels', 'url-rels'],
        )
        self.assertEqual(len(places), 2)
        self.assertEqual(places['d71ffe38-5eaf-426b-9a2e-e1f21bc84609']['name'], 'Suisto')
        self.assertEqual(places['f9587914-8505-4bd1-833b-16a3100a4948']['name'], 'Verkatehdas')

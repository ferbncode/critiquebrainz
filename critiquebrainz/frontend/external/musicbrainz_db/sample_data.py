import datetime
from mbdata.models import Area, AreaType, Artist, ArtistCredit, ArtistCreditName
from mbdata.models import ArtistIPI, ArtistISNI, ArtistMeta, ArtistType, Event
from mbdata.models import EventMeta, EventType, Gender, ISO31661, ISO31662
from mbdata.models import Link, LinkAreaArea, LinkReleaseGroupURL, LinkType, Place
from mbdata.models import PlaceType, ReleaseGroup, ReleaseGroupMeta, ReleaseGroupPrimaryType, URL


def create_sample_data(session):
    eventmeta_1 = EventMeta()
    session.add(eventmeta_1)

    eventtype_festival = EventType()
    eventtype_festival.id = 2
    eventtype_festival.name = 'Festival'
    eventtype_festival.child_order = 2
    eventtype_festival.description = 'An event where a number of different acts perform across the course of the day. Larger festivals may be spread across multiple days.'
    eventtype_festival.gid = 'b6ded574-b592-3f0e-b56e-5b5f06aa0678'
    session.add(eventtype_festival)

    event_taubertal_festival_2004_day_1 = Event()
    event_taubertal_festival_2004_day_1.id = 1607
    event_taubertal_festival_2004_day_1.gid = 'ebe6ce0f-22c0-4fe7-bfd4-7a0397c9fe94'
    event_taubertal_festival_2004_day_1.name = 'Taubertal-Festival 2004, Day 1'
    event_taubertal_festival_2004_day_1.begin_date_year = 2004
    event_taubertal_festival_2004_day_1.begin_date_month = 8
    event_taubertal_festival_2004_day_1.begin_date_day = 13
    event_taubertal_festival_2004_day_1.end_date_year = 2004
    event_taubertal_festival_2004_day_1.end_date_month = 8
    event_taubertal_festival_2004_day_1.end_date_day = 13
    event_taubertal_festival_2004_day_1.cancelled = False
    event_taubertal_festival_2004_day_1.setlist = ''
    event_taubertal_festival_2004_day_1.comment = ''
    event_taubertal_festival_2004_day_1.edits_pending = 0
    event_taubertal_festival_2004_day_1.last_updated = datetime.datetime(2016, 5, 13, 21, 24, 52, 37707)
    event_taubertal_festival_2004_day_1.ended = True
    event_taubertal_festival_2004_day_1.meta = eventmeta_1
    event_taubertal_festival_2004_day_1.type = eventtype_festival
    session.add(event_taubertal_festival_2004_day_1)

    areatype_district = AreaType()
    areatype_district.id = 5
    areatype_district.name = 'District'
    areatype_district.child_order = 5
    areatype_district.description = 'District is used for a division of a large city, e.g. Queens.'
    areatype_district.gid = '84039871-5e47-38ca-a66a-45e512c8290f'
    session.add(areatype_district)

    area_st_john_s_wood = Area()
    area_st_john_s_wood.id = 66431
    area_st_john_s_wood.gid = '57296e85-ed07-4d79-88ef-7b70d23acf8d'
    area_st_john_s_wood.name = "St John's Wood"
    area_st_john_s_wood.edits_pending = 0
    area_st_john_s_wood.last_updated = datetime.datetime(2013, 11, 6, 22, 54, 51, 28274)
    area_st_john_s_wood.ended = False
    area_st_john_s_wood.comment = ''
    area_st_john_s_wood.type = areatype_district
    session.add(area_st_john_s_wood)

    iso31662_1 = ISO31662()
    iso31662_1.code = 'GB-WSM'
    session.add(iso31662_1)

    areatype_subdivision = AreaType()
    areatype_subdivision.id = 2
    areatype_subdivision.name = 'Subdivision'
    areatype_subdivision.child_order = 2
    areatype_subdivision.description = 'Subdivision is used for the main administrative divisions of a country, e.g. California, Ontario, Okinawa. These are considered when displaying the parent areas for a given area.'
    areatype_subdivision.gid = 'fd3d44c5-80a1-3842-9745-2c4972d35afa'
    session.add(areatype_subdivision)

    area_westminster = Area()
    area_westminster.id = 3906
    area_westminster.gid = '48d08ee1-db45-4566-bb1d-c47ab6dbaf98'
    area_westminster.name = 'Westminster'
    area_westminster.edits_pending = 0
    area_westminster.last_updated = datetime.datetime(2013, 5, 21, 14, 51, 57, 923559)
    area_westminster.ended = False
    area_westminster.comment = ''
    area_westminster.iso_3166_2_codes = [
        iso31662_1,
    ]
    area_westminster.type = areatype_subdivision
    session.add(area_westminster)

    areatype_city = AreaType()
    areatype_city.id = 3
    areatype_city.name = 'City'
    areatype_city.child_order = 3
    areatype_city.description = 'City is used for settlements of any size, including towns and villages.'
    areatype_city.gid = '6fd8f29a-3d0a-32fc-980d-ea697b69da78'
    session.add(areatype_city)

    area_london = Area()
    area_london.id = 1178
    area_london.gid = 'f03d09b3-39dc-4083-afd6-159e3f0d462f'
    area_london.name = 'London'
    area_london.edits_pending = 0
    area_london.last_updated = datetime.datetime(2013, 5, 24, 0, 4, 48, 706550)
    area_london.ended = False
    area_london.comment = ''
    area_london.type = areatype_city
    session.add(area_london)

    iso31662_2 = ISO31662()
    iso31662_2.code = 'GB-ENG'
    session.add(iso31662_2)

    area_england = Area()
    area_england.id = 432
    area_england.gid = '9d5dd675-3cf4-4296-9e39-67865ebee758'
    area_england.name = 'England'
    area_england.edits_pending = 0
    area_england.last_updated = datetime.datetime(2013, 5, 18, 0, 11, 46, 530087)
    area_england.ended = False
    area_england.comment = ''
    area_england.iso_3166_2_codes = [
        iso31662_2,
    ]
    area_england.type = areatype_subdivision
    session.add(area_england)

    iso31661_1 = ISO31661()
    iso31661_1.code = 'GB'
    session.add(iso31661_1)

    areatype_country = AreaType()
    areatype_country.id = 1
    areatype_country.name = 'Country'
    areatype_country.child_order = 1
    areatype_country.description = 'Country is used for areas included (or previously included) in ISO 3166-1, e.g. United States.'
    areatype_country.gid = '06dd0ae4-8c74-30bb-b43d-95dcedf961de'
    session.add(areatype_country)

    area_united_kingdom = Area()
    area_united_kingdom.id = 221
    area_united_kingdom.gid = '8a754a16-0027-3a29-b6d7-2b40ea0481ed'
    area_united_kingdom.name = 'United Kingdom'
    area_united_kingdom.edits_pending = 0
    area_united_kingdom.last_updated = datetime.datetime(2013, 5, 16, 11, 6, 19, 672350)
    area_united_kingdom.ended = False
    area_united_kingdom.comment = ''
    area_united_kingdom.iso_3166_1_codes = [
        iso31661_1,
    ]
    area_united_kingdom.type = areatype_country
    session.add(area_united_kingdom)

    linktype_part_of = LinkType()
    linktype_part_of.id = 356
    linktype_part_of.child_order = 0
    linktype_part_of.gid = 'de7cc874-8b1b-3a05-8272-f3834c968fb7'
    linktype_part_of.entity_type0 = 'area'
    linktype_part_of.entity_type1 = 'area'
    linktype_part_of.name = 'part of'
    linktype_part_of.description = 'Designates that one area is contained by another.'
    linktype_part_of.link_phrase = 'parts'
    linktype_part_of.reverse_link_phrase = 'part of'
    linktype_part_of.long_link_phrase = 'has part'
    linktype_part_of.priority = 0
    linktype_part_of.last_updated = datetime.datetime(2014, 11, 13, 1, 8, 49, 651356)
    linktype_part_of.is_deprecated = False
    linktype_part_of.has_dates = True
    linktype_part_of.entity0_cardinality = 1
    linktype_part_of.entity1_cardinality = 0
    session.add(linktype_part_of)

    link_1 = Link()
    link_1.id = 118734
    link_1.attribute_count = 0
    link_1.created = datetime.datetime(2013, 5, 17, 20, 5, 50, 534145)
    link_1.ended = False
    link_1.link_type = linktype_part_of
    session.add(link_1)

    linkareaarea_4 = LinkAreaArea()
    linkareaarea_4.id = 173
    linkareaarea_4.edits_pending = 0
    linkareaarea_4.last_updated = datetime.datetime(2013, 5, 18, 0, 12, 5, 966838)
    linkareaarea_4.link_order = 0
    linkareaarea_4.entity0_credit = ''
    linkareaarea_4.entity1_credit = ''
    linkareaarea_4.entity0 = area_united_kingdom
    linkareaarea_4.entity1 = area_england
    linkareaarea_4.link = link_1
    session.add(linkareaarea_4)

    linkareaarea_3 = LinkAreaArea()
    linkareaarea_3.id = 964
    linkareaarea_3.edits_pending = 0
    linkareaarea_3.last_updated = datetime.datetime(2013, 5, 19, 20, 29, 59, 930277)
    linkareaarea_3.link_order = 0
    linkareaarea_3.entity0_credit = ''
    linkareaarea_3.entity1_credit = ''
    linkareaarea_3.entity0 = area_england
    linkareaarea_3.entity1 = area_london
    linkareaarea_3.link = link_1
    session.add(linkareaarea_3)

    linkareaarea_2 = LinkAreaArea()
    linkareaarea_2.id = 3672
    linkareaarea_2.edits_pending = 0
    linkareaarea_2.last_updated = datetime.datetime(2013, 5, 21, 15, 55, 43, 356589)
    linkareaarea_2.link_order = 0
    linkareaarea_2.entity0_credit = ''
    linkareaarea_2.entity1_credit = ''
    linkareaarea_2.entity0 = area_london
    linkareaarea_2.entity1 = area_westminster
    linkareaarea_2.link = link_1
    session.add(linkareaarea_2)

    linkareaarea_1 = LinkAreaArea()
    linkareaarea_1.id = 66189
    linkareaarea_1.edits_pending = 0
    linkareaarea_1.last_updated = datetime.datetime(2013, 11, 4, 9, 43, 43, 118925)
    linkareaarea_1.link_order = 0
    linkareaarea_1.entity0_credit = ''
    linkareaarea_1.entity1_credit = ''
    linkareaarea_1.entity0 = area_westminster
    linkareaarea_1.entity1 = area_st_john_s_wood
    linkareaarea_1.link = link_1
    session.add(linkareaarea_1)

    placetype_studio = PlaceType()
    placetype_studio.id = 1
    placetype_studio.name = 'Studio'
    placetype_studio.child_order = 1
    placetype_studio.description = 'A place designed for non-live production of music, typically a recording studio.'
    placetype_studio.gid = '05fa6a09-ff92-3d34-bdbb-5141d3c24f38'
    session.add(placetype_studio)

    place_abbey_road_studios = Place()
    place_abbey_road_studios.id = 775
    place_abbey_road_studios.gid = 'bd55aeb7-19d1-4607-a500-14b8479d3fed'
    place_abbey_road_studios.name = 'Abbey Road Studios'
    place_abbey_road_studios.address = "3 Abbey Road, St John's Wood, London"
    place_abbey_road_studios.coordinates = (51.53192, -0.17835)
    place_abbey_road_studios.comment = ''
    place_abbey_road_studios.edits_pending = 0
    place_abbey_road_studios.last_updated = datetime.datetime(2013, 12, 9, 22, 4, 9, 988010)
    place_abbey_road_studios.begin_date_year = 1931
    place_abbey_road_studios.ended = False
    place_abbey_road_studios.area = area_st_john_s_wood
    place_abbey_road_studios.type = placetype_studio
    session.add(place_abbey_road_studios)

    area_hameenlinna = Area()
    area_hameenlinna.id = 9598
    area_hameenlinna.gid = '4479c385-74d8-4a2b-bdab-f48d1e6969ba'
    area_hameenlinna.name = 'Hämeenlinna'
    area_hameenlinna.edits_pending = 0
    area_hameenlinna.last_updated = datetime.datetime(2013, 11, 26, 12, 59, 48, 472546)
    area_hameenlinna.ended = False
    area_hameenlinna.comment = ''
    area_hameenlinna.type = areatype_city
    session.add(area_hameenlinna)

    iso31662_3 = ISO31662()
    iso31662_3.code = 'FI-06'
    session.add(iso31662_3)

    area_kanta_hame = Area()
    area_kanta_hame.id = 440
    area_kanta_hame.gid = 'dedc20c2-22f9-4c20-9426-470424613679'
    area_kanta_hame.name = 'Kanta-Häme'
    area_kanta_hame.edits_pending = 0
    area_kanta_hame.last_updated = datetime.datetime(2013, 11, 26, 14, 29, 55, 704493)
    area_kanta_hame.ended = False
    area_kanta_hame.comment = ''
    area_kanta_hame.iso_3166_2_codes = [
        iso31662_3,
    ]
    area_kanta_hame.type = areatype_subdivision
    session.add(area_kanta_hame)

    iso31661_2 = ISO31661()
    iso31661_2.code = 'FI'
    session.add(iso31661_2)

    area_finland = Area()
    area_finland.id = 72
    area_finland.gid = '6a264f94-6ff1-30b1-9a81-41f7bfabd616'
    area_finland.name = 'Finland'
    area_finland.edits_pending = 0
    area_finland.last_updated = datetime.datetime(2013, 5, 27, 12, 46, 50, 235044)
    area_finland.ended = False
    area_finland.comment = ''
    area_finland.iso_3166_1_codes = [
        iso31661_2,
    ]
    area_finland.type = areatype_country
    session.add(area_finland)

    linkareaarea_6 = LinkAreaArea()
    linkareaarea_6.id = 200
    linkareaarea_6.edits_pending = 0
    linkareaarea_6.last_updated = datetime.datetime(2013, 5, 18, 20, 41, 42, 56054)
    linkareaarea_6.link_order = 0
    linkareaarea_6.entity0_credit = ''
    linkareaarea_6.entity1_credit = ''
    linkareaarea_6.entity0 = area_finland
    linkareaarea_6.entity1 = area_kanta_hame
    linkareaarea_6.link = link_1
    session.add(linkareaarea_6)

    linkareaarea_5 = LinkAreaArea()
    linkareaarea_5.id = 9364
    linkareaarea_5.edits_pending = 0
    linkareaarea_5.last_updated = datetime.datetime(2013, 6, 12, 5, 30, 6, 560270)
    linkareaarea_5.link_order = 0
    linkareaarea_5.entity0_credit = ''
    linkareaarea_5.entity1_credit = ''
    linkareaarea_5.entity0 = area_kanta_hame
    linkareaarea_5.entity1 = area_hameenlinna
    linkareaarea_5.link = link_1
    session.add(linkareaarea_5)

    placetype_venue = PlaceType()
    placetype_venue.id = 2
    placetype_venue.name = 'Venue'
    placetype_venue.child_order = 2
    placetype_venue.description = 'A place that has live artistic performances as one of its primary functions, such as a concert hall.'
    placetype_venue.gid = 'cd92781a-a73f-30e8-a430-55d7521338db'
    session.add(placetype_venue)

    place_suisto = Place()
    place_suisto.id = 955
    place_suisto.gid = 'd71ffe38-5eaf-426b-9a2e-e1f21bc84609'
    place_suisto.name = 'Suisto'
    place_suisto.address = 'Verkatehtaankuja 7, FI-13200 Hämeenlinna, Finland'
    place_suisto.coordinates = (60.997758, 24.477142)
    place_suisto.comment = ''
    place_suisto.edits_pending = 0
    place_suisto.last_updated = datetime.datetime(2013, 11, 8, 19, 31, 0, 585275)
    place_suisto.begin_date_year = 2009
    place_suisto.ended = False
    place_suisto.area = area_hameenlinna
    place_suisto.type = placetype_venue
    session.add(place_suisto)

    iso31661_3 = ISO31661()
    iso31661_3.code = 'US'
    session.add(iso31661_3)

    area_united_states = Area()
    area_united_states.id = 222
    area_united_states.gid = '489ce91b-6658-3307-9877-795b68554c98'
    area_united_states.name = 'United States'
    area_united_states.edits_pending = 0
    area_united_states.last_updated = datetime.datetime(2013, 6, 15, 18, 6, 39, 593230)
    area_united_states.ended = False
    area_united_states.comment = ''
    area_united_states.iso_3166_1_codes = [
        iso31661_3,
    ]
    area_united_states.type = areatype_country
    session.add(area_united_states)

    area_memphis = Area()
    area_memphis.id = 7729
    area_memphis.gid = 'c2d96f61-75a4-4375-aed5-6aacb0b6326a'
    area_memphis.name = 'Memphis'
    area_memphis.edits_pending = 0
    area_memphis.last_updated = datetime.datetime(2013, 5, 29, 0, 15, 50, 543236)
    area_memphis.ended = False
    area_memphis.comment = ''
    area_memphis.type = areatype_city
    session.add(area_memphis)

    areatype_county = AreaType()
    areatype_county.id = 7
    areatype_county.name = 'County'
    areatype_county.child_order = 7
    areatype_county.description = 'County is used for smaller administrative divisions of a country which are not the main administrative divisions but are also not municipalities, e.g. counties in the USA. These are not considered when displaying the parent areas for a given area.'
    areatype_county.gid = 'bcecec27-8bdb-3e00-8254-d948dda502fa'
    session.add(areatype_county)

    area_shelby_county = Area()
    area_shelby_county.id = 102724
    area_shelby_county.gid = '9f1c845b-0536-4c8e-b40e-6b4dcd3eaac6'
    area_shelby_county.name = 'Shelby County'
    area_shelby_county.edits_pending = 0
    area_shelby_county.last_updated = datetime.datetime(2014, 12, 16, 4, 0, 31, 717144)
    area_shelby_county.ended = False
    area_shelby_county.comment = ''
    area_shelby_county.type = areatype_county
    session.add(area_shelby_county)

    iso31662_4 = ISO31662()
    iso31662_4.code = 'US-TN'
    session.add(iso31662_4)

    area_tennessee = Area()
    area_tennessee.id = 303
    area_tennessee.gid = 'f9caf2d8-9638-4b96-bc49-8462339d4b2e'
    area_tennessee.name = 'Tennessee'
    area_tennessee.edits_pending = 0
    area_tennessee.last_updated = datetime.datetime(2013, 5, 17, 20, 27, 37, 943022)
    area_tennessee.ended = False
    area_tennessee.comment = ''
    area_tennessee.iso_3166_2_codes = [
        iso31662_4,
    ]
    area_tennessee.type = areatype_subdivision
    session.add(area_tennessee)

    linkareaarea_9 = LinkAreaArea()
    linkareaarea_9.id = 43
    linkareaarea_9.edits_pending = 0
    linkareaarea_9.last_updated = datetime.datetime(2013, 5, 17, 20, 27, 53, 498302)
    linkareaarea_9.link_order = 0
    linkareaarea_9.entity0_credit = ''
    linkareaarea_9.entity1_credit = ''
    linkareaarea_9.entity0 = area_united_states
    linkareaarea_9.entity1 = area_tennessee
    linkareaarea_9.link = link_1
    session.add(linkareaarea_9)

    linkareaarea_8 = LinkAreaArea()
    linkareaarea_8.id = 102536
    linkareaarea_8.edits_pending = 0
    linkareaarea_8.last_updated = datetime.datetime(2014, 12, 16, 4, 0, 31, 717144)
    linkareaarea_8.link_order = 0
    linkareaarea_8.entity0_credit = ''
    linkareaarea_8.entity1_credit = ''
    linkareaarea_8.entity0 = area_tennessee
    linkareaarea_8.entity1 = area_shelby_county
    linkareaarea_8.link = link_1
    session.add(linkareaarea_8)

    linkareaarea_7 = LinkAreaArea()
    linkareaarea_7.id = 7495
    linkareaarea_7.edits_pending = 0
    linkareaarea_7.last_updated = datetime.datetime(2014, 12, 16, 4, 27, 41, 200469)
    linkareaarea_7.link_order = 0
    linkareaarea_7.entity0_credit = ''
    linkareaarea_7.entity1_credit = ''
    linkareaarea_7.entity0 = area_shelby_county
    linkareaarea_7.entity1 = area_memphis
    linkareaarea_7.link = link_1
    session.add(linkareaarea_7)

    gender_male = Gender()
    gender_male.id = 1
    gender_male.name = 'Male'
    gender_male.child_order = 1
    gender_male.gid = '36d3d30a-839d-3eda-8cb3-29be4384e4a9'
    session.add(gender_male)

    artistipi_1 = ArtistIPI()
    artistipi_1.ipi = '00345256954'
    artistipi_1.edits_pending = 0
    artistipi_1.created = datetime.datetime(2012, 5, 15, 19, 4, 48, 684349)
    session.add(artistipi_1)

    artistisni_1 = ArtistISNI()
    artistisni_1.isni = '000000011450569X'
    artistisni_1.edits_pending = 0
    artistisni_1.created = datetime.datetime(2013, 5, 23, 0, 0, 58, 335967)
    session.add(artistisni_1)

    artistmeta_1 = ArtistMeta()
    artistmeta_1.rating = 96
    artistmeta_1.rating_count = 5
    session.add(artistmeta_1)

    artisttype_person = ArtistType()
    artisttype_person.id = 1
    artisttype_person.name = 'Person'
    artisttype_person.child_order = 1
    artisttype_person.gid = 'b6e035f4-3ce9-331c-97df-83397230b0df'
    session.add(artisttype_person)

    artist_justin_timberlake = Artist()
    artist_justin_timberlake.id = 55795
    artist_justin_timberlake.gid = '596ffa74-3d08-44ef-b113-765d43d12738'
    artist_justin_timberlake.name = 'Justin Timberlake'
    artist_justin_timberlake.sort_name = 'Timberlake, Justin'
    artist_justin_timberlake.begin_date_year = 1981
    artist_justin_timberlake.begin_date_month = 1
    artist_justin_timberlake.begin_date_day = 31
    artist_justin_timberlake.comment = ''
    artist_justin_timberlake.edits_pending = 0
    artist_justin_timberlake.last_updated = datetime.datetime(2015, 8, 13, 20, 0, 50, 859750)
    artist_justin_timberlake.ended = False
    artist_justin_timberlake.area = area_united_states
    artist_justin_timberlake.begin_area = area_memphis
    artist_justin_timberlake.gender = gender_male
    artist_justin_timberlake.ipis = [
        artistipi_1,
    ]
    artist_justin_timberlake.isnis = [
        artistisni_1,
    ]
    artist_justin_timberlake.meta = artistmeta_1
    artist_justin_timberlake.type = artisttype_person
    session.add(artist_justin_timberlake)

    area_agoura_hills = Area()
    area_agoura_hills.id = 22398
    area_agoura_hills.gid = 'ab42be96-8579-4952-b29a-5cbdf7227e7e'
    area_agoura_hills.name = 'Agoura Hills'
    area_agoura_hills.edits_pending = 0
    area_agoura_hills.last_updated = datetime.datetime(2013, 11, 11, 17, 15, 10, 807333)
    area_agoura_hills.ended = False
    area_agoura_hills.comment = ''
    area_agoura_hills.type = areatype_city
    session.add(area_agoura_hills)

    area_los_angeles_county = Area()
    area_los_angeles_county.id = 104685
    area_los_angeles_county.gid = '720f8272-6ba3-48f7-b78e-14cd2641c2cf'
    area_los_angeles_county.name = 'Los Angeles County'
    area_los_angeles_county.edits_pending = 0
    area_los_angeles_county.last_updated = datetime.datetime(2014, 12, 17, 12, 44, 15, 174704)
    area_los_angeles_county.ended = False
    area_los_angeles_county.comment = ''
    area_los_angeles_county.type = areatype_county
    session.add(area_los_angeles_county)

    iso31662_5 = ISO31662()
    iso31662_5.code = 'US-CA'
    session.add(iso31662_5)

    area_california = Area()
    area_california.id = 266
    area_california.gid = 'ae0110b6-13d4-4998-9116-5b926287aa23'
    area_california.name = 'California'
    area_california.edits_pending = 0
    area_california.last_updated = datetime.datetime(2013, 6, 5, 7, 15, 15, 329304)
    area_california.ended = False
    area_california.comment = ''
    area_california.iso_3166_2_codes = [
        iso31662_5,
    ]
    area_california.type = areatype_subdivision
    session.add(area_california)

    linkareaarea_12 = LinkAreaArea()
    linkareaarea_12.id = 6
    linkareaarea_12.edits_pending = 0
    linkareaarea_12.last_updated = datetime.datetime(2013, 5, 17, 20, 8, 33, 220791)
    linkareaarea_12.link_order = 0
    linkareaarea_12.entity0_credit = ''
    linkareaarea_12.entity1_credit = ''
    linkareaarea_12.entity0 = area_united_states
    linkareaarea_12.entity1 = area_california
    linkareaarea_12.link = link_1
    session.add(linkareaarea_12)

    linkareaarea_11 = LinkAreaArea()
    linkareaarea_11.id = 104500
    linkareaarea_11.edits_pending = 0
    linkareaarea_11.last_updated = datetime.datetime(2014, 12, 17, 12, 44, 15, 174704)
    linkareaarea_11.link_order = 0
    linkareaarea_11.entity0_credit = ''
    linkareaarea_11.entity1_credit = ''
    linkareaarea_11.entity0 = area_california
    linkareaarea_11.entity1 = area_los_angeles_county
    linkareaarea_11.link = link_1
    session.add(linkareaarea_11)

    linkareaarea_10 = LinkAreaArea()
    linkareaarea_10.id = 22156
    linkareaarea_10.edits_pending = 0
    linkareaarea_10.last_updated = datetime.datetime(2014, 12, 17, 13, 36, 51, 897737)
    linkareaarea_10.link_order = 0
    linkareaarea_10.entity0_credit = ''
    linkareaarea_10.entity1_credit = ''
    linkareaarea_10.entity0 = area_los_angeles_county
    linkareaarea_10.entity1 = area_agoura_hills
    linkareaarea_10.link = link_1
    session.add(linkareaarea_10)

    artistisni_2 = ArtistISNI()
    artistisni_2.isni = '0000000123251302'
    artistisni_2.edits_pending = 0
    artistisni_2.created = datetime.datetime(2015, 9, 23, 21, 0, 36, 940792)
    session.add(artistisni_2)

    artistmeta_2 = ArtistMeta()
    artistmeta_2.rating = 87
    artistmeta_2.rating_count = 18
    session.add(artistmeta_2)

    artisttype_orchestra = ArtistType()
    artisttype_orchestra.id = 5
    artisttype_orchestra.name = 'Orchestra'
    artisttype_orchestra.child_order = 0
    artisttype_orchestra.gid = 'a0b36c92-3eb1-3839-a4f9-4799823f54a5'
    session.add(artisttype_orchestra)

    artisttype_choir = ArtistType()
    artisttype_choir.id = 6
    artisttype_choir.name = 'Choir'
    artisttype_choir.child_order = 0
    artisttype_choir.gid = '6124967d-7e3a-3eba-b642-c9a2ffb44d94'
    session.add(artisttype_choir)

    artisttype_group = ArtistType()
    artisttype_group.id = 2
    artisttype_group.name = 'Group'
    artisttype_group.child_order = 2
    artisttype_group.gid = 'e431f5f6-b5d2-343d-8b36-72607fffb74b'
    artisttype_group.parent = [
        artisttype_orchestra,
        artisttype_choir,
    ]
    session.add(artisttype_group)

    artist_linkin_park = Artist()
    artist_linkin_park.id = 11330
    artist_linkin_park.gid = 'f59c5520-5f46-4d2c-b2c4-822eabf53419'
    artist_linkin_park.name = 'Linkin Park'
    artist_linkin_park.sort_name = 'Linkin Park'
    artist_linkin_park.begin_date_year = 1995
    artist_linkin_park.comment = ''
    artist_linkin_park.edits_pending = 0
    artist_linkin_park.last_updated = datetime.datetime(2015, 9, 23, 21, 0, 36, 940792)
    artist_linkin_park.ended = False
    artist_linkin_park.area = area_united_states
    artist_linkin_park.begin_area = area_agoura_hills
    artist_linkin_park.isnis = [
        artistisni_2,
    ]
    artist_linkin_park.meta = artistmeta_2
    artist_linkin_park.type = artisttype_group
    session.add(artist_linkin_park)

    artistcreditname_linkin_park = ArtistCreditName()
    artistcreditname_linkin_park.position = 0
    artistcreditname_linkin_park.name = 'Linkin Park'
    artistcreditname_linkin_park.join_phrase = ' & '
    artistcreditname_linkin_park.artist = artist_linkin_park
    session.add(artistcreditname_linkin_park)

    area_brooklyn = Area()
    area_brooklyn.id = 10861
    area_brooklyn.gid = 'a71b0d32-7752-49e9-8594-2247ad6ac12c'
    area_brooklyn.name = 'Brooklyn'
    area_brooklyn.edits_pending = 0
    area_brooklyn.last_updated = datetime.datetime(2014, 12, 17, 15, 2, 24, 481268)
    area_brooklyn.ended = False
    area_brooklyn.comment = ''
    area_brooklyn.type = areatype_district
    session.add(area_brooklyn)

    area_new_york = Area()
    area_new_york.id = 7020
    area_new_york.gid = '74e50e58-5deb-4b99-93a2-decbb365c07f'
    area_new_york.name = 'New York'
    area_new_york.edits_pending = 0
    area_new_york.last_updated = datetime.datetime(2014, 12, 2, 22, 23, 17, 690134)
    area_new_york.ended = False
    area_new_york.comment = ''
    area_new_york.type = areatype_city
    session.add(area_new_york)

    iso31662_6 = ISO31662()
    iso31662_6.code = 'US-NY'
    session.add(iso31662_6)

    area_new_york_1 = Area()
    area_new_york_1.id = 295
    area_new_york_1.gid = '75e398a3-5f3f-4224-9cd8-0fe44715bc95'
    area_new_york_1.name = 'New York'
    area_new_york_1.edits_pending = 0
    area_new_york_1.last_updated = datetime.datetime(2013, 5, 17, 20, 23, 26, 631791)
    area_new_york_1.ended = False
    area_new_york_1.comment = ''
    area_new_york_1.iso_3166_2_codes = [
        iso31662_6,
    ]
    area_new_york_1.type = areatype_subdivision
    session.add(area_new_york_1)

    linkareaarea_15 = LinkAreaArea()
    linkareaarea_15.id = 35
    linkareaarea_15.edits_pending = 0
    linkareaarea_15.last_updated = datetime.datetime(2013, 5, 17, 20, 23, 44, 235720)
    linkareaarea_15.link_order = 0
    linkareaarea_15.entity0_credit = ''
    linkareaarea_15.entity1_credit = ''
    linkareaarea_15.entity0 = area_united_states
    linkareaarea_15.entity1 = area_new_york_1
    linkareaarea_15.link = link_1
    session.add(linkareaarea_15)

    linkareaarea_14 = LinkAreaArea()
    linkareaarea_14.id = 6786
    linkareaarea_14.edits_pending = 0
    linkareaarea_14.last_updated = datetime.datetime(2013, 5, 26, 12, 1, 42, 787582)
    linkareaarea_14.link_order = 0
    linkareaarea_14.entity0_credit = ''
    linkareaarea_14.entity1_credit = ''
    linkareaarea_14.entity0 = area_new_york_1
    linkareaarea_14.entity1 = area_new_york
    linkareaarea_14.link = link_1
    session.add(linkareaarea_14)

    linkareaarea_13 = LinkAreaArea()
    linkareaarea_13.id = 10625
    linkareaarea_13.edits_pending = 0
    linkareaarea_13.last_updated = datetime.datetime(2014, 12, 17, 15, 2, 24, 481268)
    linkareaarea_13.link_order = 0
    linkareaarea_13.entity0_credit = ''
    linkareaarea_13.entity1_credit = ''
    linkareaarea_13.entity0 = area_new_york
    linkareaarea_13.entity1 = area_brooklyn
    linkareaarea_13.link = link_1
    session.add(linkareaarea_13)

    artistipi_2 = ArtistIPI()
    artistipi_2.ipi = '00240089393'
    artistipi_2.edits_pending = 0
    artistipi_2.created = datetime.datetime(2015, 12, 17, 1, 0, 51, 602397)
    session.add(artistipi_2)

    artistipi_3 = ArtistIPI()
    artistipi_3.ipi = '00240089491'
    artistipi_3.edits_pending = 0
    artistipi_3.created = datetime.datetime(2015, 12, 17, 1, 0, 51, 602397)
    session.add(artistipi_3)

    artistipi_4 = ArtistIPI()
    artistipi_4.ipi = '00240089589'
    artistipi_4.edits_pending = 0
    artistipi_4.created = datetime.datetime(2014, 5, 8, 16, 58, 29, 119194)
    session.add(artistipi_4)

    artistisni_3 = ArtistISNI()
    artistisni_3.isni = '0000000118335528'
    artistisni_3.edits_pending = 0
    artistisni_3.created = datetime.datetime(2013, 7, 16, 1, 59, 52, 301391)
    session.add(artistisni_3)

    artistisni_4 = ArtistISNI()
    artistisni_4.isni = '0000000368615389'
    artistisni_4.edits_pending = 0
    artistisni_4.created = datetime.datetime(2013, 7, 16, 2, 14, 17, 394183)
    session.add(artistisni_4)

    artistmeta_3 = ArtistMeta()
    artistmeta_3.rating = 92
    artistmeta_3.rating_count = 5
    session.add(artistmeta_3)

    artist_jay_z = Artist()
    artist_jay_z.id = 167
    artist_jay_z.gid = 'f82bcf78-5b69-4622-a5ef-73800768d9ac'
    artist_jay_z.name = 'JAY Z'
    artist_jay_z.sort_name = 'JAY Z'
    artist_jay_z.begin_date_year = 1969
    artist_jay_z.begin_date_month = 12
    artist_jay_z.begin_date_day = 4
    artist_jay_z.comment = 'US rapper, formerly Jay-Z'
    artist_jay_z.edits_pending = 0
    artist_jay_z.last_updated = datetime.datetime(2017, 3, 25, 5, 0, 42, 311319)
    artist_jay_z.ended = False
    artist_jay_z.area = area_united_states
    artist_jay_z.begin_area = area_brooklyn
    artist_jay_z.gender = gender_male
    artist_jay_z.ipis = [
        artistipi_2,
        artistipi_3,
        artistipi_4,
    ]
    artist_jay_z.isnis = [
        artistisni_3,
        artistisni_4,
    ]
    artist_jay_z.meta = artistmeta_3
    artist_jay_z.type = artisttype_person
    session.add(artist_jay_z)

    artistcreditname_jay_z = ArtistCreditName()
    artistcreditname_jay_z.position = 1
    artistcreditname_jay_z.name = 'JAY Z'
    artistcreditname_jay_z.join_phrase = ''
    artistcreditname_jay_z.artist = artist_jay_z
    session.add(artistcreditname_jay_z)

    artistcredit_linkin_park_jay_z = ArtistCredit()
    artistcredit_linkin_park_jay_z.id = 1302095
    artistcredit_linkin_park_jay_z.name = 'Linkin Park & JAY Z'
    artistcredit_linkin_park_jay_z.artist_count = 2
    artistcredit_linkin_park_jay_z.ref_count = 18
    artistcredit_linkin_park_jay_z.created = datetime.datetime(2014, 4, 12, 7, 28, 3, 370147)
    artistcredit_linkin_park_jay_z.artists = [
        artistcreditname_linkin_park,
        artistcreditname_jay_z,
    ]
    session.add(artistcredit_linkin_park_jay_z)

    releasegroupmeta_1 = ReleaseGroupMeta()
    releasegroupmeta_1.release_count = 4
    releasegroupmeta_1.first_release_date_year = 2004
    releasegroupmeta_1.first_release_date_month = 11
    releasegroupmeta_1.first_release_date_day = 29
    releasegroupmeta_1.rating = 80
    releasegroupmeta_1.rating_count = 3
    session.add(releasegroupmeta_1)

    releasegroupprimarytype_ep = ReleaseGroupPrimaryType()
    releasegroupprimarytype_ep.id = 3
    releasegroupprimarytype_ep.name = 'EP'
    releasegroupprimarytype_ep.child_order = 3
    releasegroupprimarytype_ep.gid = '6d0c5bf6-7a33-3420-a519-44fc63eedebf'
    session.add(releasegroupprimarytype_ep)

    releasegroup_collision_course = ReleaseGroup()
    releasegroup_collision_course.id = 1110052
    releasegroup_collision_course.gid = '8ef859e3-feb2-4dd1-93da-22b91280d768'
    releasegroup_collision_course.name = 'Collision Course'
    releasegroup_collision_course.comment = ''
    releasegroup_collision_course.edits_pending = 0
    releasegroup_collision_course.last_updated = datetime.datetime(2015, 2, 15, 23, 1, 28, 867540)
    releasegroup_collision_course.artist_credit = artistcredit_linkin_park_jay_z
    releasegroup_collision_course.meta = releasegroupmeta_1
    releasegroup_collision_course.type = releasegroupprimarytype_ep
    session.add(releasegroup_collision_course)

    url_1 = URL()
    url_1.id = 276953
    url_1.gid = 'e1340355-3ad0-4d6b-8eeb-ca219a95ec3f'
    url_1.url = 'https://en.wikipedia.org/wiki/Collision_Course_(album)'
    url_1.edits_pending = 0
    url_1.last_updated = datetime.datetime(2016, 10, 14, 5, 0, 2, 571367)
    session.add(url_1)

    linktype_wikipedia = LinkType()
    linktype_wikipedia.id = 89
    linktype_wikipedia.child_order = 0
    linktype_wikipedia.gid = '6578f0e9-1ace-4095-9de8-6e517ddb1ceb'
    linktype_wikipedia.entity_type0 = 'release_group'
    linktype_wikipedia.entity_type1 = 'url'
    linktype_wikipedia.name = 'wikipedia'
    linktype_wikipedia.description = 'Points to the Wikipedia page for this album.'
    linktype_wikipedia.link_phrase = 'Wikipedia'
    linktype_wikipedia.reverse_link_phrase = 'Wikipedia page for'
    linktype_wikipedia.long_link_phrase = 'has a Wikipedia page at'
    linktype_wikipedia.priority = 0
    linktype_wikipedia.last_updated = datetime.datetime(2014, 5, 18, 11, 11, 12, 332953)
    linktype_wikipedia.is_deprecated = False
    linktype_wikipedia.has_dates = False
    linktype_wikipedia.entity0_cardinality = 0
    linktype_wikipedia.entity1_cardinality = 0
    session.add(linktype_wikipedia)

    link_2 = Link()
    link_2.id = 6303
    link_2.attribute_count = 0
    link_2.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_2.ended = False
    link_2.link_type = linktype_wikipedia
    session.add(link_2)

    linkreleasegroupurl_1 = LinkReleaseGroupURL()
    linkreleasegroupurl_1.id = 38402
    linkreleasegroupurl_1.edits_pending = 0
    linkreleasegroupurl_1.last_updated = datetime.datetime(2012, 1, 29, 19, 0, 9, 103309)
    linkreleasegroupurl_1.link_order = 0
    linkreleasegroupurl_1.entity0_credit = ''
    linkreleasegroupurl_1.entity1_credit = ''
    linkreleasegroupurl_1.entity0 = releasegroup_collision_course
    linkreleasegroupurl_1.entity1 = url_1
    linkreleasegroupurl_1.link = link_2
    session.add(linkreleasegroupurl_1)

    url_2 = URL()
    url_2.id = 1028345
    url_2.gid = 'ba7a6f42-0ee2-44bd-bf21-7ed44c83ef3c'
    url_2.url = 'https://www.discogs.com/master/47318'
    url_2.edits_pending = 0
    url_2.last_updated = datetime.datetime(2016, 7, 29, 17, 0, 2, 403770)
    session.add(url_2)

    linktype_discogs = LinkType()
    linktype_discogs.id = 90
    linktype_discogs.child_order = 0
    linktype_discogs.gid = '99e550f3-5ab4-3110-b5b9-fe01d970b126'
    linktype_discogs.entity_type0 = 'release_group'
    linktype_discogs.entity_type1 = 'url'
    linktype_discogs.name = 'discogs'
    linktype_discogs.description = 'This is used to link the Discogs page for this release group.'
    linktype_discogs.link_phrase = 'Discogs'
    linktype_discogs.reverse_link_phrase = 'Discogs page for'
    linktype_discogs.long_link_phrase = 'has a Discogs page at'
    linktype_discogs.priority = 0
    linktype_discogs.last_updated = datetime.datetime(2014, 5, 24, 0, 43, 21, 316468)
    linktype_discogs.is_deprecated = False
    linktype_discogs.has_dates = False
    linktype_discogs.entity0_cardinality = 0
    linktype_discogs.entity1_cardinality = 0
    session.add(linktype_discogs)

    link_3 = Link()
    link_3.id = 6309
    link_3.attribute_count = 0
    link_3.created = datetime.datetime(2011, 5, 16, 15, 3, 23, 368437)
    link_3.ended = False
    link_3.link_type = linktype_discogs
    session.add(link_3)

    linkreleasegroupurl_2 = LinkReleaseGroupURL()
    linkreleasegroupurl_2.id = 86656
    linkreleasegroupurl_2.edits_pending = 0
    linkreleasegroupurl_2.last_updated = datetime.datetime(2012, 1, 29, 19, 0, 9, 103309)
    linkreleasegroupurl_2.link_order = 0
    linkreleasegroupurl_2.entity0_credit = ''
    linkreleasegroupurl_2.entity1_credit = ''
    linkreleasegroupurl_2.entity0 = releasegroup_collision_course
    linkreleasegroupurl_2.entity1 = url_2
    linkreleasegroupurl_2.link = link_3
    session.add(linkreleasegroupurl_2)

    url_3 = URL()
    url_3.id = 1472711
    url_3.gid = 'b38a5f72-059e-4894-b38c-865ca0a2992f'
    url_3.url = 'http://www.allmusic.com/album/mw0000709574'
    url_3.edits_pending = 0
    url_3.last_updated = datetime.datetime(2012, 8, 27, 10, 23, 40, 136004)
    session.add(url_3)

    linktype_allmusic = LinkType()
    linktype_allmusic.id = 284
    linktype_allmusic.child_order = 0
    linktype_allmusic.gid = 'a50a1d20-2b20-4d2c-9a29-eb771dd78386'
    linktype_allmusic.entity_type0 = 'release_group'
    linktype_allmusic.entity_type1 = 'url'
    linktype_allmusic.name = 'allmusic'
    linktype_allmusic.description = 'This is used to link a release group to its corresponding page on Allmusic.'
    linktype_allmusic.link_phrase = 'Allmusic'
    linktype_allmusic.reverse_link_phrase = 'Allmusic page for'
    linktype_allmusic.long_link_phrase = 'has an Allmusic page at'
    linktype_allmusic.priority = 0
    linktype_allmusic.last_updated = datetime.datetime(2014, 5, 18, 11, 11, 9, 768070)
    linktype_allmusic.is_deprecated = False
    linktype_allmusic.has_dates = False
    linktype_allmusic.entity0_cardinality = 0
    linktype_allmusic.entity1_cardinality = 0
    session.add(linktype_allmusic)

    link_4 = Link()
    link_4.id = 28614
    link_4.attribute_count = 0
    link_4.created = datetime.datetime(2011, 7, 28, 21, 43, 56, 77951)
    link_4.ended = False
    link_4.link_type = linktype_allmusic
    session.add(link_4)

    linkreleasegroupurl_3 = LinkReleaseGroupURL()
    linkreleasegroupurl_3.id = 198438
    linkreleasegroupurl_3.edits_pending = 0
    linkreleasegroupurl_3.last_updated = datetime.datetime(2012, 9, 10, 8, 0, 12, 992650)
    linkreleasegroupurl_3.link_order = 0
    linkreleasegroupurl_3.entity0_credit = ''
    linkreleasegroupurl_3.entity1_credit = ''
    linkreleasegroupurl_3.entity0 = releasegroup_collision_course
    linkreleasegroupurl_3.entity1 = url_3
    linkreleasegroupurl_3.link = link_4
    session.add(linkreleasegroupurl_3)

    url_4 = URL()
    url_4.id = 2294802
    url_4.gid = '93bb8713-3c4a-4ec3-af07-e537f39326fc'
    url_4.url = 'https://www.wikidata.org/wiki/Q20001'
    url_4.edits_pending = 0
    url_4.last_updated = datetime.datetime(2016, 7, 11, 23, 0, 2, 413799)
    session.add(url_4)

    linktype_wikidata = LinkType()
    linktype_wikidata.id = 353
    linktype_wikidata.child_order = 0
    linktype_wikidata.gid = 'b988d08c-5d86-4a57-9557-c83b399e3580'
    linktype_wikidata.entity_type0 = 'release_group'
    linktype_wikidata.entity_type1 = 'url'
    linktype_wikidata.name = 'wikidata'
    linktype_wikidata.description = 'Points to the Wikidata page for this release group, and will be used to fetch Wikipedia summaries'
    linktype_wikidata.link_phrase = 'Wikidata'
    linktype_wikidata.reverse_link_phrase = 'Wikidata page for'
    linktype_wikidata.long_link_phrase = 'has a Wikidata page at'
    linktype_wikidata.priority = 0
    linktype_wikidata.last_updated = datetime.datetime(2016, 11, 20, 9, 27, 34, 653029)
    linktype_wikidata.is_deprecated = False
    linktype_wikidata.has_dates = False
    linktype_wikidata.entity0_cardinality = 0
    linktype_wikidata.entity1_cardinality = 0
    session.add(linktype_wikidata)

    link_5 = Link()
    link_5.id = 117677
    link_5.attribute_count = 0
    link_5.created = datetime.datetime(2013, 5, 9, 9, 56, 17, 113888)
    link_5.ended = False
    link_5.link_type = linktype_wikidata
    session.add(link_5)

    linkreleasegroupurl_4 = LinkReleaseGroupURL()
    linkreleasegroupurl_4.id = 306086
    linkreleasegroupurl_4.edits_pending = 0
    linkreleasegroupurl_4.last_updated = datetime.datetime(2013, 12, 9, 0, 26, 0, 690071)
    linkreleasegroupurl_4.link_order = 0
    linkreleasegroupurl_4.entity0_credit = ''
    linkreleasegroupurl_4.entity1_credit = ''
    linkreleasegroupurl_4.entity0 = releasegroup_collision_course
    linkreleasegroupurl_4.entity1 = url_4
    linkreleasegroupurl_4.link = link_5
    session.add(linkreleasegroupurl_4)

    iso31661_4 = ISO31661()
    iso31661_4.code = 'JP'
    session.add(iso31661_4)

    area_japan = Area()
    area_japan.id = 107
    area_japan.gid = '2db42837-c832-3c27-b4a3-08198f75693c'
    area_japan.name = 'Japan'
    area_japan.edits_pending = 0
    area_japan.last_updated = datetime.datetime(2013, 5, 27, 12, 29, 56, 162248)
    area_japan.ended = False
    area_japan.comment = ''
    area_japan.iso_3166_1_codes = [
        iso31661_4,
    ]
    area_japan.type = areatype_country
    session.add(area_japan)

    iso31662_7 = ISO31662()
    iso31662_7.code = 'JP-13'
    session.add(iso31662_7)

    area_tokyo = Area()
    area_tokyo.id = 397
    area_tokyo.gid = '8dc97297-ac95-4d33-82bc-e07fab26fb5f'
    area_tokyo.name = 'Tokyo'
    area_tokyo.edits_pending = 0
    area_tokyo.last_updated = datetime.datetime(2013, 11, 4, 4, 7, 37, 787171)
    area_tokyo.ended = False
    area_tokyo.comment = ''
    area_tokyo.iso_3166_2_codes = [
        iso31662_7,
    ]
    area_tokyo.type = areatype_subdivision
    session.add(area_tokyo)

    linkareaarea_16 = LinkAreaArea()
    linkareaarea_16.id = 138
    linkareaarea_16.edits_pending = 0
    linkareaarea_16.last_updated = datetime.datetime(2013, 5, 17, 23, 28, 33, 692614)
    linkareaarea_16.link_order = 0
    linkareaarea_16.entity0_credit = ''
    linkareaarea_16.entity1_credit = ''
    linkareaarea_16.entity0 = area_japan
    linkareaarea_16.entity1 = area_tokyo
    linkareaarea_16.link = link_1
    session.add(linkareaarea_16)

    artistmeta_4 = ArtistMeta()
    artistmeta_4.rating = 100
    artistmeta_4.rating_count = 4
    session.add(artistmeta_4)

    artist_boris = Artist()
    artist_boris.id = 41488
    artist_boris.gid = '57652bf8-cfe8-42e7-b9a7-5572a7080d8d'
    artist_boris.name = 'Boris'
    artist_boris.sort_name = 'Boris'
    artist_boris.begin_date_year = 1992
    artist_boris.comment = 'Japanese stoner rock band'
    artist_boris.edits_pending = 0
    artist_boris.last_updated = datetime.datetime(2016, 8, 13, 23, 0, 40, 520302)
    artist_boris.ended = False
    artist_boris.area = area_japan
    artist_boris.begin_area = area_tokyo
    artist_boris.meta = artistmeta_4
    artist_boris.type = artisttype_group
    session.add(artist_boris)

    artistcreditname_boris = ArtistCreditName()
    artistcreditname_boris.position = 0
    artistcreditname_boris.name = 'Boris'
    artistcreditname_boris.join_phrase = ' with '
    artistcreditname_boris.artist = artist_boris
    session.add(artistcreditname_boris)

    artistisni_5 = ArtistISNI()
    artistisni_5.isni = '0000000027079426'
    artistisni_5.edits_pending = 0
    artistisni_5.created = datetime.datetime(2015, 11, 16, 14, 3, 14, 427924)
    session.add(artistisni_5)

    artistmeta_5 = ArtistMeta()
    artistmeta_5.rating = 87
    artistmeta_5.rating_count = 3
    session.add(artistmeta_5)

    artist_merzbow = Artist()
    artist_merzbow.id = 3214
    artist_merzbow.gid = '2841d983-f8c3-432a-af02-7407a84580a8'
    artist_merzbow.name = 'Merzbow'
    artist_merzbow.sort_name = 'Merzbow'
    artist_merzbow.begin_date_year = 1956
    artist_merzbow.begin_date_month = 12
    artist_merzbow.begin_date_day = 19
    artist_merzbow.comment = ''
    artist_merzbow.edits_pending = 0
    artist_merzbow.last_updated = datetime.datetime(2015, 11, 16, 14, 3, 14, 427924)
    artist_merzbow.ended = False
    artist_merzbow.area = area_japan
    artist_merzbow.begin_area = area_tokyo
    artist_merzbow.gender = gender_male
    artist_merzbow.isnis = [
        artistisni_5,
    ]
    artist_merzbow.meta = artistmeta_5
    artist_merzbow.type = artisttype_person
    session.add(artist_merzbow)

    artistcreditname_merzbow = ArtistCreditName()
    artistcreditname_merzbow.position = 1
    artistcreditname_merzbow.name = 'Merzbow'
    artistcreditname_merzbow.join_phrase = ''
    artistcreditname_merzbow.artist = artist_merzbow
    session.add(artistcreditname_merzbow)

    artistcredit_boris_with_merzbow = ArtistCredit()
    artistcredit_boris_with_merzbow.id = 989297
    artistcredit_boris_with_merzbow.name = 'Boris with Merzbow'
    artistcredit_boris_with_merzbow.artist_count = 2
    artistcredit_boris_with_merzbow.ref_count = 138
    artistcredit_boris_with_merzbow.created = datetime.datetime(2012, 5, 23, 14, 7, 38, 889324)
    artistcredit_boris_with_merzbow.artists = [
        artistcreditname_boris,
        artistcreditname_merzbow,
    ]
    session.add(artistcredit_boris_with_merzbow)

    releasegroupmeta_2 = ReleaseGroupMeta()
    releasegroupmeta_2.release_count = 1
    releasegroupmeta_2.first_release_date_year = 2002
    releasegroupmeta_2.first_release_date_month = 4
    releasegroupmeta_2.first_release_date_day = 26
    session.add(releasegroupmeta_2)

    releasegroupprimarytype_album = ReleaseGroupPrimaryType()
    releasegroupprimarytype_album.id = 1
    releasegroupprimarytype_album.name = 'Album'
    releasegroupprimarytype_album.child_order = 1
    releasegroupprimarytype_album.gid = 'f529b476-6e62-324f-b0aa-1f3e33d313fc'
    session.add(releasegroupprimarytype_album)

    releasegroup_megatone = ReleaseGroup()
    releasegroup_megatone.id = 331465
    releasegroup_megatone.gid = 'b1517b6f-5714-3f45-a568-772d63b7a438'
    releasegroup_megatone.name = 'Megatone'
    releasegroup_megatone.comment = ''
    releasegroup_megatone.edits_pending = 0
    releasegroup_megatone.last_updated = datetime.datetime(2012, 5, 23, 14, 7, 38, 889324)
    releasegroup_megatone.artist_credit = artistcredit_boris_with_merzbow
    releasegroup_megatone.meta = releasegroupmeta_2
    releasegroup_megatone.type = releasegroupprimarytype_album
    session.add(releasegroup_megatone)

    url_5 = URL()
    url_5.id = 3940144
    url_5.gid = 'fe40c167-f807-4bb5-ac3c-0354c9369a46'
    url_5.url = 'https://www.wikidata.org/wiki/Q6808938'
    url_5.edits_pending = 0
    url_5.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    session.add(url_5)

    linkreleasegroupurl_5 = LinkReleaseGroupURL()
    linkreleasegroupurl_5.id = 442165
    linkreleasegroupurl_5.edits_pending = 0
    linkreleasegroupurl_5.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    linkreleasegroupurl_5.link_order = 0
    linkreleasegroupurl_5.entity0_credit = ''
    linkreleasegroupurl_5.entity1_credit = ''
    linkreleasegroupurl_5.entity0 = releasegroup_megatone
    linkreleasegroupurl_5.entity1 = url_5
    linkreleasegroupurl_5.link = link_5
    session.add(linkreleasegroupurl_5)

    url_6 = URL()
    url_6.id = 3940145
    url_6.gid = 'd85af25b-3896-4434-b624-eb6d8c544c73'
    url_6.url = 'https://rateyourmusic.com/release/album/boris_with_merzbow/megatone/'
    url_6.edits_pending = 0
    url_6.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    session.add(url_6)

    linktype_bookbrainz = LinkType()
    linktype_bookbrainz.id = 853
    linktype_bookbrainz.child_order = 0
    linktype_bookbrainz.gid = '27cfc95c-d368-45a9-ae0d-308c274c2017'
    linktype_bookbrainz.entity_type0 = 'release_group'
    linktype_bookbrainz.entity_type1 = 'url'
    linktype_bookbrainz.name = 'BookBrainz'
    linktype_bookbrainz.description = 'Points to the BookBrainz page for this release group.'
    linktype_bookbrainz.link_phrase = 'BookBrainz'
    linktype_bookbrainz.reverse_link_phrase = 'BookBrainz page for'
    linktype_bookbrainz.long_link_phrase = 'has a BookBrainz page at'
    linktype_bookbrainz.priority = 0
    linktype_bookbrainz.last_updated = datetime.datetime(2015, 4, 21, 19, 15, 14, 332458)
    linktype_bookbrainz.is_deprecated = False
    linktype_bookbrainz.has_dates = False
    linktype_bookbrainz.entity0_cardinality = 0
    linktype_bookbrainz.entity1_cardinality = 0
    session.add(linktype_bookbrainz)

    linktype_imdb = LinkType()
    linktype_imdb.id = 97
    linktype_imdb.child_order = 0
    linktype_imdb.gid = '85b0a010-3237-47c7-8476-6fcefd4761af'
    linktype_imdb.entity_type0 = 'release_group'
    linktype_imdb.entity_type1 = 'url'
    linktype_imdb.name = 'IMDb'
    linktype_imdb.description = 'This links a soundtrack release group to the <a href="http://www.imdb.com/">IMDb</a> page for the movie, show or game of which it is a soundtrack.'
    linktype_imdb.link_phrase = 'IMDb'
    linktype_imdb.reverse_link_phrase = 'IMDb page for'
    linktype_imdb.long_link_phrase = 'has an IMDb page at'
    linktype_imdb.priority = 0
    linktype_imdb.last_updated = datetime.datetime(2016, 9, 27, 19, 42, 49, 701724)
    linktype_imdb.is_deprecated = False
    linktype_imdb.has_dates = False
    linktype_imdb.entity0_cardinality = 0
    linktype_imdb.entity1_cardinality = 0
    session.add(linktype_imdb)

    linktype_other_databases = LinkType()
    linktype_other_databases.id = 96
    linktype_other_databases.child_order = 99
    linktype_other_databases.gid = '38320e40-9f4a-3ae7-8cb2-3f3c9c5d856d'
    linktype_other_databases.entity_type0 = 'release_group'
    linktype_other_databases.entity_type1 = 'url'
    linktype_other_databases.name = 'other databases'
    linktype_other_databases.description = 'This links an entity to the equivalent entry in another database. Please respect the <a href="/doc/Other_Databases_Relationship_Type/Whitelist">whitelist</a>.'
    linktype_other_databases.link_phrase = 'other databases'
    linktype_other_databases.reverse_link_phrase = 'other databases'
    linktype_other_databases.long_link_phrase = 'has a page in a database at'
    linktype_other_databases.priority = 0
    linktype_other_databases.last_updated = datetime.datetime(2014, 5, 18, 11, 11, 8, 934960)
    linktype_other_databases.is_deprecated = False
    linktype_other_databases.has_dates = False
    linktype_other_databases.entity0_cardinality = 0
    linktype_other_databases.entity1_cardinality = 0
    linktype_other_databases.parent = [
        linktype_bookbrainz,
        linktype_allmusic,
        linktype_wikipedia,
        linktype_discogs,
        linktype_imdb,
        linktype_wikidata,
    ]
    session.add(linktype_other_databases)

    link_6 = Link()
    link_6.id = 49051
    link_6.attribute_count = 0
    link_6.created = datetime.datetime(2012, 5, 28, 19, 8, 47, 976241)
    link_6.ended = False
    link_6.link_type = linktype_other_databases
    session.add(link_6)

    linkreleasegroupurl_6 = LinkReleaseGroupURL()
    linkreleasegroupurl_6.id = 442166
    linkreleasegroupurl_6.edits_pending = 0
    linkreleasegroupurl_6.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    linkreleasegroupurl_6.link_order = 0
    linkreleasegroupurl_6.entity0_credit = ''
    linkreleasegroupurl_6.entity1_credit = ''
    linkreleasegroupurl_6.entity0 = releasegroup_megatone
    linkreleasegroupurl_6.entity1 = url_6
    linkreleasegroupurl_6.link = link_6
    session.add(linkreleasegroupurl_6)

    url_7 = URL()
    url_7.id = 3940146
    url_7.gid = '4ec44849-f6d5-4958-ae90-0db40eb44c0d'
    url_7.url = 'http://www.metal-archives.com/albums/Boris/Megatone/38662'
    url_7.edits_pending = 0
    url_7.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    session.add(url_7)

    linkreleasegroupurl_7 = LinkReleaseGroupURL()
    linkreleasegroupurl_7.id = 442167
    linkreleasegroupurl_7.edits_pending = 0
    linkreleasegroupurl_7.last_updated = datetime.datetime(2016, 10, 31, 6, 51, 30, 701528)
    linkreleasegroupurl_7.link_order = 0
    linkreleasegroupurl_7.entity0_credit = ''
    linkreleasegroupurl_7.entity1_credit = ''
    linkreleasegroupurl_7.entity0 = releasegroup_megatone
    linkreleasegroupurl_7.entity1 = url_7
    linkreleasegroupurl_7.link = link_6
    session.add(linkreleasegroupurl_7)

    session.commit()

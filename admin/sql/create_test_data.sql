BEGIN;

-- Disable trigger which deletes unused tags
ALTER TABLE tag DISABLE TRIGGER delete_unused_tag;

-- Release Group 7c1014eb-454c-3867-8854-3c95d265f8de (Numb/Encore (Single))
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '489ce91b-6658-3307-9877-795b68554c98', 222, '2013-06-15 18:06:39.59323+00', 'United States', 1),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'a71b0d32-7752-49e9-8594-2247ad6ac12c', 10861, '2014-12-17 15:02:24.481268+00', 'Brooklyn', 5),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'ab42be96-8579-4952-b29a-5cbdf7227e7e', 22398, '2013-11-11 17:15:10.807333+00', 'Agoura Hills', 3);
INSERT INTO country_area (area) VALUES (222), (10861), (22398);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(222, 10861, 4, 12, 1969, 'US rapper, formerly Jay-Z', 0, NULL, NULL, NULL, NULL, '0', 1, 'f82bcf78-5b69-4622-a5ef-73800768d9ac', 167, '2017-03-25 05:00:42.311319+00', 'JAY Z', 'JAY Z', 1),
	(222, 22398, NULL, NULL, 1995, '', 0, NULL, NULL, NULL, NULL, '0', NULL, 'f59c5520-5f46-4d2c-b2c4-822eabf53419', 11330, '2015-09-23 21:00:36.940792+00', 'Linkin Park', 'Linkin Park', 2);
INSERT INTO artist_alias (artist, begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, primary_for_locale, sort_name, type) VALUES
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 176, '2012-05-15 18:57:13.252186+00', NULL, 'Jay Z', '0', 'Jay Z', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 102, '2012-05-15 18:57:13.252186+00', NULL, 'Jayz', '0', 'Jayz', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 67507, '2012-05-15 18:57:13.252186+00', NULL, 'Jaÿ-Z', '0', 'Jaÿ-Z', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 6863, '2012-05-15 18:57:13.252186+00', NULL, 'Jay - Z', '0', 'Jay - Z', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '1', 175062, '2016-03-16 04:58:02.665073+00', NULL, 'Jay-Z', '0', 'Jay-Z', 1),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 74664, '2016-12-04 12:00:45.604632+00', NULL, 'S. Carter', '0', 'S. Carter', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 73267, '2016-12-04 12:00:45.604632+00', NULL, 'Shawn C Carter', '0', 'Shawn C Carter', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 48579, '2016-12-04 12:00:45.604632+00', NULL, 'Shawn Corey Carter', '0', 'Shawn Corey Carter', NULL),
	(167, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 186272, '2016-12-04 12:00:45.604632+00', NULL, 'Shawn Carter', '0', 'Carter, Shawn', NULL),
	(11330, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 14395, '2012-05-15 18:57:13.252186+00', NULL, 'Hybrid Theory', '0', 'Hybrid Theory', NULL),
	(11330, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 1633, '2012-05-15 18:57:13.252186+00', NULL, 'Lincoln Park', '0', 'Lincoln Park', NULL),
	(11330, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 14309, '2012-05-15 18:57:13.252186+00', NULL, 'Xero', '0', 'Xero', NULL),
	(11330, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 34211, '2012-05-15 18:57:13.252186+00', NULL, 'Limkin Park', '0', 'Limkin Park', NULL);
INSERT INTO tag (id, name, ref_count) VALUES
	(7, 'rock', 65222),
	(20, 'alternative rock', 8940),
	(47, 'industrial rock', 272),
	(62, 'rap', 2880),
	(92, 'metal', 5349),
	(111, 'american', 2199),
	(150, 'hip-hop', 9611),
	(235, 'hip hop', 3685),
	(273, 'usa', 2112),
	(349, 'nu metal', 366),
	(553, 'hiphop', 242),
	(644, 'new metal', 27),
	(748, 'américain', 557),
	(1072, 'alternative metal', 374),
	(1091, 'pop rock', 3967),
	(1102, 'rapcore', 68),
	(1182, 'pop rap', 551),
	(1277, 'rap metal', 71),
	(1915, 'rapper', 129),
	(2349, 'rap rock', 107),
	(2976, 'us', 93),
	(3295, 'nu-metal', 100),
	(3678, 'mashup', 151),
	(4662, 'rock and indie', 2005),
	(4667, 'hip hop rnb and dance hall', 664),
	(5221, 'united states', 112),
	(36080, 'boom bap', 1),
	(48881, 'east coast hip hop', 0),
	(49117, 'hardcore hip hop', 0),
	(49458, 'roxette', 0);
INSERT INTO artist_tag (artist, count, last_updated, tag) VALUES
	(167, 0, '2016-12-04 12:00:45.604632+00', 62),
	(167, 0, '2016-12-04 12:00:45.604632+00', 150),
	(167, 1, '2017-02-28 07:56:59.845663+00', 235),
	(167, 0, '2016-12-04 12:00:45.604632+00', 553),
	(167, 2, '2016-12-04 12:00:45.604632+00', 1182),
	(167, 0, '2016-12-04 12:00:45.604632+00', 1915),
	(167, 0, '2016-12-04 12:00:45.604632+00', 2976),
	(167, 1, '2016-12-04 12:00:45.604632+00', 3678),
	(167, 0, '2016-12-04 12:00:45.604632+00', 4667),
	(167, 0, '2016-12-04 12:00:45.604632+00', 5221),
	(167, 1, '2016-12-04 12:00:45.604632+00', 36080),
	(167, 2, '2016-12-04 12:00:45.604632+00', 48881),
	(167, 1, '2016-12-04 12:00:45.604632+00', 49117),
	(11330, 3, '2013-01-14 10:05:39.579132+00', 7),
	(11330, 3, '2015-07-16 22:08:24.498981+00', 20),
	(11330, 1, '2011-05-16 14:57:06.530063+00', 47),
	(11330, 1, '2011-05-16 14:57:06.530063+00', 92),
	(11330, 1, '2015-08-16 14:14:37.66654+00', 111),
	(11330, 1, '2015-07-16 22:08:24.519938+00', 235),
	(11330, 0, '2015-08-16 14:14:51.914034+00', 273),
	(11330, 4, '2017-04-17 09:33:10.844827+00', 349),
	(11330, 1, '2011-05-16 14:57:06.530063+00', 644),
	(11330, 0, '2015-07-16 22:10:13.065471+00', 748),
	(11330, 1, '2011-05-16 14:57:06.530063+00', 1072),
	(11330, 1, '2015-07-16 22:08:24.50467+00', 1091),
	(11330, 3, '2017-06-04 13:45:14.672856+00', 1102),
	(11330, 1, '2011-05-16 14:57:06.530063+00', 1277),
	(11330, 6, '2017-06-04 13:45:11.974101+00', 2349),
	(11330, 0, '2015-07-16 22:11:53.211294+00', 3295),
	(11330, 0, '2015-07-16 22:09:52.556986+00', 4662),
	(11330, 0, '2015-08-16 14:14:51.897752+00', 5221),
	(11330, 0, '2015-07-16 22:09:15.33297+00', 49458);
INSERT INTO artist_credit (artist_count, created, id, name, ref_count) VALUES
	(2, '2016-02-28 21:42:14.873583+00', 1617798, 'Jay-Z/Linkin Park', 5);
INSERT INTO artist_credit_name (artist, artist_credit, join_phrase, name, position) VALUES
	(167, 1617798, '/', 'Jay-Z', 0),
	(11330, 1617798, '', 'Linkin Park', 1);
INSERT INTO release_group (artist_credit, comment, edits_pending, gid, id, last_updated, name, type) VALUES
	(1617798, '', 0, '7c1014eb-454c-3867-8854-3c95d265f8de', 828504, '2016-03-06 22:00:23.734915+00', 'Numb/Encore', 2);
INSERT INTO tag (id, name, ref_count) VALUES
	(564, 'alternative', 5619);
INSERT INTO release_group_tag (count, last_updated, release_group, tag) VALUES
	(1, '2011-06-21 01:00:52.046546+00', 828504, 564);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, '31f19b8a-ac93-48e0-876f-f910115ac649', 1142311, '2016-08-01 00:00:02.871431+00', 'https://www.discogs.com/master/47312'),
	(0, '585e4ff6-e968-45ea-a65d-2c126aacd6bd', 3538522, '2016-02-28 21:21:38.399148+00', 'https://en.wikipedia.org/wiki/Numb/Encore');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6303, 89),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6309, 90);
INSERT INTO l_release_group_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 828504, '', 1142311, '', 156981, '2012-02-18 15:00:19.7341+00', 6309, 0),
	(0, 828504, '', 3538522, '', 411662, '2016-02-28 21:21:38.399148+00', 6303, 0);
INSERT INTO artist_credit (artist_count, created, id, name, ref_count) VALUES
	(2, '2011-07-15 16:36:51.235687+00', 839496, 'Jay-Z & Linkin Park', 118);
INSERT INTO artist_credit_name (artist, artist_credit, join_phrase, name, position) VALUES
	(167, 839496, ' & ', 'Jay-Z', 0),
	(11330, 839496, '', 'Linkin Park', 1);
INSERT INTO script (frequency, id, iso_code, iso_number, name) VALUES
	(4, 28, 'Latn', '215', 'Latin');
INSERT INTO release_packaging (id, name, parent, child_order, description, gid) VALUES (2, 'Slim Jewel Case', NULL, 0, 'A thinner jewel case, commonly used for CD singles.', '36327bc2-f691-3d66-80e5-bd03cec6060a');
INSERT INTO release (artist_credit, barcode, comment, edits_pending, gid, id, language, last_updated, name, packaging, quality, release_group, script, status) VALUES
	(1617798, '054391612328', '', 0, 'a64a0467-9d7a-4ffa-90b8-d87d9b41e311', 527716, 120, '2016-03-06 22:00:23.846304+00', 'Numb/Encore', 2, -1, 828504, 28, 1),
	(839496, '093624277309', '', 0, 'ff06ca3e-3651-4406-9549-3204e8a169e5', 898731, 120, '2012-08-13 11:00:12.768226+00', 'Numb/Encore', NULL, -1, 828504, 28, 1),
	(1617798, '054391612328', '', 0, '16bee711-d7ce-48b0-adf4-51f124bcc0df', 1738247, 120, '2016-02-28 21:42:14.873583+00', 'Numb/Encore', 2, -1, 828504, 28, 1);
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '8a754a16-0027-3a29-b6d7-2b40ea0481ed', 221, '2013-05-16 11:06:19.67235+00', 'United Kingdom', 1),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '89a675c2-3e37-3518-b83c-418bad59a85a', 241, '2013-08-28 11:55:13.834089+00', 'Europe', NULL);
INSERT INTO country_area (area) VALUES (221), (241);
INSERT INTO area_alias (area, begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, primary_for_locale, sort_name, type) VALUES
	(221, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 14, '2013-05-16 11:06:19.67235+00', NULL, 'UK', '0', 'UK', 3),
	(222, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 29, '2013-06-15 18:06:39.59323+00', NULL, 'USA', '0', 'USA', 3),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2488, '2013-05-27 13:58:23.465634+00', 'de', 'Europa', '1', 'Europa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2489, '2013-05-27 13:58:25.819485+00', 'el', 'Ευρώπη', '1', 'Ευρώπη', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2490, '2013-05-27 13:58:28.020929+00', 'en', 'Europe', '1', 'Europe', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2491, '2013-05-27 13:58:30.219483+00', 'es', 'Europa', '1', 'Europa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2492, '2013-05-27 13:58:32.403747+00', 'et', 'Euroopa', '1', 'Euroopa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2493, '2013-05-27 13:58:34.638776+00', 'fi', 'Eurooppa', '1', 'Eurooppa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2494, '2013-05-27 13:58:37.146361+00', 'fr', 'Europe', '1', 'Europe', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2495, '2013-05-27 13:58:42.992169+00', 'it', 'Europa', '1', 'Europa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2496, '2013-05-27 13:58:45.222523+00', 'ja', 'ヨーロッパ', '1', 'ヨーロッパ', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2497, '2013-05-27 13:58:47.457719+00', 'nl', 'Europa', '1', 'Europa', NULL),
	(241, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2498, '2013-05-27 13:58:49.972578+00', 'no', 'Europa', '1', 'Europa', NULL);
INSERT INTO tag (id, name, ref_count) VALUES
	(31483, 'whatever', 2),
	(46782, 'fail', 0),
	(72194, 'un member state', 0),
	(77592, 'place', 0),
	(97721, 'united states of what?', 0);
INSERT INTO area_tag (area, count, last_updated, tag) VALUES
	(221, 1, '2014-12-14 22:15:24.890705+00', 72194),
	(221, 0, '2015-09-13 20:23:22.154214+00', 77592),
	(222, 0, '2017-05-07 19:16:22.728659+00', 46782),
	(222, 0, '2017-05-07 19:16:22.740638+00', 97721),
	(222, 0, '2017-05-07 19:16:22.748833+00', 31483),
	(222, 0, '2017-04-04 14:03:06.840487+00', 72194),
	(222, 0, '2017-04-04 14:03:05.823906+00', 77592);
INSERT INTO release_country (country, date_day, date_month, date_year, release) VALUES
	(221, NULL, NULL, 2004, 527716),
	(222, NULL, NULL, 2004, 898731),
	(241, NULL, NULL, NULL, 1738247);
INSERT INTO label (area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, label_code, last_updated, name, type) VALUES
	(222, 19, 3, 1958, '“WB” logo, with or without “records” beneath or on banner across', 0, NULL, NULL, NULL, '0', 'c595c289-47ce-4fba-b999-b87503e8cb71', 56, 392, '2017-05-09 05:06:01.683868+00', 'Warner Bros. Records', 9),
	(222, NULL, NULL, 1984, '', 0, NULL, NULL, NULL, '0', 'a92d1684-4edb-48aa-b913-30e9da213004', 1010, 8427, '2012-07-12 16:08:05.093269+00', 'Def Jam Recordings', 4),
	(222, NULL, NULL, 1996, '', 0, NULL, NULL, NULL, '0', '4cccc72a-0bd0-433a-905e-dad87871397d', 4596, NULL, '2013-11-23 07:00:19.121213+00', 'Roc‐A‐Fella Records', 4),
	(222, NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'e5600a80-fd70-4fb6-8212-1a403bcb59da', 45714, NULL, '2011-11-29 05:46:52.771734+00', 'Machine Shop Recordings', NULL);
INSERT INTO label_alias (begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, label, last_updated, locale, name, primary_for_locale, sort_name, type) VALUES
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 7424, 56, '2013-03-03 00:00:33.463659+00', NULL, 'Warner Bros', '0', 'Warner Bros', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 19598, 56, '2015-05-22 03:00:40.949705+00', NULL, 'Warner Bros. (Japan)', '0', 'Warner Bros. (Japan)', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 7877, 56, '2013-07-01 01:00:33.763259+00', NULL, 'Warner Bros Records', '0', 'Warner Bros Records', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 4221, 56, '2013-06-21 13:38:07.582347+00', NULL, 'WB Records', '0', 'WB Records', 2),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 266, 56, '2012-05-15 18:57:13.252186+00', NULL, 'Warner Brothers', '0', 'Warner Brothers', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2831, 56, '2012-05-15 18:57:13.252186+00', NULL, 'Warner Brothers Records', '0', 'Warner Brothers Records', NULL),
	(NULL, NULL, 1967, 0, NULL, NULL, 1970, '1', 16225, 56, '2014-01-24 16:18:13.429686+00', 'en', 'Warner Bros.-Seven Arts', '0', 'Warner Bros.-Seven Arts', 1),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 2349, 56, '2012-05-15 18:57:13.252186+00', NULL, 'Warner Bros UK', '0', 'Warner Bros UK', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 969, 1010, '2012-05-15 18:57:13.252186+00', NULL, 'Def Jam Records', '0', 'Def Jam Records', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 5706, 1010, '2016-09-30 21:58:25.443284+00', NULL, 'Def Jam', '0', 'Def Jam', 1);
INSERT INTO tag (id, name, ref_count) VALUES
	(11, 'electronic', 59991),
	(14, 'soundtrack', 9066),
	(15, 'classical', 10467),
	(19, 'pop', 21043),
	(29, 'progressive rock', 3633),
	(303, 'funk', 2089),
	(475, 'contemporary r b', 176),
	(623, 'score', 352),
	(1060, 'dance-pop', 33),
	(1300, 'new prog', 7);
INSERT INTO label_tag (count, label, last_updated, tag) VALUES
	(1, 56, '2015-05-22 03:00:40.949705+00', 19),
	(1, 56, '2015-05-22 03:00:40.949705+00', 29),
	(1, 56, '2015-12-30 16:18:55.681483+00', 14),
	(1, 56, '2015-12-30 16:19:01.956135+00', 623),
	(1, 56, '2015-12-30 16:19:02.832346+00', 15),
	(1, 56, '2015-05-22 03:00:40.949705+00', 1300),
	(1, 56, '2015-05-22 03:00:40.949705+00', 7),
	(1, 56, '2015-05-22 03:00:40.949705+00', 748),
	(1, 56, '2015-05-22 03:00:40.949705+00', 303),
	(1, 56, '2015-05-22 03:00:40.949705+00', 11),
	(1, 56, '2015-05-22 03:00:40.949705+00', 111),
	(1, 56, '2015-05-22 03:00:40.949705+00', 20),
	(1, 56, '2015-05-22 03:00:40.949705+00', 273),
	(0, 1010, '2016-09-15 17:32:48.531716+00', 1060),
	(3, 1010, '2012-07-12 16:08:05.093269+00', 235),
	(0, 1010, '2016-09-15 17:32:48.482479+00', 111),
	(0, 1010, '2016-09-15 17:32:54.306599+00', 19),
	(0, 1010, '2016-09-15 17:32:54.317225+00', 2349),
	(0, 1010, '2016-09-15 17:32:54.330756+00', 273),
	(0, 1010, '2016-09-15 17:32:48.503386+00', 748),
	(0, 1010, '2016-09-15 17:32:48.52049+00', 475);
INSERT INTO release_label (catalog_number, id, label, last_updated, release) VALUES
	('5439 16123-2', 1222915, 56, '2016-02-28 21:40:29.467113+00', 527716),
	(NULL, 1263696, 45714, '2016-02-28 21:40:29.467113+00', 527716),
	(NULL, 1263697, 4596, '2016-02-28 21:40:29.467113+00', 527716),
	(NULL, 1263698, 1010, '2016-02-28 21:40:29.467113+00', 527716),
	('W660CD', 1263699, NULL, '2016-02-28 21:40:29.467113+00', 527716),
	('0-42773', 718293, 56, '2012-07-30 10:18:21.120323+00', 898731),
	('0-42773', 718294, 4596, '2012-07-30 10:18:21.120323+00', 898731),
	('5439 16123-2', 1263700, 56, '2016-02-28 21:42:15.327475+00', 1738247),
	(NULL, 1263701, 45714, '2016-02-28 21:42:15.327475+00', 1738247),
	(NULL, 1263702, 4596, '2016-02-28 21:42:15.327475+00', 1738247),
	(NULL, 1263703, 1010, '2016-02-28 21:42:15.327475+00', 1738247);
INSERT INTO medium (edits_pending, format, id, last_updated, name, position, release, track_count) VALUES
	(0, 1, 527716, '2011-05-16 14:57:06.530063+00', '', 1, 527716, 2),
	(0, 31, 898731, '2012-08-13 11:00:12.592828+00', '', 1, 898731, 6),
	(0, 1, 1842217, '2016-02-28 21:42:20.708007+00', '', 1, 1738247, 2);
INSERT INTO cdtoc (created, degraded, discid, freedb_id, id, leadout_offset, track_count, track_offset) VALUES
	('2011-05-16 14:57:06.530063+00', '0', 'OKUYmpdUOPGWY0cbzyhst_g4PpQ-', '05019f02', 313549, 31328, 2, '{150,15769}'),
	('2011-05-16 14:57:06.530063+00', '0', 'NXudpL4BklH7Ke3YKkuO_oMCjAA-', '0c019c02', 404303, 31098, 2, '{150,15654}');
INSERT INTO medium_cdtoc (cdtoc, edits_pending, id, last_updated, medium) VALUES
	(313549, 0, 363095, '2011-05-16 14:57:06.530063+00', 527716),
	(404303, 0, 363096, '2011-05-16 14:57:06.530063+00', 527716),
	(404303, 0, 808349, '2016-02-28 21:42:21.68881+00', 1842217);
INSERT INTO recording (artist_credit, comment, edits_pending, gid, id, last_updated, length, name, video) VALUES
	(839496, '', 0, 'daccb724-8023-432a-854c-e0accb6c8678', 3094737, '2016-11-05 13:03:07.719162+00', 205280, 'Numb/Encore (explicit)', '0'),
	(839496, '', 0, '6ca2f30f-5c9b-4a33-b1ff-3f7f14d40486', 3094738, '2012-08-13 11:00:12.418069+00', 205346, 'Numb/Encore (radio edit)', '0'),
	(839496, '', 0, '965b75df-397d-4395-aac8-de11854c4630', 3094739, '2012-02-18 15:00:19.224421+00', 207333, 'Numb/Encore (instrumental)', '0'),
	(839496, '', 0, '53296a5c-03cc-4547-b6b2-3d047867c786', 3094740, '2012-08-13 11:00:12.453242+00', 199973, 'Numb/Encore (a cappella explicit)', '0'),
	(839496, '', 0, '62d79df4-85ba-4a7d-81ae-d9b87226520c', 3094741, '2012-08-13 11:00:12.529251+00', 199146, 'Numb/Encore (a cappella radio edit)', '0'),
	(839496, '', 0, 'c2fcd41b-450e-43f8-9b68-9e1a5763545a', 3094742, '2012-02-18 15:00:19.224421+00', 101854, 'Bonus Beat', '0');
INSERT INTO isrc (created, edits_pending, id, isrc, recording, source) VALUES
	('2012-10-28 13:59:13.850746+00', 0, 344496, 'USWB10403681', 3094737, NULL),
	('2012-10-28 13:59:13.850746+00', 0, 344497, 'USWB10403690', 3094739, NULL);
INSERT INTO recording_alias (begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, primary_for_locale, recording, sort_name, type) VALUES
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 102994, '2016-11-05 13:03:07.719162+00', NULL, 'Numb / Encore', '0', 3094737, 'Numb / Encore', NULL),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 102995, '2016-11-05 13:03:07.719162+00', NULL, 'Numb/Encore (studio version)', '0', 3094737, 'Numb/Encore (studio version)', NULL);
INSERT INTO tag (id, name, ref_count) VALUES
	(43, 'heavy metal', 3753),
	(188, 'crossover', 147),
	(1216, 'hardcore rap', 14),
	(4695, 'alternative and punk', 4997),
	(5384, 'rap-metal', 4),
	(6638, 'rap hip-hop', 75),
	(31591, 'pop-rap', 3),
	(41014, 'pop/rock', 0),
	(41016, 'nü metal', 0),
	(68530, 'pop/alternative and punk', 0);
INSERT INTO recording_tag (count, last_updated, recording, tag) VALUES
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 5384),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 43),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 62),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 31591),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 235),
	(3, '2016-11-05 13:03:07.719162+00', 3094737, 4695),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 41016),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 188),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 150),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 19),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 1277),
	(2, '2016-11-05 13:03:07.719162+00', 3094737, 1216),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 41014),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 68530),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 48881),
	(2, '2016-11-05 13:03:07.719162+00', 3094737, 1072),
	(1, '2016-11-05 13:03:07.719162+00', 3094737, 6638),
	(1, '2011-05-16 16:08:20.288158+00', 3094738, 564);
INSERT INTO artist_credit (artist_count, created, id, name, ref_count) VALUES
	(1, '2011-05-16 16:32:11.963929+00', 167, 'Jay-Z', 2285),
	(1, '2011-05-16 16:32:11.963929+00', 11330, 'Linkin Park', 4948);
INSERT INTO artist_credit_name (artist, artist_credit, join_phrase, name, position) VALUES
	(167, 167, '', 'Jay-Z', 0),
	(11330, 11330, '', 'Linkin Park', 0);
INSERT INTO recording (artist_credit, comment, edits_pending, gid, id, last_updated, length, name, video) VALUES
	(11330, '', 0, '352dd518-23cd-4c5a-9551-ba02097b177b', 1047153, '2017-02-20 20:02:04.906066+00', 187520, 'Numb', '0'),
	(167, '', 0, '77349c88-a20f-479e-ba3d-7be0c6af0290', 1576549, NULL, 253026, 'Encore', '0');
INSERT INTO isrc (created, edits_pending, id, isrc, recording, source) VALUES
	('2011-05-16 16:08:20.288158+00', 0, 16160, 'USWB10300474', 1047153, 0),
	('2011-05-16 16:08:20.288158+00', 0, 157665, 'USDJ20301455', 1576549, 0);
INSERT INTO tag (id, name, ref_count) VALUES
	(783, 'post-grunge', 80),
	(2311, 'rap hip hop', 189),
	(4872, 'hip hop rap', 4264),
	(6643, 'rap-rock', 31),
	(25579, 'east coast rap', 85);
INSERT INTO recording_tag (count, last_updated, recording, tag) VALUES
	(2, '2017-02-20 20:02:04.906066+00', 1047153, 41014),
	(4, '2017-02-20 20:02:04.906066+00', 1047153, 4695),
	(3, '2017-02-20 20:02:04.906066+00', 1047153, 1072),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 1102),
	(2, '2017-02-20 20:02:04.906066+00', 1047153, 349),
	(2, '2017-02-20 20:02:04.906066+00', 1047153, 564),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 6643),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 1277),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 783),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 5384),
	(1, '2017-02-20 20:02:04.906066+00', 1047153, 43),
	(2, '2016-11-14 15:25:46.370904+00', 1576549, 1216),
	(5, '2016-11-14 15:25:50.551329+00', 1576549, 25579),
	(2, '2016-11-14 15:25:57.132775+00', 1576549, 4872),
	(1, '2016-11-14 15:25:48.457426+00', 1576549, 1182),
	(2, '2016-11-14 15:25:38.139244+00', 1576549, 2311),
	(1, '2016-11-14 15:25:42.589753+00', 1576549, 235),
	(1, '2016-11-14 15:25:47.075787+00', 1576549, 49117),
	(1, '2016-11-14 15:26:00.112337+00', 1576549, 48881),
	(1, '2012-04-11 04:24:28.371175+00', 1576549, 62);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 27070, 232);
INSERT INTO l_recording_recording (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 3094737, '', 1047153, '', 26376, '2017-02-20 20:02:04.906066+00', 27070, 0),
	(0, 3094737, '', 1576549, '', 34575, '2016-11-05 13:03:07.719162+00', 27070, 0);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(NULL, NULL, NULL, NULL, NULL, '', 0, NULL, NULL, NULL, NULL, '0', 1, 'fe0049c6-efe4-4582-ad8c-5ef9d8e9d404', 240341, '2015-05-10 03:58:14.312035+00', 'DJ Tripp', 'Tripp, DJ', 1);
INSERT INTO artist_alias (artist, begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, primary_for_locale, sort_name, type) VALUES
	(240341, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 37900, '2012-05-15 18:57:13.252186+00', NULL, 'www.bass211.com', '0', 'www.bass211.com', NULL);
INSERT INTO tag (id, name, ref_count) VALUES
	(5477, 'mash-up', 10);
INSERT INTO artist_tag (artist, count, last_updated, tag) VALUES
	(240341, 1, '2011-05-16 14:57:06.530063+00', 5477);
INSERT INTO artist_credit (artist_count, created, id, name, ref_count) VALUES
	(1, '2011-05-16 16:32:11.963929+00', 240341, 'DJ Tripp', 204);
INSERT INTO artist_credit_name (artist, artist_credit, join_phrase, name, position) VALUES
	(240341, 240341, '', 'DJ Tripp', 0);
INSERT INTO recording (artist_credit, comment, edits_pending, gid, id, last_updated, length, name, video) VALUES
	(240341, '', 0, 'acd0a208-5cb2-4e58-9908-93f47dd29ec0', 4020427, NULL, 271000, 'Numb Phone ''Core (Jay-Z & Linkin Park vs. CAKE)', '0'),
	(240341, '', 0, '9ae97674-af2e-4617-b3ca-1017a1eeec08', 4408077, NULL, 233000, 'Encore Blitz (Jay-Z vs. Linkin Park vs. Sweet)', '0');
INSERT INTO l_recording_recording (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 4020427, '', 3094741, '', 26589, '2011-05-16 16:08:20.288158+00', 27070, 0),
	(0, 4408077, '', 3094741, '', 26635, '2011-05-16 16:08:20.288158+00', 27070, 0);
INSERT INTO track (artist_credit, edits_pending, gid, id, is_data_track, last_updated, length, medium, name, number, position, recording) VALUES
	(839496, 0, '13aa9571-c0a0-3aaf-8159-9511658e5978', 7878846, '0', '2015-12-01 12:52:02.514747+00', 208253, 527716, 'Numb/Encore (explicit)', '1', 1, 3094737),
	(839496, 0, '8f0abcc1-0ec0-3427-9e3e-925ee1e5b3e6', 7878847, '0', '2015-12-01 12:52:02.514747+00', 207453, 527716, 'Numb/Encore (instrumental)', '2', 2, 3094739),
	(839496, 0, '4ee0419b-382e-3773-8692-5c76917677af', 13038509, '0', '2015-05-03 09:12:06.570954+00', 205346, 898731, 'Numb/Encore (explicit)', 'A1', 1, 3094737),
	(839496, 0, 'e313e7f2-1a1f-3315-a1c1-471a1063e872', 13038510, '0', '2015-05-03 09:12:06.570954+00', 205346, 898731, 'Numb/Encore (radio edit)', 'A2', 2, 3094738),
	(839496, 0, '8b202e60-22bf-322e-91ac-5325e1b84a7b', 13038511, '0', '2015-05-03 09:12:06.570954+00', 207333, 898731, 'Numb/Encore (instrumental)', 'A3', 3, 3094739),
	(839496, 0, '2c9a1e43-8337-30bb-b216-4a41c15049f4', 13038512, '0', '2015-05-03 09:12:06.570954+00', 199973, 898731, 'Numb/Encore (a cappella explicit)', 'B1', 4, 3094740),
	(839496, 0, 'e770d30f-e9e3-3169-9ba8-4cd0a1e0c789', 13038513, '0', '2015-05-03 09:12:06.570954+00', 199146, 898731, 'Numb/Encore (a cappella radio edit)', 'B2', 5, 3094741),
	(839496, 0, 'e6fb8730-5ea4-3ad3-8ae4-3fc2a199c6cb', 13038514, '0', '2015-05-03 09:12:06.570954+00', 101854, 898731, 'Bonus Beat', 'B3', 6, 3094742),
	(1617798, 0, 'dfe024b2-95b2-453f-b03e-3b9fa06f44e6', 20280427, '0', '2016-02-28 21:42:20.708007+00', 207000, 1842217, 'Numb/Encore (explicit)', '1', 1, 3094737),
	(1617798, 0, '4fd6d4b0-0d14-428a-a554-1052060a9a27', 20280428, '0', '2016-02-28 21:42:20.708007+00', 206000, 1842217, 'Numb/Encore (instrumental)', '2', 2, 3094739);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, '519759d7-fa20-42a6-8f2c-817f037ec4f9', 381384, '2016-10-11 22:00:02.072184+00', 'https://www.amazon.co.uk/gp/product/B0006I92LO'),
	(0, 'c7cc8274-b556-419c-b8ce-c3edb7426e08', 1451353, '2016-07-28 07:00:02.312024+00', 'https://www.discogs.com/release/368417'),
	(0, '96539c19-171e-41b9-92f3-052e301d2864', 1451354, '2016-07-28 07:00:02.312024+00', 'https://www.discogs.com/release/755049'),
	(0, '0e08938b-2e4f-4bee-a468-64f3aae97bba', 1696815, '2016-10-24 17:00:02.326542+00', 'https://www.amazon.com/gp/product/B0006GAOIG'),
	(0, 'b14d632a-cdb4-4d1f-b951-3ce847269002', 3538570, '2016-08-22 14:00:01.773206+00', 'https://www.discogs.com/release/609699');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6300, 77),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6301, 76);
INSERT INTO l_release_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 527716, '', 381384, '', 179489, '2011-05-16 16:31:52.155025+00', 6300, 0),
	(0, 527716, '', 1451353, '', 827850, '2012-08-13 11:00:11.967375+00', 6301, 0),
	(0, 898731, '', 1451354, '', 827851, '2012-08-13 11:00:12.20608+00', 6301, 0),
	(0, 898731, '', 1696815, '', 907256, '2013-05-10 16:55:49.676826+00', 6300, 0),
	(0, 1738247, '', 381384, '', 1411292, '2016-02-28 21:42:27.502195+00', 6300, 0),
	(0, 1738247, '', 3538570, '', 1411293, '2016-02-28 21:42:27.502195+00', 6301, 0);


-- Place d71ffe38-5eaf-426b-9a2e-e1f21bc84609 (Suisto)
INSERT INTO area (id, gid, name, type, edits_pending, last_updated, begin_date_year, begin_date_month, begin_date_day, end_date_year, end_date_month, end_date_day, ended, comment) VALUES
    (9598, '4479c385-74d8-4a2b-bdab-f48d1e6969ba', 'Hämeenlinna', 3, 0, '2013-11-26 12:59:48.472546+00', NULL, NULL, NULL, NULL, NULL, NULL, 'f', '');
INSERT INTO place (address, area, begin_date_day, begin_date_month, begin_date_year, comment, coordinates, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	('Verkatehtaankuja 7, FI-13200 Hämeenlinna, Finland', 9598, NULL, NULL, 2009, '', '(60.997758,24.477142)', 0, NULL, NULL, NULL, '0', 'd71ffe38-5eaf-426b-9a2e-e1f21bc84609', 955, '2013-11-08 19:31:00.585275+00', 'Suisto', 2);
INSERT INTO place_alias (begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, place, primary_for_locale, sort_name, type) VALUES
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 202, '2013-10-17 18:48:42.974373+00', NULL, 'Suistoklubi', 955, '0', 'Suistoklubi', 1),
	(NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 204, '2013-10-17 18:49:57.33084+00', NULL, 'Suisto-klubi', 955, '0', 'Suisto-klubi', NULL);
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '6a264f94-6ff1-30b1-9a81-41f7bfabd616', 72, '2013-05-27 12:46:50.235044+00', 'Finland', 1);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(72, NULL, NULL, NULL, NULL, '', 0, NULL, NULL, NULL, NULL, '0', 1, '4c5ec3e4-b63a-4066-955b-f7cb96a3de38', 623448, '2013-09-01 10:37:33.781719+00', 'Tommi Kurki', 'Kurki, Tommi', 1);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2013-10-17 18:47:21.778747+00', NULL, NULL, NULL, '0', 133815, 703);
INSERT INTO l_artist_place (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 623448, '', 955, '', 14, '2013-10-17 18:47:21.778747+00', 133815, 0);
INSERT INTO place (address, area, begin_date_day, begin_date_month, begin_date_year, comment, coordinates, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	('Paasikiventie 2, FI-13200 Hämeenlinna, Finland', 9598, NULL, NULL, NULL, '', '(60.99727,24.47651)', 0, NULL, NULL, NULL, '0', 'f9587914-8505-4bd1-833b-16a3100a4948', 734, '2013-10-17 15:06:03.748156+00', 'Verkatehdas', 2);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2013-11-10 22:08:15.777261+00', NULL, NULL, NULL, '0', 138113, 717);
INSERT INTO l_place_place (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 734, '', 955, '', 47, '2013-11-12 08:20:50.390599+00', 138113, 0);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, '7462ea62-7439-47f7-93bc-a425d1d989e8', 2003126, '2013-10-17 18:46:57.796474+00', 'http://www.suisto.fi/'),
	(0, '8de22e00-c8e8-475f-814e-160ef761da63', 2003133, '2013-10-17 18:48:25.608609+00', 'https://twitter.com/Suisto'),
	(0, '64bd3c1a-2c10-4d28-b9ef-ed284f5c0c40', 2003161, '2013-10-17 18:54:21.820148+00', 'http://www.last.fm/venue/8998267+Suisto-klubi');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2013-10-17 14:56:42.321443+00', NULL, NULL, NULL, '0', 133735, 363),
	(0, NULL, NULL, NULL, '2013-10-17 15:06:28.5838+00', NULL, NULL, NULL, '0', 133745, 429),
	(0, NULL, NULL, NULL, '2015-02-09 23:20:47.97858+00', NULL, NULL, NULL, '0', 216420, 837);
INSERT INTO l_place_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 955, '', 2003126, '', 502, '2013-10-17 18:46:57.810843+00', 133735, 0),
	(0, 955, '', 2003133, '', 507, '2013-10-17 18:48:25.619968+00', 133745, 0),
	(0, 955, '', 2003161, '', 512, '2015-02-11 22:52:12.353838+00', 216420, 0);


-- Event 6a25401c-77e4-4eef-b853-3ee3aaf0c043 (The Spyro at Suisto)
INSERT INTO event (begin_date_day, begin_date_month, begin_date_year, cancelled, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, setlist, time, type) VALUES
	(29, 5, 2009, '0', '', 0, 29, 5, 2009, '1', '6a25401c-77e4-4eef-b853-3ee3aaf0c043', 1066, '2014-12-01 17:01:50.374401+00', 'The Spyro at Suisto', '', NULL, 1);
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '39d62198-1e76-4de4-b079-e86e3a393bbc', 7713, '2013-11-26 12:07:54.977144+00', 'Helsinki', 3);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(72, 7713, NULL, NULL, 2007, '', 0, NULL, NULL, NULL, NULL, '0', NULL, '59b55c37-cb82-4c18-a805-49f486d8a1ae', 583723, '2013-07-11 18:18:11.615597+00', 'The Spyro', 'Spyro, The', 2);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2014-11-17 21:50:26.032977+00', NULL, NULL, NULL, '0', 199467, 798);
INSERT INTO l_artist_event (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 583723, '', 1066, '', 339, '2014-11-18 09:53:40.704356+00', 199467, 0);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2014-11-17 22:04:26.319871+00', NULL, NULL, NULL, '0', 199471, 794);
INSERT INTO l_event_place (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 1066, '', 955, '', 303, '2014-11-18 09:53:40.704356+00', 199471, 0);


-- Release Group fc40043d-0584-4402-ac6a-91b02a1d20c0 (Hybrid Theory EP)
INSERT INTO release_group (artist_credit, comment, edits_pending, gid, id, last_updated, name, type) VALUES
	(11330, '', 0, 'ed3e5734-7a24-32ae-9da0-c6c4b3057109', 100229, '2009-05-24 20:47:00.490177+00', 'Hybrid Theory EP', 3);
INSERT INTO tag (id, name, ref_count) VALUES
	(127, 'blues', 8831),
	(267, 'reggae', 3145);
INSERT INTO release_group_tag (count, last_updated, release_group, tag) VALUES
	(2, '2012-10-20 04:50:27.445116+00', 100229, 3295),
	(1, '2011-05-16 15:44:23.970762+00', 100229, 349),
	(1, '2011-05-16 15:44:23.970762+00', 100229, 267),
	(3, '2012-10-20 04:50:27.445116+00', 100229, 127),
	(2, '2016-12-29 22:38:37.145694+00', 100229, 1072);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, '027ebd3b-040b-4a34-af2d-c8a6314587fb', 1082523, '2016-10-20 07:00:02.164438+00', 'https://en.wikipedia.org/wiki/Hybrid_Theory_(EP)'),
	(0, '7c057bee-5a96-4561-9878-debda6ee1c5e', 1862138, '2016-06-29 16:00:02.367431+00', 'https://www.wikidata.org/wiki/Q19997');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2013-05-09 09:56:17.113888+00', NULL, NULL, NULL, '0', 117677, 353);
INSERT INTO l_release_group_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 100229, '', 1082523, '', 119650, '2012-01-07 22:25:29.107893+00', 6303, 0),
	(0, 100229, '', 1862138, '', 241411, '2013-07-30 06:41:45.946438+00', 117677, 0);
INSERT INTO release_packaging (id, name, parent, child_order, description, gid) VALUES (7, 'None', NULL, 2, NULL, '119eba76-b343-3e02-a292-f0f00644bb9b');
INSERT INTO release (artist_credit, barcode, comment, edits_pending, gid, id, language, last_updated, name, packaging, quality, release_group, script, status) VALUES
	(11330, '', '', 0, 'fc40043d-0584-4402-ac6a-91b02a1d20c0', 43210, 120, '2014-06-16 03:00:23.190656+00', 'Hybrid Theory EP', NULL, -1, 100229, 28, 1),
	(11330, NULL, 'with bonus track', 0, '49808b24-d94f-4714-9337-5340b3a8ae34', 1081253, 120, '2012-02-03 11:24:55.092023+00', 'Hybrid Theory EP', NULL, -1, 100229, 28, 1),
	(11330, '', '', 0, 'ed397e4b-b59b-4c87-99fa-d6adc501f72c', 1868030, 120, '2017-01-29 11:00:29.441076+00', 'Hybrid Theory EP', 7, -1, 100229, 28, 1);
INSERT INTO release_unknown_country (date_day, date_month, date_year, release) VALUES
	(NULL, NULL, 2000, 1081253);
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '525d4e18-3d00-31b9-a58b-a146a916de8f', 240, '2013-08-28 11:55:07.839087+00', '[Worldwide]', NULL);
INSERT INTO country_area (area) VALUES (240);
INSERT INTO tag (id, name, ref_count) VALUES
	(72193, 'special purpose area', 0);
INSERT INTO area_tag (area, count, last_updated, tag) VALUES
	(240, 1, '2016-12-10 22:44:41.918894+00', 72193);
INSERT INTO release_country (country, date_day, date_month, date_year, release) VALUES
	(240, NULL, NULL, NULL, 1868030);
INSERT INTO label (area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, label_code, last_updated, name, type) VALUES
	(NULL, NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '65c45c6b-265c-49f6-b0ed-5c878d1ba2c1', 92190, NULL, '2014-06-04 21:00:34.599873+00', 'Mix Media Entertainment', NULL);
INSERT INTO release_label (catalog_number, id, label, last_updated, release) VALUES
	(NULL, 968145, 92190, '2014-05-28 20:24:57.5997+00', 43210);
INSERT INTO medium (edits_pending, format, id, last_updated, name, position, release, track_count) VALUES
	(0, 1, 43210, '2011-07-15 17:23:08.358374+00', '', 1, 43210, 6),
	(0, 1, 1087376, '2011-10-06 10:24:35.334618+00', '', 1, 1081253, 7),
	(0, 12, 1991164, '2016-11-29 19:37:22.597458+00', '', 1, 1868030, 6);
INSERT INTO cdtoc (created, degraded, discid, freedb_id, id, leadout_offset, track_count, track_offset) VALUES
	('2011-05-16 14:57:06.530063+00', '0', '9wAvenIQov8am.1DcB1nrH80mx4-', '4806a106', 60795, 127480, 6, '{150,13677,16682,34327,54615,70382}');
INSERT INTO medium_cdtoc (cdtoc, edits_pending, id, last_updated, medium) VALUES
	(60795, 0, 63301, '2011-05-16 14:57:06.530063+00', 43210);
INSERT INTO recording (artist_credit, comment, edits_pending, gid, id, last_updated, length, name, video) VALUES
	(11330, '', 0, '7b75082c-0b20-48a6-a68f-bf804c8cd5a9', 854539, '2016-11-29 19:37:22.597458+00', 180360, 'Carousel', '0'),
	(11330, '', 0, '5c063bfc-4f8d-4b2a-83c9-b1981218c7f6', 854540, NULL, 40066, 'Technique', '0'),
	(11330, '', 0, '8b109c2b-bf04-411f-82d1-9f0aac62c804', 854541, '2016-11-29 19:37:22.597458+00', 235266, 'Step Up', '0'),
	(11330, '', 0, '5133f536-102d-4da5-889d-d928cb2f27ab', 854542, '2014-04-15 07:15:07.731885+00', 271000, 'And One', '0'),
	(11330, '', 0, '171cfd93-4850-4775-af7c-2597f0a4d2b5', 854543, NULL, 210226, 'High Voltage', '0'),
	(11330, '', 0, '830880f3-781e-44a6-b696-7968cbb9c19b', 854544, NULL, 761306, 'Part of Me', '0'),
	(11330, '', 0, '0112fc09-65d6-4f2b-a93d-e59c7098191e', 12811497, '2014-04-24 14:45:26.837896+00', 220000, 'Ambient', '0');
INSERT INTO isrc (created, edits_pending, id, isrc, recording, source) VALUES
	('2017-06-04 15:19:20.967316+00', 0, 759278, 'USWB10807730', 854542, NULL),
	('2017-06-04 15:19:20.967316+00', 0, 759281, 'USWB10807734', 854544, NULL);
INSERT INTO tag (id, name, ref_count) VALUES
	(31004, 'alt metal', 97);
INSERT INTO recording_tag (count, last_updated, recording, tag) VALUES
	(2, '2012-10-20 04:50:29.490406+00', 854539, 3295),
	(1, '2012-07-01 22:04:43.3075+00', 854539, 41014),
	(2, '2016-12-29 22:38:37.226029+00', 854539, 1072),
	(2, '2012-10-20 04:50:28.095356+00', 854540, 127),
	(1, '2013-12-27 19:57:18.165907+00', 854540, 1072),
	(2, '2016-12-29 22:38:37.582179+00', 854541, 1072),
	(4, '2012-10-20 04:50:31.181734+00', 854541, 127),
	(1, '2011-05-16 16:08:20.288158+00', 854542, 267),
	(2, '2012-10-20 04:50:33.150634+00', 854542, 41014),
	(1, '2013-12-27 19:57:23.768651+00', 854542, 1072),
	(1, '2012-07-01 22:04:43.783571+00', 854543, 41014),
	(1, '2011-05-16 16:08:20.288158+00', 854543, 31004),
	(2, '2016-12-29 22:38:37.246961+00', 854543, 1072),
	(1, '2013-12-27 19:57:22.183819+00', 854544, 1072),
	(1, '2012-07-01 21:26:31.832504+00', 854544, 41014),
	(2, '2012-10-20 04:50:31.828153+00', 854544, 127);
INSERT INTO track (artist_credit, edits_pending, gid, id, is_data_track, last_updated, length, medium, name, number, position, recording) VALUES
	(11330, 0, 'ad581e23-42c7-3d89-8b79-e2f4a9c5b9d8', 754132, '0', '2011-05-16 16:08:20.288158+00', 180360, 43210, 'Carousel', '1', 1, 854539),
	(11330, 0, 'e65b648f-91cc-300e-bafe-30985aa15085', 754133, '0', '2011-05-16 16:08:20.288158+00', 40066, 43210, 'Technique', '2', 2, 854540),
	(11330, 0, 'd081135d-5923-391f-b957-ee1eeb921f1b', 754134, '0', '2011-05-16 16:08:20.288158+00', 235266, 43210, 'Step Up', '3', 3, 854541),
	(11330, 0, '7a035553-ce68-3f09-9c55-c1e4094527f7', 754135, '0', '2011-05-16 16:08:20.288158+00', 270506, 43210, 'And One', '4', 4, 854542),
	(11330, 0, '37794fdb-053f-3290-a551-7ac01d9ce0f1', 754136, '0', '2011-05-16 16:08:20.288158+00', 210226, 43210, 'High Voltage', '5', 5, 854543),
	(11330, 0, 'aeeabad1-c244-3fec-81bd-25b816fbb1fe', 754137, '0', '2011-05-16 16:08:20.288158+00', 761306, 43210, 'Part of Me', '6', 6, 854544),
	(11330, 0, 'f6bb394b-d366-3c47-8ca7-ad4490c63279', 11244562, '0', '2011-10-06 10:24:34.967931+00', 180000, 1087376, 'Carousel', '1', 1, 854539),
	(11330, 0, 'bc395998-a941-34d7-b921-2946001ee1cd', 11244563, '0', '2011-10-06 10:24:34.967931+00', 40000, 1087376, 'Technique', '2', 2, 854540),
	(11330, 0, 'd68d52c9-d4c3-3bfc-93d7-ecba566a0322', 11244564, '0', '2011-10-06 10:24:34.967931+00', 235000, 1087376, 'Step Up', '3', 3, 854541),
	(11330, 0, 'd10ebc01-b3a8-3a5f-9deb-c0ff974d9702', 11244565, '0', '2011-10-06 10:24:34.967931+00', 271000, 1087376, 'And One', '4', 4, 854542),
	(11330, 0, 'b0855217-b2b4-31f4-bc9b-b66e5ee09458', 11244566, '0', '2011-10-06 10:24:34.967931+00', 210000, 1087376, 'High Voltage', '5', 5, 854543),
	(11330, 0, '303aaf43-f949-3cee-bd31-e39818873c52', 11244567, '0', '2011-10-06 10:24:34.967931+00', 230000, 1087376, 'Part of Me', '6', 6, 854544),
	(11330, 0, '62cdcc1d-0551-3d2e-b499-4411a06e9196', 11244568, '0', '2011-10-06 10:24:34.967931+00', 220000, 1087376, 'Ambient', '7', 7, 12811497),
	(11330, 0, 'f11cdeb2-258d-44dc-9c0c-99800880d275', 21817172, '0', '2016-11-29 19:37:22.597458+00', 180360, 1991164, 'Carousel', '1', 1, 854539),
	(11330, 0, '4c11491e-ac44-4dfa-b782-3aa8cf0937c3', 21817173, '0', '2016-11-29 19:37:22.597458+00', 40066, 1991164, 'Technique', '2', 2, 854540),
	(11330, 0, '9f97f09b-73fb-4cd8-8509-91833f31adc1', 21817174, '0', '2016-11-29 19:37:22.597458+00', 235266, 1991164, 'Step Up', '3', 3, 854541),
	(11330, 0, '27d4b8f8-1c0a-4443-88da-d06fb83fe92e', 21817175, '0', '2016-11-29 19:37:22.597458+00', 270000, 1991164, 'And One', '4', 4, 854542),
	(11330, 0, '1cc1d00d-1ad7-450f-8734-61a127d5bcb4', 21817176, '0', '2016-11-29 19:37:22.597458+00', 210226, 1991164, 'High Voltage', '5', 5, 854543),
	(11330, 0, '3f6f44f2-5166-4f65-84a1-4d9dac757f48', 21817177, '0', '2016-11-29 19:37:22.597458+00', 761306, 1991164, 'Part of Me', '6', 6, 854544);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(222, 22398, 11, 2, 1977, '', 0, NULL, NULL, NULL, NULL, '0', 1, 'c262b6bf-be56-4b26-bceb-42d7a27342f3', 242895, '2015-10-13 20:49:27.118143+00', 'Mike Shinoda', 'Shinoda, Mike', 1);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 34, 19);
INSERT INTO l_artist_release (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 242895, '', 43210, '', 215024, '2011-05-16 15:59:00.785958+00', 34, 0);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, '16ae1418-327e-433a-b152-53807777d210', 2535313, '2016-07-20 11:00:02.331746+00', 'https://www.discogs.com/release/1329398'),
	(0, 'b4e5b940-b290-4618-a0a9-de6cf3e5e25e', 3985650, '2016-11-29 19:37:26.542622+00', 'https://linkinpark.com/lpu/store/music/10803/lpu-1-digital-download');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6313, 74);
INSERT INTO l_release_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 43210, '', 2535313, '', 1038731, '2014-06-04 20:00:30.671924+00', 6301, 0),
	(0, 1868030, '', 3985650, '', 1602713, '2016-11-29 19:37:26.542622+00', 6313, 0);

-- Artist f59c5520-5f46-4d2c-b2c4-822eabf53419 (Linkin Park)
INSERT INTO area (begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, last_updated, name, type) VALUES
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', '7f1c8f3f-69a9-454a-8633-c3d3a628858b', 7731, '2013-05-29 00:16:15.445612+00', 'Phoenix', 3),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'e96f1c0d-721b-470d-a9c4-0aa2d89cf9e7', 9399, '2013-10-31 14:26:38.708115+00', 'Dallas', 3),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'e1d6ca52-681b-4868-8562-41521756bb3f', 22353, '2013-08-10 21:33:00.198199+00', 'Calabasas', 3),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'cb697c4e-6769-4cdb-909c-84e2e39f4a6a', 82611, '2013-12-04 03:01:08.958545+00', 'Plymouth', 3),
	(NULL, NULL, NULL, '', 0, NULL, NULL, NULL, '0', 'ca8b6e80-20e6-4890-a73d-d449d695687e', 116001, '2015-12-14 01:45:35.132805+00', 'Agoura', 3);
INSERT INTO artist (area, begin_area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_area, end_date_day, end_date_month, end_date_year, ended, gender, gid, id, last_updated, name, sort_name, type) VALUES
	(222, 7731, 20, 3, 1976, '', 0, NULL, NULL, NULL, NULL, '0', 1, '415e30a0-116b-4a4f-8cbf-8d0f6406bbab', 72885, '2015-10-13 21:57:03.405169+00', 'Chester Bennington', 'Bennington, Chester', 1),
	(222, 9399, 15, 3, 1977, '', 0, NULL, NULL, NULL, NULL, '0', 1, 'd07bca29-d980-4100-8cad-065a05f2b343', 242899, '2017-04-24 08:55:49.123565+00', 'Joseph “Joe” Hahn', 'Hahn, Joseph “Joe”', 1),
	(222, 22353, 20, 1, 1979, '', 0, NULL, NULL, NULL, NULL, '0', 1, 'f1dd0051-5578-45a7-a733-03113626407f', 242910, '2015-10-13 21:46:26.991639+00', 'Rob Bourdon', 'Bourdon, Rob', 1),
	(NULL, NULL, NULL, NULL, NULL, '', 0, NULL, NULL, NULL, NULL, '0', NULL, 'bd16f10c-e794-4c82-9f38-5f5c3e0f00ad', 532089, NULL, 'Scott Koziol', 'Koziol, Scott', 1),
	(222, 116001, 1, 12, 1977, '', 0, NULL, NULL, NULL, NULL, '0', 1, '2d4a1dd1-2cd8-4553-bf0b-74b8c9179633', 777393, '2015-12-14 01:46:13.189682+00', 'Brad Delson', 'Delson, Brad', 1),
	(222, NULL, NULL, NULL, NULL, 'ex-singer of Linkin Park and manager of the band Taproot', 0, NULL, NULL, NULL, NULL, '0', 1, '6bfe9806-b477-4750-8bd2-b1d0acf901a9', 963656, '2015-10-13 22:29:45.372324+00', 'Mark Wakefield', 'Wakefield, Mark', 1),
	(222, 82611, 8, 2, 1977, '', 0, NULL, NULL, NULL, NULL, '0', 1, 'c8975bbf-2778-47ae-accf-c584e644450d', 963657, '2015-10-20 22:00:41.915661+00', 'Dave Farrell', 'Farrell, Dave', 1),
	(NULL, NULL, NULL, NULL, NULL, 'former member of Linkin Park', 0, NULL, NULL, NULL, NULL, '0', NULL, 'a3e595fe-342e-448b-9dc2-8d5c777a930d', 984416, '2013-03-05 13:18:04.415442+00', 'Kyle Christener', 'Christener, Kyle', 1),
	(222, NULL, 22, 9, 1979, 'High Def', 0, NULL, NULL, NULL, NULL, '0', 1, '5c133a52-55c5-4d9e-9b70-27b863f660a1', 989670, '2013-03-27 16:13:46.564935+00', 'Jason Zenga', 'Zenga, Jason', 1);
INSERT INTO artist_alias (artist, begin_date_day, begin_date_month, begin_date_year, edits_pending, end_date_day, end_date_month, end_date_year, ended, id, last_updated, locale, name, primary_for_locale, sort_name, type) VALUES
	(72885, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 25186, '2012-05-15 18:57:13.252186+00', NULL, 'Chester Charles Bennington', '0', 'Chester Charles Bennington', NULL),
	(72885, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 22291, '2012-05-15 18:57:13.252186+00', NULL, 'Chester Bennington of Linkin Park', '0', 'Chester Bennington of Linkin Park', NULL),
	(242899, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 52653, '2012-05-15 18:57:13.252186+00', NULL, 'Joe Hahn', '0', 'Joe Hahn', NULL),
	(242899, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 67688, '2012-05-15 18:57:13.252186+00', NULL, 'Chairman Hahn', '0', 'Chairman Hahn', NULL),
	(242910, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 33469, '2015-10-13 21:44:23.312217+00', NULL, 'Robert Gregory Bourdon', '0', 'Bourdon, Robert Gregory', 2),
	(777393, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 33470, '2015-10-20 22:01:13.864757+00', NULL, 'Bradford Phillip Delson', '0', 'Delson, Bradford Phillip', 2),
	(963657, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 33471, '2015-10-20 22:00:41.915661+00', NULL, 'Phoenix Farrell', '0', 'Phoenix Farrell', NULL),
	(963657, NULL, NULL, NULL, 0, NULL, NULL, NULL, '0', 33472, '2015-10-20 22:00:41.915661+00', NULL, 'David Michael Farrell', '0', 'Farrell, David Michael', 2);
INSERT INTO tag (id, name, ref_count) VALUES
	(4916, 'alternative-rock', 3),
	(56823, 'jason zenga', 0),
	(56824, 'jason zenga high def', 0),
	(56825, 'high def', 0),
	(56826, 'zenga high def', 0),
	(56827, 'jason z', 0),
	(56828, 'zenga', 0);
INSERT INTO artist_tag (artist, count, last_updated, tag) VALUES
	(72885, 1, '2017-01-14 05:21:52.669999+00', 4916),
	(777393, 1, '2015-10-20 22:01:13.864757+00', 349),
	(777393, 1, '2015-10-20 22:01:13.864757+00', 7),
	(777393, 1, '2015-10-20 22:01:13.864757+00', 20),
	(777393, 1, '2015-10-20 22:01:13.864757+00', 92),
	(777393, 1, '2015-10-20 22:01:13.864757+00', 111),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56823),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56824),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56825),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56826),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56827),
	(989670, 1, '2013-03-21 21:12:20.793353+00', 56828);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, 1996, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6356, 103),
	(0, NULL, NULL, 1996, '2011-05-16 15:03:23.368437+00', NULL, NULL, 1998, '1', 6462, 103),
	(0, NULL, NULL, 2001, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6490, 103),
	(0, NULL, NULL, 1998, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6555, 103),
	(0, NULL, NULL, 1999, '2011-05-16 15:03:23.368437+00', NULL, NULL, 1999, '1', 6588, 103),
	(0, NULL, NULL, 2000, '2011-05-16 15:03:23.368437+00', NULL, NULL, 2001, '1', 6761, 103),
	(1, NULL, NULL, 1996, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 6999, 103),
	(0, 17, 1, 2004, '2013-04-27 20:30:33.260494+00', NULL, NULL, NULL, '0', 116242, 104);
INSERT INTO link_attribute (attribute_type, created, link) VALUES
	(525, '2011-05-16 15:03:23.368437+00', 6999);
INSERT INTO l_artist_artist (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 963657, 'David Michael Farrell', 11330, '', 117611, '2015-10-20 22:00:41.915661+00', 6462, 0),
	(0, 242899, '', 11330, '', 117757, '2013-03-12 14:00:11.518172+00', 6356, 0),
	(0, 242895, '', 11330, '', 118044, '2013-03-12 14:00:11.552523+00', 6999, 0),
	(0, 242910, '', 11330, '', 118213, '2013-03-12 14:00:11.269262+00', 6999, 0),
	(0, 777393, 'Bradford Phillip Delson', 11330, '', 118959, '2015-10-20 22:01:13.864757+00', 6999, 0),
	(0, 72885, '', 11330, '', 124796, '2013-03-12 14:00:10.901986+00', 6555, 0),
	(0, 963657, 'David Michael Farrell', 11330, '', 212459, '2015-10-20 22:00:41.915661+00', 6490, 0),
	(0, 963656, '', 11330, '', 212460, '2013-03-12 14:00:11.883629+00', 6462, 0),
	(0, 984416, '', 11330, '', 212461, '2013-03-12 14:00:12.679372+00', 6588, 0),
	(0, 532089, '', 11330, '', 212462, '2013-03-12 14:00:13.282821+00', 6761, 0),
	(0, 989670, '', 11330, '', 215416, '2013-05-04 21:00:14.435816+00', 116242, 0);
INSERT INTO label (area, begin_date_day, begin_date_month, begin_date_year, comment, edits_pending, end_date_day, end_date_month, end_date_year, ended, gid, id, label_code, last_updated, name, type) VALUES
	(240, NULL, NULL, 2005, '', 0, NULL, NULL, NULL, '0', '2f2b9c53-0a07-445d-aecc-129dbbafcf43', 46820, NULL, '2010-04-29 04:28:00.150357+00', 'Music for Relief', NULL);
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 12132, 116);
INSERT INTO l_artist_label (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 11330, '', 46820, '', 1492, '2011-05-16 15:03:23.368437+00', 12132, 0);
INSERT INTO url (edits_pending, gid, id, last_updated, url) VALUES
	(0, 'b34f7ca9-d7ac-42d6-9b07-c0b218eb91ff', 1674, '2016-10-23 21:00:02.435143+00', 'https://en.wikipedia.org/wiki/Linkin_Park'),
	(0, '4554d964-6e77-450b-9583-c46aa49b48ab', 4128, '2011-05-16 16:31:52+00', 'http://musicmoz.org/Bands_and_Artists/L/Linkin_Park/'),
	(0, 'df9624a2-2b78-42b5-b68a-5a96270de81f', 4858, '2012-09-17 07:41:41.144805+00', 'http://www.linkinpark.com/'),
	(0, 'bc60e163-3d91-4881-be04-44fb0edd13a9', 116639, '2016-07-24 00:00:02.174298+00', 'https://www.discogs.com/artist/40029'),
	(0, '76872769-cee5-44b5-8063-1f39c2d539df', 545230, '2013-08-07 09:00:17.042942+00', 'https://myspace.com/linkinpark'),
	(0, '9be1f37a-fbdd-47b3-9e82-21a04938b12f', 545232, '2011-05-16 16:31:52+00', 'http://www.purevolume.com/linkinparkofficial'),
	(0, '6a12c1b8-4852-4d27-badd-5bc4e632aa63', 545233, '2011-05-16 16:31:52+00', 'http://www.imdb.com/name/nm1245493/'),
	(0, '8bec97f2-c8fa-4f1d-a254-75d74e3bc0c9', 545236, '2016-10-18 23:00:01.877969+00', 'https://www.youtube.com/user/linkinparktv'),
	(0, '34be75ff-2ea5-4c60-a499-ee7b5bc2b19b', 585089, '2011-05-16 16:31:52+00', 'http://www.bbc.co.uk/music/artists/f59c5520-5f46-4d2c-b2c4-822eabf53419'),
	(0, 'a81d56bc-f38b-405e-9b54-9d06d69a6af3', 838313, '2013-03-05 02:23:28.149396+00', 'https://www.facebook.com/linkinPark'),
	(0, '33f75508-5950-41b6-9706-7b12ac3aad2f', 838314, '2011-05-16 16:31:52+00', 'http://www.last.fm/music/Linkin+Park'),
	(0, 'dd7fff80-fe44-4254-bdc5-1040351bf804', 838315, '2013-08-03 11:56:40.564693+00', 'https://twitter.com/linkinpark'),
	(0, '22369b05-7705-4a21-be65-e3aa725c34d2', 1025581, '2012-11-02 00:37:42.080284+00', 'http://www.allmusic.com/artist/mn0000289599'),
	(0, '16f23ffc-fbc8-4c50-a566-a441547bf828', 1598439, '2013-01-30 23:22:26.313497+00', 'http://viaf.org/viaf/149159156'),
	(0, '9ba5caa4-d7cd-40f4-ac5f-aa306e90e172', 1823072, '2016-06-29 06:00:02.654311+00', 'https://www.wikidata.org/wiki/Q261'),
	(0, '1a52ada1-dcc4-4ffe-a455-018cf78c8008', 2214625, '2013-11-20 05:40:24.613807+00', 'https://commons.wikimedia.org/wiki/File:LinkinParkBerlin2010.jpg'),
	(0, 'cc4dff05-d236-453c-a232-db4b486149a0', 2405726, '2014-03-04 14:34:09.662782+00', 'http://muzikum.eu/en/122-3742/linkin-park/lyrics.html'),
	(0, 'feb70509-32a4-4114-b5b1-e84eee7d4aa5', 2490385, '2014-04-26 13:06:24.81162+00', 'http://open.spotify.com/artist/6XyY86QOPPrYVGvF9ch6wz'),
	(0, '85c2e08d-81d6-48f8-a2d7-dd3757a4ac3b', 2566870, '2014-06-25 07:21:19.054793+00', 'https://soundcloud.com/linkin_park'),
	(0, 'c0718a8c-b73d-4230-ac02-e45eb90b3459', 3135829, '2015-06-07 13:21:50.933883+00', 'http://rateyourmusic.com/artist/linkin_park'),
	(0, 'cf31f668-0907-4f7d-9eaa-4af2572c3338', 3355849, '2015-11-07 09:36:14.387925+00', 'https://www.musik-sammler.de/artist/1288/'),
	(0, '45973004-87ea-4c62-a63b-f30bfa772d38', 3496310, '2016-02-03 13:36:32.786792+00', 'https://itunes.apple.com/us/artist/id148662'),
	(0, '8e9bf1dd-21c1-42a8-8f73-f18c971a938f', 3496311, '2016-02-03 13:36:32.786792+00', 'https://play.google.com/store/music/artist?id=Ac524cs4icx4xnekce4qkegkrce'),
	(0, 'd1a68faf-0bdd-4b66-aefa-8efc3e222443', 3953574, '2016-11-10 04:54:35.867461+00', 'http://genius.com/artists/Linkin-park'),
	(0, 'c2d181f6-07d1-4018-9c9e-0d4f75ab9f2d', 4139086, '2017-02-16 22:39:11.732951+00', 'https://www.deezer.com/artist/92'),
	(0, '3e019db0-83d2-4b6f-9d1a-63fbbd9c521b', 4139087, '2017-02-16 22:39:11.732951+00', 'https://www.instagram.com/linkinpark/'),
	(0, '04b6ec43-1a45-4be4-8672-4a6c23fbd6ff', 4139088, '2017-02-16 22:39:11.732951+00', 'http://linkinpark.tumblr.com/'),
	(0, 'fdef25a3-53c0-4a70-a4e9-962469ed828a', 4139089, '2017-02-16 22:39:11.732951+00', 'https://bandsintown.com/linkinpark'),
	(0, 'f1ba5022-ab72-44f9-8dcb-14b0fc3ce146', 4139090, '2017-02-16 22:39:11.732951+00', 'https://www.songkick.com/artists/96404-linkin-park'),
	(0, '71a40103-8a44-4933-9042-98db34847c3f', 4139091, '2017-02-16 22:39:11.732951+00', 'http://www.whosampled.com/Linkin-Park/'),
	(0, '19676f06-cb4e-4772-b2fb-1932ddcbcc52', 4139092, '2017-02-16 22:39:11.732951+00', 'https://imvdb.com/n/linkin-park'),
	(0, 'd7e98aaf-ed1f-40f2-aae9-8e200301e632', 4139093, '2017-02-16 22:39:11.732951+00', 'http://lyrics.wikia.com/wiki/Linkin_Park'),
	(0, 'ded05137-0a9c-4dfb-b67d-6cb675f05f4e', 4139094, '2017-02-16 22:39:11.732951+00', 'https://www.worldcat.org/identities/lccn-no2001005165/'),
	(0, 'dacc8966-1caf-4476-8cba-b784cf381c3f', 4186876, '2017-03-16 19:38:29.707047+00', 'http://www.spirit-of-metal.com/groupe-groupe-Linkin_Park-l-en.html'),
	(0, '44bd3d7a-7c44-472a-90b1-db584f579ebf', 4186877, '2017-03-16 19:38:29.707047+00', 'http://catalogue.bnf.fr/ark:/12148/cb140522494'),
	(0, '5b4b18db-2a4d-49dc-beaa-3e7e95d149cb', 4186878, '2017-03-16 19:38:29.707047+00', 'https://secondhandsongs.com/artist/11821'),
	(0, '0869188e-b6de-4ca9-845f-a44435d253c4', 4186879, '2017-03-16 19:38:29.707047+00', 'http://www.setlist.fm/setlists/linkin-park-bd6bdae.html'),
	(0, '7fab8395-8052-4633-9552-b33c560897b7', 4186880, '2017-03-16 19:38:29.707047+00', 'http://www.45cat.com/artist/linkin-park'),
	(0, '4d9fb52f-4a39-463f-83f9-fd2bd745b412', 4186881, '2017-03-16 19:38:29.707047+00', 'http://mvdbase.com/person.php?&id=A5545'),
	(0, '573163f0-d35d-4e8c-8177-4d3102c06ccb', 4186882, '2017-03-16 19:38:29.707047+00', 'http://d-nb.info/gnd/10081730-0'),
	(0, '2520c715-d2d7-4781-8631-d648c9f9ca46', 4186883, '2017-03-16 19:38:29.707047+00', 'http://soundtrackcollector.com/composer/9565/'),
	(0, '52c80a72-2a67-4be1-9333-72aca0402655', 4186884, '2017-03-16 19:38:29.707047+00', 'http://www.rolldabeats.com/artist/linkin_park');
INSERT INTO link (attribute_count, begin_date_day, begin_date_month, begin_date_year, created, end_date_day, end_date_month, end_date_year, ended, id, link_type) VALUES
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26038, 180),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26039, 189),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26040, 178),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26041, 179),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26042, 183),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26044, 173),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26046, 190),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26050, 199),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26052, 176),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26055, 193),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26056, 192),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26060, 174),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26062, 197),
	(0, NULL, NULL, NULL, '2011-05-16 15:03:23.368437+00', NULL, NULL, NULL, '0', 26316, 194),
	(0, NULL, NULL, NULL, '2011-07-28 21:05:31.894988+00', NULL, NULL, NULL, '0', 28613, 283),
	(0, NULL, NULL, NULL, '2011-10-07 02:17:24.134728+00', NULL, NULL, NULL, '0', 30134, 291),
	(0, NULL, NULL, NULL, '2012-05-28 19:09:02.61578+00', NULL, NULL, NULL, '0', 49052, 188),
	(0, NULL, NULL, NULL, '2012-12-09 16:27:34.907312+00', NULL, NULL, NULL, '0', 94979, 307),
	(0, NULL, NULL, NULL, '2013-01-30 01:44:45.99329+00', NULL, NULL, NULL, '0', 106477, 310),
	(0, NULL, NULL, NULL, '2013-05-09 09:31:21.507442+00', NULL, NULL, NULL, '0', 117675, 352),
	(0, NULL, NULL, NULL, '2014-11-19 11:04:17.874466+00', NULL, NULL, NULL, '0', 199852, 785),
	(0, NULL, NULL, NULL, '2014-12-06 03:53:52.533875+00', NULL, NULL, NULL, '0', 204138, 816),
	(0, NULL, NULL, NULL, '2015-02-03 11:01:37.730965+00', NULL, NULL, NULL, '0', 215573, 840),
	(0, NULL, NULL, NULL, '2015-05-13 21:01:19.547932+00', NULL, NULL, NULL, '0', 240791, 862);
INSERT INTO l_artist_url (edits_pending, entity0, entity0_credit, entity1, entity1_credit, id, last_updated, link, link_order) VALUES
	(0, 11330, '', 116639, '', 121118, '2011-05-16 16:31:52.155025+00', 26038, 0),
	(0, 11330, '', 545233, '', 198824, '2011-05-16 16:31:52.155025+00', 26040, 0),
	(0, 11330, '', 545230, '', 198827, '2011-05-16 16:31:52.155025+00', 26039, 0),
	(0, 11330, '', 545232, '', 199138, '2011-05-16 16:31:52.155025+00', 26060, 0),
	(0, 11330, '', 545236, '', 199293, '2011-05-16 16:31:52.155025+00', 26055, 0),
	(0, 11330, '', 4128, '', 227797, '2014-03-10 10:22:41.516608+00', 49052, 0),
	(0, 11330, '', 4858, '', 232984, '2011-05-16 16:31:52.155025+00', 26042, 0),
	(0, 11330, '', 1674, '', 236713, '2012-10-05 20:10:43.871277+00', 26041, 0),
	(0, 11330, '', 585089, '', 254489, '2011-05-16 16:31:52.155025+00', 26046, 0),
	(0, 11330, '', 838314, '', 305568, '2015-02-15 21:11:16.860621+00', 215573, 0),
	(0, 11330, '', 838313, '', 305899, '2011-05-16 16:31:52.155025+00', 26056, 0),
	(0, 11330, '', 838315, '', 306162, '2015-06-07 13:21:50.933883+00', 26056, 0),
	(0, 11330, '', 1025581, '', 369718, '2011-12-22 20:00:09.281306+00', 28613, 0),
	(0, 11330, '', 1598439, '', 576399, '2013-01-30 23:22:26.318972+00', 106477, 0),
	(0, 11330, '', 1823072, '', 677332, '2013-07-24 10:00:21.855339+00', 117675, 0),
	(0, 11330, '', 2214625, '', 778514, '2013-11-20 05:40:24.648579+00', 26044, 0),
	(0, 11330, '', 2405726, '', 841552, '2014-03-11 15:00:22.970446+00', 26062, 0),
	(0, 11330, '', 2490385, '', 875715, '2014-05-03 14:00:20.27945+00', 26316, 0),
	(0, 11330, '', 2566870, '', 906703, '2014-07-02 08:00:29.222973+00', 30134, 0),
	(0, 11330, '', 3135829, '', 1108437, '2015-06-14 14:01:15.731681+00', 49052, 0),
	(0, 11330, '', 3355849, '', 1202496, '2015-11-14 10:00:56.62288+00', 49052, 0),
	(0, 11330, '', 3496310, '', 1265049, '2016-02-03 13:36:32.786792+00', 26052, 0),
	(0, 11330, '', 3496311, '', 1265050, '2016-02-03 13:36:32.786792+00', 26052, 0),
	(0, 11330, '', 3953574, '', 1467007, '2016-11-10 04:54:35.867461+00', 26062, 0),
	(0, 11330, '', 4139086, '', 1549454, '2017-02-16 22:39:11.732951+00', 26316, 0),
	(0, 11330, '', 4139087, '', 1549455, '2017-02-16 22:39:11.732951+00', 26056, 0),
	(0, 11330, '', 4139088, '', 1549456, '2017-02-16 22:39:11.732951+00', 26050, 0),
	(0, 11330, '', 4139089, '', 1549457, '2017-02-16 22:39:11.732951+00', 240791, 0),
	(0, 11330, '', 4139090, '', 1549458, '2017-02-16 22:39:11.732951+00', 199852, 0),
	(0, 11330, '', 4139091, '', 1549459, '2017-02-16 22:39:11.732951+00', 49052, 0),
	(0, 11330, '', 4139092, '', 1549460, '2017-02-16 22:39:11.732951+00', 49052, 0),
	(0, 11330, '', 4139093, '', 1549461, '2017-02-16 22:39:11.732951+00', 26062, 0),
	(0, 11330, '', 4139094, '', 1549462, '2017-02-16 22:39:11.732951+00', 49052, 0),
	(0, 11330, '', 4186876, '', 1570559, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186877, '', 1570560, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186878, '', 1570561, '2017-03-16 19:38:29.707047+00', 94979, 0),
	(0, 11330, '', 4186879, '', 1570562, '2017-03-16 19:38:29.707047+00', 204138, 0),
	(0, 11330, '', 4186880, '', 1570563, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186881, '', 1570564, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186882, '', 1570565, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186883, '', 1570566, '2017-03-16 19:38:29.707047+00', 49052, 0),
	(0, 11330, '', 4186884, '', 1570567, '2017-03-16 19:38:29.707047+00', 49052, 0);

ALTER TABLE tag ENABLE TRIGGER delete_unused_tag;
COMMIT

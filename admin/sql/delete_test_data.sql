BEGIN;
TRUNCATE TABLE area CASCADE;
TRUNCATE TABLE script CASCADE;
TRUNCATE TABLE artist_credit CASCADE;
TRUNCATE TABLE link CASCADE;
TRUNCATE TABLE tag CASCADE;
TRUNCATE TABLE url CASCADE;
TRUNCATE TABLE release_packaging CASCADE;
TRUNCATE TABLE cdtoc CASCADE;
TRUNCATE TABLE event CASCADE;
COMMIT;

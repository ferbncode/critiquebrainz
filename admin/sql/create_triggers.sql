CREATE OR REPLACE FUNCTION check_blurb_length() RETURNS trigger AS
$CHECK_LENGTH_BODY$
BEGIN
    IF (SELECT blurb FROM review JOIN revision ON review.id=revision.review_id WHERE review.id = NEW.review_id ORDER BY timestamp DESC LIMIT 1) = 't' THEN
        IF char_length(NEW.text) > 280 OR char_length(NEW.text) IS NULL THEN
            IF (SELECT count(*) FROM revision WHERE review_id=NEW.review_id) = 0 THEN
                DELETE FROM review WHERE id=NEW.review_id;
            END IF;
            RAISE EXCEPTION 'Length of Blurb is not within the range (1 - 280)';
        END IF;
    END IF;
    RETURN NULL;
END;
$CHECK_LENGTH_BODY$ LANGUAGE plpgsql;

CREATE TRIGGER check_blurb_length AFTER INSERT ON revision FOR EACH ROW EXECUTE PROCEDURE check_blurb_length();

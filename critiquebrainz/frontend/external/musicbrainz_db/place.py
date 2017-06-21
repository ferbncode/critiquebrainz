from mbdata import models
import critiquebrainz.frontend.external.musicbrainz_db.db as mb


class Place(db.Model, models.Place):
    __bind_key__ = 'mbdata'

    @classmethod
    def get_by_id(cls, id):
        # Example function
        place = cls.query.filter_by(gid=id).first()
        return place

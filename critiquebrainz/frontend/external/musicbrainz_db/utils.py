import critiquebrainz.frontend.external.musicbrainz_db as mb
from sqlalchemy.schema import CreateSchema, DropSchema
from mbdata import models


def create_all():
    mb.engine.execute(CreateSchema('musicbrainz'))
    mb.engine.execute(CreateSchema('cover_art_archive'))
    mb.engine.execute(CreateSchema('wikidocs'))
    mb.engine.execute(CreateSchema('documentation'))
    mb.engine.execute(CreateSchema('statistics'))
    models.Base.metadata.create_all(mb.engine)


def drop_all():
    mb.engine.execute(DropSchema('musicbrainz', cascade=True))
    mb.engine.execute(DropSchema('cover_art_archive', cascade=True))
    mb.engine.execute(DropSchema('wikidocs', cascade=True))
    mb.engine.execute(DropSchema('documentation', cascade=True))
    mb.engine.execute(DropSchema('statistics', cascade=True))

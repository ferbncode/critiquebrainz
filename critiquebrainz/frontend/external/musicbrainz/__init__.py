from critiquebrainz.frontend.external.musicbrainz import ws
from critiquebrainz.frontend.external.musicbrainz import db

def init(app):
    # app.config['MB_DATABASE_ENABLED']:
    db.init_db_engine(app.config.get("MB_DATABASE_URI"))
    ws.init(
            app_name=app.config['MUSICBRAINZ_USERAGENT'] or "CritiqueBrainz Custom",
            app_version="1.0",
            hostname=app.config['MUSICBRAINZ_HOSTNAME'] or "musicbrainz.org",
        )

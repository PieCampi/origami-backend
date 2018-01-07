"""Module to populate the database with sample data."""

from sqlalchemy.orm import scoped_session, sessionmaker

from . import db
from .main_app import get_engine


def populate():
    """Populate the database with sample data."""
    engine = get_engine(memory=False)
    db.Base.metadata.create_all(engine)
    sess_maker = sessionmaker(bind=engine)
    Session = scoped_session(sess_maker)
    session = Session()

    player1 = db.PlayerDao("Gianni", 9, "male")
    player2 = db.PlayerDao("Federica", 8, "female")
    player3 = db.PlayerDao("Josh", 6, "male")

    session.add_all([player1, player2, player3])
    session.commit()
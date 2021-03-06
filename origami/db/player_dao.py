"""DAO module for the Player class."""

from sqlalchemy import Column, Integer, String, and_

from .meta import Base
from .base_dao import BaseDao
from .player_gender import PlayerGenderEnum


class PlayerDao(BaseDao, Base):
    """DAO class for Player objects."""

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String)
    allowed_genders = {enum_gender.value for enum_gender in PlayerGenderEnum}

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

        if gender not in self.allowed_genders:
            raise ValueError("Value {} not allowed for argument gender. See player_gender.py"
                             .format(gender))
        else:
            self.gender = gender

    @property
    def as_dict(self):
        """Returns a dictionary representation of the object."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }

    @classmethod
    def get_by_id(cls, player_id, session):
        """Get a single instance identified by its id."""
        query = session.query(cls).filter(cls.id == player_id)
        player = cls.get_one(query)

        return player

    @classmethod
    def get_by_profile(cls, name, age, gender, session):
        """Get a single instance identified by multiple attributes."""
        query = session.query(cls).filter(
            and_(cls.name == name, cls.age == age, cls.gender == gender))
        player = cls.get_one(query)

        return player

    @classmethod
    def get_list(cls, session):
        """Get a list of instances from the db."""
        players = session.query(cls).all()
        return players

    def __repr__(self):
        """Return a description of self."""
        return "<Player(id:{}, name:{}, age:{}, gender:{})>".format(
            self.id, self.name, self.age, self.gender)

# fare_rules.txt

from gtfs_util.static import data
from gtfs_util.static.models.base import Base
from gtfs_util.model import MixIn

from sqlalchemy import Column, types, schema


class FareRule(Base, MixIn):
    __tablename__ = 'fare_rule'
    __table_args__ = (
        # schema.ForeignKeyConstraint(['fare_id'], ['fare.id']),
        # schema.ForeignKeyConstraint(['route_id'], ['route.id']),
    )

    PREFIX = 'fare_rule_'

    NAME_MAPPING = {}
    DATA_MAPPING = {}

    FIELDS = {
        'id',
        'fare_id',
        'route_id',
        'origin_id',
        'destination_id',
        'contains_id',
    }

    id = Column(
        'id',
        types.Integer,
        primary_key=True,
    )

    fare_id = Column(
        'fare_id',
        types.String,
        nullable=False,
    )

    route_id = Column(
        'route_id',
        types.String,
        nullable=True,
    )

    origin_id = Column(
        'origin_id',
        types.String,
        nullable=True,
    )

    destination_id = Column(
        'destination_id',
        types.String,
        nullable=True,
    )

    contains_id = Column(
        'contains_id',
        types.String,
        nullable=True,
    )

from sqlalchemy import Column, String, Boolean, Integer, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Launch(Base):
    __tablename__ = "launches"

    id = Column(String, primary_key=True)
    flight_number = Column(String)
    name = Column(String)
    date_utc = Column(DateTime)
    date_unix = Column(Integer)
    date_local = Column(String)
    date_precision = Column(String)
    upcoming = Column(Boolean)
    success = Column(Boolean)
    details = Column(String)
    rocket = Column(String)
    launchpad = Column(String)
    static_fire_date_utc = Column(DateTime)
    static_fire_date_unix = Column(Integer)
    net = Column(Boolean)
    window = Column(Integer)
    auto_update = Column(Boolean)
    tbd = Column(Boolean)
    launch_library_id = Column(String)

    fairings = Column(JSON)
    links = Column(JSON)
    failures = Column(JSON)
    crew = Column(JSON)
    ships = Column(JSON)
    capsules = Column(JSON)
    payloads = Column(JSON)
    cores = Column(JSON)

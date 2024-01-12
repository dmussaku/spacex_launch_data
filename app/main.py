from typing import List, Dict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Launch
from src.client import SpaceXClient
from config import DATABASE_URL, logger



def setup_database() -> sessionmaker:
    # Create the database engine
    engine = create_engine(DATABASE_URL)
    logger.info(f"Connected to database via engine {engine}")
    # Bind the engine to the metadata of the Base class, so that the declaratives can be accessed
    Base.metadata.create_all(engine)
    logger.info("Created all tables")

    # Create a session factory
    Session = sessionmaker(bind=engine)
    logger.info("Created session factory")

    return Session()


def poll_launces(*args, **kwargs) -> List[Dict]:
    """Function that polls the SpaceX API for launches
    In future that function can be extended to take arguments to make the job filter the api by
    certain parameters like dates, limits etc

    Returns:
        list: A list of launches
    """
    cli = SpaceXClient()
    launches = cli.get_launches()

    return launches

def main():
    # Set up the database and get a working session
    session = setup_database()

    # Poll the SpaceX API for launches
    launches = poll_launces()
    
    # atomically add all launches to the database
    with session.begin():
        for launch in launches:
            logger.info(f"Adding launch {launch['id']} to database")
            session.add(Launch(**launch))
    logger.info(f"Added {len(launches)} launches to database")
        
if __name__ == '__main__':
    main()
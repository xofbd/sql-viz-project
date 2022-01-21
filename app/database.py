import os

from dotenv import load_dotenv
from sqlalchemy import and_, create_engine
from sqlalchemy.orm import sessionmaker

from app.models import Wells

load_dotenv()
URL_DB = os.getenv('URL_DB')


def query_db(depth_min, grad_min):
    """Return wells that fit the search criteria."""
    engine = create_engine(URL_DB)
    session = sessionmaker(bind=engine)()
    results = (
        session
        .query(Wells.latitude, Wells.longitude, Wells.depth, Wells.gradient)
        .filter(and_(Wells.depth > depth_min, Wells.gradient > grad_min))
    )

    return results


if __name__ == '__main__':
    import sys

    depth_min = float(sys.argv[1])
    grad_min = float(sys.argv[2])

    print(query_db(depth_min, grad_min))

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
URL_DB = os.getenv('URL_DB')


def query_db(depth_min, grad_min):
    """Return wells that fit the search criteria."""
    engine = create_engine(URL_DB)

    query = f"""
        SELECT latitude, longitude, depth, gradient
        FROM wells
        WHERE depth > {depth_min} AND gradient > {grad_min};
        """

    print(query)

    with engine.connect() as conn:
        results = (
            conn
            .execute(query)
            .fetchall()
        )

    return results


if __name__ == '__main__':
    depth_min = '1; DROP TABLE wells;--'
    grad_min = 0.05

    print(query_db(depth_min, grad_min))

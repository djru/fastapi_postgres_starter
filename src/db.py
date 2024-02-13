# factory lets us use a singleton for the db connection
# but still testable
from psycopg import Connection
from .config import settings


class DBConnectionFactory:
    _conn = None

    @classmethod
    def get_conn(cls) -> Connection:
        if not cls._conn:
            print("Generating initial db connection")
            cls._conn = Connection.connect(settings.pg_url)
        return cls._conn

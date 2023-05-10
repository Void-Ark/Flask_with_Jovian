
# saved in database.txt
database = "arkcareers"
username = "6fudlbuqmcabyo65a5qb"
host = "aws.connect.psdb.cloud"
password = "pscale_pw_UwUrzswMDACEUSiEnAdft1HzQ2tNCP1JGLap4IlHlMj"

from sqlalchemy import create_engine

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}?charset=utf8mb4",
    connect_args={
        "ssl": {
            "ssl_ca":"//etc//ssl//cert.pem"
        }
    }
)



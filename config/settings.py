from decouple import config

APP_ID = config("APP_ID", default="LIVE")
LOG_LEVEL = config("LOG_LEVEL", default="INFO")
CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
INSERTER_MAX_RETRIES = config("INSERTER_MAX_RETRIES", default=3, cast=int)
REQUEST_MAX_RETRIES = config("REQUEST_MAX_RETRIES", default=3, cast=int)
REQUEST_BACKOFF_FACTOR = config("REQUEST_BACKOFF_FACTOR", default=2, cast=int)
MSSQL_SERVER = config("MSSQL_SERVER")
MSSQL_DATABASE = config("MSSQL_DATABASE")
MSSQL_USERNAME = config("MSSQL_USERNAME")
MSSQL_PASSWORD = config("MSSQL_PASSWORD")

if APP_ID == "INST_HIST":
    INSTRUMENT_FIELDS = config("INSTRUMENT_FIELDS")
    INSTRUMENT_TIMEDELTA_DAYS = config(
        "INSTRUMENT_TIMEDELTA_DAYS", default=180, cast=int
    )
    INSTRUMENT_HISTORY_TABLE = config("INSTRUMENT_HISTORY_TABLE")
elif APP_ID == "LIVE":
    ISSUER_FIELDS = config("ISSUER_FIELDS")
    FUND_FIELDS = config("FUND_FIELDS")
    ISSUER_TABLE = config("ISSUER_TABLE")
    FUND_TABLE = config("FUND_TABLE")
elif APP_ID == "FUND_HIST":
    FUND_HISTORY_TABLE = config("FUND_HISTORY_TABLE")
    FUND_FIELDS = config("FUND_FIELDS")
    FUND_TIMEDELTA_DAYS = config("FUND_TIMEDELTA_DAYS", default=180, cast=int)
elif APP_ID == "ISSU_HIST":
    ISSUER_HISTORY_TABLE = config("ISSUER_HISTORY_TABLE")
    ISSUER_FIELDS = config("ISSUER_FIELDS")
    ISSUER_TIMEDELTA_DAYS = config("ISSUER_TIMEDELTA_DAYS", default=180, cast=int)

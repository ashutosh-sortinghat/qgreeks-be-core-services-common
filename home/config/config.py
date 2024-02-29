import os
import psycopg2

import os

# Define credentials
# creds = {
#     "DB_NAME": "quantumgreeks_retail",
#     "DB_USER": "ashutosh",
#     "DB_PASSWORD": "SR#4@Y3hBxhreU",
#     "DB_HOST": "quantumgreeksibrktest.centralus.cloudapp.azure.com",
#     "DB_PORT": "4435",
#     "OPTIONS_EXPIRATIONS_API": "https://twelve-data1.p.rapidapi.com/options/expiration",
#     "OPTION_CHAIN_API": "https://mboum-finance.p.rapidapi.com/v1/markets/options",
#     "MARKET_PRICE_API": "https://twelve-data1.p.rapidapi.com/price",
#     "EARNING_DATE_API": "https://mboum-finance.p.rapidapi.com/qu/quote/earnings"
#     # "OPTION_ACTIVITY_API": "https://qginternalapis.azurewebsites.net/options-activity/start-date/{start_date}/end-date/{end_date}/"
# }

# # Set environment variables
# for key, value in creds.items():
#     os.environ[key] = value

class DBConfig:
    def __init__(self, start_date=None, end_date=None):
        self.db_name = os.getenv("DB_NAME", "quantumgreeks_retail")
        self.db_user = os.getenv("DB_USER", "ashutosh")
        self.db_password = os.getenv("DB_PASSWORD", "SR#4@Y3hBxhreU")
        self.db_host = os.getenv("DB_HOST", "quantumgreeksibrktest.centralus.cloudapp.azure.com")
        self.db_port = os.getenv("DB_PORT", "4435")
        self.options_expirations_api = os.getenv("OPTIONS_EXPIRATIONS_API", "https://twelve-data1.p.rapidapi.com/options/expiration")
        self.option_chain_api = os.getenv("OPTION_CHAIN_API", "https://mboum-finance.p.rapidapi.com/v1/markets/options")
        self.market_price_api = os.getenv("MARKET_PRICE_API", "https://twelve-data1.p.rapidapi.com/price")
        self.earning_date_api = os.getenv("EARNING_DATE_API", "https://mboum-finance.p.rapidapi.com/qu/quote/earnings")
        if start_date is not None and end_date is not None:
            self.option_activity_api = f"https://qginternalapis.azurewebsites.net/options-activity/start-date/{start_date}/end-date/{end_date}/"
        else:
            self.option_activity_api = None



db_config_without_dates = DBConfig()

# print("\nWithout Dates:")
# print("DB_NAME:", db_config_without_dates.DB_NAME)
# print("DB_USER:", db_config_without_dates.DB_USER)
# print("DB_PASSWORD:", db_config_without_dates.DB_PASSWORD)
# print("DB_HOST:", db_config_without_dates.DB_HOST)
# print("DB_PORT:", db_config_without_dates.DB_PORT)
# print("OPTIONS_EXPIRATIONS_API:", db_config_without_dates.OPTIONS_EXPIRATIONS_API)
# print("OPTION_CHAIN_API:", db_config_without_dates.OPTION_CHAIN_API)
# print("MARKET_PRICE_API:", db_config_without_dates.MARKET_PRICE_API)
# print("EARNING_DATE_API:", db_config_without_dates.EARNING_DATE_API)
# print("OPTION_ACTIVITY_API:", db_config_without_dates.OPTION_ACTIVITY_API)





def connect_to_database():
    db_config = DBConfig()  

    conn = psycopg2.connect(
        dbname=db_config.db_name,
        user=db_config.db_user,
        password=db_config.db_password,
        host=db_config.db_host,
        port=db_config.db_port
    )
    return conn



# ----------------other-------------------------------
# ----------------------------------------------------

# setx DB_NAME "DemoDb1"
# setx DB_USER "postgres"
# setx DB_PASSWORD "12345"
# setx DB_HOST "localhost"
# setx DB_PORT "5432"
# def connect_to_database():
#     conn = psycopg2.connect(
#         dbname=creds.get("dbname"),
#         user=creds.get("user", "postgres"),
#         password=creds.get("password", "12345"),
#         host=creds.get("host", "localhost"),
#         port=creds.get("port", "5432")
#     )
#     return conn
# creds = {
#         "dbname" : os.getenv("DB_NAME"),
#         "user" : os.getenv("DB_USER"),
#         "password" : os.getenv("DB_PASSWORD"),
#         "host" : os.getenv("DB_HOST"),
#         "port" : os.getenv("DB_PORT")
#         }


# creds = {
#     "dbname": "DemoDb",
#     "user": "postgres",
#     "password": "12345",
#     "host": "localhost",
#     "port": "5432"
# }

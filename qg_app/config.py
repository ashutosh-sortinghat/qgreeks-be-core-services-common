import os
import psycopg2

import os


class DBConfig:
    def __init__(self, start_date=None, end_date=None):
        self.db_name = os.getenv("DB_NAME", "quantumgreeks_retail")
        self.db_user = os.getenv("DB_USER", "ashutosh")
        self.db_password = os.getenv("DB_PASSWORD", "SR#4@Y3hBxhreU")
        self.db_host = os.getenv(
            "DB_HOST", "quantumgreeksibrktest.centralus.cloudapp.azure.com")
        self.db_port = os.getenv("DB_PORT", "4435")
        self.options_expirations_api = os.getenv(
            "OPTIONS_EXPIRATIONS_API", "https://twelve-data1.p.rapidapi.com/options/expiration")
        self.option_chain_api = os.getenv(
            "OPTION_CHAIN_API", "https://mboum-finance.p.rapidapi.com/v1/markets/options")
        self.market_price_api = os.getenv(
            "MARKET_PRICE_API", "https://twelve-data1.p.rapidapi.com/price")
        self.earning_date_api = os.getenv(
            "EARNING_DATE_API", "https://mboum-finance.p.rapidapi.com/qu/quote/earnings")
        if start_date is not None and end_date is not None:
            self.option_activity_api = f"https://qginternalapis.azurewebsites.net/options-activity/start-date/{start_date}/end-date/{end_date}/"
        else:
            self.option_activity_api = None


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


db_config = DBConfig()

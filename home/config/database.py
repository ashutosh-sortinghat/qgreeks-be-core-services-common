import os
import psycopg2
# setx DB_NAME "DemoDb"
# setx DB_USER "postgres"
# setx DB_PASSWORD "12345"
# setx DB_HOST "localhost"
# setx DB_PORT "5432"

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

creds = {
    "dbname": "quantumgreeks_retail",
    "user": "ashutosh",
    "password": "SR#4@Y3hBxhreU",
    "host": "quantumgreeksibrktest.centralus.cloudapp.azure.com",
    "port": "4435"
}


def connect_to_database():
    conn = psycopg2.connect(
        dbname=creds.get("dbname"),
        user=creds.get("user", "postgres"),
        password=creds.get("password", "12345"),
        host=creds.get("host", "localhost"),
        port=creds.get("port", "5432")
    )
    return conn

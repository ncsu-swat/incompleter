import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_HOST = os.getenv("DATABASE_HOST")
try:
    CONN = psycopg2.connect(
        host=DATABASE_HOST,
        database=DATABASE_NAME,
        user=DATABASE_USERNAME,
        password=DATABASE_PASSWORD)
    print("PostgreSQL connection successful")
except (Exception, psycopg2.DatabaseError) as error:
    print("Database connection error")
    print(error)


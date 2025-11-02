import psycopg2
from psycopg2 import Error

# Replace with your Neon connection details
CONNECTION_STRING = "postgresql://username:password@hostname:5432/database?sslmode=require"

def connect_to_neon():
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(CONNECTION_STRING)
        print("Connection to Neon Postgres successful!")
        
        # Create a cursor object to execute queries
        cursor = connection.cursor()
        
        # Execute a simple query to test
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Connected to: {db_version[0]}")
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        
    except (Exception, Error) as error:
        print(f"Error while connecting to Neon: {error}")

if __name__ == "__main__":
    connect_to_neon()
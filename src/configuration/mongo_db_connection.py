import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import DATABASE_NAME, MONGODB_URL_KEY

# Load the certificate authority file to avoid timeout error when connecting to mongoDB
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the mongoDB database.

    Attributes
    ---------------
    Client: MongoClient
        A shared MongoClient instance for the class
    database: Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    ---------
    __init__(database_name)-> None
        Initializes the mongoDB connection using the given database name.
    """

    client = None  # Shared MongoClient instance across all MongocDBClient instances.

    def __init__(self,database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Paramter:
        -----------------
        database_name: str, optional
            Name of the MongoDB database to connect to, default is set by DATABASE_NAME constants.

        Raises:
        ------------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """

        try:
            #  Check if a MongoDB client connection has already been established; if not, create a new one.
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) # Retrieve MongnDB url from enviromenet variables.
                if mongo_db_url is None:
                    raise Exception (f"Environment variable '{MONGODB_URL_KEY} is not set.")

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
                
            self.client = MongoDBClient.client
            self.database = self.client[database_name] # connect to the specified database.
            self.database_name  = database_name
            logging.info('MongoDB connection successful.')

        except Exception as e:
            #  Raise a custom exception with the traceback details if connection fails.
            raise MyException(e, sys)
# db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Read from .env
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


# Create engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,           # Verify connections
    pool_size=5,                  # Adjust for traffic
    max_overflow=10,
    connect_args={"sslmode": "require"}  # Explicit SSL
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL

import sys

import config as config

if not DATABASE_URL:
    print("Variable DATABASE_URL in config.py is empty")
    sys.exit()

engine = create_engine(
    config.DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

db = SessionLocal()

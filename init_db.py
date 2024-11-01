from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from geoalchemy2 import Geometry
import time

# Database configuration
POSTGRES_USER = "user"
POSTGRES_PASSWORD = "password"
POSTGRES_DB = "urban_data"
POSTGRES_HOST = "postgres"
POSTGRES_PORT = "5432"

# SQLAlchemy setup
engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define Tables
class LinkInfo(Base):
    __tablename__ = "link_info"
    link_id = Column(Integer, primary_key=True, index=True)
    _length = Column(Float)
    road_name = Column(String)
    usdk_speed_category = Column(Integer)
    funclass_id = Column(Integer)
    speedcat = Column(Integer)
    volume_value = Column(Integer)
    volume_bin_id = Column(Integer)
    volume_year = Column(Integer)
    volumes_bin_description = Column(String)
    geometry = Column(Geometry("MULTILINESTRING", srid=4326))

class SpeedData(Base):
    __tablename__ = "speed_data"
    link_id = Column(Integer, index=True)
    date_time = Column(DateTime)
    freeflow = Column(Float)
    count = Column(Integer)
    std_dev = Column(Float)
    min = Column(Float)
    max = Column(Float)
    confidence = Column(Integer)
    average_speed = Column(Float)
    average_pct_85 = Column(Float)
    average_pct_95 = Column(Float)
    day_of_week = Column(Integer)
    period = Column(Integer)

# Initialize database
def init_db():
    try:
        # Create tables
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as e:
        print("Error creating tables:", e)

if __name__ == "__main__":
    time.sleep(10)
    init_db()

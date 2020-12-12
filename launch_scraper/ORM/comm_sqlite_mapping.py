from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# Using
engine = create_engine('sqlite:///commercialLaunch.sqlite', echo=True)
Base = declarative_base()
Base.metadata.bind = engine

class activeLicenseFact(Base):

    __tablename__ = "active_license_fact"

    id = Column(Integer, primary_key=True)
    license = Column(String, nullable=True)
    company = Column(String, nullable=True)
    vehicle = Column(String, nullable=True)
    location = Column(String, nullable=True)
    expiration = Column(String, nullable=True)

    def __init__(self, license, company, vehicle, location, expiration):
        self.License = license
        self.Company = company
        self.Vehicle = vehicle
        self.Location = location
        self.Expiration = expiration


# Start with a clean database
Base.metadata.drop_all()
Base.metadata.create_all()

# Setup session
Session = sessionmaker(bind=engine)
session = Session()

# Add reminders
licenseData = activeLicenseFact()
session.commit(licenseData)

# Fetch reminders
actlicenses = session.query(activeLicenseFact).all()
for actlicense in actlicenses:
    print(actlicense.Title)

# Fetch reminders
actlicenses = session.query(activeLicenseFact).all()
for actlicense in actlicenses:
    print(actlicense.Title)
from sqlalchemy import Column, Float, Integer, String

from app.database import Base


class HydroStation(Base):
    __tablename__ = "hydro_stations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    river = Column(String)
    region = Column(String)
    installed_capacity = Column(Float)
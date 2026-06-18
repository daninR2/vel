from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)

class Fragrance(Base):
    __tablename__ = "fragrances"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    brand = Column(String, index=True, nullable=False)
    notes = Column(String)  # Stored as a comma-separated string
    accords = Column(String)
    price_estimate = Column(String)
    
    # Relationship to get its clones
    clones = relationship("Clone", back_populates="original_fragrance")

class Clone(Base):
    __tablename__ = "clones"
    id = Column(Integer, primary_key=True, index=True)
    original_id = Column(Integer, ForeignKey("fragrances.id"), nullable=False)
    clone_name = Column(String, nullable=False)
    clone_brand = Column(String, nullable=False)
    similarity_score = Column(Float)  # Percentage out of 100
    price_estimate = Column(String)
    notes_match = Column(String)
    
    original_fragrance = relationship("Fragrance", back_populates="clones")
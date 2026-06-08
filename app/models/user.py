from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import relationship
from app.database.mysql import Base

class User(Base):
    __tablename__ = "users" # Ini nama tabel di MySQL

    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(50), nullable=False)
    full_name = Column(String(100), nullable=False)
    nik = Column(String(20), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), default="GENERAL")
    loss_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    
    # MAGIC HAPPENS HERE: 
    # Tulis "TicketRegistration" pakai tanda kutip, jangan di-import class-nya!
    tickets = relationship("TicketRegistration", back_populates="user")
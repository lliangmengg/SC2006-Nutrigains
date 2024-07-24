from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

Base = declarative_base()

class OTP(Base):
    __tablename__ = 'otp'
    user_email = Column(String, primary_key=True)
    otp = Column(Integer)
    expiry_time = Column(DateTime)

    def __init__(self, user_email, otp, expiry_minutes = 3):
        self.user_email = user_email
        self.otp = otp
        self.expiry_time = datetime.now() + timedelta(minutes=expiry_minutes)

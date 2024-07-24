import random
import string
import smtplib
import  sys
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Boundary_dir)
sys.path.append(Entity_dir)

from DatabaseCRUDOperator import DatabaseCRUDOperator as db_operator
from Otp import OTP

class Otp_handler:
    dbOperator = db_operator()
    @staticmethod
    def generate_otp(email):
        otp = ''.join(random.choices(string.digits, k=6))
        new_otp = OTP(user_email = email , otp = otp)
        try:
            Otp_handler.dbOperator.create(new_otp)
        except:
            Otp_handler.dbOperator.update(OTP, {"user_email":email}, {"expiry_time": new_otp.expiry_time, "otp": new_otp.otp})
        return otp
    @staticmethod
    def email_otp(email):
        #generate otp
        otp = Otp_handler.generate_otp(email)
        # Email configuration
        sender_email = "nutrigains.noreply@gmail.com" 
        receiver_email = email
        password = "qdec stjl svox bnuq"  # sender email password

        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = "Nutrigains Sign Up OTP"  

        # Email body
        body = "Your one time password is: " + otp
        message.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure SMTP connection
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # Login with sender's credentials
            server.login(sender_email, password)
            # Send email
            server.sendmail(sender_email, receiver_email, message.as_string())
           
        except Exception as e:
           raise Exception(f"Error sending OTP: {e}")
        finally:
            # Close the SMTP server
            server.quit()
    @staticmethod
    def OTPVerification(email, entered_otp):
        #retrieve otp record
        print(email, file = sys.stdout)
        otp_record = Otp_handler.dbOperator.read(OTP , user_email = email)[0]
        #check for time out
        if (datetime.now() > otp_record.expiry_time): 
            print(otp_record.expiry_time, file = sys.stdout)
            print(type(otp_record.expiry_time), file=sys.stdout)
            return False
        if otp_record.otp != entered_otp: 
            print("yay2", file=sys.stdout)
            return False
        return True
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Boundary_dir = os.path.join(parent_dir, 'Boundary')
Entity_dir = os.path.join(parent_dir, 'Entity')
sys.path.append(Boundary_dir)
sys.path.append(Entity_dir)

from DatabaseCRUDOperator import DatabaseCRUDOperator as dbOperator
from User import User

db = dbOperator()

class LoginHandler:
    def validateAndFetchUser(useremail, password) -> bool:
        return db.read(User, email = useremail, password = password)
    def forgotPassword():
        pass
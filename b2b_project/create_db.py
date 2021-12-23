from database import Base,engine
from models import User_data

print("creating database....")

Base.metadata.create_all(engine)
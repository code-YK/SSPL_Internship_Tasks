# setup_db.py
from db import engine
from models import Base

Base.metadata.create_all(engine)

print("Tables created successfully!")

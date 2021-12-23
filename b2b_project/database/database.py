from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://postgres:b2b123@localhost/b2b",
    echo=True
)

Base=declarative_base()
SessionLocal=sessionmaker(bind=engine)

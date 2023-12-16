from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import databases

DATABASE_URL = "postgresql://localhost:5432/webdevendterm"
database = databases.Database(DATABASE_URL)

Base = declarative_base()


class PostDB(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    dateOfCreation = Column(DateTime, default=datetime.utcnow)
    author = Column(String)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import create_engine
from sqlalchemy import sql
from sqlalchemy.orm import sessionmaker


URL = "postgresql://아이디:비밀번호@서버주소/DB이름"
engine = create_engine(URL,echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


## data model (table)
from sqlalchemy import Column, String, Integer,Boolean,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class PhotoDB(Base):
    __tablename__ = "photo_dbs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String,index=True)
    file_name = Column(String,index=True)
    url = Column(String,unique=True)
    is_down_images = Column(Boolean, default=False)

class PostDB(Base):
    __tablename__ = "Post_d"

    id = Column(Integer, primary_key=True, index=True)
    post_url = Column(String,unique=True)
    subject = Column(String)
    is_get_images = Column(Boolean, default=False)

class PhotoPath(Base):
    __tablename__ = "photo_path"

    id = Column(Integer, primary_key=True, index=True)
    photo_path = Column(String,unique=True)
    user_id = Column(String,index=True)
    file_name = Column(String,index=True)


class LogDB(Base):
    __tablename__ = "log_db"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    status = Column(String)
    time = Column(DateTime(timezone=True),server_default=sql.func.now())
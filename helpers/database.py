from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from helpers.constants import DATABASE_URL

# ✅ Database Connection
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base Model
Base = declarative_base()

# ✅ ActivityLogDB Model
class ActivityLogDB(Base):
    __tablename__ = "activity_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    action = Column(String, index=True)
    document_id = Column(Integer, ForeignKey("documents.document_id"), nullable=True)
    timestamp = Column(DateTime)

# ✅ DocumentDB Model
class DocumentDB(Base):
    __tablename__ = "documents"
    document_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)

# ✅ UserDB Model
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)

# ✅ Dependency to Get DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

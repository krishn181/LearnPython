from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

#create_engine used to connect database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False }
)
sessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class ToDo(Base):
    __tablename__ = "ToDo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

#Create table in DataBase
Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home (db:Session = Depends(get_db)):
    return{
        "message":"DB connect fine"
    }
    
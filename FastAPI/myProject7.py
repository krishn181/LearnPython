from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

#create_engine used to connect database
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False }
)

# create session for read only
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

#create data
@app.post("/todo")
def create_todo(title:str, db:Session = Depends(get_db)):
    todo = ToDo(title = title, completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "Message":"Created",
        "data":todo
    }


#read all data
@app.get("/gettodos")
def get_todos(db:Session = Depends(get_db)):
    todo = db.query(ToDo).all()
    return{
        "Message":"Data fetch",
        "Total":len(todo),
        "data":todo
    }

#read one by one by id 
@app.get("/gettodos/{todo_id}")
def get_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(
            status_code=404,
            detail="not found"
        )
    return {
    "message": f"Data fetched for todo {todo_id}",
    "data": todo
        }

#update data
@app.put("/update/{todo_id}")
def update_todo(todo_id:int, title:str, db:Session= Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
           raise HTTPException(
                    status_code=404,
                    detail="not found"
                )
    todo.title = title
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return{
        "Message":"Data update successfully",
        "data":todo
    } 

#delete todo
@app.delete("/delete/{todo_id}")
def delete_todo(todo_id:int, db:Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, data = "Not found")
    db.delete(todo)
    db.commit()
    return {
        "message":f"todo delete {todo_id}"
    }
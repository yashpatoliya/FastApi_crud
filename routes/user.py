from fastapi import APIRouter , Request,Depends,Form
from config.db import sessionLoacal
from sqlalchemy.orm import Session
from models.index import User

user = APIRouter()

def get_db():
  db = sessionLoacal()
  try:
    yield db
  finally:
    db.closed()

@user.get('/')
async def read_data(request : Request,db: Session = Depends(get_db)):
  return   db.query(User).all()

@user.get('/{id}')
async def read_data(id : int,db: Session = Depends(get_db)):
  return  db.query(User).filter(User.id == id).first()

@user.post('/')
async def write_data(request: Request, name  : str, email: str , password: str, db: Session = Depends(get_db) ):
  db_user = User(email=email, name=name, password=password)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  user_id = db_user.id # getting the last newly inserted primary key
  result = db.query(User).filter(User.id == user_id).first()
  return {"msg" : "created user successfully" , "user_id" : user_id , "result" : result}

@user.put('/{id}')
async def update_data(request: Request,id: int, name: str , email: str, password: str , db: Session = Depends(get_db)):
  print("request",request.body)
  # db_user = User(email=email, name=name, password=password)
  # db.update(db_user)
  # db.commit()
  # db.refresh(db_user)
  # user_id = db_user.id # getting the last newly inserted primary key
  # result = db.query(User).filter(User.id == user_id).first()
  return {"msg" : "update user successfully" , "request":request}

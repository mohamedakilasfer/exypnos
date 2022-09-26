from fastapi import FastAPI , Depends, Request, Form
import uvicorn

import schemas, models, predictor
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

app=FastAPI() 

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def form_post(request:Request):
    result=""
    return templates.TemplateResponse('valueform1.html', context={'request':request, 'result':result})








#@app.get("/{name}")
#def hello(name):
 #   return {"Hello {} and welcome to this API".format(name)}

#@app.get("/")
#def title():
 #   return {"Diabetes Prediction"}

@app.post("/")
def predict(request: Request, 
             text1:int=Form(...),
             text2:int=Form(...),
             text:int=Form(...),
             text3:int=Form(...),
             text4:int=Form(...),
             text5:float=Form(...),
             text6:float=Form(...),
             text7:int=Form(...),
             db:Session=Depends(get_db)):
    
    
    prediction_val = predictor.predict(text1,text2,text,text3,text4,text5,text6,text7)
    result = prediction_val
    
    

    new_data = models.Women(
    pregnancies=text1,
    glucose=text2,
    bp=text,
    skinthickness=text3,
    insulin=text4,
    bmi=text5,
    dpf=text6,
    age=text7)

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return templates.TemplateResponse('finalout.html', context={'request':request, 'result':result})

@app.get("/database")
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Women).all()
    return blogs

if __name__=="__main__":
    uvicorn.run(app)
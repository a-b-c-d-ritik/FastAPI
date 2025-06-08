from fastapi import FastAPI
#----ye package h---ye class h

app=FastAPI() #creating object of class

@app.get("/first")  #creating route
def hello():
    return {'message':"Hello Dost"}

@app.get("/")  #creating route
def root():
    return {'message':"We are @ root"}


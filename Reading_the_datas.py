from fastapi import FastAPI,Path,HTTPException,Query
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    
    return data

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str):
    #load all the data
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {'error':'Patient details not found'}
    

#adding path fn
@app.get('/Path/patient/{patient_id}')
def view_patient_bypath(patient_id:str=Path(...,description="Id of the patient in DB",example="P001")):
    #load all the data
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {'error':'Patient details not found'}


#adding httpexceptions
@app.get('/viewpatient/{patient_id}')
def view_excep(patient_id:str=Path(...,description="Id of the patient in DB",example="P001")):
    #load all the data
    data=load_data()
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404,detail="Patient details not found")



@app.get('/sort')
def sort_patients(sort_by=Query(...,description="sort on the basis of height,weight or BMI "),order : str('asc',)):
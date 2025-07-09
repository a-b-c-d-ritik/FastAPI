from fastapi import FastAPI,Path,HTTPException,Query
import json
from pydantic import BaseModel,Field,computed_field
from typing import Annotated,Literal,Optional
from fastapi.responses import JSONResponse

app=FastAPI()

#Pydantic Model :
class Patient(BaseModel):
        id: Annotated[str,Field(...,description='Id of the patient',examples=['P001'])]
        name: Annotated[str,Field(...,description='Name of the patient')]
        city: Annotated[str,Field(...,description='city name')]
        age: Annotated[int,Field(...,gt=0,lt=100,description='Id of the patient')]
        gender: Annotated[Literal['male','female'],Field(...,description='Name Gender of the patient')]
        height: Annotated[float,Field(...,gt=0,description='Height of patient in meters')]
        weight: Annotated[float,Field(...,gt=0,description='Weight of patient in kgs')]


        @computed_field
        @property
        def bmi(self)-> float:
            return round(self.weight/(self.height**2),2)
      

        @computed_field
        @property
        def verdict(self)-> str:
            if self.bmi<18.5:
                return "Underweight"
            elif self.bmi<30:
                return 'Normal'
            else :
                return 'Obesive'


# creating 2nd pydantic model because in first one all fields are mandatory
class PatientUpdate(BaseModel):
        name: Annotated[Optional[str],Field(default=None)]
        city: Annotated[Optional[str],Field(default=None)]
        age: Annotated[Optional[int],Field(default=None,gt=0)]
        gender: Annotated[Optional[Literal['male','female']],Field(default=None)]
        height: Annotated[Optional[float],Field(default=None)]
        weight: Annotated[Optional[float],Field(default=None,gt=0)]




def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)





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
def sort_patients(sort_by: str =Query(...,description="sort on the basis of height,weight or BMI "),order : str=Query('asc',description="sort in asc or desc order")):
    
    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid fields select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail=f"Invalid fields select from asc or desc ")
    
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
    

@app.post('/create')
def create_patient(patient:Patient):
    #load existing data
    data=load_data()

    #check if patient data already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail="Patient already exists")
    else:
    #adding new patient to the database
       data[patient.id] = patient.model_dump(exclude=['id'])
       save_data(data)

    return JSONResponse(status_code=201,content={'message':'Patient created successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patient_update:PatientUpdate):
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Patient not found")
    else:
        patient_info=data[patient_id]
        # now we are converting patient Model into a dictionary
        updated_patient_info=patient_update.model_dump(exclude_unset=True)

        for key,value in updated_patient_info.items():
            patient_info[key]=value
            patient_info['id']=patient_id ## adding patient id
            patient_pydantic_obj=Patient(**patient_info)
            patient_info=patient_pydantic_obj.model_dump(exclude='id')
            data[patient_id]=patient_info

            #saving
            save_data(data)
    return JSONResponse(status_code=200,content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    #load data
    data=load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404,detail='patient not found')
    
    else:
       del data[patient_id]
       save_data(data)
    
    return  JSONResponse(status_code=200,content={'message':'patient deleted'})
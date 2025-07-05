from pydantic import BaseModel
from typing import List,Dict,Optional


class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    contact_details: Dict[str,str]


patient_info={
    'name':"Banku",
    'age':'10',
    'weight':78.45,
    'married':True,
    'allergies':['dust','smoke','webs'],
    'contact_details':{'email':'bakuraj@gmail.com','phone':'9256106988'}
    }

p1=Patient(**patient_info)

def insert(patient : Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)

    for x in patient.allergies:
        print(x)
    for x in patient.contact_details:
        print(patient.contact_details[x])
    
    print("Record saved")


insert(p1)
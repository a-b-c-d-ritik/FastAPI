from pydantic import BaseModel,EmailStr,AnyUrl
from typing import List,Dict,Optional

class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married:bool
    allergies:Optional[List[str]]=None
    email: EmailStr
    linkedin_url:AnyUrl


patient_info={
    'name':"Banku",
    'age':'10',
    'weight':78.45,
    'married':True,
    'allergies':['dust','smoke','webs'],
    'email':'bakuraj@gmail.com'
    'linkedin_url':'https//facebook.com'
    }

p1=Patient(**patient_info)

def insert(patient : Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)

    for x in patient.allergies:
        print(x)
    
    print(patient.email)
    
    print("Record saved")


insert(p1)
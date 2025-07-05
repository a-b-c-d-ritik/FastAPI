from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
   # name: str
    name: Annotated[str,Field(max_length=30,title='Name of the patient',description='Give the name of patient under 50 words',examples=['Nitish','Raju'],default=None)]
    age: int
    weight:float=Field(gt=0) #gt mtlb greater than
    married:bool
    allergies:Optional[List[str]]=None
    email: EmailStr
    linkedin_url: AnyUrl


patient_info={
    'name':"Banku",
    'age':'10',
    'weight':78.45,
    'married':True,
    'allergies':['dust','smoke','webs'],
    'email':'bakuraj@gmail.com',
    'linkedin_url':'https://www.perplexity.ai/'
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
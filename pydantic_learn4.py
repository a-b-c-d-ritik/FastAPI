from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    age: int
    weight:float
    married:bool
    allergies:List[str]
    email: EmailStr
    linkedin_url: AnyUrl

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')
        if domain_name not in valid_domains:
            raise ValueError("Not in valid Domain")
        
        return value


patient_info={
    'name':"Banku",
    'age':'10',
    'weight':78.45,
    'married':True,
    'allergies':['dust','smoke','webs'],
    'email':'bakuraj@hdfc.com',
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
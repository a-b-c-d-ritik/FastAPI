from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,errors,model_validator,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    height: float
    age: int
    weight:float
    married:bool
    allergies:List[str]
    email: EmailStr
    linkedin_url: AnyUrl


    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    


    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        domain_name=value.split('@')[-1]  # this gives a list with separated items like " xyz@",'gmail.com' and we want the last one
        print(domain_name)
        if domain_name not in valid_domains:
            raise ValueError("Not in valid Domain")
        
        return value
    
    
    @field_validator('name',mode='after')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
     
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age range should be between 0 to 100")


    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient older than 60 must have an emergency contact")
        
        return model


patient_info={
    'name':"Banku",
    'height':165.3,
    'age':'30',
    'weight':78.45,
    'married':True,
    'allergies':['dust','smoke','webs'],
    'email':'bakuraj@icici.com',
    'linkedin_url':'https://www.perplexity.ai/'
    }

p1=Patient(**patient_info)

def insert(patient : Patient): 
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.bmi)

    for x in patient.allergies:
        print(x)
    
    print(patient.email)
    
    print("Record saved")


insert(p1)
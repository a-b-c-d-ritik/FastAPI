#nested models

from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str



class Patient(BaseModel):
    name: str
    gender:str
    age:int
    address: Address


Add_dict={'city':'patna','state':'bihar','pin':'800020'}

add1=Address(**Add_dict)

patient_dict={
    'name':'Rajesh',
    'gender':'Male',
    'age':42,
    'address': add1
}

patient1=Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
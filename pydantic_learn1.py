from pydantic import BaseModel
from typing import List

def insert1(name,age):
    print(f"Records Inserted-> \n Name:{name}\n Age:{age}")


insert1("Raju","fifty")
insert1("Subodh",67)

def insert2(name:str,age:int):

    if type(name) == str and type(age)==int:
        print(f"Records Inserted-> \n Name:{name}\n Age:{age}")
    else:
        raise TypeError("Incorrect datatype")



#insert2("Raju","fifty")
insert2("Subodh",67)


#Pydantic


class Patient(BaseModel):
    name: str
    age: int
    weight:float
   

patient_info={'name':"Banku",'age':'10'} # 10 can be '10'

patient1=Patient(**patient_info) ## -(**)refers to unpacking of dictionary

## Method 1
def insertM1(name,age):
    print(name)
    print(age)
    print("Record saved")

insertM1(patient1.name,patient1.age)


#Method 2
def insertM2(patient : Patient): ## syntax : (variable : Type)
    print(patient.name)
    print(patient.age)
    print("Record saved")

insertM2(patient1)



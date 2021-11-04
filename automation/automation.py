from typing import List
from faker import Faker
import shutil
import re

faker = Faker()
potential_contacts = ""

existing_contacts = ""
for _ in range(100):


    potential_contacts += faker.paragraph()
    potential_contacts += f" {faker.email()} "
    potential_contacts += faker.paragraph()
    potential_contacts += faker.sentence()
    potential_contacts += f" {faker.phone_number()} "
    potential_contacts += faker.paragraph()

with open("potential-contacts.txt",'w') as f:
    f.write(potential_contacts)

shutil.copy('potential-contacts.txt',"potential-contacts_copy.txt")

with open ("potential-contacts_copy.txt","r") as f:
    file=f.read()


x = re.findall('[a-zA-Z0-9_$%]+@+[a-z0-9]+.[a-z]+[" "]',file)
emails = sorted(x)
contant_email=''
for i in emails:
    contant_email +=f'{i}\n'

with open("email.txt","w") as f:
    f.write(contant_email)
# print(contant_email)

############################/ Phone number \###############################

number = re.findall("(\d{3}\D{0,3}\d{3}\D{0,3}\d{4})", file)
# print(number.)
contant_phone=''
for i in number:
    contant_phone +=f'{i} '
xz = re.sub(r"[)-.]", "-", str(contant_phone))
y=re.sub(r"[(]", "", xz)
y=y.split(" ")
list=[]
for i in y:
    if len(i)<11:
        list.append(f"{i[:3]}-{i[:3]}-{i[:4]}")
    else:    
        list.append(i)    
x = sorted(list)
print(x)
list_number=''
for i in x:
    list_number +=f"{i}\n"



with open("phone_number.txt",'w') as phone:
    phone.write(list_number)
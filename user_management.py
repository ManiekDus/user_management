import json
import random
import re
import os
from datetime import datetime


userData = ["Jan", "123123123", "321321321", "regon"]

def edit_user(user_id, updated_data):
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            userName = updated_data[0]
            nip = validate_nip(updated_data[1])
            pesel = validate_pesel(updated_data[2])
            regon = validate_regon(updated_data[3])
            dataToSave = {"userIndex":user_id,"userName": userName, "NIP": nip, "PESEL": pesel, "REGON":regon, "password": generate_password(), "status": True}
            data[user_id-1] = dataToSave
        with open("./data/users.json", mode="w+", encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print(f"Succesfully edited user data at {user_id}")
    else:
        print(f"File not found at {path}, there is no user data to edit.")
def remove_user(user_id):
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            dataToSave = {"userIndex":user_id,"userName": "Redacted", "NIP": data[user_id-1]["NIP"], "PESEL": data[user_id-1]["PESEL"], "REGON":data[user_id-1]["REGON"], "password": 'None', "status": False}
            data[user_id-1] = dataToSave
        with open("./data/users.json", mode="w+", encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print(f"Succesfully deleted user data at ID: {user_id}")
    else:
        print(f"File not found at {path}, there is no user data to edit.")
def load_users():
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
        for i in range(len(data)):
            if(data[i]["status"]):
                print(f"{data[i]["userIndex"]}) User: {data[i]["userName"]} with data:")
                print(f"NIP: {data[i]["NIP"]}")
                print(f"PESEL: {data[i]["PESEL"]}")
                print(f"REGON: {data[i]["REGON"]}")
            else:
                print(f"{data[i]["userIndex"]} User has been deleted")
        return data
    else:
        print(f"File not found at {path}, there is no user data to load.")
def validate_nip(nip):
    return nip
def validate_pesel(pesel):
    return pesel
def validate_regon(regon):
    return regon
def generate_password():
    return 0
def validate_password(password):
    return password

def add_user(user_data):
    userName = user_data[0]
    nip = validate_nip(user_data[1])
    pesel = validate_pesel(user_data[2])
    regon = validate_regon(user_data[3])
    index = 1
    dataToSave = {"userIndex":index,"userName": userName, "NIP": nip, "PESEL": pesel, "REGON":regon, "password": generate_password(), "status": True}
    save_user_to_file(dataToSave)
    
def save_user_to_file(dataToSave):
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            data.append(dataToSave)
            data[len(data)-1]["userIndex"] = data[len(data)-2]["userIndex"]+1
        with open("./data/users.json", mode="w+", encoding='utf-8') as out_file:
            json.dump(data, out_file)
    else:
        data = []
        data.append(dataToSave)
        if not os.path.exists("./data"):
            os.makedirs("./data")
        with open("./data/users.json", mode="w+", encoding='utf-8') as out_file:
            json.dump(data, out_file)
        print("User entry")
add_user(userData)

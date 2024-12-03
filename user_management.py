import json
import random
import re
import os

userData = ["Jan", "123123123", "321321321", "regon"]

def edit_user(user_id, updated_data):
    return 0
def remove_user(user_id):
    return 0
def load_users():
    return 0
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
    dataToSave = {"userIndex":index,"userName": userName, "NIP": nip, "PESEL": pesel, "REGON":regon}
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            data.append(dataToSave)
            data[len(data)-1]["userIndex"] = len(data)
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

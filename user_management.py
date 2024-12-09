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
        canSave = True
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
            data = list(data)
            userName = updated_data[0]
            nip = updated_data[1]
            pesel = updated_data[2]
            regon = updated_data[3]
            if(validate_nip(nip) == False):
                print("NIP number failed validation, please make sure the provided NIP is correct.")
                canSave = False
            if(validate_pesel(pesel) == False):
                print("PESEL number failed validation, please make sure the provided PESEL is correct.")
                canSave = False
            if(validate_regon(regon) == False):
                print("REGON number failed validation, please make sure the provided REGON is correct.")
                canSave = False       
            if(canSave):
                dataToSave = {"userIndex":user_id,"userName": userName, "NIP": nip, "PESEL": pesel, "REGON":regon, "password": generate_password(), "status": True}
                data[user_id-1] = dataToSave
                print(f"Succesfully edited user data at {user_id}")
        with open("./data/users.json", mode="w+", encoding='utf-8') as out_file:
            json.dump(data, out_file)    
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
def load_users(showAllData = False):
    path = './data/users.json'
    isExist = os.path.exists(path) 
    if(isExist): 
        with open("./data/users.json", mode="r", encoding='utf-8') as out_file:
            data = json.load(out_file)
        for i in range(len(data)):
            if(data[i]["status"] or showAllData):
                print(f"{data[i]["userIndex"]}) User: {data[i]["userName"]} with data:")
                print(f"NIP: {data[i]["NIP"]}")
                print(f"PESEL: {data[i]["PESEL"]}")
                print(f"REGON: {data[i]["REGON"]}")
            else:
                print(f"{data[i]["userIndex"]} User has been deleted")
        return data
    else:
        print(f"File not found at {path}, there is no user data to load.")
def validate_nip(nip:str):
    if(len(nip) == 10):
        suma = 0
        weightNIP = "657234567"
        for i in range(9):
            suma = int(weightNIP[i]) * int(nip[i]) + suma
        lastDigit = suma%11
        if(lastDigit == nip[9]):
            return True
        else:
            return False
    else:
        return False
def validate_pesel(pesel):
    if(len(pesel) == 11):
        suma = 0
        weightPESEL = "1379137913"
        for i in range(10):
            if(int(weightPESEL[i]) * int(pesel[i]) > 10 and int(weightPESEL[i]) * int(pesel[i]) < 100):
                suma = (int(weightPESEL[i]) * int(pesel[i]))%10 + suma
            else:
                suma = int(weightPESEL[i]) * int(pesel[i]) + suma
        if(suma > 10 and suma < 100):
                suma = suma%10
        lastDigit = 10 - suma
        if(lastDigit == pesel[10]):
            if(int(pesel[2:4]) > 0 and int(pesel[2:4]) < 13 or int(pesel[2:4]) > 20 and int(pesel[2:4]) < 33 or int(pesel[2:4]) > 40 and int(pesel[2:4]) < 53 or int(pesel[2:4]) > 60 and int(pesel[2:4]) < 73 or int(pesel[2:4]) > 80 and int(pesel[2:4]) < 93):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def validate_regon(regon):
    return regon
def generate_password():
    return 0
def validate_password(password):
    return password

def add_user(user_data):
    canSave = True
    userName = user_data[0]
    nip = user_data[1]
    pesel = user_data[2]
    regon = user_data[3]
    if(validate_nip(nip) == False):
            print("NIP number failed validation, please make sure the provided NIP is correct.")
            canSave = False
    if(validate_pesel(pesel) == False):
            print("PESEL number failed validation, please make sure the provided PESEL is correct.")
            canSave = False
    if(validate_regon(regon) == False):
            print("REGON number failed validation, please make sure the provided REGON is correct.")
            canSave = False    
    if(canSave):
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

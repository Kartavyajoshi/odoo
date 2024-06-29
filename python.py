import random as random
import math as math
from cryptography.fernet import Fernet
# ONLY WORKING MODEL
# roles with password
ids= {"admin":{"id":"admin","passwd":"amin@123"},
      "faculty":{"id":"faculty","passwd":"fact@123"},
      "superwiser":{"id":"Super1","passwd":"sup@123"}
}
papers=[]

def uploadPaper():
      print("Hello please upload papers : ")
      path=input("Enter file path : ")#due to locally cheking i am taking file path
      papers.push(path)  
            
while(True):
    role=input("Enter Your Role (For Admin ->A,For Faculty ->F,For sSuperviser ->S) : ")
    if(role=="A" or role=="a"):
        id=input("Enter ID : ")
        passwd=input("Enter password : ")
        if(ids["admin"]["id"]==id and ids["admin"]["passwd"]==passwd):
                print("Welcome admin : ")
                adminKey=random.randint(1000000000000000,99999999999999999999)
                print("Halfkey to access papers : ",adminKey)
                break
    if(role=="S" or role=="s"):
        id=input("Enter ID : ")
        passwd=input("Enter password : ")
        if(ids["superwiser"]["id"]==id and ids["superwiser"]["passwd"]==passwd):
                print("Welcome superwiser : ")
                SuperwiserKey=random.randint(1000000000000000,99999999999999999999)
                print("Halfkey to access papers : ",SuperwiserKey)
                break
    if(role=="F" or role=="f"):
        id=input("Enter ID : ")
        passwd=input("Enter password : ")
        if(ids["faculty"]["id"]==id and ids["faculty"]["passwd"]==passwd):
               uploadPaper()
               break
#Encrypt
#select random paper after getting key as input(Admin + superwiser)
# def genratePaper(k1,k2,ids,papers):
   

def getpaper(k1,k2,ids):
    k1=ids["admin"]["key"]
    k2=ids["superwiser"]["key"]
    paper=random.randint(0,len(papers)+1)
    paperencypt=encrypt_message(k1+k2,paper)
    if(ids["admin"]["key"]==k1 and ids["superwiser"]["key"]==k2):
               return decrypt_message(paperencypt, k1+k2)
     
     
        
# Encrypt plaintext using the generated key
def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

# Decrypt ciphertext using the same key
def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message
      
    

    
    
        
        
               

    




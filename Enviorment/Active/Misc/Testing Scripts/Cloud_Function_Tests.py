import requests
data = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"americanCities"}, "User_ID":"Josh_Testing_Script"}

import firebase_admin
from firebase_admin import credentials, firestore
import time

#cred = credentials.Certificate(r"C:\Users\Joshua\Desktop\PP5\Void-Web\Enviorment\Active\service_account\void-scribe-firebase-adminsdk-xtf9j-c41e46ae8a.json")
cred = credentials.Certificate(r"C:\Users\thepe_000\Desktop\PP5\Void-Web\Enviorment\Active\Non-Public\void-scribe-firebase-adminsdk-xtf9j-3b3a1435e9.json")


firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()

collection = DataBaseReference.collection("Algorithm_Requests")

doc = collection.document("Josh_Console_Test_" + str(time.time()))
doc.set(document_data=data)
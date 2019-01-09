#This File Will Handle FireStore Interactions Providing For Uploads
import firebase_admin
from firebase_admin import credentials, firestore
import os
from Void_Logger import Void_Log_Info

this_dir, this_filename = os.path.split(__file__)
cred_path = this_dir + r"/service_account/void-scribe-firebase-adminsdk-xtf9j-c41e46ae8a.json"
#cred_path = this_dir + r"\Non-Public\void-scribe-firebase-adminsdk-xtf9j-3b3a1435e9.json"

cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

DataBaseReference = firestore.client()
#Objects in Queue must be indexable format -> [0] collection reference [1] document contents [2] (optional) document name

def UploadDocument(collection, document_content, document_name=None):
    #collection - A reference to the collection to insert into, utalize DataBaseReference to obtain this
    #document_content - A dictionary object that is the contents of the document to upload
    #document_name - An optional string used to name the uploaded document
    #If no document name is provided push() is used to generate a unique ID
    
    doc_ref = collection.document(document_name)
    doc_ref.set(document_data=document_content)
    
    Void_Log_Info(f"Uploaded Document: {doc_ref.id} to Collection: {collection.id}")
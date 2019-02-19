import requests as req
import time

base_url = r"http://www.voidscribe.com"
#base_url = "http://127.0.0.1:5000"
#base_url = r"http://webapp-534272.pythonanywhere.com"

good_data_1_req = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"americanCities"}, "User_ID":"Josh_Testing_Script"}
good_data_2_req = {"Req_Type":"Sentence", "Req_Arguments":{"Amount":5, "Sentence_Type":"myth"}, "User_ID":"Josh_Testing_Script"}
bad_data_1_req = {"Reqqq_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"pokemon"}, "User_ID":"Josh_Testing_Script"}
bad_data_2_req = {"Req_Type":"Name", "Req_Arguments":{"Amount":5, "Name_Type":"pokeman"}, "User_ID":"Josh_Testing_Script"}
bad_data_3_req = {"Req_Type":"Sentence", "Req_Arguments":{"Amount":5, "Sentencee_Type":"myth"}, "User_ID":"Josh_Testing_Script"}
good_data_name = {"Name_Type":"weaponsOld", "Amount":120, "User_ID":"Josh_Testing_Script"}
bad_data_name = {"Name_Type":"weaponsFat", "Amount":27, "User_ID":"Josh_Testing_Script"}
good_data_sentence = {"Sentence_Type":"quest", "User_ID":"Josh_Testing_Script"}
bad_data_sentence = {"Sentence_Type":"questable", "Amount":2, "User_ID":"Josh_Testing_Script"}

def TestRequest(data):
    endpoint = base_url + "/" + data[2]
    print(endpoint)
    resp = req.post(url=endpoint, json=data[0])

    print("{} {} Successfully returned with code {}. Data Returned: {}".format(data[2], data[1], resp.status_code, str(resp.content)))
    
Tests = []

Tests.append((good_data_1_req, "White Test 1", "VoidScribeRequest"))
Tests.append((good_data_2_req, "White Test 2", "VoidScribeRequest"))
Tests.append((bad_data_1_req, "Black Test 1", "VoidScribeRequest"))
Tests.append((bad_data_2_req, "Black Test 2", "VoidScribeRequest"))
Tests.append((bad_data_3_req, "Black Test 3", "VoidScribeRequest"))
Tests.append((good_data_name, "White Test", "RetreiveNames"))
Tests.append((bad_data_name, "Black Test", "RetreiveNames"))
Tests.append((good_data_sentence, "White Test", "RetreiveSentences"))
Tests.append((bad_data_sentence, "Black Test", "RetreiveSentences"))

for test in Tests:
    TestRequest(test)


    

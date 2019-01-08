import * as functions from 'firebase-functions';
import * as admin from 'firebase-admin'
import * as req from 'request'

// Start writing Firebase Functions
// https://firebase.google.com/docs/functions/typescript

admin.initializeApp(functions.config().firebase)
  

export const getTimestamp = functions.https.onRequest((request, response) => 
{

  response.send(admin.firestore.FieldValue.serverTimestamp());
});

export const voidScribeRequest = functions.https.onRequest((request, response) => 
{
  const collection = admin.firestore().collection('Algorithm_Requests')
  const doc = collection.doc()

  const data = request.body;


  return doc.set(data).then((result) => {
    response.status(200).json(doc.id)
  });
  
});

export const voidScribeRetreive = functions.https.onRequest((request, response) =>
{
  const data = request.body;
  const id = data["Doc_ID"];

  const collection = admin.firestore().collection('Completed_Requests')
  const query = collection.where("Req_Doc_ID", "==", String(id))

  return query.get().then((snapshot) => {
    if(snapshot.size === 1)
    {
      //response.send({data:snapshot.docs[0].data(), completed:true})
      response.status(200).json({data:snapshot.docs[0].data(), completed:true})
    }
    else
    {
      //response.send({completed:false});
      response.status(200).json({completed:false});
    }
  });
});

exports.timestampRequests = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {

      return event.ref.set({timestamp: admin.firestore.FieldValue.serverTimestamp()}, {merge: true})

    });

exports.tagRequestsForProcessing = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {

      const data = event.data()

      if(data.Processed === true) return null
      else return event.ref.update({"Processed":false})
      
    });

exports.tagRequestsForProcessing = functions.firestore
    .document('Algorithm_Requests/{req_id}')
    .onCreate((event, context) => {

      const data = event.data()


      const bad_collection = admin.firestore().collection('Bad_Requests')
      //Validate Primary Fields
      if (data.Req_Type === null){ 
        const bad_req_doc = data
        bad_req_doc.Message = "Missing Required Field: Req_Type"
        bad_collection.add(bad_req_doc).then((result) => {
          return 1
        }).catch((result) => {
          return 1
        });
      }
      if (data.Req_Arguments === null){ 
        const bad_req_doc = data
        bad_req_doc.Message = "Missing Required Field: Req_Arguments"
        bad_collection.add(bad_req_doc).then((result) => {
          return 1
        }).catch((result) => {
          return 1
        });
      }
      if (data.User_ID === null){ 
        const bad_req_doc = data
        bad_req_doc.Message = "Missing Required Field: User_ID"
        bad_collection.add(bad_req_doc).then((result) => {
          return 1
        }).catch((result) => {
          return 1
        });
      }

      //Validate Secondary Fields
      if (data.Req_Type === "Name"){
        // if (data.Req_Arguments.keys().indexof("Name_Type") === -1){
        //   const bad_req_doc = data
        //   bad_req_doc.Message = "Missing Required Argument Field For A Name Request: Name_Type"
        //   bad_collection.add(bad_req_doc).then((result) => {
        //     return
        //   }).catch((result) => {
        //     return
        //   });
        // }
        //if (data.Req_Arguments.keys().indexof("Amount") === -1) data.Req_Arguments["Amount"] = 1
      }
      else if (data.Req_Type === "Sentence"){
        // if (data.Req_Arguments.keys().indexof("Sentence_Type") === -1){
        //   const bad_req_doc = data
        //   bad_req_doc.Message = "Missing Required Argument Field For A Sentence Request: Sentence_Type"
        //   bad_collection.add(bad_req_doc).then((result) => {
        //     return
        //   }).catch((result) => {
        //     return
        //   });
        // }
        //if (data.Req_Arguments.keys().indexof("Amount") === -1) data.Req_Arguments["Amount"] = 1
      }
      else{
          const bad_req_doc = data
          bad_req_doc.Message = "Unsupported Req_Type value"
          bad_collection.add(bad_req_doc).then((result) => {
            return 1
          }).catch((result) => {
            return 1
          });
      }

      //Build JSON Object To Send To HTTP Server
      const processed_data = {}

      processed_data["Req_Type"] = data.Req_Type
      processed_data["Req_Arguments"] = data.Req_Arguments
      processed_data["User_ID"] = data.User_ID
      
      if (data.Hash_Key !== null) processed_data["Hash_Key"] = data.Hash_Key
      if (data.Request_Source !== null) processed_data["Hash_Key"] = data.Hash_Key

      //Send HTTP Notification To Server
      //const headers = new HttpHeaders({'Content-Type':'application/json; charset=utf-8'});
      //https.request
      //https.post("machinelearningmadlads.pythonanywhere.com/VoidScribeRequest", JSON.stringify(processed_data), {headers: headers})
      let json_data = JSON.stringify(processed_data)
      let url = "https://machinelearningmadlads.pythonanywhere.com/VoidScribeRequest"
      req.post({
        headers: {
          'content-type': 'application/json'
        },
        url: url,
        body: json_data
      }
      )
      return 1
    });

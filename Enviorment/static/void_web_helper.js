function getApiEndpoint(Type) 
{
    switch(Type) 
    {
        case "Prompt":
            return "http://www.voidscribe.com/GeneratePrompts";
        case "NameGenerate":
            return "http://www.voidscribe.com/GenerateNames";
        case "NameRetreive":
            return "http://www.voidscribe.com/RetreiveNames";
        default:
            throw "Argument 'Type' must be value: 'Prompt', 'NameGenerate', or 'NameRetreive'.";
    }
}

function getJSON(Type, sType, Amount) 
{
    var jsonData = {}
    switch(Type) 
    {
        case "Prompt":
            jsonData["Prompt_Type"] = sType;
            break;
        case "NameGenerate":
            jsonData["Name_Type"] = sType;
            break;
        case "NameRetreive":
            jsonData["Name_Type"] = sType;
            break;
        default:
            throw "Argument 'Type' must be value: 'Prompt', 'NameGenerate', or 'NameRetreive'.";
    }
    jsonData["Amount"] = Amount;
    jsonData = JSON.stringify(jsonData);
    return jsonData;
}

function GenerateNames(NameType, Amount)
{
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
    
    var xhr = new XMLHttpRequest();
    var url = "http://www.voidscribe.com/GenerateNames";
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = getJSON("NameGenerate", NameType, Amount);
    xhr.send(data);
    if (xhr.status === 200) 
    {
        var json = JSON.parse(xhr.responseText);
        return json.Data;
    }
}

function RetreiveNames(NameType, Amount)
{
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
    
    var xhr = new XMLHttpRequest();
    var url = "http://www.voidscribe.com/RetreiveNames";
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = getJSON("NameRetreive", NameType, Amount);
    xhr.send(data);
    if (xhr.status === 200) 
    {
        var json = JSON.parse(xhr.responseText);
        return json.Data;
    }
}

function GeneratePrompts(PromptType, Amount)
{
    var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
    
    var xhr = new XMLHttpRequest();
    var url = "http://www.voidscribe.com/GeneratePrompts";
    xhr.open("POST", url, false);
    xhr.setRequestHeader("Content-Type", "application/json");
    var data = getJSON("Prompt", PromptType, Amount);
    xhr.send(data);
    if (xhr.status === 200) 
    {
        var json = JSON.parse(xhr.responseText);
        return json.Data;
    }
}

function generateOutput(){
    var sType = "";
    var num = 1;

    prompts = document.getElementById('radioPrompts');
    if (prompts.checked){
        sType = document.getElementById('promptTypeSearch').value;
        num = document.getElementById('numPrompts').value;
        document.getElementById('outputPrompts').text = GeneratePrompts(sType, num);
    } else {
        num = document.getElementById('numNames').value;
        sType = document.getElementById('nameTypeSearch').value;
        generate = document.getElementById('radioGenerate');
        if (generate.checked){
            document.getElementById('outputNames').text = GenerateNames(sType, num);
        } else {
            document.getElementById('outputNames').text = RetreiveNames(sType, num);
        }
    }
}

function showElement(elementId) {
    document.getElementById(elementId).classList.add("show");
}

function hideElement(elementId) {
    document.getElementById(elementId).classList.remove("show");
}

function switchView(viewID){
    var i = 0;
    elems = document.getElementsByClassName("View");
    for (i = 0; i < elems.length; i++){
        elems[i].style.display = "none";
    };

    document.getElementById(viewID).style.display = "block";
}

function populateSearch(searchId, input){
    document.getElementById(searchId).value = input;
}

function populateAPIfields(){
    readonlyAPI = document.getElementById('readonlyAPI');
    readonlyJSON = document.getElementById('readonlyJSON');
    var type = "";
    var sType = "";
    var num = 1;
    

    prompts = document.getElementById('radioPrompts');
    if (prompts.checked){
        type = "Prompt";
        sType = document.getElementById('promptTypeSearch').value;
        num = document.getElementById('numPrompts').value;
    } else {
        generate = document.getElementById('radioGenerate') 
        if (generate.checked){
            type = "NameGenerate";
        } else {
            type = "NameRetreive";
        }
        num = document.getElementById('numNames').value;
        sType = document.getElementById('nameTypeSearch').value;
    }
    readonlyAPI.value = getApiEndpoint(type)
    if (sType != ""){
        readonlyJSON.value = getJSON(type, sType, num);
    }
}

function copyToClipboard(elemId){
    var copyText = document.getElementById(elemId);
    copyText.select();
}

function filterFunction(inputId, spanId){
    var input, filter, ul, li, a, i;
    input = document.getElementById(inputId);
    filter = input.value.toUpperCase();
    span = document.getElementById(spanId);
    a = span.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
      txtValue = a[i].textContent || a[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        a[i].style.display = "";
      } else {
        a[i].style.display = "none";
      }
    }
  }
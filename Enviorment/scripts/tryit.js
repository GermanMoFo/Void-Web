function getJSON(Type, sType, Amount) 
// Type = Prompt, NameGenerate, or NameRetreive
// sType = type of prompt or name to get.
// Amount = number of retrievals to perform.
{
    var jsonData = {}
    switch(Type) 
    {
        case "Prompt":
            jsonData["Prompt_Type"] = sType;
            break;
        case "NameGenerate":
        case "NameRetreive":
            jsonData["Name_Type"] = sType;
            break;
        default:
            throw "Argument 'Type' must be value: 'Prompt', 'NameGenerate', or 'NameRetreive'.";
    }
    jsonData["Amount"] = Amount
    jsonData = JSON.stringify(jsonData)
    return jsonData
}

getJSON('Prompt', 'acquire', 1)

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

function populateDropDowns(value){

}

function switchView(viewID){
    elems = document.getElementsByClassName("View");
    for (elem in elems){
        elem.style.display = "none";
    };

    document.getElementById(viewID).style.display = "block";

    // if (document.getElementById('yesCheck').checked) {
    //     document.getElementById('ifYes').style.visibility = 'visible';
    // } else {
    //     document.getElementById('ifYes').style.visibility = 'hidden';
    // }
}

function filterFunction(elemId){
  var input, filter, ul, li, a, i;
  input = document.getElementById(elemId);
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("a");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}
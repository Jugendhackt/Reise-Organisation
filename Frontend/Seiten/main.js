function displayVals() {
  if ($( "#startbahnhof" ).val()=="" || $( "#zielbahnhof" ).val()=="") {
    return false;
  }
  var eingabe = [$( "#unterkunft" ).val(), $( "#kultur" ).val(),
  $( "#preisklasse" ).val(), $( "#kultur" ).val(), $( "#startbahnhof" ).val(),
  $( "#zielbahnhof" ).val()];
  console.log("test");
  $.ajax({url: "http://128.199.88.103:5000/zug2/"+eingabe[4]+"/"+eingabe[5],
  success: function(result){
    $( "#output" ).html( "<b>Result:</b> " + result);
  }});
}
$( "#formular" ).change( displayVals );
displayVals();

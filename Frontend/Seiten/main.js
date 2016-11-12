(function($){
function displayVals() {
var singleValues = $( "#startbahnhof" ).val();
var singleValues = $( "#startbahnhof" ).val();
$( "#output" ).html( "<b>Result:</b> " + singleValues);
}

$( "#startbahnhof" ).change( displayVals );
displayVals();
})(jQuery);

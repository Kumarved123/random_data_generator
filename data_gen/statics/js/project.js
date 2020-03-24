$(document).ready(function() {
    $('tbody').sortable();
});

var btn = document.getElementById("closebutton");
var cross = document.getElementById("crossbtn");
var model = document.getElementById("myModal");

btn.onclick = function goBack() {
    window.history.back()
}
cross.onclick = function close() {
    $("#myModal").modal('hide');
}

var nobtn = document.getElementById("noclosebutton");
var nomodel = document.getElementById("nomyModal");

nobtn.onclick = function nogoBack() {
    window.history.back()
}

function SomeDeleteRowFunction(o) {
    var table = o.parentNode.parentNode.parentNode.parentNode.parentNode;
    var rowCount = table.rows.length;
    if (rowCount <= 2) {
        alert('Cannot delete all the rows !!!')
    } else {
        var permission = confirm("Do you want to delete this row ?");
        if (permission == true) {
            var child = o.parentNode.parentNode.parentNode;
            var row = o.parentNode.parentNode.parentNode.parentNode;
            row.removeChild(child)
        }
    }
}
var newvalue;

function changefun(o) {
    newvalue = o.childNodes[0];
    o.style.color = "blue";
}

function formulas() {
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("exampleFormControlTextarea1");
    newvalue.value = inputVal.value;
    inputVal.value = '';
}

if (document.getElementsByClassName("testName").checked) {
    document.getElementsByClassName('testNameHidden').value = 'on';
}

function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == "" || x == null) {
        alert("Name must be filled out");
        return false;
    }
}
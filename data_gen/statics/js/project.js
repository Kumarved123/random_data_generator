// floting table rows
$(document).ready(function() {
    $('tbody').sortable();
});

// Close and display button on preview popup
var btn = document.getElementById("closebutton");
var cross = document.getElementById("crossbtn");

// function for close button
btn.onclick = function goBack() {
        window.history.back()
    }
    // function for cross Button
cross.onclick = function close() {
    window.history.back()
}

// message close button
var nobtn = document.getElementById("noclosebutton");

nobtn.onclick = function nogoBack() {
    window.history.back()
}

// function to close the delelte the row
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

// 
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
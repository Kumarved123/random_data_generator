// floating table rows
$(document).ready(function() {
    $('tbody').sortable();
    $('#previewbtn').click(function() {
        var form = $('#myForm')
        $.post('', $(form).serialize() + '&button=' + "Preview", function(data) {
            $('.table').html(data.table_content);
        });
        $('#myForm').submit.preventDefault();
    })


});


// function to close the delete the row
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
};

if (document.getElementsByClassName("testName").checked) {
    document.getElementsByClassName('testNameHidden').value = 'on';
};
// floating table rows
$(document).ready(function() {
    $('tbody').sortable();
    $('#previewbtn').click(function() {
        // $(':disabled').each(function(e) {
        //     $(this).removeAttr('disabled');
        // })
        var form = $('#myForm')
        $('#previewbtn').removeAttr('disabled');
        $.post('', $(form).serialize() + '&button=' + "Preview", function(data) {
            $('.message').html(data.table_content);
        });
        // $('input[type=text]').each(function() {
        //     var val = parseInt($(this).val());
        //     var name = $(this).attr("name")
        //     if (val == 0 && name == "valEmpty") {
        //         $(this).attr("disabled", true);
        //     }
        // });
    });
    // $('#downloadbtn').click(function() {
    //     $(':disabled').each(function(e) {
    //         $(this).removeAttr('disabled');
    //     });
    //     var form = $('#myForm')
    //     $.post('', $(form).serialize() + '&button=' + "download", function(data) {
    //         console.log(data)
    //         $.fileDownload('download/random_data.xlsx')
    //             .done(function() { alert('File download a success!'); })
    //             .fail(function() { alert('File download failed!'); });

    //     });
    //     $('input[type=text]').each(function() {
    //         var val = parseInt($(this).val());
    //         var name = $(this).attr("name")
    //         if (val == 0 && name == "valEmpty") {
    //             $(this).attr("disabled", true);
    //         }
    //     });
    // });
});



// function to close the delete the row
function SomeDeleteRowFunction(o) {
    var table = o.parentNode.parentNode.parentNode.parentNode.parentNode;
    var rowCount = table.rows.length;
    var row = o.parentNode.parentNode.parentNode.parentNode;
    var child = o.parentNode.parentNode.parentNode;
    if (rowCount <= 2 || rowCount - 1 == child.rowIndex) {
        alert('Cannot delete this row !!!')
    } else {
        var permission = confirm("Do you want to delete this row ?");
        if (permission == true) {
            row.removeChild(child)
        }
    }
}

// 
var newvalue;

function changefun(o) {
    newvalue = o.childNodes[0];
}

function formulas() {
    // Selecting the input element and get its value 
    var inputVal = document.getElementById("exampleFormControlTextarea1");
    newvalue.value = inputVal.value;
    inputVal.value = '';
    if (newvalue.value != "") {
        newvalue.parentNode.style.color = "blue"
    }
};

if (document.getElementsByClassName("testName").checked) {
    document.getElementsByClassName('testNameHidden').value = 'on';
};
if (document.getElementsByClassName("test").disabled) {
    document.getElementsByClassName('testHidden').value = "0";
};

function hero(o) {
    // Get the checkbox
    // Get the output text
    var text = o.parentNode.parentNode.children[4].children[0].children[0];
    // var text2 = o.parentNode.parentNode.children[4].children[0].children[1];
    // If the checkbox is checked, display the output text

    if (o.checked == true) {
        text.disabled = false;
        // text2.disabled = true;

    } else {
        text.disabled = true;
        // text2.disabled = false;

    }
    // console.log(text2.disabled)
    // console.log(text.disabled)
}
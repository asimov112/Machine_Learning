$(document).ready(function() {
    
    $("#clearAction").click(function() {
        $(this).text = "";
    });
    $("#copy").click(function() {
        var copyText = $("#correctText");
        copyText.text().select();
        navigator.clipboard.writeText(copyText.value);
        
    });
});
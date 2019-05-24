function testTime() {
	document.getElementById('tes1').innerHTML = Date();
}

function buttonWindow(where, ver1, ver2) {
	var table = document.getElementById(where.attributes.rel.value);
	where.value = ( where.value == ver1) ? ver2 : ver1;
	table.style.display =  (table.style.display == 'block') ? 'none' : 'block';
}
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
	if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
		document.getElementById("myTop").style.display = "block";		
	} else {
		document.getElementById("myTop").style.display = "none";
	}
}

function toTop() {
	document.body.scrollTop = 0;
	document.documentElement.scrollTop = 0;
}

function cancel() {	
	document.getElementById('loginIframe').style.display="none";
	document.getElementById('cancelButton1').style.display="none";

}
function cancel2() {	
	document.getElementById('loginIframe2').style.display="none";
	document.getElementById('cancelButton2').style.display="none";

}


function pictures() {
var i=0;
for (i=0;i<=30;i++)
	{
	document.getElementById("ShowPicHere").innerHTML += "<img src=\"../Pic/Pictures/Test/"
	i + ".jpg\" width=\"50px\" height=\"50px\" <br \> ";
	}
}


function ClickMe() {
	document.getElementById("hideText").style.display="none";
	document.getElementsByClassName("Open").style.display="none";	
	document.getElementById("loginDrop").style.display="none";
	document.getElementById("registerDrop").style.display="none";
	document.getElementById("HideAll").style.display="none";	
}

/*
	
$(document).ready(function(){
		$('#ShowPicHere').append("<img id=\"Test001\" src='./Pic/Pictures/Test/0.jpg' />");
});





$(document).scroll(function () {
    var y = $(this).scrollTop();
    if (y > 400) {
				$('#ShowPicHere').fadeIn(800);			
		} 			
		else {
        $('#ShowPicHere').fadeOut(300);
    }

});
*/
		
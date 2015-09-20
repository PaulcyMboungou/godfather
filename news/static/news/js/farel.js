function removeChosenNumber(MatriculeNo) {
	// console.log('yes')
   var num = document.querySelector("#number").value;
   MatriculeNo.splice(MatriculeNo.indexOf(num), 1);
}

$(document).ready(function(){
	$('.handle').on('click', function(){
        // console.log('Farel')
           $('nav ul').toggleClass('showing');
           // console.log('Farel')
       });

});

$(document).ready(function(){
	$('#comment').click(function(){
		$('#comment-box').css("display", "block");
	});
	// $('#comment').click(function(){
	// 	$('#comment-box').css("display", "none");
	// });

});

function Comment()
{

}





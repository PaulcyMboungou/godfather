function removeChosenNumber(MatriculeNo) {
	// console.log('yes')
   var num = document.querySelector("#number").value;
   MatriculeNo.splice(MatriculeNo.indexOf(num), 1);
}

// $('.handle').on('click', function(){
//             // console.log('Farel')
//                $('nav ul').toggleClass('showing');
//                // console.log('Farel')
//            });

// function autocomplete(MatriculeNo){
//   loadAutocomplete("#number", MatriculeNo);
// }
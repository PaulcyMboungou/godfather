function removeChosenNumber(MatriculeNo) {
   var num = document.querySelector("#number").value;
   MatriculeNo.splice(MatriculeNo.indexOf(num), 1);
}

// function autocomplete(MatriculeNo){
//   loadAutocomplete("#number", MatriculeNo);
// }
const userName=document.querySelector('.user-name');
const memberOption = document.querySelector('.member-option')

userName.addEventListener('click', function(event){
  if (memberOption.style.display =="none"){
    memberOption.style.display = "flex";
    setTimeout(function() {
       memberOption.style.top = "55px";
     }, 10);
    
  }else{
    memberOption.style.top = "10px";
    setTimeout(function() {
      memberOption.style.display = "none";
     }, 10);
  }
});


addRoomBtn = document.querySelector('.add-room-btn');
cancelBtn = document.querySelector('#cancel-btn');
 addRoomBtn.addEventListener('click', function () {
   document.querySelector('.add-room-form').style.display = 'block';
});
 cancelBtn.addEventListener('click',function(event){
   event.preventDefault();
   document.querySelector('.add-room-form').style.display = 'none';
 })
// Code By Webdevtrick ( https://webdevtrick.com )
$('.form').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');
 
   if (e.type === 'keyup') {
 if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
     if( $this.val() === '' ) {
     label.removeClass('active highlight'); 
 } else {
     label.removeClass('highlight');   
 }   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
     label.removeClass('highlight'); 
 } 
      else if( $this.val() !== '' ) {
     label.addClass('highlight');
 }
    }
 
});
 
$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');
 
  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);

});

async function signup(){
    alert("I made it");
    const response = await $.post("/signup",{
	"username": document.getElementId("username").value,
	"password": document.getElementId("password").value }, "json");

    token = await response.data;
    alert(token);
    alert(response.data.message);

    return true;
}

async function login(){
    const response = await $.post("/authU",{
	"username": document.getElementId("username").value,
	"password": document.getElementId("password").value }, "json");

    if (response == 200){
	token = await response.data;
	alert("dude, you did it bro");
    }else{
	alert("fudge dawg, somethin aint right");
    }
}


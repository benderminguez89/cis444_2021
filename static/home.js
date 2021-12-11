function send_form(){
    console.log("made it login");
    var user = $('#username').val();
    var pw = $('#password').val();

    if(user.length == 0 || pw.length ==0){return false;}	
    $.post("/open_api/login", { "username": user, "password":pw},
	   
           function(data, textStatus) {
	       console.log("made it here");
	       //this gets called when browser receives response from server
	       console.log(data.token);
	       //Set global JWT
	       jwt = data.token;
	       //make secure call with the jwt
	       return window.location.href='letsGo.html';
           }, "json").fail( function(response) {
	       //this gets called if the server throws an error
	       console.log("error");
	       console.log(response);
	   });
    
    return false;
}


function send_form2(){
    console.log("made it signup");
    var user = $('#username').val();
    var pw = $('#password').val();

    if(user.length == 0 || pw.length ==0){return false;}	
    $.post("/open_api/signup", { "username":user, "password":$pw},
           function(data, textStatus) {
	       console.log("made it here");
	       //this gets called when browser receives response from server
	       console.log(data.token);
	       //Set global JWT
	       jwt = data.token;
	       //make secure call with the jwt
	       return window.location.href='letsGo.html';
           }, "json").fail( function(response) {
	       //this gets called if the server throws an error
	       console.log("error");
	       console.log(response);
           });
    
    return false;
}

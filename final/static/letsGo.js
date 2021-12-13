//js file
//login function
function login(){

    var user = $('#username').val();
    var pass = $('#password').val();
    if(user.length == 0 || pass.length == 0){
	return false;
    }
    $.post("/open_api/login", { "username": user, "password": pass},
           function(data, textStatus) {
               console.log("made it here");
               //this gets called when browser receives response from server
               console.log(data.token);
               //Set global JWT
               jwt = data.token;
               //make secure call with the jwt
	       home();
	                          
           }, "json").fail( function(response) {
               //this gets called if the server throws an error
               console.log("error");
               console.log(response);
           });
    return false;
}

//sign up function
function signup(){
    
    var user = $('#username').val();
    var pass = $('#password').val();
    if(user.length == 0 || pass.length == 0){
	return false;
    }
    $.post("/open_api/signup", { "username": user, "password": pass},
           function(data, textStatus) {
               console.log("made it here");
               //this gets called when browser receives response from server
               console.log(data.token);
               //Set global JWT
               jwt = data.token;
               //make secure call with the jwt
	       home();
	                          
           }, "json").fail( function(response) {
               //this gets called if the server throws an error
               console.log("error");
               console.log(response);
           });
    return false;
}

function home(){
    $("#Start").hide();    
    $("#Home").show();

}

function amigos(){
    $("#Home").hide();
    $("#Start").show();    
}

function movies(){
    $("#Home").hide();
    $("#Start").show();        
}

function sports(){
    $("#Home").hide();
    $("#Start").show();    
}

function adios(){
    $("#Home").hide();
    $("#Start").show();

}

function letsGo(){
    $("#Home").hide();
    $("#Start").show();

}

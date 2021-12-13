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
               //Set global JWT
               jwt = data.token;
               //make secure call with the jwt
	       home(data);
	                          
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
    console.log("Take me to the Movies!");
    console.log(data);
    secure_get_with_token("/secure_api/amc",  function(data){
        console.log("got movies");
        console.log(data);
        

       // table = document.getElementById("content-table");

        for(var i=0; i< Object.keys(data.data.movies).length; i++) {
            console.log(data.data.movies[i]);
           // row = table.insertRow(i+1);
           // cell1 = row.insertCell(0);
           // cell2 = row.insertCell(1);
           // cell3 = row.insertCell(2);
           // cell4 = row.insertCell(3);
           // cell1.innerHTML = data.data.books[i].title;
           // cell2.innerHTML = data.data.books[i].author;
           //cell3.innerHTML = data.data.books[i].price;
           // cell4.innerHTML = '<button onclick="addCart(\'' + data.data.books[i].title + '\')">Buy</button>';
        }

        for(var i=0; i< Object.keys(data.data.coming_soon).length; i++) {
            console.log(data.data.coming_soon[i]);
           // row = table.insertRow(i+1);
           // cell1 = row.insertCell(0);
           // cell2 = row.insertCell(1);
           // cell3 = row.insertCell(2);
           // cell4 = row.insertCell(3);
           // cell1.innerHTML = data.data.books[i].title;
           // cell2.innerHTML = data.data.books[i].author;
           //cell3.innerHTML = data.data.books[i].price;
           // cell4.innerHTML = '<button onclick="addCart(\'' + data.data.books[i].title + '\')">Buy</button>';
        }
	$("#Start").show();        
    },
                          function(err){ console.log(err) });
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

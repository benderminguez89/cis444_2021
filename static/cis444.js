var jwt = null

function secure_get_with_token(endpoint, on_success_callback, on_fail_callback){
    xhr = new XMLHttpRequest();
    function setHeader(xhr) {
	xhr.setRequestHeader('Authorization', 'Bearer:'+jwt);
    }
    function get_and_set_new_jwt(data){
	console.log(data);
	jwt  = data.token
	on_success_callback(data)
    }
    $.ajax({
	url: endpoint,
	type: 'GET',
	datatype: 'json',
	success: on_success_callback,
	error: on_fail_callback,
	beforeSend: setHeader
    });
       
}

function secure_get_with_data(endpoint, data_to_send, on_success_callback, on_fail_callback){
        xhr = new XMLHttpRequest();
        function setHeader(xhr) {
                xhr.setRequestHeader('Authorization', 'Bearer:'+jwt);
        }
        function get_and_set_new_jwt(data){
                console.log(data);
                jwt  = data.token
                on_success_callback(data)
        }
        $.ajax({
            url: endpoint,
	    data: data_to_send,
            type: 'GET',
            datatype: 'json',
            success: on_success_callback,
            error: on_fail_callback,
            beforeSend: setHeader
        });
}

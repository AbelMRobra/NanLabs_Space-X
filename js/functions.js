
window.onload = service_get_lists()

async function service_get_lists(){
    host = 'https://spacexmanager.herokuapp.com'
    const url = `${host}/list`

    var response = await fetch(url ,{
        method: "GET",
        headers: {
            'Content-Type': 'application/json',
        },
    })

    var response_text = await response.json();
    var status = await response.status;
    return validate_lists(response_text, status);
}

async function service_api(){
    host = 'https://spacexmanager.herokuapp.com'
    const url = `${host}/cards`

    swal({
        title: "In process!",
        text: "Your request is processing",
        icon: "warning",
        timer: 3000
        });

    var response = await fetch(url ,{
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },

        body: JSON.stringify({
            'list' : document.getElementById("list").value,
            'name' : document.getElementById("name").value,
            'desc' : document.getElementById("desc").value

        })

    })

    var response_text = await response.json()
    var status = await response.status
    return validate_response(response_text, status)
}

function validate_lists(response, status){
    if (status >= 200 && status <300){
        console.log(response);
   
    } else {
        console.log(response);
    }
}

function validate_response(response, status){
    if (status >= 200 && status <300){
        swal("Good job!", "You sent the card!", "success");
   
    } else {
        console.log(response);
        swal("Ups ..", "problems!", "warning");
    }
}
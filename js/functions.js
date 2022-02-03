
async function service_api(){
    host = 'https://spacexmanager.herokuapp.com'
    const url = `${host}/cards`

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

function validate_response(response, status){
    if (status >= 200 && status <300){
        swal("Good job!", "You sent the card!", "success");
   
    } else {
        console.log(response)
        swal("Ups ..", "problems!", "warning");
    }
}
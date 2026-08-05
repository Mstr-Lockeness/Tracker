function handleToggle(checkbox) {
    const form = checkbox.parentElement;
    const input = form.querySelector("input[name=mount_name]");
    const mountName = input.value;
    const url = form.action;
    const card = form.parentElement.parentElement;

    fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        mount_name: mountName
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        console.log(data.obtained, typeof data.obtained);
        if (data.obtained == true) {
            card.style.backgroundColor = "#c6f5c6";
        } 
        else {
            card.style.backgroundColor = "#f5c6d6";
        }
    });
}
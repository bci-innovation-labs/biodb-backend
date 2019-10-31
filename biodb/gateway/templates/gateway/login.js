function onLoginClick() {
    const usernameElement = document.getElementById("username");
    const username = usernameElement.value;
    console.log(username)
    const passwordElement = document.getElementById("password");
    const password = passwordElement.value;
    console.log(password);

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            const loginObject = JSON.parse(this.responseText);
            if (loginObject.was_successful === true) {
                window.location.href = "{% url 'dashboad' %}";
            } else {
                alert(loginObject.reason);
            }
        }
    }
    xhttp.open("POST", "{% url 'login_api' %}", true);
    xhttp.setRequestHeader("content-type", "application/x-www-form-urlencoded");
    const string = "username="+username+"&password="+password
    xhttp.send(string)
}

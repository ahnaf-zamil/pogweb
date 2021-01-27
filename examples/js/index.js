const sendRequest = () => {
  fetch("/api")
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("ok").innerHTML = data.msg
    });
};

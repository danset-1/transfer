async function reset(){
    const response = await fetch("/r");
    const data = await response.json();

    document.getElementById("aValue").innerText = data.a;
    document.getElementById("bValue").innerText = data.b;
    document.getElementById("yValue").innerText = data.y;
}

async function stop(){
    const response = await fetch("/stop");
    const data = await response.json();

    document.getElementById("aValue").innerText = data.a;
    document.getElementById("bValue").innerText = data.b;
    document.getElementById("yValue").innerText = data.y;
}


function sendSignal(x) {
  const payload = { id: x };

  fetch("/signal_stop", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  })
  .catch(error => console.error("Error:", error));
}

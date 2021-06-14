const socket = io("http://localhost:3000/");

socket.on("hello", (message) => {
  console.log(message);
});

function removeNotif(event) {
  event.target.parentNode.remove();
}

const server = require("http").createServer();
const { Server } = require("socket.io");
const io = new Server(server, {
  cors: {
    origin: function (origin, fn) {
      return fn(null, origin);
    },
    credentials: true,
  },
  allowEIO3: true,
});

io.on("connection", (socket) => {
  socket.emit("hello", "Socket WORKS!");
  console.log("a user connected");
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});

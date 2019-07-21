import openSocket from 'socket.io-client';
const  socket = openSocket('http://localhost:5001');
function subscribeToServer(cb) {
  socket.on('js-cli', obj => cb(obj));
}
export { subscribeToServer };

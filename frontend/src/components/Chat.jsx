import { useEffect, useState } from 'react';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [message, setMessage] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    // Retrieve the JWT token from localStorage
    const token = localStorage.getItem('access_token');

    // Add the token as a query parameter to the WebSocket URL
    const ws = new WebSocket(`ws://localhost:8000/ws/chat/?token=${token}`);

    ws.onopen = () => {
      console.log('WebSocket connection established');
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      const newMessage = {
        message: data.message,
        username: data.username,
        color: data.color,
      };
      setMessages((prevMessages) => [...prevMessages, newMessage]);
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    ws.onclose = (event) => {
      console.log('WebSocket closed:', event.code, event.reason);
    };

    setSocket(ws);

    return () => ws.close();
  }, []);

  const sendMessage = () => {
    if (socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify({ message }));
      setMessage('');  // Clear the input field after sending the message
    } else {
      console.error('WebSocket connection is not open');
    }
  };

  return (
      <div>
        <h2>Chat Room</h2>
        <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={sendMessage}>Send</button>
        <div>
          {messages.map((msg, index) => (
              <p key={index}>
                <strong style={{color: msg.color}}>{msg.username}: </strong>
                {msg.message}
              </p>
          ))}
        </div>
      </div>
  );
};

export default Chat;

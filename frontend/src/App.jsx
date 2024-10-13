import { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom'; // Use Routes instead of Switch
import SignUp from './components/SignUp';
import Login from './components/Login';
import Chat from './components/Chat';

const App = () => {
  const [token, setToken] = useState(localStorage.getItem('access_token'));

  return (
    <Router>
      <div>
        {/* Navigation Links */}
        <nav>
          <ul>
            <li>
              <Link to="/signup">Sign Up</Link>
            </li>
            <li>
              <Link to="/login">Log In</Link>
            </li>
            {token && (
              <li>
                <Link to="/chat">Chat</Link>
              </li>
            )}
          </ul>
        </nav>

        {/* Routes */}
        <Routes>
          <Route path="/signup" element={<SignUp />} />
          <Route path="/login" element={<Login setToken={setToken} />} />
          {token && (
            <Route path="/chat" element={<Chat />} />
          )}
        </Routes>
      </div>
    </Router>
  );
};

export default App;

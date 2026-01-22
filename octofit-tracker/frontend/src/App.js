import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
          <div className="container-fluid">
            <Link className="navbar-brand" to="/">OctoFit Tracker</Link>
            <button 
              className="navbar-toggler" 
              type="button" 
              data-bs-toggle="collapse" 
              data-bs-target="#navbarNav" 
              aria-controls="navbarNav" 
              aria-expanded="false" 
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav">
                <li className="nav-item">
                  <Link className="nav-link" to="/">Home</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Users</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Teams</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/activities">Activities</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Workouts</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <Routes>
          <Route path="/" element={
            <div className="container mt-4">
              <div className="hero-section text-center">
                <h1 className="display-3">Welcome to OctoFit Tracker! 🏋️</h1>
                <p className="lead">Track your fitness activities, compete with your team, and stay motivated.</p>
                <hr className="hero-divider" />
                <p className="mb-0">Use the navigation menu above to explore users, teams, activities, leaderboard, and workout suggestions.</p>
              </div>
              
              <div className="row mt-5 mb-4">
                <div className="col-md-4 mb-4">
                  <Link to="/users" className="text-decoration-none">
                    <div className="card text-center clickable-card">
                      <div className="card-body">
                        <h3 className="card-title">👥 Users</h3>
                        <p className="card-text">View all registered users and their fitness stats.</p>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col-md-4 mb-4">
                  <Link to="/teams" className="text-decoration-none">
                    <div className="card text-center clickable-card">
                      <div className="card-body">
                        <h3 className="card-title">🏆 Teams</h3>
                        <p className="card-text">Explore teams and their collective achievements.</p>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col-md-4 mb-4">
                  <Link to="/activities" className="text-decoration-none">
                    <div className="card text-center clickable-card">
                      <div className="card-body">
                        <h3 className="card-title">📊 Activities</h3>
                        <p className="card-text">Track and monitor all fitness activities.</p>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
              
              <div className="row mb-4">
                <div className="col-md-4 mb-4">
                  <Link to="/leaderboard" className="text-decoration-none">
                    <div className="card text-center clickable-card">
                      <div className="card-body">
                        <h3 className="card-title">🏅 Leaderboard</h3>
                        <p className="card-text">See the top performers and compete for the best rank.</p>
                      </div>
                    </div>
                  </Link>
                </div>
                <div className="col-md-4 mb-4">
                  <Link to="/workouts" className="text-decoration-none">
                    <div className="card text-center clickable-card">
                      <div className="card-body">
                        <h3 className="card-title">💪 Workouts</h3>
                        <p className="card-text">Discover workout activities and earn points.</p>
                      </div>
                    </div>
                  </Link>
                </div>
              </div>
            </div>
          } />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

import React, { useState, useEffect } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log('Leaderboard API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Leaderboard fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const leaderboardData = data.results || data;
        setLeaderboard(Array.isArray(leaderboardData) ? leaderboardData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching leaderboard:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  if (loading) return (
    <div className="container mt-4">
      <div className="loading-container">
        <div className="spinner-border text-primary" role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <span className="ms-3">Loading leaderboard...</span>
      </div>
    </div>
  );
  
  if (error) return (
    <div className="container mt-4">
      <div className="alert alert-danger" role="alert">
        <h4 className="alert-heading">Error!</h4>
        <p>Error: {error}</p>
      </div>
    </div>
  );

  const getRankBadge = (rank) => {
    if (rank === 1) return <span className="badge bg-warning text-dark">🥇 1st</span>;
    if (rank === 2) return <span className="badge bg-secondary">🥈 2nd</span>;
    if (rank === 3) return <span className="badge bg-danger">🥉 3rd</span>;
    return <span className="badge bg-light text-dark">{rank}th</span>;
  };

  return (
    <div className="container mt-4">
      <h1 className="page-header">🏆 Leaderboard</h1>
      <div className="table-container">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="mb-0">Top Performers</h5>
          <span className="badge bg-primary">{leaderboard.length} Competitors</span>
        </div>
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>Rank</th>
                <th>Type</th>
                <th>Name</th>
                <th>Alias/Username</th>
                <th>Total Points</th>
                <th>Activities</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard.length > 0 ? (
                leaderboard.map((entry, index) => (
                  <tr key={entry._id || entry.id || index} className={entry.rank <= 3 ? 'table-active' : ''}>
                    <td>{getRankBadge(entry.rank)}</td>
                    <td><span className={`badge ${entry.type === 'team' ? 'bg-info' : 'bg-secondary'}`}>
                      {entry.type === 'team' ? '👥 Team' : '👤 Individual'}
                    </span></td>
                    <td><strong>{entry.entity_name}</strong></td>
                    <td>{entry.entity_alias ? <span className="badge bg-light text-dark">{entry.entity_alias}</span> : '-'}</td>
                    <td><span className="badge bg-primary">{entry.total_points || 0}</span></td>
                    <td>{entry.activities_count || '-'}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="text-center text-muted">No leaderboard data available</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Leaderboard;

import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;
    console.log('Teams API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Teams fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(Array.isArray(teamsData) ? teamsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
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
        <span className="ms-3">Loading teams...</span>
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

  return (
    <div className="container mt-4">
      <h1 className="page-header">🏆 Teams</h1>
      <div className="mb-4">
        <p className="text-muted">Total Teams: <span className="badge bg-primary ms-2">{teams.length}</span></p>
      </div>
      <div className="row">
        {teams.length > 0 ? (
          teams.map(team => (
            <div key={team._id || team.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card">
                <div className="card-body">
                  <h5 className="card-title">👥 {team.name}</h5>
                  <p className="card-text text-muted">{team.description || 'No description available'}</p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center mb-2">
                    <span><strong>Members:</strong></span>
                    <span className="badge bg-info">{team.member_count || 0}</span>
                  </div>
                  <div className="d-flex justify-content-between align-items-center">
                    <span><strong>Created:</strong></span>
                    <span className="text-muted small">{new Date(team.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No teams found
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Teams;

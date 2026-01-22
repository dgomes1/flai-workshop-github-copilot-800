import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
    console.log('Workouts API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Workouts fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(Array.isArray(workoutsData) ? workoutsData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
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
        <span className="ms-3">Loading workouts...</span>
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
      <h1 className="page-header">💪 Workout Activities</h1>
      <div className="mb-4">
        <p className="text-muted">Available Workouts: <span className="badge bg-primary ms-2">{workouts.length}</span></p>
      </div>
      <div className="row">
        {workouts.length > 0 ? (
          workouts.map(workout => (
            <div key={workout._id || workout.id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-body">
                  <h5 className="card-title">
                    <span style={{fontSize: '2rem'}}>{workout.icon}</span> {workout.name}
                  </h5>
                  <p className="card-text text-muted">{workout.description || 'No description available'}</p>
                  <hr />
                  <div className="d-flex justify-content-between align-items-center mb-2">
                    <span><strong>Unit:</strong></span>
                    <span className="badge bg-info">{workout.unit}</span>
                  </div>
                  <div className="d-flex justify-content-between align-items-center mb-2">
                    <span><strong>Points per {workout.unit}:</strong></span>
                    <span className="badge bg-success">{workout.points_per_unit}</span>
                  </div>
                  <div className="d-flex justify-content-between align-items-center">
                    <span><strong>Created:</strong></span>
                    <span className="text-muted small">{new Date(workout.created_at).toLocaleDateString()}</span>
                  </div>
                </div>
              </div>
            </div>
          ))
        ) : (
          <div className="col-12">
            <div className="alert alert-info text-center" role="alert">
              No workout activities available
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Workouts;

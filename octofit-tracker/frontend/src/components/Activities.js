import React, { useState, useEffect } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/activities/`;
    console.log('Activities API endpoint:', apiUrl);
    
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Activities fetched data:', data);
        // Handle both paginated (.results) and plain array responses
        const activitiesData = data.results || data;
        setActivities(Array.isArray(activitiesData) ? activitiesData : []);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching activities:', error);
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
        <span className="ms-3">Loading activities...</span>
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
      <h1 className="page-header">🏃 Activities</h1>
      <div className="table-container">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="mb-0">Recent Activities</h5>
          <span className="badge bg-primary">{activities.length} Total</span>
        </div>
        <div className="table-responsive">
          <table className="table table-hover">
            <thead>
              <tr>
                <th>User</th>
                <th>Username</th>
                <th>Workout</th>
                <th>Quantity</th>
                <th>Points Earned</th>
                <th>Date</th>
              </tr>
            </thead>
            <tbody>
              {activities.length > 0 ? (
                activities.map(activity => (
                  <tr key={activity._id || activity.id}>
                    <td><strong>{activity.user_name}</strong></td>
                    <td><span className="badge bg-secondary">{activity.user_alias}</span></td>
                    <td>
                      <span style={{fontSize: '1.2rem'}}>{activity.workout_icon}</span>{' '}
                      <span className="badge bg-info">{activity.workout_name}</span>
                    </td>
                    <td>{activity.quantity} {activity.unit}</td>
                    <td><span className="badge bg-success">{activity.points_earned}</span></td>
                    <td>{new Date(activity.completed_at).toLocaleDateString()}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="6" className="text-center text-muted">No activities found</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;

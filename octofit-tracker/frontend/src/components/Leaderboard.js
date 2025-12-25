import React, { useEffect, useState } from 'react';

const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;

function Leaderboard() {
  const [data, setData] = useState([]);
  useEffect(() => {
    console.log('Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        console.log('Leaderboard data:', results);
        setData(results);
      });
  }, []);
  return (
    <div>
      <h2 className="mb-4">Leaderboard</h2>
      <div className="card shadow-sm">
        <div className="card-body">
          <table className="table table-striped table-hover">
            <thead className="table-primary">
              <tr>
                <th>User</th>
                <th>Score</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, idx) => (
                <tr key={idx}>
                  <td>{item.user}</td>
                  <td>{item.score}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
export default Leaderboard;

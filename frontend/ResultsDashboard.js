import React from 'react';

function ResultsDashboard({ results }) {
  if (!results) return null;

  return (
    <div className="results-dashboard">
      <h2>Analysis Results</h2>
      <div className="result-section">
        <h3>Claim Verdict</h3>
        <p><strong>Verdict:</strong> {results.verdict}</p>
        <p><strong>Evidence:</strong> {results.evidence}</p>
      </div>
      <div className="result-section">
        <h3>Topics & Sentiment</h3>
        <p><strong>Topics:</strong> {results.topics.join(', ')}</p>
        <p><strong>Sentiment:</strong> {results.sentiment}</p>
        <p><strong>Entities:</strong> {results.entities.join(', ')}</p>
      </div>
      <div className="result-section">
        <h3>Generated Infographic</h3>
        <img src={results.infographic} alt="Generated Infographic" className="infographic" />
      </div>
    </div>
  );
}

export default ResultsDashboard;
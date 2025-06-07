import React, { useState } from 'react';
import InputForm from './components/InputForm';
import ResultsDashboard from './components/ResultsDashboard';
import './styles.css';

function App() {
  const [results, setResults] = useState(null);

  const handleSubmit = async (inputText) => {
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: inputText }),
      });
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="app">
      <h1>AI Fact-Check & Multimedia Generator</h1>
      <InputForm onSubmit={handleSubmit} />
      <ResultsDashboard results={results} />
    </div>
  );
}

export default App;
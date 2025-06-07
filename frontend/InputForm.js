import React, { useState } from 'react';

function InputForm({ onSubmit }) {
  const [inputText, setInputText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(inputText);
  };

  return (
    <form onSubmit={handleSubmit} className="input-form">
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Enter a URL or text to fact-check"
        rows="4"
        className="input-textarea"
      />
      <button type="submit" className="submit-button">Analyze</button>
    </form>
  );
}

export default InputForm;
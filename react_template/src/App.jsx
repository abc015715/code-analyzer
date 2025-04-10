// src/App.jsx
import { useState } from 'react';
import { analyzeCode } from './services/api';

function App() {
  const [code, setCode] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!code.trim()) {
      alert('Please enter some code to analyze');
      return;
    }

    setLoading(true);
    try {
      const result = await analyzeCode(code);
      setResponse(result);
    } catch (error) {
      setResponse('Error: Failed to analyze code. Please try again.');
      console.error('Analysis error:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-gray-800">Code Analysis Tool</h1>
        
        <div className="bg-white rounded-lg shadow-md p-6 mb-6">
          <textarea
            className="w-full h-64 p-4 border border-gray-300 rounded-lg font-mono text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            placeholder="Type your code here..."
            value={code}
            onChange={(e) => setCode(e.target.value)}
          />
          
          <button
            className={`mt-4 px-6 py-2 rounded-lg text-white font-medium ${
              loading 
                ? 'bg-gray-500 cursor-not-allowed'
                : 'bg-blue-600 hover:bg-blue-700'
            }`}
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? 'Analyzing...' : 'Analyze Code'}
          </button>
        </div>

        {response && (
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-4 text-gray-800">Analysis Result</h2>
            <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded-lg text-sm">
              {response}
            </pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
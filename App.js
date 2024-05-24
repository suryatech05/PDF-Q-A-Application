import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [documentId, setDocumentId] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post("/upload/", formData, {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    });

    setDocumentId(response.data.id);
  };

  const handleAsk = async () => {
    const response = await axios.post("/ask/", {
      document_id: documentId,
      question: question,
    });

    setAnswer(response.data);
  };

  return (
    <div className="App">
      <h1>PDF Q&A</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload PDF</button>
      {documentId && (
        <>
          <input
            type="text"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={handleAsk}>Ask Question</button>
          {answer && <p>Answer: {answer}</p>}
        </>
      )}
    </div>
  );
}

export default App;

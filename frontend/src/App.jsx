import { useState } from "react";

function App() {
  const [resume, setResume] = useState("");
  const [jd, setJd] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // 🔒 Internal toggle (user doesn't need to see this)
  const USE_LLM = false;

  const analyzeResume = async () => {
    if (!resume.trim() || !jd.trim()) {
      setError("Resume and Job Description cannot be empty");
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          resume_text: resume,
          job_description: jd,
          use_llm: USE_LLM,
        }),
      });

      if (!response.ok) {
        throw new Error("Failed to analyze resume");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "900px", margin: "auto", padding: "2rem" }}>
      <h1>ATS Resume Analyzer</h1>

      <label><strong>Resume Text</strong></label>
      <textarea
        rows={8}
        value={resume}
        onChange={(e) => setResume(e.target.value)}
        style={{ width: "100%", marginBottom: "1rem", padding: "0.75rem" }}
      />

      <label><strong>Job Description</strong></label>
      <textarea
        rows={8}
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        style={{ width: "100%", marginBottom: "1rem", padding: "0.75rem" }}
      />

      <button
        onClick={analyzeResume}
        disabled={loading}
        style={{ padding: "0.6rem 1.2rem", cursor: "pointer" }}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {error && (
        <p style={{ color: "red", marginTop: "1rem" }}>{error}</p>
      )}

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h2>ATS Score: {result.ats_score}%</h2>
          <p><strong>Level:</strong> {result.level}</p>

          <hr />

          <h3>Matched Skills</h3>
          {result.matched_skills?.length > 0 ? (
            <ul>
              {result.matched_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          ) : (
            <p>No strong skill matches detected.</p>
          )}

          <h3>Missing Skills</h3>
          {result.missing_skills?.length > 0 ? (
            <ul>
              {result.missing_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          ) : (
            <p>No critical skills missing.</p>
          )}

          <hr />

          <h3>Suggestions</h3>
          <p>{result.ml_suggestions?.skills}</p>
          <p>{result.ml_suggestions?.experience}</p>
          <p>{result.ml_suggestions?.projects}</p>
        </div>
      )}
    </div>
  );
}

export default App;

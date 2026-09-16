import { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";
import "./App.css";

function App() {
  // -------------------------
  // Dashboard Data
  // -------------------------

  const [summary, setSummary] = useState(null);
  const [anomalies, setAnomalies] = useState(null);

  // Analytics data
  const [productRevenue, setProductRevenue] = useState([]);
  const [regionRevenue, setRegionRevenue] = useState([]);
  const [dailyRevenue, setDailyRevenue] = useState([]);

  // -------------------------
  // AI Chat
  // -------------------------

  const [question, setQuestion] = useState("");
  const [chatResponse, setChatResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  // -------------------------
  // Load Dashboard Data
  // -------------------------

  useEffect(() => {
    // Overall summary
    fetch("http://127.0.0.1:8000/analytics/summary")
      .then((response) => response.json())
      .then((data) => setSummary(data));

    // Anomaly detection
    fetch("http://127.0.0.1:8000/anomalies")
      .then((response) => response.json())
      .then((data) => setAnomalies(data));

    // Revenue by product
    fetch("http://127.0.0.1:8000/analytics/products")
      .then((response) => response.json())
      .then((data) => setProductRevenue(data));

    // Revenue by region
    fetch("http://127.0.0.1:8000/analytics/regions")
      .then((response) => response.json())
      .then((data) => setRegionRevenue(data));

    // Daily revenue
    fetch("http://127.0.0.1:8000/analytics/daily")
      .then((response) => response.json())
      .then((data) => setDailyRevenue(data));
  }, []);

  // -------------------------
  // Ask AI
  // -------------------------

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setChatResponse(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Something went wrong");
      }

      setChatResponse(data);
    } catch (error) {
      setChatResponse({
        explanation: `Error: ${error.message}`,
      });
    } finally {
      setLoading(false);
    }
  };

  // -------------------------
  // UI
  // -------------------------

  return (
    <div className="dashboard">

      {/* Header */}
      <header className="header">
        <div>
          <h1>DataPilot AI</h1>
          <p>
            Intelligent Data Engineering & Analytics Platform
          </p>
        </div>

        <div className="status">
          <span className="status-dot"></span>
          System Online
        </div>
      </header>

      {/* Statistics */}
      <section className="stats-grid">

        {/* Total Orders */}
        <div className="stat-card">
          <span>Total Orders</span>

          <h2>
            {summary?.total_orders ?? "—"}
          </h2>
        </div>

        {/* Total Revenue */}
        <div className="stat-card">
          <span>Total Revenue</span>

          <h2>
            {summary
              ? `₹${Number(
                  summary.total_revenue
                ).toLocaleString("en-IN")}`
              : "—"}
          </h2>
        </div>

        {/* Average Order Value */}
        <div className="stat-card">
          <span>Average Order Value</span>

          <h2>
            {summary
              ? `₹${Number(
                  summary.average_order_value
                ).toLocaleString("en-IN")}`
              : "—"}
          </h2>
        </div>

        {/* Anomalies */}
        <div className="stat-card anomaly-card">
          <span>Anomalies Detected</span>

          <h2>
            {anomalies?.count ?? "—"}
          </h2>
        </div>

      </section>

      {/* Main Content */}
      <section className="content-grid">

        {/* Anomaly Panel */}
        <div className="panel">

          <div className="panel-header">
            <h2>Anomaly Detection</h2>

            <span className="badge">
              AI Powered
            </span>
          </div>

          {anomalies?.count > 0 ? (
            <>
              {anomalies.anomalies.map((anomaly) => (
                <div
                  className="anomaly"
                  key={anomaly.order_id}
                >

                  <div>
                    <strong>
                      Order #{anomaly.order_id}
                    </strong>

                    <p>
                      {anomaly.product} × {anomaly.quantity}
                    </p>
                  </div>

                  <strong>
                    ₹
                    {Number(
                      anomaly.total_amount
                    ).toLocaleString("en-IN")}
                  </strong>

                </div>
              ))}

              <div className="explanation">

                <strong>
                  AI Analysis
                </strong>

                <p>
                  {anomalies.ai_explanation}
                </p>

              </div>
            </>
          ) : (
            <p>
              No anomalies detected.
            </p>
          )}

        </div>

        {/* Platform Status */}
        <div className="panel">

          <div className="panel-header">
            <h2>
              Platform Status
            </h2>
          </div>

          <div className="pipeline">

            <div>
              ✓ Data Ingestion
            </div>

            <div>
              ✓ Data Validation
            </div>

            <div>
              ✓ PostgreSQL
            </div>

            <div>
              ✓ Analytics Engine
            </div>

            <div>
              ✓ AI Anomaly Detection
            </div>

            <div>
              ✓ Gemini AI
            </div>

          </div>

        </div>

      </section>

      {/* -------------------------
          Analytics Data
      ------------------------- */}

      <section className="content-grid">

        {/* Product Revenue Chart */}
        <div className="panel">

          <div className="panel-header">
            <h2>Revenue by Product</h2>
            <span className="badge">Analytics</span>
          </div>

          <div className="chart-container">
            <ResponsiveContainer width="100%" height={320}>
              <BarChart
                data={productRevenue}
                margin={{
                  top: 10,
                  right: 20,
                  left: 10,
                  bottom: 10,
                }}
              >
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="product" />

                <YAxis
                  tickFormatter={(value) =>
                    `₹${(value / 1000).toFixed(0)}K`
                  }
                />

                <Tooltip
                  formatter={(value) =>
                    `₹${Number(value).toLocaleString("en-IN")}`
                  }
                />

                <Bar
                  dataKey="revenue"
                  name="Revenue"
                  radius={[6, 6, 0, 0]}
                />
              </BarChart>
            </ResponsiveContainer>
          </div>

        </div>

        {/* Region Revenue */}
        {/* Region Revenue Chart */}
        <div className="panel">

          <div className="panel-header">
            <h2>Revenue by Region</h2>
            <span className="badge">Analytics</span>
          </div>

          <div className="chart-container">
            <ResponsiveContainer width="100%" height={320}>
              <BarChart
                data={regionRevenue}
                margin={{
                  top: 10,
                  right: 20,
                  left: 10,
                  bottom: 10,
                }}
              >

                <CartesianGrid strokeDasharray="3 3" />

                <XAxis
                  dataKey="region"
                />

                <YAxis
                  tickFormatter={(value) =>
                    `₹${(value / 1000).toFixed(0)}K`
                  }
                />

                <Tooltip
                  formatter={(value) =>
                    `₹${Number(value).toLocaleString("en-IN")}`
                  }
                />

                <Bar
                  dataKey="revenue"
                  name="Revenue"
                  radius={[6, 6, 0, 0]}
                />

              </BarChart>
            </ResponsiveContainer>
          </div>

        </div>

      </section>

      {/* Daily Revenue */}
 {/* Daily Revenue Chart */}
      <section className="panel">

        <div className="panel-header">
          <h2>Daily Revenue</h2>
          <span className="badge">Trend</span>
        </div>

        <div className="chart-container">
          <ResponsiveContainer width="100%" height={320}>
            <LineChart
              data={dailyRevenue}
              margin={{
                top: 10,
                right: 20,
                left: 10,
                bottom: 10,
              }}
            >

              <CartesianGrid strokeDasharray="3 3" />

              <XAxis
                dataKey="order_date"
                tickFormatter={(value) =>
                  new Date(value).toLocaleDateString("en-IN", {
                    day: "2-digit",
                    month: "short",
                  })
                }
              />

              <YAxis
                tickFormatter={(value) =>
                  `₹${(value / 1000).toFixed(0)}K`
                }
              />

              <Tooltip
                labelFormatter={(value) =>
                  new Date(value).toLocaleDateString("en-IN", {
                    day: "2-digit",
                    month: "short",
                    year: "numeric",
                  })
                }
                formatter={(value) =>
                  `₹${Number(value).toLocaleString("en-IN")}`
                }
              />

              <Line
                type="monotone"
                dataKey="revenue"
                name="Revenue"
                strokeWidth={3}
                dot={{ r: 4 }}
                activeDot={{ r: 7 }}
              />

            </LineChart>
          </ResponsiveContainer>
        </div>

      </section>

      {/* -------------------------
          AI Chat
      ------------------------- */}

      <section className="chat-panel">

        <div className="panel-header">

          <h2>
            Ask DataPilot AI
          </h2>

          <span className="badge">
            Gemini AI
          </span>

        </div>

        <div className="chat-input">

          <input
            type="text"
            placeholder="Ask a question about your data..."
            value={question}
            onChange={(e) =>
              setQuestion(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                askQuestion();
              }
            }}
          />

          <button
            onClick={askQuestion}
            disabled={loading}
          >
            {loading
              ? "Analyzing..."
              : "Ask AI"}
          </button>

        </div>

        {chatResponse && (
          <div className="chat-response">

            <p>
              <strong>
                Question:
              </strong>{" "}
              {chatResponse.question}
            </p>

            <p>
              <strong>
                AI Answer:
              </strong>
            </p>

            <p>
              {chatResponse.explanation}
            </p>

            {chatResponse.sql && (
              <>
                <p>
                  <strong>
                    Generated SQL:
                  </strong>
                </p>

                <pre>
                  {chatResponse.sql}
                </pre>
              </>
            )}

          </div>
        )}

      </section>

    </div>
  );
}

export default App;
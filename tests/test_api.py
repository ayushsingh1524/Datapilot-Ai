from fastapi.testclient import TestClient

from api.main import app
import api.routes.anomalies as anomalies_route


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "DataPilot AI API is running"


def test_summary():
    response = client.get("/analytics/summary")

    assert response.status_code == 200

    data = response.json()

    assert "total_orders" in data
    assert "total_revenue" in data
    assert "average_order_value" in data


def test_products():
    response = client.get("/analytics/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_regions():
    response = client.get("/analytics/regions")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_daily_revenue():
    response = client.get("/analytics/daily")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
def test_anomalies(monkeypatch):

    monkeypatch.setattr(
        anomalies_route,
        "explain_anomalies",
        lambda anomalies: "Test anomaly explanation"
    )

    response = client.get("/anomalies")

    assert response.status_code == 200

    data = response.json()

    assert "count" in data
    assert "anomalies" in data
    assert "ai_explanation" in data
    assert isinstance(data["anomalies"], list)

def test_chat_rejects_empty_question():
    response = client.post(
        "/chat",
        json={
            "question": "",
            "session_id": "test-session",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Question cannot be empty."
def test_chat_rejects_long_question():
    response = client.post(
        "/chat",
        json={
            "question": "a" * 501,
            "session_id": "test-session",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Question is too long. Please keep it under 500 characters."
    )
def test_chat_rejects_empty_session_id():
    response = client.post(
        "/chat",
        json={
            "question": "What is the total revenue?",
            "session_id": "",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == (
        "Session ID cannot be empty."
    )
def test_sql_validator_blocks_dangerous_query():
    from src.ai.sql_validator import validate_sql

    dangerous_queries = [
        "DELETE FROM orders",
        "DROP TABLE orders",
        "UPDATE orders SET quantity = 100",
        "INSERT INTO orders VALUES (1)",
    ]

    for query in dangerous_queries:
        try:
            validate_sql(query)
            assert False, f"Dangerous SQL was allowed: {query}"
        except ValueError:
            pass

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.ai.sql_generator import generate_sql
from src.ai.sql_validator import validate_sql
from src.ai.explainer import explain_results
from src.ai.retriever import retrieve_relevant_schema
from src.database.queries import execute_query


router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    session_id: str = "default"


conversation_history = {}


@router.post("/chat")
def chat(request: ChatRequest):
    try:
        # Validate question
        if not request.question.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty."
            )

        if len(request.question) > 500:
            raise HTTPException(
                status_code=400,
                detail="Question is too long. Please keep it under 500 characters."
            )

        if not request.session_id.strip():
            raise HTTPException(
                status_code=400,
                detail="Session ID cannot be empty."
            )

        # 1. Get previous conversation
        history = conversation_history.get(
            request.session_id,
            []
        )

        # 2. Retrieve relevant knowledge using RAG
        relevant_schema = retrieve_relevant_schema(
            request.question
        )

        schema = "\n\n".join(relevant_schema)

        # 3. Add conversation context
        conversation_context = ""

        if history:
            conversation_context = "\nPrevious conversation:\n"

            for item in history[-5:]:
                conversation_context += (
                    f"User: {item['question']}\n"
                    f"Assistant: {item['answer']}\n"
                )

        # 4. Generate SQL
        sql = generate_sql(
            request.question,
            schema + conversation_context
        )

        # 5. Validate SQL
        sql = validate_sql(sql)

        # 6. Execute SQL
        results = execute_query(sql)

        # 7. Generate explanation
        try:
            explanation = explain_results(
                request.question,
                results
            )
        except Exception:
            explanation = (
                "The query was executed successfully, "
                "but the AI explanation is temporarily unavailable."
            )

        # 8. Save conversation
        conversation_history.setdefault(
            request.session_id,
            []
        ).append(
            {
                "question": request.question,
                "answer": explanation,
            }
        )

        # Keep only the latest 10 messages per session
        conversation_history[request.session_id] = (
            conversation_history[request.session_id][-10:]
        )

        # 9. Return response
        return {
            "question": request.question,
            "sql": sql,
            "results": results,
            "explanation": explanation,
            "rag_used": True,
            "retrieved_contexts": len(relevant_schema),
            "session_id": request.session_id,
        }

    except HTTPException:
        raise

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        print("CHAT ERROR:", error)

        return {
            "question": request.question,
            "sql": None,
            "results": [],
            "explanation": (
                "The AI analytics request could not be completed. "
                "Please try again later."
            ),
            "session_id": request.session_id,
        }
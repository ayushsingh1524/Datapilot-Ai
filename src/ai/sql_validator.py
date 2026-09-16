import re


FORBIDDEN_KEYWORDS = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "GRANT",
    "REVOKE",
}


def validate_sql(sql: str) -> str:
    """
    Validate AI-generated SQL before executing it.

    Only SELECT queries are allowed.
    """

    if not sql or not sql.strip():
        raise ValueError("SQL query cannot be empty.")

    # Remove markdown code fences if Gemini returns them
    sql = sql.replace("```sql", "").replace("```", "").strip()

    # Remove trailing semicolon
    cleaned_sql = sql.rstrip(";").strip()

    # Only SELECT statements are allowed
    if not re.match(r"^(SELECT|WITH)\b", cleaned_sql, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed.")

    # Block dangerous SQL keywords
    sql_upper = cleaned_sql.upper()

    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", sql_upper):
            raise ValueError(
                f"Unsafe SQL detected: {keyword}"
            )

    # Prevent multiple SQL statements
    if ";" in cleaned_sql:
        raise ValueError("Multiple SQL statements are not allowed.")

    return cleaned_sql
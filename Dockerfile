FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv

RUN uv sync --frozen --no-dev

RUN uv pip install --python /app/.venv/bin/python \
    torch \
    --index-url https://download.pytorch.org/whl/cpu

COPY . .

EXPOSE 8000

CMD [".venv/bin/uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
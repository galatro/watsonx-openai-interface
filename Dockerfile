FROM python:3.11-slim AS builder

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt && \
    pip install --no-cache-dir pyarrow==18.1.0


FROM builder AS production-image
COPY main.py /app/ 
COPY utils/ /app/utils/
COPY app/ /app/app/

EXPOSE 8080
ENV PYTHONUNBUFFERED=1
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s CMD curl -f http://localhost:8080/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "8"]

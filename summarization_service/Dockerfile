# FROM python:3.10.8-slim

# WORKDIR /summarization_service

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# ENV FLASK_APP=summarization_service.py

# EXPOSE 5001

# CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]


FROM python:3.10.8-slim

WORKDIR /summarization_service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/summarization_service

EXPOSE 5001

CMD ["python", "summarization_service.py"]

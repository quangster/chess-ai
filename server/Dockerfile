FROM python:3.12.3
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY data/ ./data
COPY engine/ ./engine
COPY main.py ./
COPY tests.py ./ 

EXPOSE 5000

CMD ["python", "main.py"]
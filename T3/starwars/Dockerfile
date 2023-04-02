FROM python:3.11.2-alpine

WORKDIR /app

ENV PORT=3000

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 3000

COPY app.py .
ADD bl ./bl

CMD ["python","/app/app.py"]

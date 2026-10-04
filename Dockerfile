FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip --disable-pip-version-check
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt
RUN python -m nltk.downloader punkt punkt_tab stopwords
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
FROM python:3.14.0a3-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /backend
EXPOSE 8000

COPY . /backend/
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "django.wsgi"]

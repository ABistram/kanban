FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python3 ./kanban/manage.py makemigrations
RUN python3 ./kanban/manage.py migrate
CMD ["python3", "./kanban/manage.py", "runserver", "0.0.0.0:8000"]
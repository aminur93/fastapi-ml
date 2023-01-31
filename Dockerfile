FROM python:3.10

WORKDIR /code

COPY ./requirements.txt ./

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]



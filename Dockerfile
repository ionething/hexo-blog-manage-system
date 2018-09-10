FROM python:3.6-alpine3.8

WORKDIR /usr/src/app

COPY release/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -r ./requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]
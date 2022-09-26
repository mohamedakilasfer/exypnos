FROM python:3.10.4

WORKDIR /final

COPY ./requirements.txt /final/requirements.txt

RUN pip install  -r /final/requirements.txt

COPY ./ /final

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]
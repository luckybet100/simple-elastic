FROM python:3.9

WORKDIR /

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV extra = ""

CMD sleep 30 && uvicorn node.main:app --host 0.0.0.0 $extra

FROM python:3.12

RUN apt-get update && apt-get install -y locate jq
RUN pip install --upgrade pip
RUN pip install --no-cache mlflow==2.9.0

RUN sed -i 's/.get("mlflow.app", \[\])/.select(group="mlflow.app")/g' /usr/local/lib/python3.12/site-packages/mlflow/cli.py

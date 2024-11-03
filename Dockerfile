FROM public.ecr.aws/docker/library/python:3.12.1-slim
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter
WORKDIR /var/task
COPY requirements.txt ./
COPY project/ ./project/
RUN python -m pip install -r requirements.txt
ENV PYTHONPATH /var/task
CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:8080", "project.__init__:create_app()"]

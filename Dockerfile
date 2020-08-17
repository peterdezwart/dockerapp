FROM python:3.7
WORKDIR /usr/src/app
ENV FLASK_APP package1/module1.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
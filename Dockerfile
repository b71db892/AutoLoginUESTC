FROM python:3.9-slim

# config app
ENV APP_PATH="/app" 

RUN apt-get update && \
  apt-get -y install wget inetutils-ping && \
  apt-get -y autoremove && \
  apt-get clean

RUN pip install requests
RUN mkdir -p $APP_PATH 

COPY . $APP_PATH/

RUN cd $APP_PATH && cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
  echo "Asia/Shanghai" > /etc/timezone

WORKDIR ${APP_PATH}

# RUN main.py
CMD ["/usr/local/bin/python", "-u", "/app/always_online_docker.py"]
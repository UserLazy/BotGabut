# Using Python Slim-Buster
FROM biansepang/weebproject:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/UserLazy/BotGabut /home/weebproject/ \
    && chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/weebproject/

# Setup Working Directory
WORKDIR /home/weebproject/
COPY . /home/weebproject/bin/
RUN pip3 install -U -r requirements.txt

# Finalization
CMD ["python3","-m","userbot"]

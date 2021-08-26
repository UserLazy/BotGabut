# Using Python Slim-Buster
FROM userlazy/botgabut:buster

# Clone repo and prepare working directory
RUN git clone -b master https://github.com/UserLazy/BotGabut /home/botgabut/ \
    && chmod 777 /home/botgabut \
    && mkdir /home/botgabut/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/botgabut/

# Setup Working Directory
WORKDIR /home/botgabut/

# Finalization
CMD ["python3","-m","userbot"]

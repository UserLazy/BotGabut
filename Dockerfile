# Using Python Slim-Buster
FROM biansepang/weebproject:buster


RUN git clone https://github.com/UserLazy/BotGabut.git /home/weebproject/ \
    && pip3 install --no-cache-dir -r home/weebproject/requirements.txt \
    && chmod 777 /home/weebproject \
    && mkdir /home/weebproject/bin/


# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/weebproject/

# changing workdir
WORKDIR /home/weebproject/

# Finalization
CMD ["python3","-m","userbot"]

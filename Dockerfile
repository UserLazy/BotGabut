# Using Python Slim-Buster
FROM theteamultroid/ultroid:main

ENV TZ=Asia/Jakarta

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone https://github.com/UserLazy/BotGabut.git /root/TeamUltroid/ \
    && pip3 install --no-cache-dir -r root/TeamUltroid/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av


# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/weebproject/

# changing workdir
WORKDIR /root/TeamUltroid/

# Finalization
CMD ["python3","-m","userbot"]

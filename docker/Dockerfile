FROM fnndsc/ubuntu-python3
RUN apt-get update \
  && apt-get install -y ffmpeg
RUN pip3 install ffmpeg-python
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
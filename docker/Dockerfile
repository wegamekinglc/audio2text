FROM fnndsc/ubuntu-python3
RUN apt-get update \
  && apt-get install -y ffmpeg
RUN pip3 install ffmpeg-python
RUN pip3 install flask
RUN pip3 install flask_restful
RUN pip3 install gunicorn
COPY ./entrypoint.sh /app/entrypoint.sh
COPY ./mp3 /app/mp3
COPY ./audio_serve /app/audio_serve
RUN chmod +x /app/entrypoint.sh
WORKDIR /app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD []
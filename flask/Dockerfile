FROM python:latest
EXPOSE 5000
RUN useradd -m flaskuser

USER flaskuser 
RUN mkdir /home/flaskuser/app

ADD . /home/flaskuser/app
WORKDIR /home/flaskuser/app

RUN pip install --user --no-warn-script-location -r requirements.txt
#RUN ls -la /home/flaskuser/.local/bin
ENTRYPOINT ["/home/flaskuser/app/entrypoint.sh"]
CMD ["flask", "run", "--host=0.0.0.0"]

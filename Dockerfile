# light image 
FROM python:3.8.2-alpine

# wheel filename
ENV WHEELNAME="playersMindset-0.0.1-py3-none-any.whl"

# workplace
WORKDIR="/mind"

# copy wheel to container path
COPY dist/playersMindset-0.0.1-py3-none-any.whl $WORKDIR

# install wheel
RUN pip install $WHEELNAME

# test program init
CMD ["python", "playersMindset.cmd", "-h"]

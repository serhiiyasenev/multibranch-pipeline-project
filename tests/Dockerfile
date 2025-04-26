FROM ubuntu:16.04

WORKDIR /app/tests
COPY . /app/tests

RUN apt-get update
RUN apt-get install -y python python-pip wget xvfb libssl-dev
RUN pip install -r requirements.txt

# Install and uninstall latest firefox to get all needed dependencies
RUN apt-get -y install firefox && apt-get -y purge firefox

# Install Firefox 47.01
RUN wget http://ftp.mozilla.org/pub/firefox/releases/47.0.1/linux-x86_64/en-US/firefox-47.0.1.tar.bz2 && \
        tar -xjf firefox-47.0.1.tar.bz2 && \
        mv firefox /opt/firefox47 && \
    ln -s /opt/firefox47/firefox /usr/bin/firefox && \
    rm firefox-47.0.1.tar.bz2

CMD ["nosetests", "-v", "test.py"]

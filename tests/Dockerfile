FROM python:3.13-slim

WORKDIR /app/tests
COPY . /app/tests

RUN apt-get update && apt-get install -y \
    wget \
    xvfb \
    libssl-dev \
    unzip \
    gnupg \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | \
    gpg --dearmor -o /usr/share/keyrings/google-chrome.gpg

RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] \
    http://dl.google.com/linux/chrome/deb/ stable main" > \
    /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && apt-get install -y google-chrome-stable

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["pytest", "-v", "test.py"]

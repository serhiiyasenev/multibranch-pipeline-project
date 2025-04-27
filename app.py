from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_url = os.getenv("REDIS_URL", "redis://redis:6379/0")
redis = Redis.from_url(redis_url)

@app.route("/")
def hello():
    visits = redis.incr('counter')
    html = "<h3 id='header'>Hello World!</h3>" \
           "<b>Visits:</b>" \
           "<b id='visits'>{visits}</b>" \
           "<br/>"
    return html.format(visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

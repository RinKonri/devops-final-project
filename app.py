from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)  # подключаемся к контейнеру Redis

@app.route('/')
def hello():
    count = r.incr('hits')  # увеличиваем счётчик
    return f"Привет! Страницу открыли {count} раз(а)."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
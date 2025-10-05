from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, World! It works!</h1>"

# 다른 모든 라우트와 데이터베이스 관련 코드는 일단 모두 제거합니다.

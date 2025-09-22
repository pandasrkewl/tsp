from flask import Flask
from sqlalchemy import create_engine, text
app = Flask(__name__)


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

@app.route('/')
def hello_world():
    return 'Hello, from Flask!'

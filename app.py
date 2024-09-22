from flask import Flask
from repository import GitHubEvent,insert_to_db

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/health', methods=["GET"])
def health():
    return "<p>OK!</p>"


@app.route('/receiver', methods=["POST"])
def receiver(githubevent : GitHubEvent):
    insert_to_db(githubevent)

app.run()

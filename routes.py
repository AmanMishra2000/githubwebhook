from flask import Blueprint, json, request
from repository import insert_to_db,GitHubEvent

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver(githubevent : GitHubEvent):
    insert_to_db(githubevent)

@webhook.route('/health', methods=["GET"])
def ping():
    return "ok"


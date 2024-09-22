import pymongo
from pydantic import BaseModel
import json

from extensions import db,collection,client
class GitHubEvent(BaseModel):
    author : str
    request_id : str
    action : str
    from_branch : str
    to_branch : str
    timestamp : datetime

def insert_to_db(githubevent : GitHubEvent):
    data = {
        'author': githubevent.author,
        'request_id': githubevent.request_id,
        'action': githubevent.action,
        'from_branch': githubevent.from_branch,
        'to_branch': githubevent.to_branch,
        'timestamp': githubevent.timestamp,
    }
    collection.insert_one(data)

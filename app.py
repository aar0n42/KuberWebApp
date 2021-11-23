from flask import Flask
import pymongo
import os
import socket
from pymongo import MongoClient

client = MongoClient('mongodb://name-of-your-mongodb-service:27017')

app = Flask(__name__)

@app.route("/")
def hello():
    myHostName = socket.gethostname()
    db = client.company
    people = db.people
    people_data = {
        'name' : 'Jean',
        'lastname' : 'Herrera'
    }

    result = people.insert_one(people_data)

    inserted_id = result.inserted_id
    
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Lab #4:</b> Kubernetes <br/>" \
           "<b>Data BS inserted ID:</b> {inserted_id} "
           
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), inserted_id=inserted_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

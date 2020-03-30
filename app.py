from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Ad
import json
import redis

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/ads'
}

client = redis.Redis(host='localhost', port=6379)

initialize_db(app)

@app.route('/')
def hello():
    ads = Ad.objects().to_json()
    return Response(ads, mimetype="application/json", status=200)

@app.route('/ad', methods=['POST'])
def add_ad():
    body = request.get_json()
    ad = Ad(**body).save()
    id = ad.id
    ad_json = ad.to_json()
    client.set(str(id), str(ad_json))
    return Response(ad_json, mimetype="application/json", status=200)

@app.route('/ad/<id>')
def get_ad(id):
    cache_dict = client.get(str(id))
    result = {'откуда достали': 'из базы данных'}
    if cache_dict:
        result['откуда достали'] = 'из кэша'
        result.update(json.loads(cache_dict.decode("utf-8")))
    else:
        result.update(json.loads(Ad.objects.get(id=id).to_json()))
    return Response(json.dumps(result), mimetype="application/json", status=200)

@app.route('/addtag/<id>', methods=['POST'])
def addtag(id):
    ad = Ad.objects.get(id=id)
    ad.tags = json.loads(ad.to_json())['tags'] + request.get_json()['tags']
    ad.save()
    ad_json = ad.to_json()
    client.set(str(id), str(ad_json))
    return Response(ad_json, mimetype="application/json", status=200)

@app.route('/addcomm/<id>', methods=['POST'])
def addcomm(id):
    ad = Ad.objects.get(id=id)
    ad.comments = json.loads(ad.to_json())['comments'] + request.get_json()['comments']
    ad_json = ad.to_json()
    client.set(str(id), str(ad_json))
    return Response(ad_json, mimetype="application/json", status=200)

@app.route('/stat/<id>')
def stat(id):
    ad = json.loads(Ad.objects.get(id=id).to_json())
    stat = {
        'tag count': len(ad['tags']),
        'comment count': len(ad['comments'])
    }
    return Response(json.dumps(stat), mimetype="application/json", status=200)

@app.route('/clear')
def clear():
    client.flushdb()
    return Response('Кэш очищен', status=200)

if __name__ == "__main__":
    app.run()
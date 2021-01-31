import json
import uuid

from flask import Flask, jsonify, request

app = Flask(__name__)


def rnd_id():
    return str(uuid.uuid4())[0:12].replace('-', '').upper()


def load_json_file(path):
    with open(path, 'r') as f:
        response_payload = json.loads(f.read())
    return response_payload


def save_json_file(req_data, path):
    with open(path, 'w') as j:
        json.dump(req_data, j)


@app.route('/lists')
def get_lists():
    db = load_json_file('./db.json')
    return jsonify(db), 200


@app.route('/lists', methods=['POST'])
def create_list():
    req_payload = request.get_json()
    if sorted([i for i in req_payload.keys()]) == sorted(['listName', "listType"]):
        new_list_payload = load_json_file('./list/list_payload.json')
        new_list_payload['listID'] = rnd_id()
        new_list_payload['listName'] = req_payload['listName']
        new_list_payload['listType'] = req_payload['listType']
        db = load_json_file('./db.json')
        db['lists'].append(new_list_payload)
        save_json_file(db, './db.json')
        return jsonify({"listID": new_list_payload['listID']}), 200
    else:
        return "bad request, mandatory field is missing in request payload", 400


@app.route('/lists/<id_>')
def get_list(id_):
    db = load_json_file('./db.json')
    list_payload = [i for i in db['lists'] if i['listID'] == id_]
    if len(list_payload) > 0:
        return jsonify(list_payload[0]), 200
    else:
        return jsonify(sucess=False), 404


@app.route('/lists/<id_>', methods=['PUT'])
def update_list(id_):
    req_payload = request.get_json()
    if sorted([i for i in req_payload.keys()]) == sorted(['listName', "listType"]):
        db = load_json_file('./db.json')
        list_payload = [i for i in db['lists'] if i['listID'] == id_]
        if len(list_payload) > 0:
            list_payload[0]['listName'] = req_payload['listName']
            list_payload[0]['listType'] = req_payload['listType']
            for n, i in enumerate(db['lists']):
                if i['listID'] == id_:
                    db['lists'][n] = list_payload[0]
            save_json_file(db, './db.json')
            return jsonify(sucess=True), 200
        else:
            return jsonify(sucess=False), 404

    else:
        return "bad request, mandatory field is missing in request payload", 400


@app.route('/lists/<id_>', methods=['DELETE'])
def delete_list(id_):
    db = load_json_file('./db.json')
    list_payload = [i for i in db['lists'] if i['listID'] == id_]
    if len(list_payload) > 0:
        for n, i in enumerate(db['lists']):
            if i['listID'] == id_:
                del db['lists'][n]
                save_json_file(db, './db.json')
                return jsonify(sucess=True), 200
    else:
        return jsonify(sucess=False), 404


@app.route('/lists/<id_>/items', methods=['PATCH'])
def update_list_items(id_):
    item_payload = request.get_json()
    if 'itemName' in [i for i in item_payload]:
        db = load_json_file('./db.json')
        list_payload = [i for i in db['lists'] if i['listID'] == id_]
        if len(list_payload) > 0:
            for n, i in enumerate(db['lists']):
                if i['listID'] == id_:
                    db['lists'][n]['listItems'].append(item_payload)
                    save_json_file(db, './db.json')
                    return jsonify(sucess=True), 200

        else:
            return "bad request, mandatory field: itemName, is missing in request payload", 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

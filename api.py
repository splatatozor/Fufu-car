import json
from flask import Flask, request

app = Flask(__name__)

file_to_save = "direction.json"


def update_json(right, left, status="normal"):
    with open(file_to_save) as json_file:
        data = json.load(json_file)
        if status == "autonomous":
            data["status"] = status
            data["vitesse"]["right"] = ""
            data["vitesse"]["left"] = ""
        data["status"] = status
        data["vitesse"]["right"] = right
        data["vitesse"]["left"] = left
        return data


@app.route("/health")
def health():
    return "Ok"


@app.route("/action", methods=["POST"])
def set_direction():

    if request.method == "POST":
        right = request.args.get("right")
        left = request.args.get("left")
        data = update_json(right, left, "normal")
        with open(file_to_save, 'w') as json_file:
            json.dump(data, json_file)
            json_file.close()
            return "Ok", 200

    else:
        return "It's a POST Route", 405


@app.route("/autonomous", methods=["POST"])
def set_autonomous_mode():
    data = update_json("", "", "autonomous")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/stop", methods=["POST"])
def shutdown():
    with open(file_to_save, 'w') as json_file:
        json.dump({"vitesse": {"right": "", "left": ""}, "status": "normal"}, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/direction", methods=["GET"])
def get_direction():
    with open(file_to_save) as json_file:
        data = json.load(json_file)
        return json.dumps(data), 200


shutdown()


if __name__ == '__main__':
    app.run(debug=True)


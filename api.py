import json
from flask import Flask, request

app = Flask(__name__)

file_to_save = "direction.json"
right = 0
left = 0


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


def convert_x_and_y_to_speed(x, y):
    global right
    global left
    if y > 0:
        if x > 0:  # On tourne a droite en marche avant
            left = y
            right = 100 - x
        else:  # On tourne a gauche en marche avant
            right = 100
            left = 100 + x
    else:
        if x < 0:  # On tourne a droite en marche arriere
            right = -100 + x
            left = -100
        else:  # On tourne a gauche en marche arriere
            left = -100 - x
            right = -100


@app.route("/health")
def health():
    return "Ok"


@app.route("/action", methods=["POST"])
def set_direction():

    if request.method == "POST":
        x = request.args.get("x")
        y = request.args.get("y")
        convert_x_and_y_to_speed(x, y)
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


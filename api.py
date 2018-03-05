import json
from flask import Flask

app = Flask(__name__)

file_to_save = "direction.json"


def update_json(value, axe, status="normal"):
    with open(file_to_save) as json_file:
        data = json.load(json_file)
        if axe == "y":
            data["status"] = status
            data["direction"]["y"] = value
        if axe == "x":
            data["status"] = status
            data["direction"]["x"] = value
        if status == "autonomous":
            data["status"] = status
            data["direction"]["x"] = ""
            data["direction"]["y"] = ""
        return data


@app.route("/health")
def health():
    return "Ok"


@app.route("/forward")
def set_direction_to_forward():
    data = update_json("forward", "y", "normal")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/reverse")
def set_direction_to_reverse():
    data = update_json("reverse", "y", "normal")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/left")
def set_direction_to_left():
    data = update_json("left", "x", "normal")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/right")
def set_direction_to_right():
    data = update_json("right", "x", "normal")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        return "Ok", 200


@app.route("/autonomous")
def set_autonomous_mode():
    data = update_json("", "", "autonomous")
    with open(file_to_save, 'w') as json_file:
        json.dump(data, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/stop")
def shutdown():
    with open(file_to_save, 'w') as json_file:
        json.dump({"direction": {"x": "", "y": ""}, "status": "normal"}, json_file)
        json_file.close()
        return "Ok", 200


@app.route("/direction")
def get_direction():
    with open(file_to_save) as json_file:
        data = json.load(json_file)
        return json.dumps(data), 200


shutdown()


if __name__ == '__main__':
    app.run(debug=True)


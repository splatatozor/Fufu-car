import json
from flask import Flask

app = Flask(__name__)

file_to_save = "direction.json"

with open(file_to_save, 'w') as json_file:
    json.dump('stop', json_file, ensure_ascii=False)


@app.route("/health")
def health():
    return "Ok"


@app.route("/forward")
def set_direction_to_forward():
    with open(file_to_save, 'w') as json_file:
        json.dump('forward', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/reverse")
def set_direction_to_reverse():
    with open(file_to_save, 'w') as json_file:
        json.dump('reverse', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/left")
def set_direction_to_left():
    with open(file_to_save, 'w') as json_file:
        json.dump('left', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/right")
def set_direction_to_right():
    with open(file_to_save, 'w') as json_file:
        json.dump('right', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/autonomous")
def set_autonomous_mode():
    with open(file_to_save, 'w') as json_file:
        json.dump('autonomous', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/stop")
def shutdown():
    with open(file_to_save, 'w') as json_file:
        json.dump('stop', json_file, ensure_ascii=False)
    return "Ok", 200


@app.route("/direction")
def get_direction():
    with open(file_to_save) as json_file:
        data = json.load(json_file)
    return data, 200


if __name__ == '__main__':
    app.run(debug=True)


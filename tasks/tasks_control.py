from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []


@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    if 'title' not in data or data.get('title') == "":
        return jsonify({'error': 'Title is required'}), 400

    new_task = {
        'id': len(tasks) + 1,
        'title': data['title']
    }
    tasks.append(new_task)

    return jsonify({'message': 'Task added successfully'}), 201


@app.route('/tasks', methods=['GET'])
def list_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)

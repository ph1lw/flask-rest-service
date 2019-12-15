#  Author: (2019) Philipp Wurm <phiwu@gmx.at>
#
#  This file is part of flask-rest-service
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

from flask import Flask, request, jsonify
import random
import json

from com.appstruction.example.random.random_range import RandomRange

app = Flask(__name__)


@app.route('/health/ready', methods=['GET'])
def ready():
    return jsonify(status='UP', checks=[{'name': 'Flask Rest Service is running.', 'status': 'UP'}])


@app.route('/rest/v1/hello', methods=['GET'])
def hello():
    return 'Hello World!'


@app.route('/rest/v1/hello/<string:name>', methods=['GET'])
def hello_user(name):
    return 'Hello ' + name


@app.route('/rest/v1/random', methods=['POST'])
def random_number():
    rrand = RandomRange(**json.loads(json.dumps(request.json)))
    return f'New random value [{rrand.to_range}-{rrand.to_range}]: {random.randint(rrand.from_range, rrand.to_range)}'


if __name__ == '__main__':
    app.run()

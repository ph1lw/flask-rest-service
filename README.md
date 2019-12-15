# flask-rest-service
Simple rest service with Flask by Philipp Wurm <phiwu@gmx.at>

This service provides a simple rest api with 3 methods:
* GET hello
    * /rest/v1/hello
        * returns "Hello World".
* GET helloUser
    * /rest/v1/hello/{name}
        * returns "Hello <UserName>" depending on the username.
* POST randomNumber
    * /rest/v1/random
    * expects a random range as json in body, e.g. `{"from": 0, "to": 100}`.
        * returns a random value between from and to.
* GET healthCheck
    * /health/ready
        * returns a ready message
        
        
### Prerequisites
* Python 3.7+
* PIP3
* Virtualenv


### Run example
To start the example in development mode (Linux/Fedora 30):

1. open a terminal and install virtualenv `pip3 install virtualenv --user`
2. in project root create a virtual environment `virtualenv --python=python3 target` (choose another name instead of *target* if you wish).
3. enter *target* directory `cd target`
4. call `source bin/activate` (The source command can be used to load any functions file into the current shell script or a command prompt.)
5. install flask inside this virtual environment `pip install flask` (**not** pip3 just pip)
6. return to root directory with `cd ..`
6. run the application `python3 app.py`



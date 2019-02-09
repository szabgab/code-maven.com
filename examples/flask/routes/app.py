from flask import Flask
demoapp = Flask(__name__)

@demoapp.route("/")
def main():
    return "Main page"

@demoapp.route("/some/path")
def some_path():
    return "A fixed path"

@demoapp.route("/user/<name>")
def user_name(name):
    return "The name is {}".format(name)


@demoapp.route("/title/<string:name>")
def title(name):
    return "The title is {}".format(name)

@demoapp.route("/id/<int:uid>")
def user_id(uid):
    return "The uid is {}".format(uid)

@demoapp.route("/coord-x/<float:x>")
def coord_x(x):
    return "The x coordinate is {}".format(x)

@demoapp.route("/place/<path:location>")
def place(location):
    return "The location is {}".format(location)

@demoapp.route("/coord/<float:x>/<float:y>")
def coord(x, y):
    return "The coordinate is ({}, {})".format(x, y)

@demoapp.route("/street/<name>/zip/<code>")
def machine(name, code):
    return "The input is {} and {}".format(name, code)


import converters
demoapp.url_map.converters['ipv4'] = converters.IPv4Converter

@demoapp.route('/ip/<ipv4:address>')
def ip_address(address):
    return "The IP is {}".format(address)


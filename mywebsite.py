import flask
myapp = flask.Flask("MyAPP")
@myapp.route("/")
def my_home_page():
    return "Hello"
if __name__ == "__main__":
    myapp.run(host='0.0.0.0',port=1234)
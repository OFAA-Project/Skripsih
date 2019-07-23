from flask import Flask, render_template
import docker

app = Flask(__name__)
client = docker.from_env()


@app.route('/')
@app.route('/container')
def index():
    client = docker.from_env()
    a = client.containers.list()
    print (a)
    return render_template (container.html)
@app.route('/hello/<user>')
def hallo_name(user):
    return render_template('hello.html', name = user)

if __name__ == "__main__":
    app.run(debug=True)
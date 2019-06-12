from flask import Flask
app = Flask(__name__)
print(__name__)
@app.route('/')
def helloworld():
    return 'flask first project'
app.run(port=5000)

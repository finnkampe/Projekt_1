from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, DevOps World! Dies ist Version 1.'

if __name__ == '__main__':
    # host='0.0.0.0' ist wichtig, damit der Server später 
    # auch im Docker Container erreichbar ist.
    app.run(host='0.0.0.0', port=5000)
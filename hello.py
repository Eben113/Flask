from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
#@app.route('/home')
#def door():
#   return('welcome')
if __name__ == '__main__' :
    app.run(port = 5000, debug = True)
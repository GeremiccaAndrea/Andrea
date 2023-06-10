from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Home')
def GotoMenu():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
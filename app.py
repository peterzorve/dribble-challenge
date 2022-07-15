from flask import Flask, render_template


#create instance
app = Flask(__name__)

@app.route("/") #decorator
def index():
    return render_template('index.html')
    

@app.route("/shots") #decorator
def about():
    return render_template('inspiration.html')

@app.route('/learn')
def contact():
    return render_template('learn.html')

@app.route('/marketplace')
def portfolio():
    return render_template('marketplace.html')


if __name__ == '__main__':
    app.run(debug=True)
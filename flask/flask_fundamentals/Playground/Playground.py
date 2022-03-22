from flask import Flask , render_template
app = Flask(__name__)

@app.route('/play')                           
def boxes():
    return render_template("index.html",mult=3,change='red')
    # return render_template("index.html")

@app.route('/play/<num>')                           
def boxes1(num):
# return render_template('index.html')
    return render_template("index.html",mult = int(num))

@app.route('/play/<num>/<color>')                           
def boxes2(num,color):
# return render_template('index.html')
    return render_template("index.html",mult = int(num),change = color)

if __name__=="__main__": 
    app.run(debug=True)
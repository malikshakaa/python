from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'have it say "Dojo!'  # Return the string 'Hello World!' as a response
@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def say(name):
    return 'Hi'+ name

@app.route('/repeat/<num>/<name>')          # The "@" decorator associates this route with the function immediately following
def repeat(num,name):
    return name*int(num)


if __name__=="__main__":    
    app.run(debug=True)
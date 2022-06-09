# importing modules from flask library
from unicodedata import name
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "" # write your name
    age = "" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father():
    name=""
    age = ""

    return render_template('father.html', name = name , age = age)

# define the route to mother webpage
def mother():
    name=""
    age = ""

    return render_template('mother.html', name = name , age = age)


# define the route to friends webpage
def friend():
    name=""
    age = ""

    return render_template('friend.html', name = name , age = age)

# add other routes, if you want
#@app.route("/father")



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)

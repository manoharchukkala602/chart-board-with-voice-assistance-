from flask import Flask
app =Flask(__name__)
app.route('/')
def home():
  return "welcome to our chart board"
app.run(debug =True)
          
          

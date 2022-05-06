
from flask import Flask, render_template
app = Flask (__name__)



users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html",users=users)
    
   

    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>This is the home page </h1>"

@app.route("/who")
@app.route("/who/<name>")
def name(name="default"):
    page = """
    <h1> the page name </h1>
    This is a page with someone's name
    <hr>
    The name is: 
    """
    page=page+name+"<hr>"
    return page

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"
    


if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=5005)
    

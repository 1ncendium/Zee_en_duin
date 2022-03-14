

from flask import Flask, render_template

app = Flask(__name__)

# ------- Begin of routes ---------

@app.route('/', methods=['GET'])
def index():
    """
    Main page function (index.html)
    Returns the index.html page trough render_template.
    Accepts only GET requests.
    """
    return render_template('index.html')

@app.route('/aanbod', methods=['GET'])
def aanbod():
    """
    Page function for aanbod.html.
    Returns the aanbod.html page trough render_template.
    Accepts only GET requests.
    """    
    return render_template('aanbod.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    """
    Page function for auth/login.html.
    Returns the login.html page trough render_template.
    Accepts POST and GET requests.
    """    
    return render_template('login.html')

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    """
    Page function for auth/register.html.
    Returns the register.html page trough render_template.
    Accepts POST and GET requests.
    """ 
    return render_template('register.html')

# ------- End of routes ---------
if __name__ == "__main__":
    app.run(debug=True)
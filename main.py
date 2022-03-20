from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from db import login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VerySecret'

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

@app.route('/login', methods=['GET', 'POST'])
def login_user():
    """
    Page function for auth/login.html.
    Returns the login.html page trough render_template.
    Accepts POST and GET requests.
    """

    error = "Foute gebruikersnaam / wachtwoord!"

    if request.method == 'POST' and request.form['gebruikersnaam'] != '':
        if login(request.form['gebruikersnaam'], request.form['wachtwoord']) == True:
            return render_template('login.html', error=error)
        else:
            return render_template('index.html')
    else:
        return render_template('login.html')

@app.route('/registreren', methods=['GET', 'POST'])
def register():
    """
    Page function for auth/register.html.
    Returns the register.html page trough render_template.
    Accepts POST and GET requests.
    """ 
    return render_template('registreren.html')

# ------- End of routes ---------

if __name__ == "__main__":
    app.run(debug=True)
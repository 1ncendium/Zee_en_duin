from mijnproject import app, db
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from mijnproject.models import User, Bungalow
from mijnproject.forms import LoginForm, RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aanbod')
@login_required
def aanbod():
    user = current_user.username

    bungalow = Bungalow.query.filter_by(id=1)

    return render_template('aanbod.html', user=user, bungalow=bungalow)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!', 'info')
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            # Log in the user

            login_user(user)
            flash('Succesvol ingelogd!.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0] == '/':
                next = url_for('aanbod')

            return redirect(next)
    return render_template('login.html', form=form)


@app.route('/registreren', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        print(True)
        try:
            user = User(email=form.email.data,
                        username=form.username.data,
                        password=form.password.data)

            db.session.add(user)
            db.session.commit()
            flash('Dank voor de registratie. Er kan nu ingelogd worden! ')
            return redirect(url_for('login'))
        except Exception as e:
            print(e)
    return render_template('registreren.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

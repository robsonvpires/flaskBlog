from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bf9c3bb7288d52597b82f0745a1b43a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


posts = [
    {
        'author': 'Robson Pires',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Jun 27, 2020'
    },
    {
        'author': 'Robson Pires',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'Jun 28, 2020'
    }

]
@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Logged Unsuccessul', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)



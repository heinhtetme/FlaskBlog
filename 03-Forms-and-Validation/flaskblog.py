# October 25, 2019
# pip install flask-wtf
# import secrets and secrets.token_hex(16)

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Ye Tun Aung',
        'title': 'Blog Post 1',
        'content': 'JavaScript is pretty cool!',
        'date_posted': 'October 25, 2019'
    },
    {
        'author': 'Thura Ye Tun',
        'title': 'Blog Post 2',
        'content': 'So tired from all that learning!',
        'date_posted': 'October 26, 2019'
    },
    {
        'author': 'Maythansin Ye Tun',
        'title': 'Blog Post 2',
        'content': 'Scratch is so cool!',
        'date_posted': 'October 27, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

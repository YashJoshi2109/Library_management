from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Dummy database for library books
library_books = {
    1: {'title': 'Book 1', 'author': 'Author 1', 'available': True},
    2: {'title': 'Book 2', 'author': 'Author 2', 'available': False},
    3: {'title': 'Book 3', 'author': 'Author 3', 'available': True}
}


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'username' in session:
        return render_template("home.html", username=session['username'], books=library_books)
    else:
        return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy user validation
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)


app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Dummy user validation
        if username == 'admin' and password == 'password':
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()

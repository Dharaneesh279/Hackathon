from django.apps import AppConfig


class CegConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ceg'
import sqlite3
#from flask import Flask, render_template, request, redirect, url_for, session, flash
#from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Replace with a secure key in production

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        phone TEXT,
        recent_project TEXT,
        most_viewed_project TEXT
    )''')
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):  # user[3] is the password field
            session['user_id'] = user[0]
            session['email'] = user[2]
            flash('Login successful!', 'success')
            return redirect(url_for('profile1'))
        else:
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # Hash the password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

    

@app.route('/profile1')
def profile1():
    if 'user_id' not in session:
        flash('Please log in to view your profile', 'error')
        return redirect(url_for('login'))

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT name, email, phone, recent_project, most_viewed_project FROM users WHERE id = ?", (session['user_id'],))
    user = c.fetchone()
    conn.close()

    if user:
        return render_template('profile1.html', user=user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('email', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

# URL mapping for Watertracking (placeholder, assuming it exists)
@app.route('/Watertracking')
def Watertracking():
    if 'user_id' not in session:
        flash('Please log in to access Watertracking', 'error')
        return redirect(url_for('login'))
    return render_template('Watertracking.html')  # Assuming Watertracking.html exists

# Placeholder routes for other pages
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access the dashboard', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html')  # Placeholder

@app.route('/waterbilling')
def waterbilling():
    if 'user_id' not in session:
        flash('Please log in to access water billing', 'error')
        return redirect(url_for('login'))
    return render_template('waterbilling.html')  # Placeholder

@app.route('/notifications')
def notifications():
    if 'user_id' not in session:
        flash('Please log in to access notifications', 'error')
        return redirect(url_for('login'))
    return render_template('notifications.html')  # Placeholder

if __name__ == '__main__':
    app.run(debug=True)

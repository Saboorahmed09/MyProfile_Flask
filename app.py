from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure secret key


# In-memory data structure to store posts (replace with a database in a real-world scenario)
posts = []


@app.route('/')
def myprofile():
    return render_template('myprofile.html', posts=posts)

@app.route('/home')
def home():
    return render_template('home.html', title='Welcome to Profile Overview')

# Explicitly define the myprofile route to handle POST requests
@app.route('/', methods=['POST'])
def handle_post():
    # Placeholder response for the POST request on the myprofile page
    return jsonify({"message": "Received POST request on myprofile page"})


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Simple example: check if the username and password match
        if username == 'admin' and password == 'admin':
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('admin'))

        flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out successfully.', 'info')
    return render_template('logout.html')

def check_login():
    return 'username' in session

@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if not check_login():
        return redirect(url_for('no_access'))

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        # Create a new post and add it to the posts list
        new_post = {"title": title, "content": content}
        posts.append(new_post)

        # Redirect to the myprofile page after adding the post
        return redirect(url_for('myprofile'))

    return render_template('admin.html')

@app.route('/no_access')
def no_access():
    return render_template('no_access.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/get_profile')
def get_profile():
    # Dynamic profile data (replace this with your data retrieval logic)
    profile_data = [
        {"title": "Course 1", "description": "Description for Course 1."},
        {"title": "Course 2", "description": "Description for Course 2."},
        # Add more courses as needed
    ]

    return jsonify(profile_data)

if __name__ == '__main__':
    app.run(debug=True)

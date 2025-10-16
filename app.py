from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message = "Please log in to access this page."

#User model
class User(UserMixin,db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(150), nullable=False)
    username=db.Column(db.String(150), unique=True, nullable=False)
    password=db.Column(db.String(60), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.name}', '{self.username}')"

# Your models here
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.title}"

#User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))






@app.route("/register", methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']

        #Check if user already exists
        existing_user=User.query.filter_by(username=username).first()

        if existing_user:
            flash('Username already exists. Choose a different one.','danger')
            return redirect(url_for('register'))
    
        #Hash password and create new user
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        user=User(name=name, username=username, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        flash('Registration successful! You can now log in.','success')
        return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]

        user=User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!','success')
            return redirect(url_for('show'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.','info')
    return redirect(url_for('login'))



@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/add", methods=['GET','POST'])
@login_required
def add():
    if request.method=='POST':
        print("Form data received:", request.form)  # Debug line
        print("Current user ID:", current_user.id)  # Debug line
        
        title=request.form.get("title")  # Use .get() to avoid KeyError
        desc=request.form.get("desc")    # Use .get() to avoid KeyError
        
        print(f"Title: {title}, Description: {desc}")  # Debug line
        
        if title and desc:  # Check if fields are not empty
            todo=Todo(title=title, description=desc, user_id=current_user.id)
            db.session.add(todo)
            db.session.commit()
            # print("Todo added successfully")  # Debug line
            flash('Todo added successfully!', 'success')
        else:
            # print("Missing title or description")  # Debug line
            flash('Please fill in both title and description', 'danger')
        
        return redirect(url_for('show'))
    
    return render_template("add.html")


@app.route("/show", methods=['GET','POST'])
@login_required
def show():
    allTodo=Todo.query.filter_by(user_id=current_user.id).all()
    return render_template("show.html",allTodo=allTodo)

@app.route("/delete/<int:sno>")
@login_required
def delete(sno):
    todo=Todo.query.filter_by(sno=sno, user_id=current_user.id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect("/show")

@app.route("/update/<int:sno>", methods=['GET','POST'])
@login_required
def update(sno):
    todo=Todo.query.filter_by(sno=sno, user_id=current_user.id).first()
    if not todo:
        return redirect(url_for("show"))
    
    if request.method=="POST":
        title=request.form["title"]
        desc=request.form["desc"]
        todo.title=title
        todo.description=desc
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('show'))
    
    return render_template("update.html",todo=todo)

# @app.route("/debug")
# @login_required
# def debug():
#     all_todos = Todo.query.all()
#     user_todos = Todo.query.filter_by(user_id=current_user.id).all()
#     return f"Total todos in DB: {len(all_todos)}<br>User todos: {len(user_todos)}<br>Current user ID: {current_user.id}"



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

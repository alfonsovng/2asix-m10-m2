import psycopg2
from flask import Flask, request, redirect, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

con = psycopg2.connect(database="cronaldo_p8", user="cronaldo_p8", password="mir", host="127.0.0.1", port="5432")
cur = con.cursor()

app = Flask(__name__)

app.config.update(
    SECRET_KEY = 'secret_xxx'
)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):

    def __init__(self, id, email):
        self.id = id
        self.email = email
        
    def __repr__(self):
        return "%d/%s" % (self.id, self.email)

# some protected url
@app.route('/')
@login_required
def home():
    return f"""
    <h1>Contingut exclusiu per a tu, {current_user.email}</h1>

    <hr />
    
    <h3> AQUÍ HAURIA DE MOSTRAR LA LLISTA DE LA COMPRA DEL USUARI AMD ID #{current_user.id} </h3>
    
    <hr />

    <a href="/logout">Logout</a>
    """

# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email_introduit = request.form['email']
        password_introduit = request.form['password']

        #consulto a la base de dades si tot és correcte
        cur.execute(f"""
            SELECT id 
            FROM users
            WHERE email = '{email_introduit}' 
            AND password = crypt('{password_introduit}', password)
        """)

        row = cur.fetchone()
        if row is None:
            # usuari/password incorrectes
            return abort(401)
        else:
            user = User(id = int(row[0]), email = email_introduit)
            login_user(user)
            return redirect("/")
    else:
        return """
        <form action="" method="post">
            <p><input type="email" placeholder="email" name="email">
            <p><input type="password" placeholder="password" name="password">
            <p><input type="submit" value="Login">
        </form>
        """

# somewhere to logout
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return """<h3>Logged out</h3><a href="/login">Login again?</a>"""

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return """<h3>Login failed</h3><a href="/login">Try login again?</a>"""
    
# callback to reload the user object        
@login_manager.user_loader
def load_user(id):
    #busco en base de datos el usuario
    cur.execute(f"""select email from users where id = {id}""")
    row = cur.fetchone()

    if row is None:
        # no existeix l'usuari a la base de dades
        return None
    else:
        return User(id = id, email = row[0])

if __name__ == '__main__':
    app.run(debug = True)
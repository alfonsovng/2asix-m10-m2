import psycopg2
from flask import Flask

con = psycopg2.connect(database="cronaldo_p8", user="cronaldo_p8", password="mir", host="127.0.0.1", port="5432")
cur = con.cursor()

app = Flask(__name__)

@app.route('/')
def llistat_emails():
    cur.execute("""select email from users""")

    rows = cur.fetchall()

    llista_emails = list()
    for row in rows:
        llista_emails.append(row[0])
    emails = ", ".join(llista_emails)

    return f"""
    <!doctype html>
    <html>
    <head>
    <title>La meva segona web amb Python & Flask</title>
    </head>
    <body>
    <h1>Emails a la taula users:</h1>
    <h2>{emails}</h2>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug = True)
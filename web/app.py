from flask import Flask, render_template, request
from flask import g
from configparser import ConfigParser
import psycopg2
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nombrEstudent = request.form['nombre']

        try:
            result = get_estudiante_by_NombreSeguro(nombrEstudent)
            return render_template('index.html', estudiantes=result)
        except:
            return 'Ocurrío un problema al buscar'

    else:
        result = get_estudiante_All()
        return render_template('index.html', estudiantes=result)
def get_estudiante_by_Nombre(nombre):
    db, cur = get_db()
    cur.execute('select * from lab9b.estudiante where nombres ='+"'"+nombre+"'")
    return cur.fetchall()

def get_estudiante_by_NombreSeguro(nombre):
    db, cur = get_db()
    print(nombre)
    cur.execute('prepare myplan as select * from lab9b.estudiante where nomres like $1;')
    cur.execute('execute myplan (%s)', (nombre,))
    return cur.fetchall()

def get_estudiante_All():
    db, cur = get_db()
    cur.execute('select * from lab9b.estudiante')
    return cur.fetchall()

def get_db():
    """Attempt to connect to database and attach to global app"""
    if ("db" not in g) or ("cur" not in g):
        db_config = get_config()
        g.db = psycopg2.connect(**db_config) # db connection
        g.db.autocommit = True
        #g.cur = g.db.cursor(cursor_factory=extras.DictCursor) # operation cursor
        g.cur = g.db.cursor()  # operation cursor
    return g.db, g.cur

def get_config(filename="database.ini", section="postgresql"):
    """Parses and gets database config from file"""
    parser = ConfigParser()
    parser.read(filename)

    db_config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db_config[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found".format(section))

    return db_config

if __name__ == '__main__':
    app.run()

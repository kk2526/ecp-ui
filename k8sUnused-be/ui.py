import psycopg2
import os

from flask import Flask, render_template, request, flash, redirect
from psycopg2.extras import RealDictCursor
from config.config import db_conn
from flask import session as login_session

app = Flask(__name__)
app.secret_key = os.urandom(24)

conn = None
params = db_conn()
conn = psycopg2.connect(**params)
cursor = conn.cursor(cursor_factory=RealDictCursor)

@app.route('/')
def k8sui():
    cursor.execute('SELECT * FROM staleobj')
    staleobjs=cursor.fetchall()
    return render_template('index.html', staleobjs=staleobjs)

@app.route('/action/<string:actions>', methods=['POST'])
def dynamic_action(actions):
    for getid in request.form.getlist('mycheckbox'):
        if actions == 'delete':
            cursor.execute("Update staleobj set state = %s where id = %s",["Delete", getid])
            conn.commit()
        elif actions == 'keep':
            cursor.execute("Update staleobj set state = %s where id = %s",["Keep-It", getid])
            conn.commit()
        else:
            cursor.execute("Update staleobj set state = %s where id = %s",["In-Review", getid])
            conn.commit()

    flash('Successfully Updated!')
    return redirect('/')

# @app.route('/delete', methods=['POST'])
# def delete():
#     for getid in request.form.getlist('mycheckbox'):
#         print(getid)
#         cursor.execute("Update staleobj set state = %s where id = %s",["Delete", getid])
#         conn.commit()
#     flash('Successfully Updated!')
#     return redirect('/')
#
# @app.route('/keep', methods=['POST'])
# def keep():
#     for getid in request.form.getlist('mycheckbox'):
#         print(getid)
#         cursor.execute("Update staleobj set state = %s where id = %s",["Keep-It", getid])
#         conn.commit()
#     flash('Successfully Updated!')
#     return redirect('/')
#
# @app.route('/inreview', methods=['POST'])
# def inreview():
#     for getid in request.form.getlist('mycheckbox'):
#         print(getid)
#         cursor.execute("Update staleobj set state = %s where id = %s",["In-Review", getid])
#         conn.commit()
#     flash('Successfully Updated!')
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

import sqlite3
from functools import wraps
from flask import Flask, flash, redirect, render_template, \
    request, session, url_for, g
from forms import AddCarForm

app = Flask(__name__)
app.config.from_object('_config')


def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))

    return wrap


@app.route('/logout/')
def logout():
    session.pop('logged in', None)
    flash('See you next time!')
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] \
                or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            flash('Welcome!')
            return redirect(url_for('garage'))
    return render_template('login.html')


@app.route('/garage/')
@login_required
def garage():
    g.db = connect_db()
    cur = g.db.execute(
        'select make, model, color, year, car_id from garage'
    )
    car_garage = [
        dict(make=row[0], model=row[1], color=row[2], year=row[3],
             car_id=row[4]) for row in cur.fetchall()
        ]
    g.db.close()
    return render_template(
        'garage.html',
        form=AddCarForm(request.form),
        car_garage=car_garage
    )


@app.route('/details/')
@login_required
def details():
    g.db = connect_db()
    cur = g.db.execute(
        'select odom, oil, trans, brake, car_id from details'
    )
    car_details = [
        dict(odom=row[0], oil=row[1], trans=row[2], brake=row[3],
             car_id=row[4]) for row in cur.fetchall()
                ]
    g.db.close()
    return render_template(
        'details.html',
        form=AddCarForm(request.form),
        car_details=car_details
    )


@app.route('/add/', methods=['POST'])
@login_required
def new_car():
    g.db = connect_db()
    make = request.form['make']
    model = request.form['model']
    color = request.form['color']
    year = request.form['year']
    if not make or not model or not color or not year:
        flash("All fields are required. Please try again.")
        return redirect(url_for('garage'))
    else:
        g.db.execute('insert into garage (make, model, color, year) \
            values (?, ?, ?, ?)', [
            request.form['make'],
            request.form['model'],
            request.form['color'],
            request.form['year']
        ]
                     )
        g.db.commit()
        g.db.close()
        flash('New car added. Someone\'s rich.')
    return redirect(url_for('garage'))


@app.route('/delete/<int:car_id>/')
@login_required
def delete_car(car_id):
    g.db = connect_db()
    g.db.execute('delete from garage where car_id=' + str(car_id))
    g.db.commit()
    g.db.close()
    flash('That car just got blown the hell up.')
    return redirect(url_for('garage'))


@app.route('/update/<int:car_id>/', methods=['POST'])
@login_required
def update_car(car_id):
    g.db = connect_db()
    odom = request.form['odomoter']
    oil = request.form['oil']
    trans = request.form['transmission']
    brake = request.form['brake']
    if not odom or not oil or not trans or not brake:
        flash("All fields are required. Please try again.")
        return redirect(url_for('garage'))
    else:
        g.db.execute('update details set odom= ? where car_id= ' + str(car_id), (odom,))
        g.db.execute('update details set oil= ? where car_id= ' + str(car_id), (oil,))
        g.db.execute('update details set trans= ? where car_id= ' + str(car_id), (trans,))
        g.db.execute('update details set brake= ? where car_id= ' + str(car_id), (brake,))
        g.db.commit()
        g.db.close()
        return redirect(url_for('details'))

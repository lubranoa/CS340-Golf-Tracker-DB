from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes

@app.route('/')
def root():
    '''Route to home page'''
    return render_template("main.j2")

@app.route('/clubs')
def clubs():
    '''Route to clubs table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("clubs.j2", gt_clubs=results)

@app.route('/holes')
def holes():
    '''Route to holes table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM holes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("course_holes.j2", gt_holes=results)

@app.route('/courses')
def courses():
    '''Route to courses table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("courses.j2", gt_courses=results)

@app.route('/player-clubs')
def player_clubs():
    '''Route to player_clubs intersection table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM player_clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_clubs.j2", gt_player_clubs=results)

@app.route('/players')
def players():
    '''Route to players table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("players.j2", gt_players=results)

@app.route('/rounds')
def rounds():
    '''Route to rounds table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM rounds;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_rounds.j2", gt_rounds=results)

@app.route('/swings')
def player_round_swings():
    '''Route to swings table'''
    db_connection = db.connect_to_database()
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("player_round_swings.j2", gt_player_round_swings=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15432))
    app.run(port=port, debug=True)

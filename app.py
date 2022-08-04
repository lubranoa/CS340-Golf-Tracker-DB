from flask import Flask, render_template, json, request, redirect
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# ----------------------------------------------------------------------------
# READ ROUTES: Home Page and Display Entities Handlers
# 
# The following flask route functions handle reading the data for all entities
# in the Golf Tracker MySQL database. Each route connects to the database, 
# gets necessary data from it, and renders a read_entity Jinja template that 
# displays the sent information. All read templates have buttons to insert new
# entity instances, while only select ones have update and delete buttons. 
# ----------------------------------------------------------------------------

@app.route('/')
def root():
    """Route that displays home page"""
    return render_template("main.j2")


@app.route('/clubs')
def read_clubs():
    """Route that handles displaying clubs table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_clubs.j2", gt_clubs=results)


@app.route('/holes')
def read_holes():
    """Route that handles displayin holes table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM holes;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_holes.j2", gt_holes=results)


@app.route('/courses')
def read_courses():
    """Route that handles displaying courses table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_courses.j2", gt_courses=results)


@app.route('/player-clubs')
def read_player_clubs():
    """Route that handles displaying player_clubs intersection table"""
    db_connection = db.connect_to_database()    
    query = "SELECT * FROM player_clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_player_clubs.j2", gt_player_clubs=results)


@app.route('/players')
def read_players():
    """Route that handles displaying players table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_players.j2", gt_players=results)


@app.route('/rounds')
def read_rounds():
    """Route that handles displaying rounds table"""
    db_connection = db.connect_to_database()
    query = "SELECT " \
            "    rounds.round_id, " \
            "    rounds.course_id, " \
            "    courses.course_name, " \
            "    rounds.player_id, " \
            "    players.player_name, " \
            "    rounds.round_date, " \
            "    rounds.round_score " \
            "FROM rounds " \
            "    INNER JOIN courses ON rounds.course_id = courses.course_id " \
            "    INNER JOIN players ON rounds.player_id = players.player_id;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_rounds.j2", gt_rounds=results)


@app.route('/swings')
def read_swings():
    """Route that handles displaying swings table"""
    db_connection = db.connect_to_database()
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_swings.j2", gt_player_round_swings=results)


# ----------------------------------------------------------------------------
# INSERT ROUTES: Update Entity Handlers
#
# The following flask route functions handle inserting new entity instances 
# into the Golf Tracker MySQL Database. Each route connects to the database,
# renders an insert_entity Jinja template, getting any entity data necessary
# for insertion, and inserts the new entity into the database.
# ----------------------------------------------------------------------------

@app.route("/insert-club", methods=["POST", "GET"])
def insert_club():
    """Route that handles inserting a club into the database"""
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_club.j2")
    
    elif request.method == "POST":
        brand = request.form["brand"]
        club_name = request.form["club_name"]
        club_type = request.form["club_type"]

        insert_query = "INSERT INTO clubs (brand, club_name, club_type) VALUES (%s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(brand, club_name, club_type)
        )
        return redirect("/clubs")


@app.route("/insert-course", methods=["POST", "GET"])
def insert_course():
    """Route that handles inserting a course into the database"""
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_course.j2")
    
    elif request.method == "POST":
        course_name = request.form["course_name"]
        course_state = request.form["course_state"]

        insert_query = "INSERT INTO courses (course_name, course_state) VALUES (%s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(course_name, course_state)
        )
        return redirect("/courses")


@app.route("/insert-hole", methods=["POST", "GET"])
def insert_hole():
    """Route that handles inserting a hole into the database"""
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        courses_query = "SELECT * FROM courses;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=courses_query
        )
        courses_res = cursor.fetchall()
        return render_template("insert_hole.j2", gt_courses=courses_res)
    
    elif request.method == "POST":
        course_id = request.form["course_id"]
        par_swing_count = request.form["par_swing_count"]
        distance = request.form["distance"]

        insert_query = "INSERT INTO holes (course_id, par_swing_count, distance) VALUES (%s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(course_id, par_swing_count, distance)
        )
        return redirect("/holes")


@app.route("/insert-player-club", methods=["POST", "GET"])
def insert_player_club():
    """
    Route that handles inserting a player_club intersection table entry into
    the database.
    """
    
    if request.method == "GET":
        db_connection = db.connect_to_database()
        
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=p_query
        )
        p_res = cursor.fetchall()

        c_query = "SELECT club_id, brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()
        
        return render_template("insert_player_club.j2", gt_players=p_res, gt_clubs=c_res)
            
    elif request.method == "POST":    
        db_connection = db.connect_to_database()
        player_id = request.form['player']
        club_id = request.form['club']

        query = f"INSERT INTO player_clubs (player_id, club_id) VALUES ({player_id}, {club_id});"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect("/player-clubs")


@app.route("/insert-player", methods=["POST", "GET"])
def insert_player():
    """Route that handles inserting a player into the database"""
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_player.j2")
    
    elif request.method == "POST":        
        player_name = request.form["player_name"]
        player_city = request.form["player_city"]
        player_state = request.form["player_state"]

        insert_query = "INSERT INTO players (player_name, player_city, player_state) VALUES (%s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(player_name, player_city, player_state)
        )
        return redirect("/players")


@app.route("/insert-round", methods=["POST", "GET"])
def insert_round():
    """Route that handles inserting a round into the database"""
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=p_query
        )
        p_res = cursor.fetchall()

        c_query = "SELECT course_id, course_name FROM courses;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()
        
        return render_template("insert_round.j2", gt_players=p_res, gt_courses=c_res)
    
    elif request.method == "POST":
        course_id = request.form["course_id"]
        player_id = request.form["player_id"]
        unformatted_date = request.form["round_date"]
        round_score = request.form["round_score"]

        # Reformat date to SQL datetime format ("YYYY-MM-DDT00:00" ==> "YYYY-MM-DD 00:00:00")
        round_date = unformatted_date.replace("T", " ") + ":00"

        insert_query = "INSERT INTO rounds (course_id, player_id, round_date, round_score) VALUES (%s, %s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(course_id, player_id, round_date, round_score)
        )    
        return redirect("/rounds")


@app.route("/insert-swing", methods=["POST", "GET"])
def insert_swing():
    """Route that handles inserting a swing into the database"""
    
    db_connection = db.connect_to_database()

    #TODO: implement route
    
    if request.method == "GET":

        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=p_query
        )
        p_res = cursor.fetchall()

        r_query = """
            SELECT courses.course_name, rounds.round_date 
            FROM rounds 
            INNER JOIN courses 
            ON courses.course_id = rounds.course_id;"""
        cursor = db.execute_query(
            db_connection=db_connection,
            query=r_query
        )
        r_res = cursor.fetchall()

        c_query = "SELECT club_id, brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()

        h_query = """
            SELECT course_name, hole_id
            FROM holes
            INNER JOIN courses
            ON courses.course_id = holes.course_id;"""
        cursor = db.execute_query(
            db_connection=db_connection,
            query=h_query
        )
        h_res = cursor.fetchall()

        return render_template("insert_swing.j2", gt_players=p_res, gt_rounds=r_res, gt_clubs=c_res, gt_holes=h_res)
    
    elif request.method == "POST":
    
        return redirect("/swings")


# ----------------------------------------------------------------------------
# UPDATE ROUTES: Update Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/update-player/<int:id>", methods=["POST", "GET"])
def update_player(id):
    """Route that handles updating a player's data"""
    
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("update_player.j2", gt_player=results)
    
    elif request.method == "POST":
        player_id = id
        player_name = request.form["player_name"]
        player_city = request.form["player_city"]
        player_state = request.form["player_state"]

        update_query = "UPDATE players SET players.player_name = %s, players.player_city =%s, players.player_state = %s WHERE players.player_id = %s;"
        db.execute_query(
            db_connection=db_connection, 
            query=update_query, 
            query_params=(player_name, player_city, player_state, player_id)
        )
        return redirect("/players")


@app.route("/update-round/<int:id>", methods=["POST", "GET"])
def update_round(id):
    """Route that handles updating a rounds's data"""

    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT " \
                     "    rounds.round_id, " \
                     "    rounds.course_id, " \
                     "    courses.course_name, " \
                     "    rounds.player_id, " \
                     "    players.player_name, " \
                     "    rounds.round_date, " \
                     "    rounds.round_score " \
                     "FROM rounds " \
                     "    INNER JOIN courses ON rounds.course_id = courses.course_id " \
                     "    INNER JOIN players ON rounds.player_id = players.player_id " \
                     "WHERE round_id = '%s';" % (id)

        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()

        reformat_date = results[0]["round_date"].strftime("%Y-%m-%dT%H:%M")
        results[0]["form_date"] = reformat_date

        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(db_connection=db_connection, query=p_query)
        p_res = cursor.fetchall()

        c_query = "SELECT course_id, course_name FROM courses;"
        cursor = db.execute_query(db_connection=db_connection, query=c_query)
        c_res = cursor.fetchall()

        return render_template("update_round.j2", gt_round=results, gt_players=p_res, gt_courses=c_res)
    
    elif request.method == "POST":

        round_id = id
        course_id = request.form["course_id"]
        player_id = request.form["player_id"]
        unformatted_date = request.form["round_date"]
        round_score = request.form["round_score"]

        # Reformat date to SQL datetime format ("YYYY-MM-DDT00:00" ==> "YYYY-MM-DD 00:00:00")
        round_date = unformatted_date.replace("T", " ") + ":00"

        update_query = "UPDATE rounds SET " \
                       "    rounds.course_id = %s, " \
                       "    rounds.player_id =%s, " \
                       "    rounds.round_date = %s, " \
                       "    rounds.round_score = %s " \
                       "WHERE rounds.round_id = %s;"
        db.execute_query(
            db_connection=db_connection, 
            query=update_query, 
            query_params=(course_id, player_id, round_date, round_score, round_id)
        )
    
        return redirect("/rounds")

@app.route("/test")
def test_route():
    db_connection = db.connect_to_database()
    read_query = read_query = "SELECT " \
                              "    rounds.round_id, " \
                              "    rounds.course_id, " \
                              "    courses.course_name, " \
                              "    rounds.player_id, " \
                              "    players.player_name, " \
                              "    rounds.round_date, " \
                              "    rounds.round_score " \
                              "FROM rounds " \
                              "    INNER JOIN courses ON rounds.course_id = courses.course_id " \
                              "    INNER JOIN players ON rounds.player_id = players.player_id " \
                              "WHERE round_id = 1;"
    cursor = db.execute_query(db_connection=db_connection, query=read_query)
    res = cursor.fetchall()
    results = json.dumps(res)
    return results


@app.route("/update-swing/<int:id>", methods=["POST", "GET"])
def update_swing(id):
    """Route that handles updating a swing's data"""

    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM swings WHERE swing_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("update_swing.j2", gt_swing=results)
    
    elif request.method == "POST":

        #TODO: implement update query

        return redirect("/swings")


# ----------------------------------------------------------------------------
# DELETE ROUTES: Delete Entity Handlers
#
#
# ----------------------------------------------------------------------------

@app.route("/delete-club/<int:id>", methods=["POST", "GET"])
def delete_club(id):
    """Route that handles deleting a club from the database"""
    
    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM clubs WHERE club_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_club.j2", gt_club=results)
    
    elif request.method == "POST":
        club_id = id
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM clubs WHERE club_id = '%s';"
            db.execute_query(
                db_connection=db_connection, 
                query=delete_query, 
                query_params=(club_id,)
            )

        return redirect("/clubs")


@app.route("/delete-player/<int:id>", methods=["POST", "GET"])
def delete_player(id):
    """Route that handles deleting a player from the database"""

    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_player.j2", gt_player=results)
    
    elif request.method == "POST":
        player_id = id
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM players WHERE player_id = '%s';"
            db.execute_query(
                db_connection=db_connection, 
                query=delete_query, 
                query_params=(player_id,)
            )

        return redirect("/players")


@app.route("/delete-round/<int:id>", methods=["POST", "GET"])
def delete_round(id):
    """Route that handles deleting a round from the database"""
    
    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM rounds WHERE round_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_round.j2", gt_round=results)
    
    elif request.method == "POST":
    
        round_id = id
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM rounds WHERE round_id = '%s';"
            db.execute_query(
                db_connection=db_connection, 
                query=delete_query, 
                query_params=(round_id,)
            )
        
        return redirect("/rounds")


@app.route("/delete-swing/<int:id>", methods=["POST", "GET"])
def delete_swing(id):
    """Route that handles deleting a swing from the database"""
    
    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM swings WHERE swing_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_swing.j2", gt_swing=results)
    
    elif request.method == "POST":
        
        # TODO: implement delete query

        return redirect("/swings")


@app.route("/delete-player-club/<int:player_id>/<int:club_id>/", methods=["POST", "GET"])
def delete_player_club(player_id, club_id):
    """Route that handles deleting a player_club relationship from the database"""
    
    db_connection = db.connect_to_database()

    if request.method == "GET":
        read_query = "SELECT * FROM player_clubs WHERE player_id = %s and club_id = %s;" % (player_id, club_id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_player_club.j2", gt_clubs=results)
    
    elif request.method == "POST":
        
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM player_clubs WHERE player_id = %s and club_id = %s;" % (player_id, club_id)
            cursor = db.execute_query(db_connection=db_connection, query=delete_query)
            return redirect("/player-clubs")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15432))
    app.run(port=port, debug=True)

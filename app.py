# ----------------------------------------------------------------------------
# Authors: Conner Marchell and Alexander Lubrano
# Course: CS 340 - Introduction to Databases
# File Name: app.py
# Last Modified: 08/05/2022
# Description: This Flask app allows a database administrator to interact with 
#     our Golf Tracker database data using CRUD operations through a web app. 
#     These CRUD operations are implemented in Flask route handler functions 
#     that read data from the database, render it in Jinja2 html templates as 
#     web pages that provide read functionality. Each read page has insert 
#     buttons for each entity as well as update and delete buttons for 
#     appropriate entities. These buttons link to separate insert, update, and
#     delete pages that contain forms with inputs for submission. If one of 
#     these forms are submitted, the route handlers detect a POST and perform
#     the proper insert, update, or delete operation on the database.
#  
# ----------------------------------------------------------------------------


from flask import Flask, render_template, json, request, redirect
import os
import database.db_connector as db


# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# ----------------------------------------------------------------------------
# READ ROUTES: Home Page and Display Entities Handlers
# 
# The following Flask route functions handle reading the data for all entities
# in the Golf Tracker MySQL database. Each route connects to the database, 
# gets necessary data from it, and renders a read_entity Jinja template that 
# displays the sent information. All read templates have buttons to insert new
# entity instances, while only select ones have update and delete buttons. 
# ----------------------------------------------------------------------------

@app.route('/')
def root():
    """Display Home Page

    Route that renders the app's home page
    """
    return render_template("main.j2")


@app.route('/clubs')
def read_clubs():
    """Display clubs Page

    Route that handles reading all clubs data from the database and rendering
    the clubs table in a Jinja2 template with insert and delete buttons.
    """
    db_connection = db.connect_to_database()
    query = "SELECT * FROM clubs;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_clubs.j2", gt_clubs=results)


@app.route('/courses')
def read_courses():
    """Display courses Page

    Route that handles reading all courses data from the database and 
    rendering the courses table in a Jinja2 template with an insert button.
    """
    db_connection = db.connect_to_database()
    query = "SELECT * FROM courses;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_courses.j2", gt_courses=results)


@app.route('/holes')
def read_holes():
    """Display holes Page

    Route that handles reading all holes data from the database and rendering
    the holes table in a Jinja2 template with an insert button.
    """
    db_connection = db.connect_to_database()
    query = ('SELECT '
             'holes.hole_id, '
             'holes.course_id, '
             'courses.course_name, '
             'holes.hole_number, '
             'holes.par_swing_count, '
             'holes.distance '
             'FROM holes '
             'INNER JOIN courses ON '
             'holes.course_id = courses.course_id;'
             )
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_holes.j2", gt_holes=results)


@app.route('/player-clubs')
def read_player_clubs():
    """Display player_clubs Page

    Route that handles reading all player_clubs data from the database and 
    rendering the player_clubs intersection table in a Jinja2 template with 
    insert and delete buttons.
    """
    db_connection = db.connect_to_database()
    query = """SELECT player_clubs.player_id, players.player_name, player_clubs.club_id, CONCAT(clubs.brand, ' ', clubs.club_name, ' ', clubs.club_type) AS club
                FROM player_clubs
                INNER JOIN players
                ON player_clubs.player_id = players.player_id
                INNER JOIN clubs
                ON player_clubs.club_id = clubs.club_id;"""
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_player_clubs.j2", gt_player_clubs=results)


@app.route('/player-clubs/search')
def read_player_clubs_search():
    """Route that handles displaying player_clubs intersection table"""

    player_name = request.args.get("player_name")

    db_connection = db.connect_to_database()
    query = f"""SELECT player_clubs.player_id, players.player_name, player_clubs.club_id, CONCAT(clubs.brand, ' ', clubs.club_name, ' ', clubs.club_type) AS club
                FROM player_clubs
                INNER JOIN players
                ON player_clubs.player_id = players.player_id
                INNER JOIN clubs
                ON player_clubs.club_id = clubs.club_id
                WHERE players.player_name LIKE '%{player_name}%';"""

    cursor = db.execute_query(db_connection=db_connection, query=query, query_params=None)
    results = cursor.fetchall()
    return render_template("read_player_clubs.j2", gt_player_clubs=results)


@app.route('/players')
def read_players():
    """Display players Page

    Route that handles reading all players data from the database and 
    rendering the players table in a Jinja2 template with insert, update, and
    delete buttons.
    """
    db_connection = db.connect_to_database()
    query = "SELECT * FROM players;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_players.j2", gt_players=results)


@app.route('/rounds')
def read_rounds():
    """Display rounds Page

    Route that handles reading all rounds data from the database and rendering
    the rounds table in a Jinja2 template with insert, update, and delete 
    buttons.
    """
    db_connection = db.connect_to_database()
    query = ('SELECT '
             'rounds.round_id, '
             'rounds.course_id, '
             'courses.course_name, '
             'rounds.player_id, '
             'players.player_name, '
             'rounds.round_date, '
             'rounds.round_score '
             'FROM rounds '
             'INNER JOIN courses ON '
             'rounds.course_id = courses.course_id '
             'INNER JOIN players ON '
             'rounds.player_id = players.player_id;'
             )
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_rounds.j2", gt_rounds=results)


@app.route('/swings')
def read_swings():
    """Display swings Page

    Route that handles reading all swings data from the database and rendering
    the swings table in a Jinja2 template with insert, update, and delete 
    buttons.
    """
    db_connection = db.connect_to_database()
    query = "SELECT * FROM swings;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("read_swings.j2", gt_player_round_swings=results)


# ----------------------------------------------------------------------------
# INSERT ROUTES: Update Entity Handlers
#
# The following Flask route functions handle inserting new entity instances 
# into the Golf Tracker MySQL Database. Each route connects to the database,
# renders an insert_entity Jinja template, getting any entity data necessary
# for insertion, and inserts the new entity into the database on submission.
# ----------------------------------------------------------------------------

@app.route("/insert-club", methods=["POST", "GET"])
def insert_club():
    """Insert club Page

    If request method is GET from the read_clubs page insert button, route
    handles rendering an insert_club page with a form containing necessary 
    club attribute inputs.

    If request method is POST from an insert_club page submit, route handles 
    getting the new club input, inserting it into the database, and
    redirecting to the read_clubs page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_club.j2")
    
    elif request.method == "POST":
        # Get new club data from form submission
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
    """Insert course Page

    If request method is GET from the read_courses page insert button, route
    handles rendering an insert_course page with a form containing necessary
    course attribute inputs.

    If request method is POST from an insert_course page submit, route handles
    getting the new course input, inserting it into the database, and
    redirecting to the read_courses page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_course.j2")
    
    elif request.method == "POST":
        # Get new course data from form submission
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
    """Insert hole Page

    If request method is GET from the read_holes page insert button, route
    handles rendering an insert_hole page with a form containing necessary
    hole attribute inputs.

    If request method is POST from an insert_hole page submit, route handles
    getting the new hole input, inserting it into the database, and
    redirecting to the read_holes page.
    """
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
        # Get new hole data from form submission
        course_id = request.form["course_id"]
        hole_number = request.form["hole_number"]
        par_swing_count = request.form["par_swing_count"]
        distance = request.form["distance"]

        insert_query = "INSERT INTO holes (course_id, hole_number, par_swing_count, distance) VALUES (%s, %s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(course_id, hole_number, par_swing_count, distance)
        )
        return redirect("/holes")


@app.route("/insert-player-club", methods=["POST", "GET"])
def insert_player_club():
    """Insert player_clubs Page

    If request method is GET from the read_player_clubs page insert button,
    route handles rendering an insert_player_club page with a form containing
    necessary player_club attribute inputs.

    If request method is POST from an insert_player_club page submit, route
    handles getting the new player_club input, inserting it into the database,
    and redirecting to the read_player_clubs page.
    """
    
    if request.method == "GET":
        db_connection = db.connect_to_database()
        
        # Get necessary player data for dropdown
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=p_query
        )
        p_res = cursor.fetchall()

        # Get necessary club data for dropdown
        c_query = "SELECT club_id, brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()
        
        return render_template("insert_player_club.j2", gt_players=p_res, gt_clubs=c_res)
            
    elif request.method == "POST":    
        db_connection = db.connect_to_database()
        
        # Get new player_club data from form submission
        player_id = request.form['player']
        club_id = request.form['club']

        query = f"INSERT INTO player_clubs (player_id, club_id) VALUES ({player_id}, {club_id});"
        db.execute_query(db_connection=db_connection, query=query)

        return redirect("/player-clubs")


@app.route("/insert-player", methods=["POST", "GET"])
def insert_player():
    """Insert player Page

    If request method is GET from the read_players page insert button, route
    handles rendering an insert_player page with a form containing necessary
    player attribute inputs.

    If request method is POST from an insert_players page submit, route
    handles getting the new player input, inserting it into the database, and
    redirecting to the read_players page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        return render_template("insert_player.j2")
    
    elif request.method == "POST":
        # Get new player data from form submission
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
    """Insert round Page

    If request method is GET from the read_rounds page insert button, route
    handles rendering an insert_round page with a form containing necessary
    round attribute inputs.

    If request method is POST from an insert_round page submit, route handles
    getting the new round input, inserting it into the database, and
    redirecting to the read_rounds page.
    """
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        # Get necessary player data for dropdown
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection, 
            query=p_query
        )
        p_res = cursor.fetchall()

        # Get necessary course data for dropdown
        c_query = "SELECT course_id, course_name FROM courses;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()
        
        return render_template("insert_round.j2", gt_players=p_res, gt_courses=c_res)
    
    elif request.method == "POST":
        # Get new round data from form submission
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
    """Insert swing Page

    If request method is GET from the read_swings page insert button, route
    handles rendering an insert_swing page with a form containing necessary
    swing attribute inputs.

    If request method is POST from an insert_swing page submit, route handles
    getting the new swing input, inserting it into the database, and
    redirecting to the read_swings page.
    """
    
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        # Get necessary player data for dropdown
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=p_query
        )
        p_res = cursor.fetchall()

        # Get necessary round data for dropdown
        r_query = """
            SELECT rounds.round_id, courses.course_name, rounds.round_date 
            FROM rounds 
            INNER JOIN courses 
            ON courses.course_id = rounds.course_id;"""
        cursor = db.execute_query(
            db_connection=db_connection,
            query=r_query
        )
        r_res = cursor.fetchall()

        # Get necessary club data for dropdown
        c_query = "SELECT club_id, brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()

        # Get necessary hole data for dropdown
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
        # Get new swing data from form submission
        swing_player = request.form["player_id"]
        swing_round = request.form["round_id"]
        swing_hole = request.form["hole_id"]
        swing_club = request.form["club_id"]
        swing_dist = request.form["dist_traveled_yd"]

        insert_query = "INSERT INTO swings (player_id, round_id, hole_id, club_id, dist_traveled_yd) VALUES (%s, %s, %s, %s, %s);"
        db.execute_query(
            db_connection=db_connection, 
            query=insert_query, 
            query_params=(swing_player, swing_round, swing_hole, swing_club, swing_dist)
        )
        return redirect("/swings")


# ----------------------------------------------------------------------------
# UPDATE ROUTES: Update Entity Handlers
#
# The following Flask route functions handle updating data already in the Golf
# Tracker's MySQL Database. Each route connects to the database, collects 
# necessary data from it, renders an update_entity Jinja template that 
# displays the selected entity's current data and loads it into a form along 
# with data from the database that could be used to update the entity, and 
# insertion, and updates the entity in the database on submission.
# ----------------------------------------------------------------------------

@app.route("/update-player/<int:id>", methods=["POST", "GET"])
def update_player(id):
    """Update player Page

    If request method is GET from any read_players page update buttons, route
    handles rendering an update_player page with the data of the player being 
    updated and a form containing necessary player attribute inputs prefilled 
    with that player's data.

    If request method is POST from an update_player page submit, route handles
    getting the updated player input, inserting it into the database, and
    redirecting to the read_players page.
    """
    db_connection = db.connect_to_database()
    
    if request.method == "GET":
        # Get necessary player data for display
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("update_player.j2", gt_player=results)
    
    elif request.method == "POST":
        # Get updated player data from form submission
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
    """Update round Page

    If request method is GET from any read_rounds page update buttons, route
    handles rendering an update_round page with the data of the round being 
    updated and a form containing necessary round attribute inputs prefilled 
    with that round's data and other necessary data to be chosen from.

    If request method is POST from an update_round page submit, route handles
    getting the updated round input, inserting it into the database, and
    redirecting to the read_rounds page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary round data for display and update inputs
        read_query = ('SELECT '
                     'rounds.round_id, '
                     'rounds.course_id, '
                     'courses.course_name, '
                     'rounds.player_id, '
                     'players.player_name, '
                     'rounds.round_date, '
                     'rounds.round_score '
                     'FROM rounds '
                     'INNER JOIN courses ON rounds.course_id = courses.course_id '
                     'INNER JOIN players ON rounds.player_id = players.player_id '
                     "WHERE round_id = '%s';" % (id)
                     )

        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()

        reformat_date = results[0]["round_date"].strftime("%Y-%m-%dT%H:%M")
        results[0]["form_date"] = reformat_date

        # Get necessary player data for dropdown
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(db_connection=db_connection, query=p_query)
        p_res = cursor.fetchall()

        # Get necessary course data for dropdown
        c_query = "SELECT course_id, course_name FROM courses;"
        cursor = db.execute_query(db_connection=db_connection, query=c_query)
        c_res = cursor.fetchall()

        return render_template("update_round.j2", gt_round=results, gt_players=p_res, gt_courses=c_res)
    
    elif request.method == "POST":
        # Get updated round data from form submission
        round_id = id
        course_id = request.form["course_id"]
        player_id = request.form["player_id"]
        unformatted_date = request.form["round_date"]
        round_score = request.form["round_score"]

        # Reformat date to SQL datetime format ("YYYY-MM-DDT00:00" ==> "YYYY-MM-DD 00:00:00")
        round_date = unformatted_date.replace("T", " ") + ":00"

        update_query = ("UPDATE rounds SET "
                        "rounds.course_id = %s, "
                        "rounds.player_id = %s, "
                        "rounds.round_date = %s, "
                        "rounds.round_score = %s "
                        "WHERE rounds.round_id = %s;"
                        )
        db.execute_query(
            db_connection=db_connection, 
            query=update_query, 
            query_params=(course_id, player_id, round_date, round_score, round_id)
        )
    
        return redirect("/rounds")

@app.route("/test")
def test_route():
    db_connection = db.connect_to_database()
    read_query = ('SELECT '
                  'rounds.round_id, '
                  'rounds.course_id, '
                  'courses.course_name, '
                  'rounds.player_id, '
                  'players.player_name, '
                  'rounds.round_date, '
                  'rounds.round_score '
                  'FROM rounds '
                  'INNER JOIN courses ON rounds.course_id = courses.course_id '
                  'INNER JOIN players ON rounds.player_id = players.player_id '
                  "WHERE round_id = '2';"
                  )
    cursor = db.execute_query(db_connection=db_connection, query=read_query)
    res = cursor.fetchall()
    results = json.dumps(res)
    return results


@app.route("/update-swing/<int:id>", methods=["POST", "GET"])
def update_swing(id):
    """Update swing Page

    If request method is GET from any read_swings page update buttons, route
    handles rendering an update_swing page with the data of the swing being 
    updated and a form containing necessary swing attribute inputs prefilled 
    with that swing's data and other necessary data to be chosen from.

    If request method is POST from an update_swing page submit, route handles
    getting the updated swing input, inserting it into the database, and
    redirecting to the read_swings page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary swing data for display and update inputs
        read_query = "SELECT * FROM swings WHERE swing_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()

        # Get necessary player data for dropdown
        p_query = "SELECT player_id, player_name FROM players;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=p_query
        )
        p_res = cursor.fetchall()

        # Get necessary round data for dropdown
        r_query = """
            SELECT rounds.round_id, courses.course_name, rounds.round_date 
            FROM rounds 
            INNER JOIN courses 
            ON courses.course_id = rounds.course_id;"""
        cursor = db.execute_query(
            db_connection=db_connection,
            query=r_query
        )
        r_res = cursor.fetchall()

        # Get necessary club data for dropdown
        c_query = "SELECT club_id, brand, club_name, club_type FROM clubs;"
        cursor = db.execute_query(
            db_connection=db_connection,
            query=c_query
        )
        c_res = cursor.fetchall()

        # Get necessary hole data for dropdown
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
        return render_template("update_swing.j2", gt_swing=results, gt_players=p_res, gt_rounds=r_res, gt_clubs=c_res, gt_holes=h_res)
    
    elif request.method == "POST":
        # Get updated swing data from form submission
        swing_id = id
        swing_player = int(request.form["player_id"])
        swing_round = int(request.form["round_id"])
        swing_hole = int(request.form["hole_id"])
        swing_club = int(request.form["club_id"])
        swing_dist = int(request.form["dist_traveled_yd"])

        insert_query = f"UPDATE swings SET player_id = {swing_player}, round_id = {swing_round}, hole_id = {swing_hole}, club_id = {swing_club}, dist_traveled_yd = {swing_dist} WHERE swing_id = {swing_id};"

        print(insert_query)
        db.execute_query(
            db_connection=db_connection,
            query=insert_query
        )
        return redirect("/swings")


# ----------------------------------------------------------------------------
# DELETE ROUTES: Delete Entity Handlers
#
# The following Flask route functions handle deleting data already in the Golf
# Tracker's MySQL Database. Each route connects to the database, collects the 
# selected entity's data from it, renders a delete_entity Jinja template that 
# displays the selected entity's current data, asks the user if they want to 
# delete the entity, and deletes the entity in the database on submission if 
# the user chose "Yes". Otherwise, redirects back to the entity's read page.
# ----------------------------------------------------------------------------

@app.route("/delete-club/<int:id>", methods=["POST", "GET"])
def delete_club(id):
    """Delete club Page

    If request method is GET from any read_clubs page delete buttons, route
    handles rendering a delete_club page with the data of the club being 
    deleted, an "are you sure" title, and a form with "Yes" or "No" options.

    If request method is POST from a delete_club page submit, route handles
    getting the yes or no input and club_id to delete, deleting the club from
    the database, and redirecting to the read_clubs page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary club data for display
        read_query = "SELECT * FROM clubs WHERE club_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_club.j2", gt_club=results)
    
    elif request.method == "POST":
        # Get user's delete decision data from form submission
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
    """Delete player Page

    If request method is GET from any read_players page delete buttons, route
    handles rendering a delete_player page with the data of the player being 
    deleted, an "are you sure" title, and a form with "Yes" or "No" options.

    If request method is POST from a delete_player page submit, route handles
    getting the yes or no input and player_id to delete, deleting the player
    from the database, and redirecting to the read_players page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary player data for display
        read_query = "SELECT * FROM players WHERE player_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_player.j2", gt_player=results)
    
    elif request.method == "POST":
        # Get player data from form submission for deletion
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
    """Delete round Page

    If request method is GET from any read_rounds page delete buttons, route
    handles rendering a delete_round page with the data of the round being 
    deleted, an "are you sure" title, and a form with "Yes" or "No" options.

    If request method is POST from a delete_round page submit, route handles
    getting the yes or no input and round_id to delete, deleting the round
    from the database, and redirecting to the read_rounds page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary round data for display
        read_query = "SELECT * FROM rounds WHERE round_id = '%s';" % (id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_round.j2", gt_round=results)
    
    elif request.method == "POST":
        # Get round data from form submission for deletion
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
    """Delete swing Page

    If request method is GET from any read_swings page delete buttons, route
    handles rendering a delete_swing page with the data of the swing being 
    deleted, an "are you sure" title, and a form with "Yes" or "No" options.

    If request method is POST from a delete_swing page submit, route handles
    getting the yes or no input and swing_id to delete, deleting the swing
    from the database, and redirecting to the read_swings page.
    """
    
    db_connection = db.connect_to_database()
    swing_id = id

    if request.method == "GET":
        # Get necessary swing data for display
        read_query = "SELECT * FROM swings WHERE swing_id = '%s';" % (swing_id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_swing.j2", gt_swing=results)
    
    elif request.method == "POST":
        # Get swing data from form submission for deletion
        delete = request.form["delete"]
        if delete == "yes":
            delete_query = "DELETE FROM swings WHERE swing_id = %s;" % (swing_id)
            cursor = db.execute_query(db_connection=db_connection, query=delete_query)
        
        return redirect("/swings")


@app.route("/delete-player-club/<int:player_id>/<int:club_id>", strict_slashes=False, methods=["POST", "GET"])
def delete_player_club(player_id, club_id):
    """Delete player_club Page

    If request method is GET from any read_player_clubs page delete buttons,
    route handles rendering a delete_player_club page with the data of the
    player_club being deleted, an "are you sure" title, and a form with "Yes"
    or "No" options.

    If request method is POST from a delete_player_club page submit, route
    handles getting the yes or no input and id's necessary to delete the
    player_club, deleting the player_club from the database, and redirecting
    to the read_player_clubs page.
    """
    db_connection = db.connect_to_database()

    if request.method == "GET":
        # Get necessary player_club data for display
        read_query = "SELECT * FROM player_clubs WHERE player_id = %s and club_id = %s;" % (player_id, club_id)
        cursor = db.execute_query(db_connection=db_connection, query=read_query)
        results = cursor.fetchall()
        return render_template("delete_player_club.j2", gt_clubs=results)
    
    elif request.method == "POST":
        # Get player_club data from form submission for deletion
        delete = request.form["delete"]

        if delete == "yes":
            delete_query = "DELETE FROM player_clubs WHERE player_id = %s and club_id = %s;"
            cursor = db.execute_query(db_connection=db_connection, query=delete_query, query_params=(player_id, club_id))
        
        return redirect("/player-clubs")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 15432))
    app.run(port=port, debug=True)

-- Golf Tracker Data Manipulation Query
-- {brackets} indicate variable that would be adjusted by other programming language

-----------------
--- SELECTs
-----------------
-- Pulls all clubs from the clubs table - used for /clubs route
SELECT *
FROM clubs;

-- Pulls all courses from the courses table- used for /courses route
SELECT *
FROM courses;

-- Pulls all holes from the holes table, adds information from related courses - for /holes route
SELECT holes.hole_id
	,holes.course_id
	,courses.course_name
	,holes.hole_number
	,holes.par_swing_count
	,holes.distance
FROM holes
INNER JOIN courses ON holes.course_id = courses.course_id;

-- Pulls all player-to-club relationships in the player_clubs table - for /player-clubs route
SELECT player_clubs.player_id
	,players.player_name
	,player_clubs.club_id
	,CONCAT (
		clubs.brand
		,' '
		,clubs.club_name
		,' '
		,clubs.club_type
		) AS club
FROM player_clubs
INNER JOIN players ON player_clubs.player_id = players.player_id
INNER JOIN clubs ON player_clubs.club_id = clubs.club_id;

-- Pulls all holes from the holes table - for /players route
SELECT *
FROM players;

-- Pulls all rounds from the rounds table, adds information from related tables (coureses, players) - for /rounds route
SELECT rounds.round_id
	,rounds.course_id
	,courses.course_name
	,rounds.player_id
	,players.player_name
	,rounds.round_date
	,rounds.round_score
FROM rounds
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON rounds.player_id = players.player_id;

-- Pulls all swings from the swings table, adds information from related tables (holes, rounds, courses, players) - for /rounds route
SELECT swings.swing_id
	,swings.dist_traveled_yd
	,swings.hole_id
	,courses.course_name
	,holes.hole_number
	,swings.round_id
	,rounds.round_date
	,swings.player_id
	,players.player_name
	,swings.club_id
	,CONCAT (
		clubs.brand
		," "
		,clubs.club_name
		," "
		,clubs.club_type
		) AS club
FROM swings
INNER JOIN holes ON swings.hole_id = holes.hole_id
INNER JOIN rounds ON swings.round_id = rounds.round_id
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON swings.player_id = players.player_id
LEFT JOIN clubs ON swings.club_id = clubs.club_id

-- Pulls all players with name like the input - used for searching for player by name - for /player-clubs/search route
SELECT player_clubs.player_id
	,players.player_name
	,player_clubs.club_id
	,CONCAT (
		clubs.brand
		,' '
		,clubs.club_name
		,' '
		,clubs.club_type
		) AS club
FROM player_clubs
INNER JOIN players ON player_clubs.player_id = players.player_id
INNER JOIN clubs ON player_clubs.club_id = clubs.club_id
WHERE players.player_name LIKE '%{player_name}%'

-- Select check used to prevent attempting to insert duplicate rows into clubs  - for /insert-club route (POST)
SELECT brand
	,club_name
	,club_type
FROM clubs
WHERE brand = {brand}
	AND club_name = {club_name}
	AND club_type = {club_type} LIMIT 1;

-- Pulls all course information for insert hole form - for /insert-hole route
SELECT *
FROM courses;

-- Pulls specific columns from the players table to be used for inserting a new player-club relationship - for /insert-player-club route
SELECT player_id
	,player_name
FROM players;

-- Pulls specific columns from the clubs table to be used for inserting a new player-club relationship - for /insert-player-club route
SELECT club_id
	,brand
	,club_name
	,club_type
FROM clubs;

-- Select check used to prevent attempting to insert duplicate rows into the player_clubs table  - for /insert-player-club route
SELECT player_id
	,club_id
FROM player_clubs
WHERE player_id = {player_id}
	AND club_id = {club_id} LIMIT 1;

-- Pulls specific columns from the players table to be used for inserting a round into the rounds table - for /insert-round route
SELECT player_id
	,player_name
FROM players;

-- Pulls specific columns from the courses table to be used for inserting a round into the rounds table - for /insert-round route
SELECT course_id
	,course_name
FROM courses;

-- Pulls specific columns from the players table to be used for inserting a swing into the swings table - for /insert-swing route
SELECT player_id
	,player_name
FROM players;

-- Pulls specific columns from the rounds and coureses table to be used for inserting a swing into the swings table - for /insert-swing route
SELECT rounds.round_id
	,courses.course_name
	,rounds.round_date
FROM rounds
INNER JOIN courses ON courses.course_id = rounds.course_id;

-- Pulls specific columns from the clubs table to be used for inserting a swing into the swings table - for /insert-swing route
SELECT club_id
	,brand
	,club_name
	,club_type
FROM clubs;

-- Pulls specific columns from the holes and coureses table to be used for inserting a swing into the swings table - for /insert-swing route
SELECT course_name
	,hole_id
FROM holes
INNER JOIN courses ON courses.course_id = holes.course_id;

-- Pulls data for specific player using player id to be used for updating players table- for /update-player route
SELECT *
FROM players
WHERE player_id = {player_id};

-- Pulls data from rounds, courses, and player for displaying in update form - for /update-round route
SELECT rounds.round_id
	,rounds.course_id
	,courses.course_name
	,rounds.player_id
	,players.player_name
	,rounds.round_date
	,rounds.round_score
FROM rounds
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON rounds.player_id = players.player_id
WHERE round_id = {round_id};

-- Pulls specific columns from players for players dropdown in update rounds form - for /update-round route
SELECT player_id
	,player_name
FROM players;

-- Pulls specific columns from courses for courses dropdown in update rounds form - for /update-round route
SELECT course_id
	,course_name
FROM courses;

-- Pulls relevant data for a specific swing - for displaying in update form - for /update-swing route
SELECT swings.swing_id
	,swings.dist_traveled_yd
	,swings.hole_id
	,courses.course_name
	,holes.hole_number
	,swings.round_id
	,rounds.round_date
	,swings.player_id
	,players.player_name
	,swings.club_id
	,CONCAT (
		clubs.brand
		," "
		,clubs.club_name
		," "
		,clubs.club_type
		) AS club
FROM swings
INNER JOIN holes ON swings.hole_id = holes.hole_id
INNER JOIN rounds ON swings.round_id = rounds.round_id
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON swings.player_id = players.player_id
LEFT JOIN clubs ON swings.club_id = clubs.club_id
WHERE swings.swing_id = {swing_id};

-- Pulls specific columns from players for players dropdown in update swings form - for /update-swings route
SELECT player_id
	,player_name
FROM players;

-- Pulls specific columns from rounds and courses for dropdown in update swings form - for /update-swings route
SELECT rounds.round_id
	,courses.course_name
	,rounds.round_date
FROM rounds
INNER JOIN courses ON courses.course_id = rounds.course_id;

-- Pulls specific columns from courses and holes for dropdown in update swings form - for /update-swings route
SELECT course_name
	,hole_id
FROM holes
INNER JOIN courses ON courses.course_id = holes.course_id;

-- Pulls a specific club to show which club might get deleted by delete form - for /delete-club route
SELECT *
FROM clubs
WHERE club_id = {club_id}

-- Pulls a specific player to show which player might get deleted by delete form - for /delete-player route
SELECT *
FROM players
WHERE player_id = {player_id};

-- Pulls a specific round and (related data from courses and player) that will be deleted by delete form - for /delete-round route
SELECT rounds.round_id
	,rounds.course_id
	,courses.course_name
	,rounds.player_id
	,players.player_name
	,rounds.round_date
	,rounds.round_score
FROM rounds
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON rounds.player_id = players.player_id
WHERE round_id = {round_id};

-- Pulls a specific swing and (related data from holes, rounds, coureses, players, and clubs) that will be deleted by delete form - for /delete-swing route
SELECT swings.swing_id
	,swings.dist_traveled_yd
	,swings.hole_id
	,courses.course_name
	,holes.hole_number
	,swings.round_id
	,rounds.round_date
	,swings.player_id
	,players.player_name
	,swings.club_id
	,CONCAT (
		clubs.brand
		," "
		,clubs.club_name
		," "
		,clubs.club_type
		) AS club
FROM swings
INNER JOIN holes ON swings.hole_id = holes.hole_id
INNER JOIN rounds ON swings.round_id = rounds.round_id
INNER JOIN courses ON rounds.course_id = courses.course_id
INNER JOIN players ON swings.player_id = players.player_id
LEFT JOIN clubs ON swings.club_id = clubs.club_id
WHERE swings.swing_id = {swing_id};

-- Pulls a specific player_club relationship row and (related data from players and clubs) that will be deleted by delete form - for /delete-player-club route
SELECT player_clubs.player_id
	,players.player_name
	,player_clubs.club_id
	,CONCAT (
		clubs.brand
		,' '
		,clubs.club_name
		,' '
		,clubs.club_type
		) AS club
FROM player_clubs
INNER JOIN players ON player_clubs.player_id = players.player_id
INNER JOIN clubs ON player_clubs.club_id = clubs.club_id
WHERE players.player_id = {player_id}
	AND clubs.club_id = {club_id};

-----------------
--- INSERTs
-----------------
-- Inserts new club into clubs table  - for /insert-club route (POST)
INSERT INTO clubs (
	brand
	,club_name
	,club_type
	)
VALUES (
	{brand}
	,{club_name}
	,{club_type}
	);

-- Inserts new course into the courses table  - for /insert-course route (POST)
INSERT INTO courses (
	course_name
	,course_state
	)
VALUES (
	{course_name}
	,{course_state}
	);

-- Inserts new hole into the holes table  - for /insert-hole route (POST)
INSERT INTO holes (
	course_id
	,hole_number
	,par_swing_count
	,distance
	)
VALUES (
	{course_id}
	,{hole_number}
	,{par_swing_count}
	,{distance}
	);

-- Inserts new player-club relationship row into the player_clubs table  - for /insert-player-club route (POST)
INSERT INTO player_clubs (
	player_id
	,club_id
	)
VALUES (
	{player_id}
	,{club_id}
	);

-- Inserts new player into the players table  - for /insert-player route (POST)
INSERT INTO players (
	player_name
	,player_city
	,player_state
	)
VALUES (
	{player_name}
	,{player_city}
	,{player_state}
	);

-- Inserts new round into the rounds table  - for /insert-round route (POST)
INSERT INTO rounds (
	course_id
	,player_id
	,round_date
	,round_score
	)
VALUES (
	{course_id}
	,{player_id}
	,{round_date}
	,{round_score}
	);

-- Inserts new swing into the swings table  - for /insert-swing route (POST)
INSERT INTO swings (
	player_id
	,round_id
	,hole_id
	,club_id
	,dist_traveled_yd
	)
VALUES (
	{swing_player}
	,{swing_round}
	,{swing_hole}
	,{swing_club}
	,{swing_dist}
	);

-----------------
--- UPDATES
-----------------
-- Updates specific player based on player id - for /update-players route (POST)
UPDATE players
SET players.player_name = {player_name}
	,players.player_city = {player_city}
	,players.player_state = {player_state}
WHERE players.player_id = {player_id};

-- Updates specific round based on round id - for /update-rounds route (POST)
UPDATE rounds
SET rounds.course_id = {course_id}
	,rounds.player_id = {player_id}
	,rounds.round_date = {round_date}
	,rounds.round_score = {round_score}
WHERE rounds.round_id = {round_id};

-- Updates specific swing based on swing id - for /update-swing route (POST)
UPDATE swings
SET player_id = {swing_player}
	,round_id = {swing_round}
	,hole_id = {swing_hole}
	,club_id = {swing_club}
	,dist_traveled_yd = {swing_dist}
WHERE swing_id = {swing_id};

-----------------
--- DELETES
-----------------
-- Deletes specific club from clubs using club_id - for /delete-club route (POST)
DELETE
FROM clubs
WHERE club_id = {club_id}

-- Deletes specific player from players using player_id - for /delete-player route (POST)
DELETE
FROM players
WHERE player_id = {player_id};

-- Deletes specific round from rounds using round_id - for /delete-round route (POST)
DELETE
FROM rounds
WHERE round_id = {round_id}

-- Deletes specific swing from swings using swing_id - for /delete-swing route (POST)
DELETE
FROM swings
WHERE swing_id = {swing_id};

-- Deletes specific player_club relationship row from player_clubs using player_id and club_id - for /delete-player-clubs route (POST)
DELETE
FROM player_clubs
WHERE player_id = {player_id}
	AND club_id = {club_id};


-----------------
--- RESET Button
-----------------
-- Code for the "reset all data" button is available at database/golf-tracker-reset.sql
-- The SQL is very similar to the DDQ, except all comments were remove so that it could be parsed easily by the app.
-- Truncates were added at the top of the reset file to clear out old data.
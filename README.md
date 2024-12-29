<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="https://www.linkedin.com/in/lubrano-alexander">
      <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin" alt="linkedin link" />
    </a>
    <a href="https://lubranoa.github.io">
      <img src="https://img.shields.io/badge/Personal_Site-47b51b?style=for-the-badge" alt="personal website link" />
    </a>
    <a href="https://github.com/lubranoa">
      <img src="https://img.shields.io/badge/GitHub-8A2BE2?style=for-the-badge&logo=github" alt="github profile link" />
    </a>
  </p>
  <br />
  <!-- Titles and Subtitles -->
  <h1 align="center">Golf Tracking Database Administration Web App</h1>
  <p align="center">
    <b>A Database Administrator's Flask Web Application for Managing Golf Data on a Cloud-hosted MySQL Relational Database</b>
  </p>
  <p align="center">
    By Conner Marchell and Alexander Lubrano
  </p>
  <p align="center">
    Summer 2022 · <a href="https://ecampus.oregonstate.edu/soc/ecatalog/ecoursedetail.htm?subject=CS&coursenumber=340&termcode=ALL">CS 340 Introduction to Databases</a> · Oregon State University
  </p>
  <br />
</div>

<!-- Table of Contents -->
<details>
  <summary>Table of Contents</summary>
    
  - [Project Description](#project-description)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Usage](#usage)
    - [Database Layout](#database-layout)
    - [Simple Admin Website](#simple-administrator-website)
  - [Skills Applied](#skills-applied)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

</details>

<!-- Project Description -->
## Project Description

This project is a web-based Golf Tracking application designed for Database Administrators to manage and interact with a cloud-hosted MySQL relational database containing golf-related data. Developed over one academic term, the application underwent multiple iterations, incorporating peer and instructor feedback to refine database modeling, SQL queries, client and server-side code, and the user interface and experience. <ins>Note</ins>: As per assignment specifications, the application does not implement RESTful practices or user authentication features, as it is intended solely for administrative use. The primary objective of this project is to offer Database Administrators an intuitive web interface for efficient data management.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Technologies Used -->
## Technologies Used

  - Backend:
    - [![python][python]][python-url]
    - [![flask][flask]][flask-url]
  - Frontend:
    - [![jinja][jinja]][jinja-url]
    - [![css][css]][css-url]
  - Database:
    - [![mysql-cli][mysql-cli]][mysql-cli-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Features -->
## Features

Golf Tracker offers an array of features for a Database Admin to interact with the Golf Tracker's database:

  - Provides comprehensive CRUD operations for managing golf-related data.

  - Offers a user-friendly web interface with dynamic dropdown menus and pre-filled update forms.

  - Ensures data integrity through user input validation and relational dependency handling.

  - Enables search functionality within the player-club association table.

  - Includes SQL scripts for database schema creation and data manipulation.
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage

This application was deployed on Oregon State's own servers and used a cloud-hosted MySQL database for data persistence. I do not have access to those servers or the database anymore so this project will not run anymore in its current form. To see the old setup steps, check out the [STARTUP-README](/STARTUP-README.md), which is the old version and contains how we set up the project using our school systems.

### Database Layout

This relational database has seven different tables of entities that it stores, including one intersection table of the single Many-to-Many relationship in the database. Each entity has its own unique (per-table) ID number along with other notable attributes and any relationships it has with other entities.

  - `courses` Entity
    - Stores golf courses with a name and a US state location.
    - Deletions cascade to delete rounds.

  - `holes` Entity
    - Stores holes of a golf course with a hole number, par swing count, hole distance, and the course it's part of (uses course ID number). Dependent on `courses`.

  - `clubs` Entity
    - Stores golf clubs with a brand name, club name, and a club type. These are not directly tied to players inside the `clubs` table due to the many-to-many relationship needing an intersection table to hold the relationships.
    - Deletions cascade to delete player-club relationships and removes the club from any `swings` they were used for.
    
  - `players` Entity
    - Stores players with a name, a city, and a US state.
    - Deletions cascade to delete rounds and player-club relationships.

  - `player_clubs` Entity
    - Stores the relationships of players and the clubs they own. These are many-to-many relationships because a player can own multiple clubs and a single club can be owned by multiple players.
    
  - `rounds` Entity
    - Stores players' rounds of golf with a date, the score, the player whose round it is, and which course it was on. Dependent on `courses` and `players`.
    - Deletions cascade to delete swings.

  - `swings` Entity
    - Stores players' swings taken with a distance traveled, the club used, the player who swung, the hole it was done on, and the round in which it occurred. Dependent on `clubs`, `players,`, `rounds`, and `holes`.

For detailed specifics on the database's design, take a look at its [ERD](/screenshots/340-ERD.png), [schema](/screenshots/340-schema.png), and the *Database Outline* section of the [project document](/docs/Group%2066%20Step%205%20Final.pdf).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Simple Administrator Website

When the application was still deployed and functional, the website was accessible through a URL to the deployed application on the OSU servers along with our choice of a port number, something like `http://flipX.engr.oregonstate.edu:15432`. There were no login requirements laid out by the assignment specifications. The following are some of the highlights of the Golf Tracker's admin website. Take a look at the [Project Document](/docs/Group%2066%20Step%205%20Final.pdf) for more. 

  - Home Page
    - A simple web page that contains links to each table in the Golf Tracker database. It also has a button to reset the data in the database back to its original state for when peers and staff wanted to reset after testing.

      ![Screenshot of the home page of the Golf Tracker website with links to all the tables in the database and a reset database button](/screenshots/340-home-page.png)

  - View/Read a Single Table
    - Each database table has its own "View" page that displays all entries in the table. For example, below you can see the `players` table, which displays all the data in the table along with an insert button at the bottom and edit and delete buttons for each entry.

      ![Screenshot of the players table web page that contains each player's information in the Golf Tracker DB along with create, edit, and delete buttons.](/screenshots/340-player-table.png)

  - Insert/Create an Entry
    - At the bottom of tables on any "View" pages, there is a blue "+" button that takes the admin to another page titled "Insert `entity` Entry". These pages have all necessary input fields for each entity in the database. 
    - All text input is validated by the pages and must be correct before submission. The selections of some dropdowns are dynamically populated with database data, such as in the screenshot below where the "Course Name" and "Player Name" dropdowns will only contain choices of courses and players already in the database.

      ![Screenshot of the insert round entry page that has the necessary input fields for a round entry and an insert round button.](/screenshots/340-insert-round.png)

  - Edit/Update an Entry
    - Most of the tables on "View" pages have update buttons in the tables next to each entry, which navigates the admin to another page titled "Update `entity` Entry". Only some of the entities in the application are allowed to be edited, which was a design choice to fulfill assignment requirements.
    - These "Update" web pages show the entry being updated in a table and have the same validating and dynamically populated inputs as "Insert" pages. The input fields are pre-populated with the entry's current data.

      ![Screenshot of an update swing entry page that has all of the swing's information displayed in a table, has the necessary input fields for a swing that are pre-populated with all of the swing's current data, and has an update swing button.](/screenshots/340-update-swing.png)
  
  - Delete an Entry
    - Most of the tables on "View" pages also have delete buttons for each entry in the table. This navigates the admin to a page of the application confirming whether or not they want to delete the entry.
    - On submit, the entry will be deleted along with any cascading deletions that need to be carried out by the database's `CASCADE` rules.

      ![Screenshot of an entry deletion confirmation page that asks if the user is sure if they want to delete an entry and has radio buttons for yes and no and a submit button.](/screenshots/340-delete-player.png)

  - View and Search Intersection Table of M:M Relationship
    - This intersection table shows which player owns what clubs in the database. This relationship is many-to-many since a player can own multiple clubs and a club can be owned by multiple players, as described in the [Database Layout section](#database-layout).
    - This web page also has the functionality to search for relationships by player. For a screenshot of how that looks, take a look at this [screenshot of a search](/screenshots/340-player-club-search.png) when the admin searches for "Happy".

      ![Screenshot of the player-clubs intersection table that shows which players own what clubs with delete buttons next to each entry, an insert button at the bottom of the table, and a search bar below the table for the user to search for relationships by player](/screenshots/340-player-club-table.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

The term-long development of the Golf Tracker project involved the application of a wide range of skills and technologies, making it a comprehensive learning experience. The key skills utilized in the project include:

  - Relational database design and schema/ERD creation

  - Python-based web application development with Flask

  - Front-end development using Jinja, HTML, and CSS

  - Creating CRUD operations for various entities
  
  - Handling user input and form submissions

  - Data validation and consistency

  - Data relationship management

  - User interface design and user experience improvements

These skills were applied collaboratively to create Golf Tracker. The project not only demonstrates proficiency in web development and database management but also showcases the ability to transform a conceptual idea into a fully functional web application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact

Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Conner Marchell - [GitHub][conner-github-url]

Project Link: [https://github.com/lubranoa/CS340-Golf-Tracker-DB][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Acknowledgments -->
## Acknowledgments

- [Jinja 2.11.x Template Designer Documentation][jinja-url]
- [Flask Documentation][flask-url]
- [MySQL CLI Documentation][mysql-cli-url]
- [Diagrams.net (formerly Draw.io)][drawio-url]
- [Shields.io][shields-url]
- [Simple Icons][icons-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[python-url]: https://www.python.org/

[flask]: https://img.shields.io/badge/Flask-grey?style=for-the-badge&logo=flask
[flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[dotenv]: https://img.shields.io/badge/Dotenv-grey?style=for-the-badge&logo=dotenv&logoColor=ecd53f
[dotenv-url]: https://pypi.org/project/python-dotenv/

[mysql-cli]: https://img.shields.io/badge/MySQL_CLI_Client-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[mysql-cli-url]: https://dev.mysql.com/doc/refman/8.0/en/mysql.html

[phpmyadmin]: https://img.shields.io/badge/phpMyAdmin-6C78AF?style=for-the-badge&logo=phpmyadmin&logoColor=white
[phpmyadmin-url]: https://www.phpmyadmin.net/

[gunicorn]: https://img.shields.io/badge/Gunicorn-grey?style=for-the-badge&logo=gunicorn
[gunicorn-url]: https://gunicorn.org/

[jinja]: https://shields.io/badge/Jinja2_Templates-B41717?style=for-the-badge&logo=jinja
[jinja-url]:https://jinja.palletsprojects.com/en/2.11.x/templates/

[css]: https://shields.io/badge/CSS-grey?style=for-the-badge&logo=css3&logoColor=1572B6
[css-url]: https://www.w3.org/Style/CSS/

[email]: mailto:lubrano.alexander@gmail.com
[linkedin-url]: https://www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/CS340-Golf-Tracker-DB
[conner-github-url]: https://github.com/CMarchell

[shields-url]: https://shields.io/
[icons-url]: https://simpleicons.org/
[drawio-url]: https://app.diagrams.net/
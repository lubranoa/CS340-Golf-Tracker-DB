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

This application was previously deployed on Oregon State University's servers, utilizing a cloud-hosted MySQL database for data persistence. As access to these servers and the database is no longer available, the application is currently non-operational in its existing form.

For detailed setup instructions used during the initial deployment, please refer to the [STARTUP-README](https://github.com/lubranoa/CS340-Golf-Tracker-DB/blob/main/STARTUP-README.md), which outlines the procedures followed using the university's systems.

To run this application locally, you would need to set up a compatible environment, including a local MySQL database and a Flask server. Please note that modifications to the configuration files may be necessary to accommodate a local setup.

### Database Layout

The Golf Tracker database uses a relational model to manage golf-related data. Below is an overview of its entities, attributes, and relationships:

#### Entities and Attributes

| Entity       | Attributes                                                                 | Description                                  |
|--------------|-----------------------------------------------------------------------------|----------------------------------------------|
| **Players**  | `player_id` (PK), `player_name`, `player_city`, `player_state`             | Stores details of registered players.        |
| **Clubs**    | `club_id` (PK), `brand`, `club_name`, `club_type`                          | Records details about available golf clubs.  |
| **Courses**  | `course_id` (PK), `course_name`, `course_state`                            | Tracks information about golf courses.       |
| **Rounds**   | `round_id` (PK), `player_id` (FK), `course_id` (FK), `round_score`         | Records individual rounds of golf.          |
| **Swings**   | `swing_id` (PK), `round_id` (FK), `hole_id` (FK), `club_id` (FK)           | Tracks each swing during a round of golf.    |
| **Holes**    | `hole_id` (PK), `course_id` (FK), `hole_number`, `par_swing_count`, `distance` | Stores details about individual holes.      |
| **Player-Clubs** | `player_id` (FK), `club_id` (FK)                                       | Manages the many-to-many relationship between players and clubs. |

#### Relationships

- **Players and Rounds:** One player can participate in many rounds (`1:M`).

- **Rounds and Swings:** Each round consists of multiple swings (`1:M`).

- **Players and Clubs:** Players can own multiple clubs, and each club can belong to multiple players (`M:M`).

- **Courses and Holes:** Each course consists of multiple holes (`1:M`).

For detailed specifics on the database's design, take a look at its [ERD](/screenshots/340-ERD.png), [schema](/screenshots/340-schema.png), and the *Database Outline* section of the [project document](/docs/Group%2066%20Step%205%20Final.pdf).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Web-Based Administration Interface

This interface was designed to facilitate efficient database management through the following key workflows:

#### Access the Home Page
- Provides an overview of the database with navigation links to all entities.
- Displays summary statistics, such as the total number of players, clubs, and rounds.

  ![Screenshot of the home page of the Golf Tracker website with links to all the tables in the database and a reset database button](/screenshots/340-home-page.png)

#### View Records in a Table
- Allows administrators to browse entity data (e.g., players, courses) in a clean, tabular format.
- Includes sortable columns and pagination for improved data exploration.

  ![Screenshot of the players table web page that contains each player's information in the Golf Tracker DB along with create, edit, and delete buttons.](/screenshots/340-player-table.png)

#### Add a New Entry
- Supports the creation of new records for all entities (e.g., players, clubs).
- Includes dynamic dropdown menus to ensure accurate foreign key selection.

  ![Screenshot of the insert round entry page that has the necessary input fields for a round entry and an insert round button.](/screenshots/340-insert-round.png)

#### Update Existing Records
- Offers pre-filled forms for quick editing of existing records.
- Automatically validates input to maintain data consistency.

  ![Screenshot of an update swing entry page that has all of the swing's information displayed in a table, has the necessary input fields for a swing that are pre-populated with all of the swing's current data, and has an update swing button.](/screenshots/340-update-swing.png)

#### Delete a Record
- Enables safe record deletion with confirmation prompts to avoid errors.
- Manages relational dependencies to ensure database integrity.

  ![Screenshot of an entry deletion confirmation page that asks if the user is sure if they want to delete an entry and has radio buttons for yes and no and a submit button.](/screenshots/340-delete-player.png)

#### Search Many-to-Many Relationships
- Provides a searchable interface for viewing and managing relationships, such as players and their associated clubs.
- Supports rapid filtering to locate specific records efficiently.

  ![Screenshot of the player-clubs intersection table that shows which players own what clubs with delete buttons next to each entry, an insert button at the bottom of the table, and a search bar below the table for the user to search for relationships by player](/screenshots/340-player-club-table.png)

This design highlights an emphasis on usability and functionality, ensuring that database administrators can perform key operations seamlessly.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied

- Designed and implemented a normalized relational database schema to support CRUD operations and complex queries.

- Utilized MySQL to manage persistent data storage and enforce data integrity through primary and foreign key constraints.

- Developed a Flask-based backend to handle routing and server-side logic for the web application.

- Created dynamic and responsive user interfaces using Jinja templates, HTML, and CSS.

- Incorporated user-friendly features such as pre-filled forms, dropdown menus, and search functionality for many-to-many relationships.

- Iteratively designed, tested, and refined database and application components based on peer and instructor feedback.

- Conducted detailed testing of SQL queries to optimize performance and ensure reliable data manipulation.

- Gained hands-on experience with debugging relational dependency issues and ensuring safe data deletions.

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
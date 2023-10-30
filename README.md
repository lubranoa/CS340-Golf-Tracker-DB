<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- Centered title section with descriptive lines -->
<div align="center">
  <!-- Badges -->
  <p>
    <a href="www.linkedin.com/in/lubrano-alexander">
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
  <h1 align="center">Golf Tracker Database</h1>
  <p align="center">
    <b>A Database Administrator's Flask Web Application for Managing Golf Data on a Cloud-hosted MySQL Database</b>
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
  - [Skills Applied](#skills-applied)
    - [Skill 1](#skill-1)
    - [Skill 2](#skill-2)
  - [Acknowledgements](#acknowledgements)

</details>

<!-- Project Description -->
## Project Description
This project is a Golf Tracking application that provides a web-based user interface (UI) for a Database Administrator to interact with a cloud-hosted MySQL database of golf data. It is the culmination of an entire term's worth of effort to deploy this database administration application using a development process involving multiple iterative steps of designing, developing, and implementing peer and staff feedback on our database modeling and diagrams, SQL queries, client and server-side code, and UI/UX of the web application.

**Note:** The assignment specifications did not require the use of RESTful practices in the application. The specifications also stated that this would *not* be a customer facing application, thus there was no need for login pages, sessions, registering users, etc. The main purpose of the project was to provide the primary user, a Database Admin, with a web interface for data tables.

<!-- Technologies Used -->
## Technologies Used
  - Backend:
    - [![python][python]][python-url]
    - [![flask][flask]][flask-url]
    - [![mysql][mysql]][mysql-url]
    - [![dotenv][dotenv]][dotenv-url]
  - Frontend:
    - [![jinja][jinja]][jinja-url]
    - [![gunicorn][gunicorn]][gunicorn-url]
    - [![css][css]][css-url]

<!-- Features -->
## Features
Golf Tracker offers an array of features for a Database Admin to interact with the Golf Tracker's database.
  - **Data Management**: Provides requisite create, read, update, and delete (CRUD) operations for the admin to manage the golf data in the database.
  - **Easy-to-use, Simple UI**: Implemented as a simple website, the UI is easy to use and navigate and does not have extensive styling.
  - **Website Functionality**: The website allows the admin to easily view each table in the database and to easily perform insertions, updates, and deletions on the data in those tables.
  - **Input Validation**: Validates any data input on create and update operations' pages before submission via required inputs and regular expressions (RegEx).
  - **Search Many-to-Many Relationships**: Allows the admin to search the Players-Clubs intersection table for certain relationships between players and the clubs they own.
  - **Resolves Relationship Dependencies**: Resolves relationship issues that arise via editing or deleting an entity by properly updating any of its dependent entities.
  - **Data Definition Queries** (DDQ): [SQL file](/database/golf-tracker-DDQ.sql) that can be used to create the database schema and populate it with data.
  - **Data Manipulation Queries** (DMQ): [SQL file](/database/golf-tracker-DDQ.sql) that contains all of the data manipulation queries used when the application communicates with the database.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Usage -->
## Usage
This application was deployed on Oregon State's own servers and used a cloud-hosted MySQL database for data persistence. I do not have access to those servers or the database anymore so this project will not run anymore in its current form. To see the old setup steps, check out the [STARTUP-README](/STARTUP-README.md), which is the old version and contains how we set up the project using our school systems.

When the application was still deployed and functional, the website was accessible through a URL to the deployed application on the OSU servers with our choice of a port number. There were no login requirements laid out by the assignment specifications. The following are some of the pages that could be seen on the website.

  - Home Page

TODO:
  - Add homepage screenshot and description
  - Add a view entity screenshot and description
  - Add a create entity screenshot and description
  - Add a update entity screenshot and description
  - Add a delete entity screenshot and description
  - Add a player-clubs entity and description

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Skills Applied -->
## Skills Applied
#### Skill 1:
  - description
#### Skill 2:
  - description

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contact -->
## Contact
Alexander Lubrano - [lubrano.alexander@gmail.com][email] - [LinkedIn][linkedin-url]

Project Link: [https://github.com/lubranoa/CS340-Golf-Tracker-DB][repo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgements

- OSU starter app linked in our course: [OSU Flask Starter App](https://github.com/osu-cs340-ecampus/flask-starter-app)
- OSU starter app repo references this repo sometimes: [CS340_starter_app](https://github.com/mlapresta/cs340_starter_app)
- [Jinja 2.11.x Template Designer Documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Markdown links -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffd343
[python-url]: https://www.python.org/

[flask]: https://img.shields.io/badge/Flask-grey?style=for-the-badge&logo=flask
[flask-url]: https://flask.palletsprojects.com/en/3.0.x/

[dotenv]: https://img.shields.io/badge/Dotenv-grey?style=for-the-badge&logo=dotenv&logoColor=ecd53f
[dotenv-url]: https://pypi.org/project/python-dotenv/

[mysql]: https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[mysql-url]: https://www.mysql.com/

[gunicorn]: https://img.shields.io/badge/Gunicorn-grey?style=for-the-badge&logo=gunicorn
[gunicorn-url]: https://gunicorn.org/

[jinja]: https://shields.io/badge/Jinja2_Templates-B41717?style=for-the-badge&logo=jinja
[jinja-url]:https://jinja.palletsprojects.com/en/2.11.x/templates/

[css]: https://shields.io/badge/CSS-grey?style=for-the-badge&logo=css3&logoColor=1572B6
[css-url]: https://www.w3.org/Style/CSS/

[shields-url]: https://shields.io/
[icons-url]: https://simpleicons.org/

[email]: mailto:lubrano.alexander@gmail.com
[linkedin-url]: www.linkedin.com/in/lubrano-alexander
[repo-url]: https://github.com/lubranoa/CS340-Golf-Tracker-DB

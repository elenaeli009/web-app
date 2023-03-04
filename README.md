# Flask application for Big Data Purification (Company names) and transferring data from a relational database (SQL lite) to a non-relational one (MongoDB)
### `The Flask application is written with Python language in Pycharm`
[![N|Solid](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuZNP8K1HFw-mHFkBoR5Xbx0BydDGu7ZzhwYRV4QjJvTrWrQcMKaFwrqa8UZ9J1vQ0mRk&usqp=CAU)](https://www.jetbrains.com/pycharm/download/#section=windows)[![N|Solid](https://www.python.org/static/img/python-logo.png)](https://www.python.org/downloads/)

Click on the pictures above to view the web page of the applications
### `For my Front-End web application, I used HTML, CSS, and Bootstrap`
### Very important for making this project
- Creating a new Git repository in which this project will work
- Writing a Python script (Flask application) with the appropriate API functions
- Testing the Flask application with local calls via localhost
- Viewing and exploring the data set (what names are there, what
contain in them etc.)
- Writing a Python script that will make calls to the Flask application and process the company names
- Cleaning company names
- Install python modules and test each part of the code while building the entire project
- Create an index HTML file at the root of the project to make a Front-End of the application
- You can use HTML, CSS, and Bootstrap for Front-End of the application
- ✨Functional flask app for Big Data Purification✨
### Important things to clear the company names

- Reading a company from a local SQLite database with GET
request through the Flask application
- Processing company names
me. 
- Purification of company names from unwanted characters
(commas and whole text after the commas, brackets, and the text inside them,
quotation marks, dash when it is not part of the company name, etc.)
- Cleaning up company names to be free of theirs
legal entity (LIMITED, LTD., ltd. Limited, limited, etc.)
- Normalization of the company name
- The name should only have initial capital letters, not all of them
large (eg VET LIFE SERVICES should be Vet Life Services)
- If acronyms are used in the company name, then the acronym
should be capitalized (eg AT&T should stay that way, not
At&t)
- Writing the result for the company in the Mongo database
by making a POST request, with the key being the purified name of
the company, and values the rest of the attributes

`The applications you need for successful application development`

| Application | Link |
| ------ | ------ |
| Pycharm | https://www.jetbrains.com/pycharm/download/#section=windows |
| MongoDB | https://www.mongodb.com/try/download/community |
| SQLite | https://sqlitebrowser.org/dl |
| GitHub | https://github.com |

| Programming language | Link |
| ------ | ------ |
| Python | https://www.python.org/downloads |

| Markup Language | Link |
| ------ | ------ |
| HTML | https://developer.mozilla.org/en-US/docs/Web/HTML |

| Stylesheet language | Link |
| ------ | ------ |
| CSS | https://developer.mozilla.org/en-US/docs/Web/CSS |

| Framework | Link |
| ------ | ------ |
| Bootstrap | https://getbootstrap.com/docs/5.0/getting-started/introduction |
| Flask  | https://flask.palletsprojects.com/en/2.2.x |
## Addition important information 

The following python modules are required to build the project:

| Python module | Link |
| ------ | ------ |
| Flask | https://pypi.org/project/Flask |
| sqlite3 | https://pypi.org/project/pysqlite3 |
| json | https://pypi.org/project/jsonlib |
| requests | https://pypi.org/project/requests |
| pymongo | https://pypi.org/project/pymongo |


```sh
Flask install --
pip install Flask
```
```sh
sqlite3 install --
pip install pysqlite3
```
```sh
json install --
pip install jsonlib
```
```sh
requests install --
pip install requests
```
```sh
pymongo install --
pip install pymongo
```


> `Or you can simply type in PyCharm `
- import Flask, 
- sqlite3,
- import json, 
- import requests, 
- import pymongo 
and place the mouse on the module name and choose Install package pymongo, Install package requests, etc.

> Below it's some links that I used for the project:

|Link to site| Link to content |
| ------ | ------ |
| https://www.geeksforgeeks.org | https://www.geeksforgeeks.org/how-to-execute-many-sqlite-statements-in-python |
| https://www.geeksforgeeks.org | https://www.geeksforgeeks.org/flask-app-routing |
| https://stackabuse.com | https://stackabuse.com/integrating-mongodb-with-flask-using-flask-pymongo |
| https://www.geeksforgeeks.org | https://www.geeksforgeeks.org/get-post-requests-using-python |
| https://www.educative.io | https://www.educative.io/answers/what-is-the-difference-between-jsonloads-and-jsondumps |
| https://stackoverflow.com | https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python |
| https://www.geeksforgeeks.org | https://www.geeksforgeeks.org/python-string-replace |
| https://www.geeksforgeeks.org | https://www.geeksforgeeks.org/python-string-methods |
| https://www.w3schools.com | https://www.w3schools.com/python/ref_string_split.asp |
| https://www.freecodecamp.org | https://www.freecodecamp.org/news/how-to-split-a-string-in-python |
| https://www.w3schools.com | https://www.w3schools.com/bootstrap/bootstrap_ref_css_tables.asp |
| https://learningactors.com | https://learningactors.com/how-to-use-bootstrap-with-flask |
| https://getbootstrap.com | https://getbootstrap.com/docs/4.1/content/tables |

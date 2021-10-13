This is a simple python blogging web application implementation using the Flask web server and Jinja templates. To run the server:

0. Get the code on your local machine.

``git clone <this-repo-url>``

cd to the code's base directory.

1. Install the poetry python dependency manager:

``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -``

2. Update poetry to the latest version.

``poetry self update``

3. Install dependencies:

``poetry install``


4. Set the Flask app environment variable:

``export FLASK_APP=src/blogapp/app.py``

5. Then run the server as follows:

``poetry run flask run``


6. Navigate to http://127.0.0.1:5000 on your browser and play with the application.

Simple Python project demostrating using data from a relational database to create a visualization. The [`master`](https://github.com/xofbd/sql-viz-project/tree/master) branch is the starting template and [`minimal-app`](https://github.com/xofbd/sql-viz-project/tree/minimal-app) is the branch that contains a minimal working Flask application.

To run, create a file in the project's root named `.env` based on the contents of `.env.template`. Make sure to fill in the database's URL. Afterwards, run:

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `source .env`
* `flask run`

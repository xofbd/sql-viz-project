Simple Python project demostrating using data from a relational database to create a visualization. The [`master`](https://github.com/xofbd/sql-viz-project/tree/master) branch is the starting template and [`minimal-app`](https://github.com/xofbd/sql-viz-project/tree/minimal-app) is the branch that contains a minimal working Flask application.

To run, create a file in the project's root named `.env` based on the contents of `.env.template`. Make sure to fill in the database's URL. Afterwards, run:

* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `source .env`
* `flask run`

Alternatively, there's a `Dockerfile`. You'll need to build the image and run a container:
1. `docker build -t sql-viz-app .`
1. `docker run --init --rm -d --publish 127.0.0.1:5000:5000 -e URL_DB=<URL-DB> sql-viz-app`

Make sure to replace `<URL-DB>` with the actual URL of the PostgreSQL database.

import os
import sqlite3
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from flask import redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
module_dir = os.path.dirname(os.path.abspath(__file__))


def get_db_connection():
    conn = sqlite3.connect(module_dir + '/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute(
        "SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    conn.close()
    return post


def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY created desc").fetchall()
    conn.close()
    return posts


@app.route("/")
def index():
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)


@app.route("/posts", methods=('GET', 'POST'))
def create_post():
    if request.method == 'GET':
        return render_template('create.html')
    title = request.form['title']
    content = request.form['content']
    if not title or len(title.strip()) <= 0:
        flash('Title is required!')
        return render_template('create.html')
    else:
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)", (
                title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

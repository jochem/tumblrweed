from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tumblrweed.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from tumblrweed.models import Post


@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    posts = Post.query.filter_by(state='published').order_by('-id').paginate(
        page, per_page=50)
    return render_template('index.html', posts=posts)


@app.route('/drafts/')
@app.route('/drafts/<int:page>')
def drafts(page=1):
    posts = Post.query.filter_by(state='draft').order_by('-id').paginate(
        page, per_page=50)
    return render_template('index.html', posts=posts)


@app.route('/queued/')
@app.route('/queued/<int:page>')
def queued(page=1):
    posts = Post.query.filter_by(state='queued').order_by('-id').paginate(
        page, per_page=50)
    return render_template('index.html', posts=posts)


@app.route('/videos/')
@app.route('/videos/<int:page>')
def videos(page=1):
    posts = Post.query.filter_by(type='video').order_by('-id').paginate(
        page, per_page=50)
    return render_template('index.html', posts=posts)


@app.route('/post/<id>/')
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)

from sqlalchemy.ext.hybrid import hybrid_property

from tumblrweed.app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Blog %r>' % self.name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    url_with_slug = db.Column(db.String)
    type = db.Column(db.String)
    date_gmt = db.Column(db.DateTime)
    date = db.Column(db.DateTime)
    unix_timestamp = db.Column(db.Integer)
    format = db.Column(db.String)
    reblog_key = db.Column(db.String)
    slug = db.Column(db.String)
    state = db.Column(db.String)
    is_reblog = db.Column(db.Boolean)
    tumblelog = db.Column(db.Integer, db.ForeignKey('blog.name'))
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    direct_video = db.Column(db.Boolean)
    bookmarklet = db.Column(db.Boolean)
    html = db.Column(db.Text)

    @hybrid_property
    def get_photos(self):
        return Photo.query.filter_by(post=self.id).group_by('hash')


class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Integer, db.ForeignKey('blog.id'))
    file = db.Column(db.String())
    hash = db.Column(db.String())

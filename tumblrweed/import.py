import hashlib
import logging
import os
import re
from datetime import datetime
from xml.dom import minidom

from tumblrweed.app import db
from tumblrweed.models import Photo, Post

""" config section """
root = '/Volumes/Home Directory/tumblr/'
""" / """

logging.warning("Creating database")
db.create_all()

logging.warning("Reading XML")
xmldoc = minidom.parse('posts.xml')
posts = xmldoc.getElementsByTagName('post')

logging.warning("Reading media")
media_list = os.listdir(os.path.join(root, 'media'))

for p in posts:
    post = {k.replace('-', '_'): v for k, v in p.attributes.items()}
    post['date'] = datetime.strptime(post['date'], '%a, %d %b %Y %H:%M:%S')
    post.pop('date_gmt')
    for b in ('is_reblog', 'direct_video', 'bookmarklet'):
        if b in post:
            post[b] = bool(post[b])
    with open(os.path.join(root, 'html/{}.html'.format(post['id'])),
              'r') as file:
        post['html'] = file.read()
    obj = Post(**post)
    print("Adding post {0.id}".format(obj))
    db.session.add(obj)
    if obj.type == 'photo':
        # match 123456789.jpg and 123456789_0.jpg
        regex = re.compile('{0.id}(|_\d+)\.\w+'.format(obj))
        for file in filter(regex.search, media_list):
            hash = hashlib.md5(open(os.path.join(
                root, 'media', file), 'rb').read()).hexdigest()
            photo_obj = Photo(post=obj.id, file=file, hash=hash)
            print("- Adding photo {0.file}".format(photo_obj))
            db.session.add(photo_obj)
    logging.info("Commit to db")
    db.session.commit()

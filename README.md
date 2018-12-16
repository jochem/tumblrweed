Tumblrweed
==========

Python tool to import your exported Tumblr blog to a local webinterface, so that you browse your archived blog. Built on Flask, sqlalchemy and sqlite.

Created on a rainy Sunday, so don't expect bells, whistles or harps.

Getting started
---------------

Make sure you have Python 3 and flask-sqlalchemy. You can used the provided [Pipenv](https://pipenv.readthedocs.io/en/latest/) files to automatically create a virtualenv, otherwise just manually create a virtualenv and install flask-sqlalchemy - that's all you need.

Step 1: [request an export](https://tumblr.zendesk.com/hc/en-us/articles/360005118894-Export-your-blog) of your Tumblr blog!
(This is the most critical step as time may be limited for what you want to get.)

Step 2: download the export and clone this repo. Now unzip your export and place posts.xml in the root of this project. Open `import.py` from the tumblrweed dir and change the variable `root` in the designated config section to point to the directory containing your unzipped export. Create a symlink named `static` in the tumblrweed directory that points to the `media` dir of your export.

Step 3: run the following command and wait for the import to complete:

    $ python -m tumblrweed.import


Step 4: start the Flask server and brose your blog!

    $ FLASK_APP=tumblrweed.app flask run

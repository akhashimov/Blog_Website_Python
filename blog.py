from flask import Flask , render_template
from content import *
wapp = Flask(__name__)

@wapp.route('/')
def entries():
    return render_template('index.html',entries=get_all_entries())
@wapp.route('/entry/<name>')
def entry(name):
    return render_template('entry.html',entry=get_entry(name))
if __name__ == "__main__":
    wapp.run()




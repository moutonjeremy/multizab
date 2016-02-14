from flask import Blueprint, render_template, request
from flask import redirect, url_for, flash
from flask import current_app
from multizab.gui.forms import HostForm

from slugify import slugify

import json

gui = Blueprint('gui', __name__, template_folder='templates')


@gui.route('/')
def index():
    return render_template('index.html')


@gui.route('/graphics')
def graphics():
    return render_template('graphs.html')


@gui.route('/config', methods=['POST', 'GET'])
def config():
    with open(current_app.config['DATABASE_FILE'], 'r') as f:
        json_file = json.load(f)
    form = HostForm()
    if request.method == 'POST':
        if slugify(form.name.data) not in json_file['hosts']:
            json_file['hosts'].append({'name': slugify(form.name.data),
                                       'uri': form.uri.data,
                                       'username': form.username.data,
                                       'password': form.password.data})
        with open(current_app.config['DATABASE_FILE'], 'w') as f:
            json.dump(json_file, f, indent=4)
        f.close()
        flash('Host added !!!')
        return redirect(url_for('gui.config'))
    return render_template('config.html', form=form, hosts=json_file['hosts'])


@gui.route('/config/delete/host/<host_id>')
def config_delete_host(host_id):
    with open(current_app.config['DATABASE_FILE'], 'r') as f:
        json_file = json.load(f)
    for i in json_file['hosts']:
        if host_id == i['name']:
            json_file['hosts'].pop(json_file['hosts'].index(i))
            with open(current_app.config['DATABASE_FILE'], 'w') as f:
                json.dump(json_file, f, indent=4)
            f.close()
            flash('Host deleted !!!')
            return redirect(url_for('gui.config'))
    flash('Invalid Host')
    return redirect(url_for('gui.config'))

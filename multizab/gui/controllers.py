from flask import Blueprint, render_template, request
from flask import redirect, url_for, flash
from forms import HostForm

from multizab.data.models import db, Zabbix

gui = Blueprint('gui', __name__, template_folder='templates')


@gui.route('/')
def index():
    """

    :return:
    """
    return render_template('index.html')


@gui.route('/config', methods=['POST', 'GET'])
def config():
    """

    :return:
    """
    form = HostForm()
    if request.method == 'POST':
        if Zabbix.query.filter(Zabbix.host == form.hostname.data).first():
            flash('Hostname already exist !!!')
        u = Zabbix(host=form.hostname.data,
                   username=form.username.data,
                   password=form.password.data)
        db.session.add(u)
        db.session.commit()
        flash('Host added !!!')
        return redirect(url_for('gui.config'))
    hosts = Zabbix.query.all()
    return render_template('config.html', form=form, hosts=hosts)

# multizab
[![Code Climate](https://codeclimate.com/github/Jeremmm/multizab/badges/gpa.svg)](https://codeclimate.com/github/Jeremmm/multizab)

![ScreenShot](https://github.com/Jeremmm/multizab/blob/master/multizab/static/img/multizab_screen.png)

![ScreenShot](https://github.com/Jeremmm/multizab/blob/master/multizab/static/img/multizab_screen_graphics.png)


## Update
### 18 Feb 2016
 - Add filter by priority

### 13 Feb 2016
 - Remove database (json file used now)
 - Logging if a zabbix backend is ko
 - python 3 compatibility
 - Graph (per trigger level/hosts/Zabbix)

## Requirements
 - ``flask``: web framework
 - ``flask-wtf``: flask plugin (WTForms)
 - ``flask-script``: flask plugin
 - ``gunicorn``: python wsgi
 - ``python-slugify``: A Python Slugify application that handles Unicode
 - ``requests``: HTTP Library

## Install
```bash
git clone git@github.com:Jeremmm/multizab.git
cd multizab
virtualenv env -p python2.7
env/bin/pip install -r requirements.txt
cp multizab\config-template.py multizab\config.py
env/bin/python manage.py runserver
```

## Usage with gunicorn
```bash
env/bin/gunicorn -w 4 multizab:app -b 127.0.0.1:8000 -D
```

## Author
Jeremy Mouton (@jeremmm) <jeremmm@labbs.fr>

## Licence
MIT. See ``LICENSE`` for more details.
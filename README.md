# multizab
![ScreenShot](https://github.com/Jeremmm/multizab/blob/master/multizab/static/img/multizab_screen.png)

### Comming
 - DB less
 - Graph (per trigger level/hosts/Zabbix)

## First usage

### Clone repo
```bash
git clone git@github.com:Jeremmm/multizab.git
```

### Create virtualenv
```bash
cd multizab
virtualenv env -p=python2.7
```

### Install dependencies
```bash
env/bin/pip install -r requirements.txt
```

### Copy config file and init DB (sqlite)
```bash
cp multizab\config-template.py multizab\config.py
env/bin/python manage.py db init
env/bin/python manage.py db migrate
env/bin/python manage.py db upgrade
```

### Run server
```bash
env/bin/python manage.py runserver
```

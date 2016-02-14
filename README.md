# multizab
[![Code Climate](https://codeclimate.com/github/Jeremmm/multizab/badges/gpa.svg)](https://codeclimate.com/github/Jeremmm/multizab)

![ScreenShot](https://github.com/Jeremmm/multizab/blob/master/multizab/static/img/multizab_screen.png)

![ScreenShot](https://github.com/Jeremmm/multizab/blob/master/multizab/static/img/multizab_screen_graphics.png)


## Update
### 13 Feb 2016
 - Remove database (json file used now)
 - Logging if a zabbix backend is ko
 - python 3 compatibility
 - Graph (per trigger level/hosts/Zabbix)

### Coming
 ...

## First usage

### Clone repo
```bash
git clone git@github.com:Jeremmm/multizab.git
```

### Create virtualenv
```bash
cd multizab
virtualenv env -p python2.7
```

### Install dependencies
```bash
env/bin/pip install -r requirements.txt
```

### Copy config file
```bash
cp multizab\config-template.py multizab\config.py
```

### Run server
```bash
env/bin/python manage.py runserver
```

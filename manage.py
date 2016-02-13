from flask_script import Manager, Server

from multizab import app

manager = Manager(app)
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port='8000'))

if __name__ == '__main__':
    manager.run()

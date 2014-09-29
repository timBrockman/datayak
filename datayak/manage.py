import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask.ext.script import Manager, Server, Command
from datayak import app
from forager import Groups

manager = Manager(app) 

class GetGroups(Command):
    def run(self):
        g=Groups()
        g.find_groups()

if __name__ == "__main__":
    manager.run({
                 'runserver':Server(),
                 'getgroups':GetGroups(), 
                 })
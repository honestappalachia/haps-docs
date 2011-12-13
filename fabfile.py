from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['happalachia@happalachia.webfactional.com']

def commit():
    local("git add -p && git commit")

def pack():
    local("tar czf /tmp/haps-docs.tgz .")

def prepare_deploy():
    commit()
    pack()

def deploy():
    sphinx_dir = '/home/happalachia/webapps/sphinx'
    put('/tmp/haps-docs.tgz', '/tmp/')
    with cd(sphinx_dir):
        run('tar xzf /tmp/haps-docs.tgz')

from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['happalachia@happalachia.webfactional.com']

local_html_dir = "_build/html"

def build():
    local("make html")
    local("open %s/index.html" % local_html_dir)

def commit():
    # git add -p ??
    local("git add -i && git commit")

def pack():
    local("make html")
    local("cd %s && tar czf /tmp/haps-docs.tgz ." % local_html_dir)

def prepare_deploy():
    commit()

def deploy():
    pack()
    remote_dir = '/home/happalachia/webapps/sphinx'
    put('/tmp/haps-docs.tgz', '/tmp/')
    with cd(remote_dir):
        run('tar xzf /tmp/haps-docs.tgz')

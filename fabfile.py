'''
usage:
    $ fab prod host_info
    $ fab prod deploy
'''
import os

from fabric.api import *

def prod():
    env.user = 'matt'
    env.hosts = ['kepler']
    env.project_dir = '/home/matt/nanubhai'
    env.branch = 'master'


def deploy():
    # push changes of specific branch
    local('git push origin %s' % env.branch)

    # update the remote with these changes
    run('cd %s; git pull origin %s' % (env.project_dir, env.branch))

    # restart via supervisor


''' misc
'''
def host_info():
    print 'checking lsb_release of host: '
    run('lsb_release -a')

def uptime():
    run('uptime')

def grep_python():
    run('ps aux | grep python')

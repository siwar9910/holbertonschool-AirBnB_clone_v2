#!/usr/bin/python3
""" package the  web static files and deploy """
import datetime
import os
from fabric.api import put, env, run, local


env.hosts = ["35.231.86.106", "34.148.233.36"]

env.user = "ubuntu"


def do_deploy(archive_path):
    """ deploy the package """
    if archive_path is None or not os.path.isfile(archive_path):
        print("NOT PATH")
        return False

    aname = os.path.basename(archive_path)
    rname = aname.split(".")[0]

    put(local_path=archive_path, remote_path="/tmp/")
    run("mkdir -p /data/web_static/releases/{}".format(rname))
    run("tar -xzf /tmp/{} \
        -C /data/web_static/releases/{}".format(aname, rname))
    run("rm /tmp/{}".format(aname))
    run("rm -rf /data/web_static/current")
    run("ln -fs /data/web_static/releases/{}/ \
        /data/web_static/current".format(rname))
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/curren/web_static")

    return True


def do_pack():
    """ package func """
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    ntime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(ntime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), ntime))


def deploy():
    """ package and deploy to the servers """
    path = do_pack()
    if path is None:
        return False
    return(do_deploy(path))


def do_clean(number=0):
    """script (based on the file 3-deploy that deletes out-of-date using the function do_clean """
    number = int(number)
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
          xargs -d '\n' rm -rf --".format(2 if number < 1 else number + 1))

#!/usr/bin/python3
""" 
script that generates a .tgz archive from the contents of 
the web_static folder of your AirBnB Clone repo,  
"""
import datetime
import os
from fabric.api import local

def do_pack():
    """ package  of funct"""
    if not os.path.isdir("./versions"):
        os.makedirs("./versions")
    ntime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("tar -czzf versions/web_static_{}.tgz web_static/*".format(ntime))
    return ("{}/versions/web_static_{}.tgz".format(os.path.dirname(
        os.path.abspath(__file__)), ntime))

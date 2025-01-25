#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local('mkdir -p versions')
        archive_path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

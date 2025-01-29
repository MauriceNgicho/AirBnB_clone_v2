#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from web_static folder.
"""

from fabric.api import local, env, put, run
from datetime import datetime
import os
from os.path import exists
env.hosts = ['52.87.234.192', '34.202.159.235']
env.user = "ubntu"


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if exists(archive_path) is False:
        return False
    try:
        # Extract file name and archive folder name
        archive_file = os.path.basename(archive_path)
        folder_name = archive_file.split(".")[0]
        release_folder = f"/data/web_static/releases/{folder_name}"

        # Upload the archive to the /tmp/ directory on the server
        put(archive_path, f"/tmp/{archive_file}")

        # Create the target directory
        run(f"mkdir -p {release_folder}")

        # Uncompress the archive into the target directory
        run(f"tar -xzf /tmp/{archive_file} -C {release_folder}")

        # Remove the archive from the server
        run(f"rm /tmp/{archive_file}")

        # Move files to the correct location
        run(f"mv {release_folder}/web_static/* {release_folder}/")
        run(f"rm -rf {release_folder}/web_static")

        # Delete the current symbolic link and recreate it
        run("rm -rf /data/web_static/current")
        run(f"ln -s {release_folder} /data/web_static/current")

        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

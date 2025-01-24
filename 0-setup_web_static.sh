#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    sudo apt update -y
    sudo apt install nginx -y
fi

# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

# Create a fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    ALX
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate the symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ folder to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/
if ! grep -q "location /hbnb_static" /etc/nginx/sites-enabled/default; then
    sudo sed -i '/listen 80 default_server;/a \    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }' /etc/nginx/sites-enabled/default
fi

# Restart Nginx to apply the changes
sudo service nginx restart

exit 0

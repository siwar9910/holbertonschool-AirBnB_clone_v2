#!/usr/bin/env bash
# NGINX configuration for the webstatic
# install the nginx
sudo apt-get -y update
sudo apt-get -y install nginx
# making the file structure
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# adding simple content
echo "simple content, to test your Nginx configuration" >> /data/web_static/releases/test/index.html
# adding symbolic link
ln -fs /data/web_static/releases/test/ /data/web_static/current
# giving ownership to user and grp
chown -R ubuntu:ubuntu /data
# Update the Nginx config to serve the content of
# /data/web_static/current/ to hbnb_static 
sed -i "/listen 80 default_server;/a location /hbnb_static {alias /data/web_static/current/;}" /etc/nginx/sites-available/default
sudo ufw allow "Nginx HTTP"
sudo service nginx restart
exit 0

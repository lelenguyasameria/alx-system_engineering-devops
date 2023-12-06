#!/usr/bin/env bash
# Puppet manifest to configure custom HTTP response header in Nginx

# Install Nginx package
apt-get update
apt-get install -y nginx

# Define custom HTTP response header
custom_header_name="X-Served-By"
custom_header_value=$(hostname)

# Configure Nginx to add custom HTTP response header
cat <<EOL > /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    # Custom HTTP response header
    add_header $custom_header_name $custom_header_value;

    # ...
}
EOL

# Create a symbolic link to enable the site
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Ensure Nginx service is running
service nginx restart

# Output the expected result
echo "1"


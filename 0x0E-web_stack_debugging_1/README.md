#!/usr/bin/env bash

# Check if Nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Please install it first."
    exit 1
fi

# Check if Nginx is already running
if pgrep -x "nginx" &> /dev/null; then
    echo "Nginx is already running."
else
    # Start Nginx
    nginx
    echo "Nginx has been started."
fi

# Check Nginx's configuration file for the presence of a server block listening on port 80
if grep -q "listen 80;" /etc/nginx/nginx.conf; then
    echo "Nginx is configured to listen on port 80."
else
    # Add a server block to the Nginx configuration file if not present
    echo "server {
        listen 80;
        server_name _;
        location / {
            root /usr/share/nginx/html;
            index index.html;
        }
    }" | tee -a /etc/nginx/nginx.conf

    # Reload Nginx to apply the new configuration
    nginx -s reload

    echo "Nginx has been configured to listen on port 80."
fi

echo "Script execution completed."


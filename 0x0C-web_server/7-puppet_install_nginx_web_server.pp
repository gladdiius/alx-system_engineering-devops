# Define the Nginx package and service
package { 'nginx':
  ensure => present,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
  
      root /var/www/html;
      index index.html;
  
      server_name _;
  
      location / {
        try_files \$uri \$uri/ =404;
      }

      location = /redirect_me {
        return 301 https://www.example.com/;
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define the index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!",
  require => Package['nginx'],
}

# Restart Nginx when the configuration changes
exec { 'nginx-reload':
  command     => 'systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

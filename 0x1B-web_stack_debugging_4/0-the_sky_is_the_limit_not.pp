# Description: Puppet manifest to optimize Nginx configurations for improved performance.

class { 'nginx':
  worker_processes  => auto,
  worker_connections => 1024,
}

nginx::resource::vhost { 'default':
  ensure   => present,
  listen   => '80',
  location => {
    '/' => {
      try_files => '$uri $uri/ =404',
    },
  },
}

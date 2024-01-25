# File: optimize_nginx.pp

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

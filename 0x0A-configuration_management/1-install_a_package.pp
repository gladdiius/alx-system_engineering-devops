#!/usr/bin/pup
# install_flask.pp
# Puppet manifest to install Flask version 2.1.0 using the pip3 provider

# install_flask.pp
# Puppet manifest to install Flask version 2.1.0 using the pip3 provider

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  notify   => Exec['print_flask_notice'],
}

exec { 'print_flask_notice':
  command => '/bin/echo "Flask installation completed"',
}



# Description: Puppet manifest to set file limits for the holberton user.
class { 'limits':
  confdir => '/etc/security/limits.d',
}

limits::limits { 'holberton_limits':
  ensure => present,
  limits => {
    'nofile' => {
      'soft' => '10000',
      'hard' => '20000',
    },
  },
  users => ['holberton'],
}

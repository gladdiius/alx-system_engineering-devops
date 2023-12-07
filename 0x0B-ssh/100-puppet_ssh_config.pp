# Ensure the SSH client configuration file exists
file { '/etc/ssh/ssh_config':
  ensure => present,
  mode   => '0644',
  owner  => 'root',
  group  => 'root',
}

# Set up SSH client configuration to use the private key ~/.ssh/school
file_line { 'ssh_private_key':
  path    => '/etc/ssh/ssh_config',
  line    => '   IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile ~/.ssh/school',
  require => File['/etc/ssh/ssh_config'],
}

# Set up SSH client configuration to refuse password authentication
file_line { 'ssh_password_authentication':
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  require => File['/etc/ssh/ssh_config'],
}

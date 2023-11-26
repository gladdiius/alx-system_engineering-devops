file { '/home/your_username/.ssh/config':
  ensure => file,
  content => "
    Host your_server_alias
      HostName your_server_ip_or_domain
      User ubuntu
      IdentityFile ~/.ssh/school
      PreferredAuthentications publickey
      PasswordAuthentication no
      LogLevel QUIET
  ",
}


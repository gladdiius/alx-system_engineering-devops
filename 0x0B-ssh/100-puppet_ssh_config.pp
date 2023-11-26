file { '/home/ubuntu/.ssh/config': # Replace 'your_username' with your actual username
  ensure => file,
  content => "\
Host *
    IdentityFile ~/.ssh/school
",
  mode => '0600',
  owner => 'your_username', # Replace 'your_username' with your actual username,
}


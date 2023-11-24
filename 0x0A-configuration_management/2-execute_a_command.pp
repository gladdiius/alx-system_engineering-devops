# kill_process.pp
# Puppet manifest to kill a process named "killmenow" using pkill

exec { 'kill_killmenow_process':
  command     => 'pkill -f "killmenow"',
  provider    => 'shell',
  returns     => [0, 1],
}


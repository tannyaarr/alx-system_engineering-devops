# kills a process named killmenow

exec { 'killmenow':
   command  => 'pkill -f killmenow',
   onlyif   => '/usr/bin/pgrep -f killmenow >/dev/null',
   path     => ['/bin', '/usr/bin'],
}

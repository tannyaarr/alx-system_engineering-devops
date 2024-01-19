# kills a process named killmenow

exec { 'killmenow':
   command => 'pkill -f killmenow',
   onlyif  => '/usr/bin/pgrep -f killmenow',
   path    => ['/bin', '/usr/bin'],
}

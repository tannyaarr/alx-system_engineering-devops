#kills a process named killmenow

exec { 'killmenow_process':
   command => 'pkill -f killmenow',
   onlyif  => 'grep -f killmenow'
}

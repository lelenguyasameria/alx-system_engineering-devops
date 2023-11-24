# Puppet manifest to kill a process named 'killmenow'
# File: kill_process.pp

exec { 'kill_killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}


# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error identified using strace

package { 'apache2':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello, this is the correct page!',
}

service { 'apache2':
  ensure  => running,
  enable  => true,
  require => Package['apache2'],
}


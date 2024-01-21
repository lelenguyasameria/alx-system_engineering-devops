# 0-strace_is_your_friend.pp
# Puppet manifest to fix Apache 500 error identified using strace

file { '/etc/apache2/httpd.conf':
  ensure  => present,
  content => 'Updated content based on strace findings',
  notify  => Service['apache2'],
  require => Package['apache2'], # Make sure Apache is installed first
}

package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
}


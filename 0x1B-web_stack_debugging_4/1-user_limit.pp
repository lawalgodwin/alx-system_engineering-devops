# A puppet manifest that increase the limit on the number
# of files that can the oepned by a user

exec { 'increase-user-limit-hard':
  command => 'sed -i -e "s/holberton hard nofile 5/holberton hard nofile 8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/'
}


exec { 'increase-user-limit-soft':
  command => 'sed -i -e "s/holberton soft nofile 4/holberton soft nofile 8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/'
}

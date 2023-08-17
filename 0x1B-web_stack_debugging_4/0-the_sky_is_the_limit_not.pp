# A puppet manifest that optimises an nginx worker process to handle more requests

exec { 'increase-number-of-open-file-limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/',
  notify  => Service['nginx']
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['increase-number-of-open-file-limit']
}

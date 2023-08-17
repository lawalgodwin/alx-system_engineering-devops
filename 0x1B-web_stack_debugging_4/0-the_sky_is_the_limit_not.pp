# A puppet manifest that increases the number of files nginx worker process can open(No of requests it can handle concurrently)

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

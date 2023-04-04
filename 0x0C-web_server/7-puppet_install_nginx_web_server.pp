# The manifest installs and configures an uduntu bare metal server with a NGINX web server
# Install Nginx web server (using Puppet)

# update system
exec { 'apt-get update':
  command => 'apt-get update ; apt-get upgrade -y',
  path    => '/usr/bin'
}

# install nginx
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}

# configure the index page
exec { 'index.html':
  command  => 'echo "Hello World!" > /var/www/html/index.html',
  provider => shell
}

# write a custom 404 page
exec { '404.html':
  command  => 'echo "Ceci n\'est pas une page." > /var/www/html/404.html',
  provider => shell
}

# customize the default config file
exec { 'configure-permanent-redirect':
  command => 'sed -i "s/listen 80 default_server;/listen 80 default_server;\n\tlocation ^\/redirect_me {\n\t\treturn 301 \'https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4\';\n\t}/" /etc/nginx/sites-enabled/default',
  path    => '/usr/bin'
}

# configure custom 404 page
exec { 'configure-how-404-is-handled':
  command => 'sed -i "s/server_name _;/server_name _;\n\terror_page 404 \/404.html;\n\tlocation =\/404.html {\n\t\tinternal;\n\t}/" /etc/nginx/sites-enabled/default',
  path    => '/usr/bin'
}

# start nginx daemon
service { 'nginx':
  ensure => 'running',
  enable => 'true'
}

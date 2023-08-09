# A puppet manifest that automates fixing the error 500 being returned
# by Apache webserver, after finding out the issue using 'strace' command

exec { 'Fix-error-500':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/'
}

# fix wordpress site
exec { 'fix wordpress':
  path     => ['/bin', '/usr/bin', '/usr/sbin'],
  provider => 'shell',
  command  => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}

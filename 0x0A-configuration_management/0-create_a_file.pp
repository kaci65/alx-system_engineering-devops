# create a file in /tmp
file { '/tmp/holberton':
  path    => '/tmp/holberton',
  mode    => '0744',
  group   => 'www-data',
  owner   => 'www-data',
  content => 'I love Puppet',
}

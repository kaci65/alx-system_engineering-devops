# using Puppet to make changes to our configuration file
file_line { 'Config IdentityFile':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Remove password authentification':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentification no',
}

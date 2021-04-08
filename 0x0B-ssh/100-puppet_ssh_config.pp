# using Puppet to make changes to our configuration file
file_line { 'configure identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'remove password authentification':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentification no',
}

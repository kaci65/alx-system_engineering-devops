# using Puppet to make changes to our configuration file
file_line { 'configure using private key':
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'disable password authentification':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentification no',
}

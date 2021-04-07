# using Puppet to make changes to our configuration file
file_line { 'configure using private key':
  line => 'IdentityFile ~/.ssh/holberton',
  path => '/etc/ssh/sshd_config'
}

file_line { 'disable password authentification':
  line => 'PasswordAuthentification no',
  path => '/etc/ssh/sshd_config'
}

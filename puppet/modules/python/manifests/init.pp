# == Class: python
#
# Installs python dev packages
#
class python {
  include python::packages

  package { 'python':
    ensure => installed;
  }
}
class python::packages {
  $apt = ['python-dev', 'build-essential', 'python-pip']
  $pip = ['virtualenv', 'flask', 'psycopg2', 'sqlalchemy', 'flask-sqlalchemy', 'flask-migrate']

  package { $apt:
    require => Class['python'],
    ensure 	=> installed;
  }

  package { $pip:
    require   => Class['python', 'postgresql'],
    ensure    => installed,
    provider  => pip;
  }
}
# == Class: postgresql
#
# Installs and configures PostgreSQL
#
class postgresql {
  package { ['postgresql', 'postgresql-server-dev-all']:
    ensure => installed;
  }

  service { 'postgresql':
    ensure  => running,
    require => Package['postgresql'],
  }
}
# == Class: nginx
#
# Install packages for Nginx and sets config files.
#
class nginx {
  package { 'nginx':
    ensure => present;
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure => absent;
  }
    file { '/srv/www':
    ensure => directory;
  }

  service { 'nginx':
    ensure => running,
    require => Package['nginx'];
  }
}
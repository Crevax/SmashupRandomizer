# == Define: load_server
#
# Adds and enables an Nginx server block
#
define nginx::load-server(
  $socket = $name
) {

  file {
    "/etc/nginx/sites-available/${name}":
      content => template('nginx/server-conf.erb'),
      require => Package['nginx'],
      notify  => Service['nginx'];

    "/etc/nginx/sites-enabled/${name}":
      ensure => link,
      target => "/etc/nginx/sites-available/${name}",
      notify => Service['nginx'];
  }
}
# == Define: create-role

# Creates a PostgreSQL role
#
define postgresql::create-role() {
  $userexists = "psql --tuples-only -c 'SELECT rolname FROM pg_catalog.pg_roles;' | grep '^ ${name}$'"

  exec { "createuser ${name}":
    command => "createuser --no-superuser --no-createdb --no-createrole ${name}",
    user    => 'postgres',
    unless  => $userexists,
    path => ["/bin", "/sbin", "/usr/bin"],
    require => [Package["postgresql"], Service["postgresql"]]
  }
}
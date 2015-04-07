# == Define: create-role

# Creates a PostgreSQL role
#
define postgresql::create-role() {
  $userexists = "psql --tuples-only -c 'SELECT rolname FROM pg_catalog.pg_roles;' | grep '^ ${name}$'"

  exec { "CREATE ROLE":
    command => "psql -c \"CREATE ROLE \"${name}\" ENCRYPTED PASSWORD '123four' LOGIN;\"",
    user    => 'postgres',
    unless  => $userexists,
    path => ["/bin", "/sbin", "/usr/bin"],
    require => [Package["postgresql"], Service["postgresql"]],
    logoutput => on_failure
  }
}
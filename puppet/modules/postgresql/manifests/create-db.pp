# == Define: create-db

# Creates a PostgreSQL database
#
define postgresql::create-db(
  $owner
) {
  $dbexists = "psql -ltA | grep '^${name}|'"

  exec { "createdb ${name}":
    command => "createdb -O ${owner} -E UTF8 ${name}",
    user    => 'postgres',
    unless  => $dbexists,
    path => ["/bin", "/sbin", "/usr/bin"],
    require => [Postgresql::Create-role[$owner], Package["postgresql"], Service["postgresql"]]
  }
}
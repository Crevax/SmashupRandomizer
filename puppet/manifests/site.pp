# create a new run stage to ensure certain modules are included first
stage { 'pre':
  before => Stage['main']
}

# add the baseconfig module to the new 'pre' run stage
class { 'baseconfig':
  stage => 'pre'
}

include baseconfig, users, nginx, postgresql, python, uwsgi

# Note: PostgreSQL doesn't like hyphens
postgresql::create-role {'smashup_user':
}

postgresql::create-db {'smashup_randomizer':
  owner => 'smashup_user'
}

uwsgi::vassal {'smashup-randomizer-api':
}

nginx::load-server {'smashup-randomizer':
  socket => 'smashup-randomizer-api'
}
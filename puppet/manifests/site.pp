# create a new run stage to ensure certain modules are included first
stage { 'pre':
  before => Stage['main']
}

# add the baseconfig module to the new 'pre' run stage
class { 'baseconfig':
  stage => 'pre'
}

include baseconfig, users, nginx, postgresql, python, uwsgi

postgresql::create-role {'smashup-user':
}

postgresql::create-db {'smashup-randomizer':
  owner => 'smashup-user'
}

uwsgi::vassal {'smashup-randomizer':
}

nginx::load-server {'smashup-randomizer':
}
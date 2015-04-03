# create a new run stage to ensure certain modules are included first
stage { 'pre':
  before => Stage['main']
}

# add the baseconfig module to the new 'pre' run stage
class { 'baseconfig':
  stage => 'pre'
}

include baseconfig, users, nginx, python, uwsgi

uwsgi::vassal {'smashup-randomizer':
}

nginx::load-server {'smashup-randomizer':
}
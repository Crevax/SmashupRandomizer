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
  $pip = ['virtualenv', 'flask']

  package { $apt:
  	require => Class['python'],
  	ensure 	=> installed;
	}

	package { $pip:
		require		=> Class['python'],
		ensure		=> installed,
		provider	=> pip;
	}
}
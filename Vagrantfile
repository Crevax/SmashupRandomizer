# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

settings = {
  :hostname => "perseus",
  :box      => "ubuntu/trusty32",
  :ip       => "192.168.0.42",
  :timezone => "America/Detroit"
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = settings[:box]
  config.vm.host_name = settings[:hostname]
  config.vm.network "private_network", ip: settings[:ip]
  config.vm.synced_folder "./applications", "/srv/www",
    mount_options: ["dmode=755", "fmode=644"],
    group: "www-data"

  config.vm.provision :shell, :inline => "if [ $(grep -c UTC /etc/timezone) -gt 0 ]; then echo \"#{settings[:timezone] }\" | sudo tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata; fi"

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = 'puppet/manifests'
    puppet.manifest_file = 'site.pp'
    puppet.module_path = 'puppet/modules'
    puppet.options = ["--graphdir=/vagrant/graphs --graph"]
  end
end

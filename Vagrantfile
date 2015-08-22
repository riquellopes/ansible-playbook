# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "project"
  config.vm.box_url = "https://dl.dropboxusercontent.com/u/6032045/Box/ubuntu-14.04-amd64-vbox.box"

  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.synced_folder "project", "/var/www/project"

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end

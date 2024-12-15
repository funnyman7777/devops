# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.ssh.insert_key = false

  config.vm.define "dobweb" do |dobweb|
    dobweb.vm.box = "CentosBox/Centos-7-v7.4-Minimal-CLI"
    dobweb.vm.hostname = "node"
    dobweb.vm.network "public_network", bridge: 'eno2', ip: "192.168.100.91",  netmask: "255.255.255.224"
    dobweb.vm.network "forwarded_port", guest: 80, host: 8082, auto_correct: true
    dobweb.vm.synced_folder "vagrant/web/", "/vagrant"
    #dobweb.vm.provision "shell", path: "dobweb.sh"
 
  end



  config.vm.define "dobdb" do |dobdb|
    dobdb.vm.box = "CentosBox/Centos-7-v7.4-Minimal-CLI"
    dobdb.vm.hostname = "node1"
    dobdb.vm.network "public_network", bridge: 'eno2', ip: "192.168.100.92", netmask: "255.255.255.224"
    dobdb.vm.network "forwarded_port", guest: 80, host: 8081, auto_correct: true
    dobdb.vm.synced_folder "vagrant/db/", "/vagrant"
    #dobdb.vm.provision "shell", path: "dobdb.sh"

  end

end

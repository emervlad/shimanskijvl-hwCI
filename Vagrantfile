# -*- mode: ruby -*-
# vi: set ft=ruby :

$update_script1=<<SCRIPT
apt-get update
apt-get upgrade -y
apt-get install -y python3-pip
pip3 install opencv-python numpy pytest
SCRIPT

$update_script2=<<SCRIPT
yum -y upgrade
yum -y install epel-release
yum install -y python3
python3 -m pip install --upgrade pip
python3 -m pip install opencv-python numpy pytest opencv-python-headless opencv-contrib-python-headless
SCRIPT

Vagrant.configure("2") do |config|

  vm_distr=['bento/ubuntu-20.04','centos/7']
  vm_url=['~/Downloads/401ad560-e62e-4e55-9cbc-772264c9835c','~/Downloads/CentOS-7-x86_64-Vagrant-2004_01.VirtualBox.box']

  config.vm.provider "virtualbox" do |vb|
      vb.cpus = '1'
      vb.memory = "2048"
    end

 #   manager.vm.provision "shell", :inline => $update_script
  
#   ips = ['192.168.56.21','192.168.56.31','192.168.56.41']
 #  ports = ['2222', '2223', '2224']
   (1..2).each do |i|
     config.vm.define "node-#{i}" do |node|
       node.vm.box = vm_distr[i - 1]
       node.vm.box_url = vm_url[i - 1]
       if "#{i}" == "1"
         node.vm.provision "shell", :inline => $update_script1
       else
         node.vm.provision "shell", :inline => $update_script2
       end
   #    node.vm.network "forwarded_port", guest: 22, host: "#{ports[i - 1]}" 
#       node.vm.network :private_network, ip: "#{ips[i - 1]}"
     end
   end

end

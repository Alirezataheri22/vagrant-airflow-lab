Vagrant.configure("2") do |config|
  # Base box for all machines
  config.vm.box = "ubuntu/focal64"

  # ---------- DB VM ----------
  config.vm.define "db" do |db|
    db.vm.hostname = "db"
    db.vm.network "private_network", ip: "192.168.56.10"

    db.vm.provider "virtualbox" do |vb|
      vb.name = "db-vm"
      vb.memory = 2048
      vb.cpus = 1
    end

    db.vm.provision "shell", inline: <<-SHELL
      set -e
      export DEBIAN_FRONTEND=noninteractive
      apt-get update -y
      apt-get install -y ansible postgresql postgresql-contrib python3-psycopg2
      ansible-playbook /vagrant/provisioning/db_playbook.yml -i "localhost,"
    SHELL
  end

  # ---------- Airflow VM ----------
  config.vm.define "airflow" do |air|
    air.vm.hostname = "airflow"
    air.vm.network "private_network", ip: "192.168.56.11"

    # Forward Airflow web UI (8080 in VM) to 8081 on your laptop
    air.vm.network "forwarded_port", guest: 8080, host: 8081, auto_correct: true

    # Give this VM more time to boot
    air.vm.boot_timeout = 600

    air.vm.provider "virtualbox" do |vb|
      vb.name = "airflow-vm"
      vb.memory = 4096   # smaller to avoid RAM issues
      vb.cpus = 1
      vb.gui = true      # show VM window so we can see boot if needed
    end

    air.vm.provision "shell", inline: <<-SHELL
      set -e
      export DEBIAN_FRONTEND=noninteractive
      apt-get update -y
      apt-get install -y ansible docker.io docker-compose
      systemctl enable docker
      systemctl start docker
      usermod -aG docker vagrant
      ansible-playbook /vagrant/provisioning/airflow_playbook.yml -i "localhost,"
    SHELL
  end
end
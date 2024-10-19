#! /bin/bash
sudo apt update
sudo apt install -y snapd
sudo systemctl enable --now snapd apparmor
echo "now restart kali vm"

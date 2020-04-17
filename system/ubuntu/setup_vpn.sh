adduser xiaojueguan
usermod -aG sudo xiaojueguan

ufw app list
ufw allow OpenSSH


sudo apt update -y
sudo apt install openvpn -y


wget -P ~/ https://github.com/OpenVPN/easy-rsa/releases/download/v3.0.4/EasyRSA-3.0.4.tgz
cd ~
tar xvf EasyRSA-3.0.4.tgz

cd ~/EasyRSA-3.0.4/
cp vars.example vars

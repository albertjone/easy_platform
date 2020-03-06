#!/usr/bin/env bash

set -o xtrace
unset LANG
unset LANGUAGE
LC_ALL=en_US.utf8
export LC_ALL

TOP_DIR=$(cd $(dirname "$0") && pwd)

function config_clock() {
    sudo ntpdate -u ntp.api.bz
    sudo cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
    sudo hwclock
}

function config_yum() {
    sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
    sudo curl -L https://mirrors.aliyun.com/repo/Centos-7.repo -o /etc/yum.repos.d/CentOS-Base.repo
    sudo yum clean all
    sudo yum makecache
    sudo yum update -y

}

function install_v2ray() {
    if [[ ! -f $TOP_DIR/files/v2ray/v2ray.zip ]]; then
        echo "file v2ray.zip not exists start to download from github.com"
        curl -L https://github.com/v2ray/v2ray-core/releases/download/v4.20.0/v2ray-linux-64.zip -o $TOP_DIR/files/v2ray/v2ray.zip -#
}

# configing
function config_v2ray() {

}

function config_git() {
    git config --global http.proxy http://127.0.0.1:1081
    git config --global https.proxy http://127.0.0.1:1081
}

function config_curl() {
cat <<EOF > ~/.curlrc
proxy = 127.0.0.1:1081
EOF
}

function config_wget() {
cat <<EOF > ~/.wgetrc
http_proxy = http://127.0.0.1:1081
https_proxy = http://127.0.0.1:1081
ftp_proxy = http://127.0.0.1:1081
EOF
}

function config_pip() {
cat <<EOF > ~/.pip/pip.conf
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
EOF
}

function config_dnf() {
    sudo cat <<EOF > /etc/dnf/dnf.conf
[main]
gpgcheck=1
installonly_limit=3
clean_requirements_on_remove=True
proxy = https://127.0.0.1:1080
EOF
}

function main() {
# config clock
config_clock
# install softwares
install_v2ray
yum_install git vim pip

config_v2ray
config_git
config_pip
config_dnf

}




main
yum remove docker \
                  docker-client \
                  docker-client-latest \
                  docker-common \
                  docker-latest \
                  docker-latest-logrotate \
                  docker-logrotate \
                  docker-engine -y
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2 -y

yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo

yum install docker-ce docker-ce-cli containerd.io -y

systemctl enable docker && systemctl start docker && systemctl status docker


mkdir -p /etc/systemd/system/docker.service.d

cat << EOF > /etc/systemd/system/docker.service.d/http-proxy.conf
[Service]
Environment="HTTP_PROXY=http://127.0.0.1:1087"
EOF

systemctl daemon-reload

systemctl restart docker

systemctl show --property=Environment docker

# cat << EOF > ~/.docker/config.json
# {
#  "proxies":
#  {
#    "default":
#    {
#      "httpProxy": "http://127.0.0.1:1087",
#      "httpsProxy": "http://127.0.0.1:1087",
#      "noProxy": "*.test.example.com,.example2.com,localhost"
#    }
#  }
# }
# EOF



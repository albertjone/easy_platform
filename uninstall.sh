# Warning! Dangerous step! Destroys VMs
for x in $(virsh list --all | grep instance- | awk '{print $2}') ; do
    virsh destroy $x ;
    virsh undefine $x ;
done ;

yum remove -y "*openstack*" "*nova*" "*keystone*" "*glance*" "*cinder*" "*swift*";

ps -ef | grep -i repli | grep swift | awk '{print $2}' | xargs kill ;

# Warning! Dangerous step! Deletes local OpenStack application data
rm -rf  /etc/yum.repos.d/packstack_* /var/lib/glance /var/lib/nova /etc/nova /etc/swift \
/srv/node/device*/* /var/lib/cinder/ /etc/rsync.d/frag* \
/var/cache/swift /var/log/keystone /var/log/cinder/ /var/log/nova/ \
/var/log/glance/ /var/log/quantum/ ;

# Ensure there is a root user and that we know the password
service mysql stop
cat > /tmp/set_mysql_root_pwd < < EOF
FLUSH PRIVILEGES;
EOF

/usr/bin/mysqld_safe --init-file=/tmp/set_mysql_root_pwd &
rm /tmp/set_mysql_root_pwd

mysql -uroot -pMyNewPass -e "drop database nova; drop database cinder; drop database keystone; drop database glance;"

umount /srv/node/device* ;
vgremove -f cinder-volumes ;
losetup -a | sed -e 's/:.*//g' | xargs losetup -d ;
find /etc/pki/tls -name "ssl_ps*" | xargs rm -rf ;
for x in $(df | grep "/lib/" | sed -e 's/.* //g') ; do
    umount $x ;
done
#!/bin/sh

set -o xtrace

possible_pid_dirs="/var/lib/mysql/ /var/run/mysqld/ /usr/local/mysql/data/"
init_file=/tmp/mysql-init
pid=0

make_init_file(){
    if [[ -e $init_file ]]
    then
        rm -fr $init_file
    fi
#     cat << EOF > $init_file
# CREATE USER
#   'robot'@'localhost' IDENTIFIED WITH mysql_native_password
#                                    BY 'Mr.Robot@123',
#   REQUIRE X509 WITH MAX_QUERIES_PER_HOUR 60
#   PASSWORD HISTORY 5
#   ACCOUNT LOCK;
# FLUSH PRIVILEGES;
# EOF
    cat << EOF > $init_file
ALTER USER 'root'@'localhost' IDENTIFIED BY 'Mr.Robot@123';
FLUSH PRIVILEGES;
EOF
#     cat << EOF > $init_file
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';
# EOF
    chown mysql $init_file
    chgrp mysql $init_file
}

for dir in $possible_pid_dirs
do
    if [[ -n `cat "$dir"mysqld.pid`  ]]
    then
        pid=`cat "$dir"mysqld.pid`
    else
        echo "no mysql pid in dir: $dir"
    fi
done
if [[ $pid -gt 0 ]]
then
    kill -9 $pid
    ps -aux | grep -i mysql
    make_init_file
    `mysqld-debug --init-file="$init_file" --user=mysql &`
else
    echo "no pid of mysql"
fi

ps -aux | grep -i mysql

# rm /root/mysql-init

ps -aux | grep -i mysql

# mysql -uroot -pMr.Robot@123 -h127.0.0.1
# mysql -urobot -pMr.Robot@123
# mysql -urobot -pMr.Robot@123 -h127.0.0.1 
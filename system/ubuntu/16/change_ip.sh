# config interface
# config interface ip in 192.168.199.0/24 subnet on ubuntu16
# param ip
#set -x

target_ip=$1
interfaces=`ls /sys/class/net`
valued_interfaces=()

function config_ip () {
    config=""
    interfaces=($(sort <<< $@))
    for index in "${!interfaces[@]}"
    do
        if [[ $index == 0 ]]
        then
            IFS='' read -r -d '' current << EOF
auto ${interfaces[$index]}
iface ${interfaces[$index]} inet static
	    address $target_ip
	    netmask 255.255.255.0
	    gateway 192.168.199.1
EOF
        else
            IFS='' read -r -d '' current << EOF
auto ${interfaces[$index]}
iface ${interfaces[$index]} inet dhcp
EOF
         fi
        config+=$current
    done
    echo $config > ~/test.conf
    cat ~/test.conf


}


for interface in ${interfaces}
do
    if [[ $interface == "lo" ]]
    then
        continue
    fi
    valued_interfaces+="$interface "
done

#printf "valued_interfaces are %s \n" $valued_interfaces

config_ip ${valued_interfaces[@]}

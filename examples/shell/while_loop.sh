count=5

while [ $count -lt 10 ]; do
    echo $count
    sleep 1
    count=$(($count + 1))
done

#while true; do
#    echo $count
#    sleep 1
#    count=$(($count + 1))
#    if [ $count -gt 10 ];
#    then
#        break
#    fi
#done


#while true; do
#    echo $count
#    sleep 1
#    count=$(($count + 1))
#    if [ $count -lt 10 ];
#    then
#        continue
#    fi
#    echo "=="
#    break
#done



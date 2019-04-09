count=5
while true; do
    echo $count
    sleep 1
    if [ $count -lt 9 ];
    then
        count=$(($count + 1))
        continue
    fi
    break
done



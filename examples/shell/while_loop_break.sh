count=5
while true; do
    echo $count
    sleep 1
    count=$(($count + 1))
    if [ $count -gt 9 ];
    then
        break
    fi
done


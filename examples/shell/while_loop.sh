count=5

while [ $count -lt 10 ]; do
    echo $count
    sleep 1
    count=$(($count + 1))
done

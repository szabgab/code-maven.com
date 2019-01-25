START_TIME=$(date +%s)

sleep 1 # put some real task here instead of sleeping

END_TIME=$(date +%s)
echo "It took $(($END_TIME - $START_TIME)) seconds to sleep of 1 second..."


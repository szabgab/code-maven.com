filename=$1
limit=$2

for ((i=1;i<=$limit;i++));
do
    grep y $filename
done

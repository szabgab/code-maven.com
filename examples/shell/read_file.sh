filename="$1"

while read -r line
do
   echo $line
   echo '----'

done < "$filename"


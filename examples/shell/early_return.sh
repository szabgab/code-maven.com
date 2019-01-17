function foo()
{
   param=$1
   if [ "$param" == "ok" ]
   then
       echo "short"
       return
   fi
      echo "long"
}

foo

foo ok

foo

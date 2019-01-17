function foo()
{
   echo "param: '$1'  param: '$2'"
}

echo before
foo "one" "and two"
echo after

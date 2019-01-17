name=$1
if [ "$name" == "" ]
then
    echo Usage: $0 module_name
    exit 1
fi

python -c"import $name; print($name.__version__)"

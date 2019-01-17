
function module_version()
{
    name=$1
    if [ "$name" == "" ]
    then
        echo Usage: $0 module_name
        exit 1
    fi

    python -c"import $name; print($name.__version__)"
}

module_version urllib3


version=$(module_version urllib3)
echo before
echo $version
echo after


import shlex

cmd = './bin/application --source /some/directory --target /other/dir --verbose -d --name "Foo Bar"'
print(cmd.split(' '))


print(shlex.split(cmd))

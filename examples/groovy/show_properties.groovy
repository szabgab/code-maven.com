for (key in System.properties.keySet().sort()) {
    printf('%-30s   %s\n', key, System.properties[key])
}

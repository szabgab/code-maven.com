def tools = new GroovyScriptEngine( '.' ).with {
    loadScriptByName( 'class_tools.gvy' )
}
this.metaClass.mixin tools
greet()

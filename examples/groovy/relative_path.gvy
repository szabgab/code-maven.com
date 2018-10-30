import groovy.transform.SourceURI
import java.nio.file.Path
import java.nio.file.Paths

@SourceURI
URI sourceUri

Path scriptLocation = Paths.get(sourceUri)
println(scriptLocation)                     // path to the current executable
println(scriptLocation.getParent())         // parent dir
println(scriptLocation.resolveSibling('tools.gvy'))  //sibling of the current executable

File.createTempFile("temp",".tmp").with {
   //deleteOnExit()  // Including this line will cause the temp file to be deleted automatically

   write "Hello world"    // write to the temp file
   println absolutePath   // This is the path to the file
}

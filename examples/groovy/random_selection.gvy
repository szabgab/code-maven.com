def z = ["a", "b", "c", "d", "e"]
Random rnd = new Random()

for (i=0; i < 10; i++) {
   println(z[rnd.nextInt(z.size)])
}

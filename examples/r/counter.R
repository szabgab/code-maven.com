filename = "count.txt"
count = 0

if (file.exists(filename)) {
    as.numeric(readLines(filename)) -> count
}

count <- count + 1

cat(count, end="\n")

fh <- file(filename, "w")
cat(count, end="\n", file = fh)
close(fh)



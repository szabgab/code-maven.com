package main

import (
    "fmt"
    "os"
    "bufio"
    "strconv"
    "strings"
)

func main() {
    filename := "counter.txt"
    var fh *os.File

    counter := 0
    _, err := os.Stat(filename)
    if !os.IsNotExist(err) {
        fh, _ = os.Open(filename)
        reader := bufio.NewReader(fh)
        var line string
        line, err := reader.ReadString('\n')
        if err != nil {
            fmt.Println("error")
            fmt.Println(err)
            os.Exit(1)
        }
        line = strings.TrimSuffix(line, "\n")
        counter, err = strconv.Atoi(line)
        if err != nil {
            fmt.Println("error")
            fmt.Println(err)
            os.Exit(1)
        }
    }

    counter++
    fmt.Printf("%d\n", counter)

    fh, err = os.Create(filename)
    if err == nil {
        fh.WriteString(fmt.Sprintf("%d\n", counter))
        fh.Close()
    }
}

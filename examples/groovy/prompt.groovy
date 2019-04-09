
def prompt(text, Integer cnt) {
    def pw = 'secret'
    while (cnt > 0) {
        res = System.console().readLine text
        if (res == 'secret') {
            return true
        }
        cnt--
    }
    return false
}

def prompt(text) {
    prompt(text, 3)
}

// println(prompt('Password: ', 2))
println(prompt('Password: '))


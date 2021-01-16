import time

test = "abc"
alpha = "abcdefghijklmnopqrstuvwxyz"
numerics = "0123456789"
accents = "éàçèù"
programming = "()[]{}~\"\'\\"
internet = "&@"
punctuation = ":;.?,"
mathematic = "%*/!+=-"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


alphabet = alpha + numerics

start_time = time.time()

def searchPassword(alphabet, password, maxDepth, word="", currentDepth=1):
    if currentDepth > maxDepth:
        return False
    for letter in alphabet:
        if word + letter == password:
            print(word+letter)
            return True
        if searchPassword(alphabet, password, maxDepth, word + letter, currentDepth + 1):
            return True
    return False

password = "jfj2"

maxDepth = len(password)

asnwer = searchPassword(alphabet, password, maxDepth)

end_time = time.time()
print("Execution time: " + str(end_time - start_time))


print (str(asnwer))
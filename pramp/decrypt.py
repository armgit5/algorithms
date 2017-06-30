word = "dnotq"

def decrypt(word):
    prev = 1
    result = ""

    for i in range(len(word)):
        ascii = ord(word[i])
        diff = ascii - prev

        while diff < ord('a'):
            diff += 26

        result += chr(diff)
        prev = ascii
    return result

print(decrypt(word))

print(ord("a"), ord("z"))

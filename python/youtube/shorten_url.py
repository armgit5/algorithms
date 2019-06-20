# https://www.youtube.com/watch?v=_28Kei8hhF0
# Shorten url to 6 digits
# If base 10 (000001 - 999999) = 10^6 possibilities or 1 mil
# Need base 62 0-1 a-z and A-Z = 62^6 possibilities or 56800235584


class URL_Shortener:
    url2id = {}
    id = 1

    def shorten_url_base10(self, original_url):

        if original_url in self.url2id:
             shorten_url = str(self.url2id[original_url])
        else:
            self.url2id[original_url] = self.id
            shorten_url = str(self.id)
            self.id += 1
        return "short_url.com/" + shorten_url



    def shorten_url_base62(self, original_url):

        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten_url = self.encode(id)
        else:
            self.url2id[original_url] = self.id
            shorten_url = self.encode(self.id)
            self.id += 1
        return "short_url.com/" + shorten_url

    def encode(self, id):
        # base 62 characters
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)

        ret = []

        # Loop to find the index of id in characters
        # id 0-61 = 0-Z, if id = 62 -> id = 10
        while id > 0:
            val = id % base
            ret.append(characters[val])
            id = id // 62

        return "".join(ret[::-1]) # Convert ["0", "1"] to 10



shortener = URL_Shortener()
print(shortener.shorten_url_base10("google.com"))
print(shortener.shorten_url_base10("google.com"))
print(shortener.shorten_url_base10("test.com"))
print(shortener.shorten_url_base10("hello.com"))

print("")

print(shortener.shorten_url_base62("google.com"))
print(shortener.shorten_url_base62("google.com"))
print(shortener.shorten_url_base62("test.com"))
print(shortener.shorten_url_base62("hello.com"))




# https://leetcode.com/problems/longest-string-chain/
# https://www.youtube.com/watch?v=zqe_zIkyVGQ

# O(L*A*L)
# for(position): -1 to L-1
#     for(newChar): # a-z
#         s = A[0..pos] + newChar + A[pos+1..]
# add char to A

chars = 'abcd'

def longestStrChainBruteForce(words):
    words.sort(key=lambda x: len(x))
    arr = [words[0]]

    for i in range(0, len(words)-1): #a b ba...
        w = words[i] # a
        nextW = words[i+1] # b
        for p in range(0, len(w)+1): # 0 to 1 for a
            for c in chars: # a to z
                s = w[:p] + c + w[p:] # -1 a -> a 1... ba -> ab
                if s == nextW:
                   arr.append(nextW)

    print(arr)

# O(L*L)
# for(position): -1 to L-1
#     s = B[0..pos-1] + B[pos + 1]
#          if (s==A) -> we have a match
# removing one from B
def longestStrChainBruteForce2(words):
    words.sort(key=lambda x: len(x))

    hash = {}

    for j in range(0, len(words)):
        tmpW = words[:j] + words[j+1:]

        if words[j] not in hash:
            hash[words[j]] = 1

        for i in range(0, len(tmpW)):
            nextW = tmpW[i] # b

            if len(nextW) > len(words[j]):
                for p in range(0, len(nextW)): # 1 to last
                    s = nextW[:p] + nextW[p+1:] # -1 a -> a 1... ba -> ab
                    if s == words[j]:
                        hash[nextW] = hash[words[j]] + 1
                        break

    maxKey = max(hash, key=lambda key:hash[key])
    print(hash[maxKey])

# https://leetcode.com/problems/longest-string-chain/discuss/511235/Python-solution-O(N)
def longestStrChain(words):

    mmap = {}
    wordBags = [set() for i in range(17)]
    for word in words:
        if len(word) == 1:
            mmap[word] = 1
        else:
            wordBags[len(word)].add(word)

    # print(wordBags)
    # i = 0
    # for wordBag in wordBags:
    #     print(i, wordBag)
    #     i += 1

    for wordBag in wordBags:
        for word in wordBag:
            currentMax = 1
            for i in range(len(word)):
                possiblePre = word[:i] + word[i + 1:]
                if possiblePre in mmap:
                    currentMax = max(mmap[possiblePre] + 1, currentMax)

            mmap[word] = currentMax

    print(max(mmap.values()))



# output 4
words = ["a","b","ba","bca","bda","bdca"]
# longestStrChainBruteForce(words)
# longestStrChainBruteForce2(words)
# longestStrChain(words)

# expect return of 7 ['czvh', 'zczvh', 'zcpzvh', 'zczpzvh', 'zczpzvhx', 'zczpzvdhx', 'zczpzfvdhx']
words = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
# longestStrChainBruteForce(words)
# print(sorted(words, key=lambda x: len(x)))
# longestStrChainBruteForce2(words)
# longestStrChain(words)


# expect return of 6 ['sgtz', 'sgtnz', 'srgtnz', 'srqgtnz', 'srqgotnz']
words = ["sgtnz","sgtz","sgz","ikrcyoglz","ajelpkpx","ajelpkpxm","srqgtnz","srqgotnz","srgtnz","ijkrcyoglz"]
# longestStrChainBruteForce2(words)
# longestStrChain(words)


words = ["kwigbkfeqp","tpiufntqzo","blmwegckaplqwjpo","uiesdrhcbvbbk","przuvuo","kntmjgnqbxlwh","glac","uz","qqhw","gdtunmaw","neymepxl","eqtxh","qz","bek","xgadqztq","cicgtxs","grakdthb","kwigbkfeqop","uqyqhjqwegizcx","kewiygbkfejqop","tufntz","gulamac","sluiobdm","ujdyugagn","fuyz","eth","vzxiobwgyhrdkh","ikfjaivyvreql","jimpyin","cuotmvfqzizu","tkopssxh","gmwmzsowjf","nel","zo","kntmmjgnqbxtlwh","cyuicglbdtxwsu","vjrenjwntklm","uevrxuklobce","tkaopssxh","rwkedydnadd","uqyqhjqdwegizcx","ouethhse","zcmmrtilpti","tmfuxxyk","honyw","nyepl","qqhqwix","mjhg","gdtwunmaw","kigbkfeqp","wnyhsm","oeqatxhree","qyqhjqweizcx","xadqztq","wqnyghsmt","ndozeaylmetnpxlj","przuvuhob","wqnlyghnqsmtt","tkossxh","qyqhjqwix","epwcjxytvt","bexk","ga","em","zojodbw","gulmac","cizocgw","suibdm","nvcyutywhus","bwjofkuchx","f","pdtwv","dzohajcodbw","kuc","tpawplvfzlx","mg","re","oh","wciqob","el","wciqo","mftmgv","grakkdthtbd","cnbnyvuhmrj","odqphbhkf","oeqatxhre","sqzrlhs","bwsjofvkuptchx","xdqztq","tmv","kewigbkfejqop","faepomn","bdwwnalubrvxtdgu","cotmfqziz","lvzl","dmqz","hdmqz","gdigs","ujdyugag","mepjqbuvdku","g","kigbkeqp","oegqataxhree","zscinzobcgtwdwhn","fuaepwobimn","qf","cusotmvfqziknzu","qvroffuk","rweydnadd","zoow","meqcfzkbnrb","tpaplvzlx","zscinzocgwdwhn","zcmmrtilpt","ndeaymenpxlj","jimpn","wofkuchx","tkaopsssxh","vodwqphbhkfx","faepwoimn","gzenkasrciui","nyhm","tpufntqzo","ovqeyvxfdll","tufntzo","gmyrmf","vxobwgrdkh","faepwobimn","przujvuhobk","vzxobwgyrdkh","ksszdumgko","kewiylgbkfejqop","rey","vo","qqfe","moyddffrwwyzk","qzwsbnuejvsi","vodwqpzhbhjkfx","r","vttpoelti","sqzrlehhs","tpiuftntqzo","qfe","qyvsrofgnfuk","evxuklce","wiqo","prpzuujvuaxhkobk","gy","vnjxkjvmz","qroffuk","qqhwi","przuvuhobk","mfttmgvj","moydfrwzk","jibmpuyin","pwcytvt","eqtxhre","gcdtwunmaw","wfkucx","ryedhy","vttpolti","qyqhqwix","kutkavldvvqvp","el","tmfuxxyku","tplvzlx","gdtu","z","ksg","xmgadqzptq","qcqfre","zcmmrtiklpti","hobxltexk","vburq","funyz","kc","vjrenjwntklqm","wqnlyghnqsmt","sibdm","vodwqpzhbhkfx","zsnv","pouegzfyk","arci","vzxobwgyhrdkh","fetoesaot","riyedhy","cyuicgtxsu","gdtua","gchdtwgwunmaw","cuotmvfqziz","obltexk","epwcytvt","scinzocgw","ptwv","jimpuyin","uevrxukloce","tkqaopsssxh","pdtwdv","fetsaot","cyuicgldtxsu","przujvuaxhkobk","wciqoxb","gdtuna","lvzlx","ytpawcplvfzlx","uyugag","ksszdumugiko","bm","pgdmigs","grakdthtbd","uyz","zscinzobcgwdwhn","oeqataxhree","qzsbnuvs","gznkarciui","zoodw","jimpin","tqksugh","zuvo","tmgv","gdmigs","sluibdm","nvcxyzwyutywhus","bwsjofkuchx","fetsat","kgbeqp","neymenpxlj","vzxobwgrdkh","tpawcplvfzlx","qbzwsbnuejvsi","przuvuho","wqnlyguhnqsmtt","ujhadylujgaazgsn","axuelrnnnwhg","qbzwsbnuejvsmoi","qzsbnuvsi","yugag","bwsjofvkupchx","mqz","gchdtwunmaw","kntmmjgnqbxlwh","xfpt","vvburq","moydfrwk","qksgh","faepoimn","odwqphbhkfx","ryey","gchdtwwunmaw","uiesdrhcvbbk","qyqhjqwicx","yilxbltwwxh","jrenjwntkm","gzenkarciui","moyddffrhwwyezk","tqksugvhr","oveyvxfl","agmyrmf","scinzocgwdn","neymenpxl","gonpxzngjv","rwkeydnadd","zohjodbw","bdwwnalubvxtdgu","jrenjwntk","ovqheyvxubfdtll","qcqfqrezof","znkarcii","b","qzsnuvs","ndzeaylmenpxlj","tossxh","fetsa","przujvuxhkobk","ovqeyvxubfdll","tpufntzo","cuicgtxs","mv","vbur","moyddffrhwwyzk","yilxcbltwwxh","eqtxhe","zow","qbzwsbnuejvsoi","nvczwyutywhus","cyquicglbdtxwsu","evxukce","axuelrnnwhg","aci","ouemthhqse","wfkuchx","bwsjofvkmuptchx","mfjhg","bwsjofvkuchx","qffu","qyqhjqwegizcx","rzuvuo","uvo","qh","qvsrofgfuk","neymepl","mepjqybuvdku","sqzrlehs","cnbnyvumrj","qcqfqrezoif","gyrm","przujvuhkobk","cuotmvfqzinzu","gym","ujdylujgaagn","thdmmqz","honw","odwqphbhkf","ksszgko","qbzwsbnuejvsmvoi","m","gtu","qyvsrofgfuk","uqqyqhjqdwegizcx","obtexk","hobltexk","ftmgv","bwsjofvkmuptchxy","taynfxo","tqksugvhrc","jibmpduyin","vxue","zuvuo","gonpxzngv","gmpwamzsowjf","rwednadd","zv","tosh","pqdtwdv","zcmmrtsiklpti","tkqaopesssxh","ovqeyvxbfdll","gac","gsqzrlehhs","znv","cuotmvfqziknzu","ryedy","vnjoxkjvmz","pouegnzfyk","evrxuklce","ujdyujgagn","tmfnuxxyku","semj","xmgadvqzptq","cnnyvmrj","gonpxzvngjv","meqczkbnrb","bwofkuchx","fuvnyz","znarci","moydffrwzk","kwigbkfejqop","wqnyghnsmt","uiesdrehcbvobbk","qcqfreo","zohajodbw","nvcxyzwyutywhuhs","scinzocgwdwn","ksyszdumugiko","qfu","mjg","zsnuvs","eqth","ccgtxs","pgdmidtgs","rwednad","lel","cusotmvfqzwiknzu","znkarciui","o","qzsbnuevsi","veodwqpzhbhjkfx","jrenjwntklm","gmwamzsowjf","ndeymenpxlj","moydffrwwzk","nvczyutywhus","dzohajodbw","ujadylujgaazgsn","nvcytywhus","qcqfrezo","mfttmgv","tqksugvh","qksg","njxkjvmz","udyugag","qffuk","ksszdugko","wkuc","tmfxxyk","qqh","sbdm","rwedna","ovqheyvxubsfdtll","ndzeaymenpxlj","neyepl","qf","xgadqzptq","redna","pougzfyk","zarci","mftbtmgvj","taplvzlx","uiesdrhcbvobbk","ovqeyvxfdl","qcqfrezof","qvrofgfuk","scizocgw","mftbtmgvdj","rsgwmsted","ovqheyvxubfdll","oveyvxfdl","m","wi","znkarci","ikfjaivyvrql","pgdmidgs","btexk","cuotmfqziz","xdqzq","jimp","qqhqwi","lvz","ilojawyersju","wnyhm","gsqzrlenhhs","bu","wkucx","bdm","lsel","tpawplvzlx","ai","kntmmjognqbxtlwh","hkonyw","vxuce","zsnvs","qyqhjqweicx","nyel","cyuicgtxs","qzsbnuejvsi","ujadylujgaagsn","thdmqz","ilojawyersu","uevirxuklobce","qrffuk","zoodbw","sem","cyuicgldtxwsu","wnyhsmt","prpzujvuaxhkobk","uesdrhcvbbk","vhvburq","ndzeaylmetnpxlj","ksszdgko","scinzocgwd","cyuicgltxsu","ptw","mplaxm","scinzocgwdwhn","ytpawcplvifzlx","evxuce","bur","kigbeqp","ksszdumugko","cnnyvumrj","toh","kewiylgbkfejqfop","gulac","pugzfyk","nvcyzwyutywhus","ouemthhse","wqnyghnqsmt","b","ujdylujgagn","tlvzlx","pgidmidtgs","eqatxhre","gmyrm","dqzq","oveyvxl","vttpoeltci","gk","wqnyhsmt","zcmmrtsitklpti","iaxuelrnnnwhg","gdtunma","ujadylujgaagn","tqksgh","moydffrwwyzk","mfftbtmgvdj","wio","fetosaot","grakdthtb","nxmrvm","evrxukloce","ikfjaivyrql","tosxh","grakkbdthtbd","epwcxytvt","blmwegckaplwjpo","qcqfe"]
# print(sorted(words, key=lambda x: len(x)))
# longestStrChainBruteForce2(words)
longestStrChain(words)
# print(len('qbzwsbnuejvsmvoi'), len('kewiylgbkfejqfop'))


# h = {'a': 1, 'b': 20, 'c': 3}
# print(max(h, key=lambda key:h[key]))
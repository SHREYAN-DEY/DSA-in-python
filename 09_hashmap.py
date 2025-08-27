def anagram(str):
    hash = {}
    for char in str:
        count = str.count(char)
        hash[char] = count
    return hash



st1 = "racecar"
st2 = "carrace"

hash1 = anagram(st1)
hash2 = anagram(st2)

# print(hash1)
# print(hash2)

if hash1 == hash2 :
    print("the strings are anagram")
else:
    print("They are not anagram")
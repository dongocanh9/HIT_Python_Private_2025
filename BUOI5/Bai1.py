import string
def remove_punctuation(s):
    return "".join([c for c in s if c not in string.punctuation])

s = input("Nhập 1 chuỗi s bất kì: ")
print("Chuỗi sau khi loại bỏ dấu câu là:", remove_punctuation(s))

def to_lower(s):
    return s.lower()

print(to_lower(s))

def remove_stopwords(s, stopwords):
    return " ".join([word for word in s.split() if word not in stopwords])

s = input("Nhập 1 chuỗi bất kì : ")
stopwords = ["is", "a", "this"]
print(remove_stopwords(s, stopwords))

def count_words(s):
    words = s.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

s = input("Nhập 1 chuỗi bất kì: ")
print(count_words(s))


    




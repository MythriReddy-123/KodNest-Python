n = int(input())
word_frequency = {}

for _ in range(n):
    word = input().strip()
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

for word, count in word_frequency.items():
    print(word, count)
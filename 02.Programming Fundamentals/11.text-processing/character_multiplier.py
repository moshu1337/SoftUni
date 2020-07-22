two_strings = input().split()

word1 = two_strings[0]
word2 = two_strings[1]
total_sum = 0
smaller_length = min(len(word1), len(word2))

for i in range(smaller_length):
    total_sum += ord(word1[i]) * ord(word2[i])

long_word = word1
if len(word2) > len(word1):
    long_word = word2

for n in range(smaller_length, len(long_word)):
    total_sum += ord(long_word[n])

print(total_sum)
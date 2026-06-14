'''Task 3: Word Frequency Counter (Medium)
Objective

Count how many times each word appears.'''
sentence = 'This is a sample sentence. This sentence is for testing the word frequency counter.'
word_count = {}
for word in sentence.split():
    word = word.strip('.').lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word Frequency:")    
for word, count in word_count.items():
    print(f"{word}: {count}")
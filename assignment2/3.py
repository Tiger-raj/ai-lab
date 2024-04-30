#Read a text file, count the frequency of each word, and print the top 10 most frequent words along with their counts.
from collections import Counter

#function to count the words in given file
def count_words(file_path):
    # read the file
    with open(file_path, 'r') as file:
        text = file.read()

    # remove punctuation and convert to lowercase
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    text = text.lower()

    # count the frequency of each word using Counter function
    word_counts = Counter(text.split())

    # print the top 10 most frequent words
    print('The top 10 most frequent words are:')
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

# call function 
count_words('example.txt')

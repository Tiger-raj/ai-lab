#program that accepts sentence as input and reverses each word and then reverses the entire sentence in python
def reverse_sentence(sentence):
    # Split the sentence into words stored in list
    words = sentence.split()

    # Reverse each word in the list words
    reversed_words = [word[::-1] for word in words]

    # Reverse the entire list & join to form reversed sentence
    reversed_sentence = ' '.join(reversed_words[::-1])

    return reversed_sentence

#user input for sentence
sentence = input("Enter Sentence to reverse:")

reversed_sentence = reverse_sentence(sentence) #call function reverse_sentence() to reverse the sentence 

#print the reversed sentence
print("Modified sentence is : ",reversed_sentence)

string = "Hello World"                  # Input string
new_string = ""                         # Empty string to store the new string
for i in range(len(string)):            # Loop through the string
    if i % 2 == 1:                      # If the index is odd
        new_string += string[i].upper() # Add the uppercase letter to the new string

    else:                               # If the index is even
        new_string += string[i].lower() # Add the lowercase letter to the new string

print(new_string)                       # Print the new string

# Output: hElLo wOrLd

sentence = "I am learning to code"  # Input sentence
words = sentence.split()            # Split the sentence into words
if i % 2 == 0:
    new_words = [words[i].lower()  
                 
else: 
    words[i].upper() for i in range(len(words))]
new_sentence = " ".join(new_words)  # Join the words into a sentence
print(new_sentence)

# Output: i AM learning TO code






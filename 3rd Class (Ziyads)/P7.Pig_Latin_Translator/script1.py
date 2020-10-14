#Get sentence from user
original = input("Please enter a sentence: ").strip().lower()

#Split sentence into words
words = original.split()

#Loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        consonates = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + consonates + "ay"
        new_words.append(new_word)        

#Stick words back together in a sentence
output = " ".join(new_words)

#Output final string
print(output)
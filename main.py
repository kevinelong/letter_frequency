def letter_frequency(text):
    output = {}
    for letter in text:
        if letter not in output:
            output[letter] = 1
        else:
            output[letter] += 1
    return output


print(letter_frequency("This is a sample sentence to use for counting letter frequency."))

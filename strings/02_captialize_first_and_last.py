def capitalize_first_last(string):
    words = string.split()
    captialize = []

    for word in words:
        if len(word)>1:
            captialize_word = word[0].upper()+word[1:-1]+word[-1].upper()
        else:
            captialize_word = word[0].upper()
        captialize.append(captialize_word)
    captialize_string = " ".join(captialize)
    return captialize_string

input_string = "take u forward is awesome"
output_string = capitalize_first_last(input_string)
print(output_string)
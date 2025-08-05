word = input("Enter a sentence:")
w_list = word.split()
end_sentence = ""

result = ""
resultarray = []

for bean in w_list:
    wordlist = list(word)
    wordlist[0] = "b"
    result = end_sentence.join(wordlist)
    resultarray.append(result)
    

final = " ".join(resultarray)

print(final)
    


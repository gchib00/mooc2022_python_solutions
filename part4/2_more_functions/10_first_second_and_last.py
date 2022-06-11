# Write your solution here
def first_word(string):
    first_space = string.find(" ")
    return string[0:first_space]
def second_word(string):
    sub_string = string[len(first_word(string))+1:]
    second_space = sub_string.find(" ")
    if second_space != -1:
        return sub_string[0:second_space]
    return sub_string[0:]
def last_word(string):
    last_space = string.rfind(" ")
    return string[last_space+1:]
if __name__ == "__main__":
    sentence = "once upon"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
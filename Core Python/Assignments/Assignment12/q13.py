# 13. Python Program to count the occurrences of each word in a string.

def wordOccurrences(string):

    checked = ""
    word = ""

    string += " "      # Add one space at the end

    for ch in string:

        if ch != ' ':
            word += ch

        else:

            if word not in checked:

                count = 0
                temp = ""

                for ch2 in string:

                    if ch2 != ' ':
                        temp += ch2
                    else:
                        if temp == word:
                            count += 1
                        temp = ""

                print(word, ":", count)

                checked += word + " "

            word = ""


string = input("Enter the String: ")
wordOccurrences(string)
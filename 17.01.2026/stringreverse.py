class StringReverse:
    def __init__(self, text):
        self.__text = text   # private variable (encapsulation)

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)


# Example usage
sentence = input("Enter a sentence: ")
obj = StringReverse(sentence)
print("Reversed sentence:", obj.reverse_words())

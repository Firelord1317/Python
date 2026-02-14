class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

        num = self.number
        roman = ""

        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]

        return roman


# Example usage
number = int(input("Enter an integer: "))
converter = IntegerToRoman(number)
print("Roman Numeral:", converter.convert())

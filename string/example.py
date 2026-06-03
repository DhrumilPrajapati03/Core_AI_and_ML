letter = '''congratulations {name},
            you're selected as SDE,
            and your joining date is {date}
            Thank you'''

name = input("enter the name: ")
date = input("enter the date: ")

letter = letter.replace("{name}", name)
letter = letter.replace("{date}", date)

print(letter)


letter = '''congratulations'''

print(letter[0::2])
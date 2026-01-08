blank = ""
space = "      "
name = "Kostya"
email = "stadnyk@gmail.com"
python_code = "print(" + name + ", " + email + ")"
book_title = "lord of the rings"
print(python_code)
print(name)
print(email)
print(blank)
print(space)

print(book_title.capitalize())

print(book_title.count("o"))
print(email.count("@") == 1)

print(book_title.replace("lord", "port"))

print(book_title.startswith("lord"))

print(book_title.endswith("rings"))

print(book_title.index("of")) #5
print(book_title.index("port")) #ValueError: substring not found

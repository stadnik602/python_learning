def say_message(my_name, age, language = "Python"):
    print("Hello World")
    print(f"My name is {my_name}")
    print(f"My age is {age}")
    print(f"I'm Learning {language}")

say_message("Kostya", 18, "Ruby")
say_message("Dmytro", 15)
say_message("Kostya", 18, "Java")

say_message(language="C#", age=17, my_name="Mark")

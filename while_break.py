qs = ["What is your name?",
      "What is your fav. colour?",
      "What is your Quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == 'q':
        break
    n = (n + 1) % 3
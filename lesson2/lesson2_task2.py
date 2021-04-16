name = "Artem"
surname = "Shestak"

# 1
print("Hello " + name + " " + surname + ". How are you doing?")

# 2
print("Hell0 {0} {1}. How are you doing?".format(name, surname))

# 3
print("Hello %s %s. How are you doing?" % (name, surname))

# 4
s = "Hell0 {} {}. How are you doing?"
print(s.format(name, surname))

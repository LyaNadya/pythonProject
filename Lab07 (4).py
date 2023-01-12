#Lab07 part 4
f = open("myContact.txt")
print(f)

#write in text mode
f = open("myContact.txt", "w")
f = open("myContact.txt", mode = "w", encoding = "utf-8")
print(f)

f.close()
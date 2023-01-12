#Lab07 part 5
try:
    f = open('myContact.txt', encoding = 'utf-8')
    #perform file operations
    print(f.readlines())

except:
    print('Error')
finally:
    f.close()


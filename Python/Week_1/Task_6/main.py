import firelink

while True:
    website = input("Choose website number:\n 1- Facebook\n 2- Youtube\n")
    firelink.firefox(website)
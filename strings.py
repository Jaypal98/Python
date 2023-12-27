s = "Tops Technologies"
print(s)
print(len(s))
print(s.capitalize())
print(s.casefold())
print(s.upper())
print(s.lower())
print("parmar jaypal".title())
print(s.swapcase())
""" 40 na space na centre ma top technology print thase ane vadhela ma star print thase"""
print(s.center(40,"*")) 
""" count chractre in String """
print(s.count("o"))
"jo string es sathe end thase to true and end es sathe nai hoy to false "
print(s.endswith("es"))
"string To thi start thase to true jo nai hoy to false"
print(s.startswith("To"))
""" string kaya index par che te show karshe """
print(s.find("log"))
""" find from 4th string """
print(s.index("T",4))

print("tops123".isalnum())
print("tops 123".isalnum())
print("tops".isalnum())
print("123".isalnum())  
print("tops".isalpha())
print("123".isnumeric())
print("  ".isspace())
print(s.istitle())
print("tops".islower())
print("TOPS".isupper())
""" hello string l replace to w """
print("Hello".replace("l","w"))
""" in string for every chracter in new line"""
for i in s :
    print(i)



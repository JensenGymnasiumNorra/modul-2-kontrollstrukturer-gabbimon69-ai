"""
Låt användaren mata in sitt namn och ålder. 
Välkomna användaren till programmet och skriv ut ett meddelande baserat på dens ålder.
Det ska finnas minst 3 olika meddelanden som kan skrivas ut baserat på åldern.

Exempel på utskrift, det inom () ska ändras om variablerna ändras:
Hej (Ulrika)!
Oj vad du är gammal.
"""
name=input("what is your name. ")
age=int(input("how old are you"))
if age > 17:
    print(f"hello {name}, you are old as shit")
if age < 17:
    print(f"Hello {name}, you are a fine young man")
if age<18:
    print(f"GoGo GaGa {name}. Go back to kindergarden")
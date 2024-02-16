palabra=input()
palabra_inv= palabra [::-1]
if palabra == palabra_inv:
    print ("es palindromo")
else:
    print ("no es palindromo")
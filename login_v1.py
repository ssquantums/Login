def logowanie():
    b = ["mops", "szmops", "zmops"]
    a = input("username:")
    while a not in b:
        print("wrong_login")
        a = input("username:")
    else:
        print("good")
        return True  
def kod():
    z = {"mops": "119", "szmops": "111", "zmops": "173"}
    a = input("username:")
    while a not in z:
        print("wrong_username")
        a = input("username:")
    else:
        d = input("password:")
        while d != z[a]:
            print("wrong_password")
            d = input("password:")
        else:
            print("good_password")
if logowanie():  
    kod()
else:
    print("error_1")
print("end")





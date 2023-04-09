def login():
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
           print("authorized")
login()
print("its_2023!")

        
        

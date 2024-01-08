
name = str(input("Enter your name: "))

age = int(input("Enter your age " + name.capitalize() + ": "))

if age >= 18:
    print("Hello, " + name.capitalize()+ "! " + "You are " + str(age) + " years old!")
else:
    print(name.capitalize() + ", you are not 18 years old! " + "Wait another", int(18 - age), "years!")


    # claim = tk.Label(window, text="After sign up, you can claim your gifts!", font=("Arial Bold", 15), fg="White", bg="#203255")
# claim.place(x=175, y=230)

# button2 = tk.Button(window, text="Claim gifts", width='20', font=("Arial Bold", 9), height='2', bg="#203255", fg='White')
# button2.place(x = 280, y=270)


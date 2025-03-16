class chat:
    contact={'Anubhav':764456225, 'Puja':7653165372, 'Aditya':21341251543 }
    via='Enter the class name:'
class facebook(chat):
    send=input("Enter the name::  ")
    if send in chat.contact:
        message=input("Enter the message::    ")
        print(message,'Your msg has been sent to the recipent via facebook ::', send)
    else:
        print("Recipent name not found")
class instagram(chat):
    send=input("Enter the name::  ")
    if send in chat.contact:
        message=input("Enter the message::    ")
        print(message,'Your msg has been sent to the recipent via instagram::', send)
    else:
        print("Recipent name not found")

#obj=facebook()
obj1=instagram()
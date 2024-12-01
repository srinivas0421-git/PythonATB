# #Global and local varaible
# # The varaiable which are declared in and outside of the function and which is called in and outside
# # function is called Global variable
#
#
# def Outer_Function():
#     a = 10
#     print(a)
#     def inner_function():
#         print(a)
#     def inner_function2():
#         print(a)
#
#
#     # calling inner function
#     inner_function()
#     inner_function2()
# Outer_Function()
#Decorators
def add_extra_security(func):
    def wrapper():
        print("1.Before the function is called")
        print("2.add Helment,Daswash,gloves,knee pads")
        func() #@add_extra_security
        print("3.After the function is called")
        print("4.sercure driving,leave all the items")
    return wrapper()
@add_extra_security
def drive_ola_Scooter():
    print("drive ola")

@add_extra_security
def driving_Scooty():
    print("Noraml Function!")
    print("I am driving a scooty")
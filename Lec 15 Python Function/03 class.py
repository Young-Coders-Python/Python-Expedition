# phone is a class
# when iPhone inherit phone class, then phone class is called parent class / super class / base class
class phone:
    # Inside class the functions are called method
    def call():
        print("Call is posiible")

    def message():
        print("Message is possible")

print(phone)
phone.call()
phone.message()

# iPhone is a class
# when iphone inherit phone class then iphone is called child class / sub class / derived class
# when iphone inherit properties from parent class phone, we have to write parent class inside parenthesis
class iPhone (phone):
    def camera():
        print("Camera is working to get photo")

iPhone.camera()
iPhone.message()
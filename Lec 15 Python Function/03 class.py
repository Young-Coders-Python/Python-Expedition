# phone is a class
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
class iPhone (phone):
    def camera():
        print("Camera is working to get photo")

iPhone.camera()
iPhone.message()
# Uygulama - Mülakat Sorusu

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    newString = ""
    for stringIndex in range(len(string)):
        if stringIndex % 2 == 0:
            newString += string[stringIndex].upper()
        else:
            newString += string[stringIndex].lower()
    print(newString)

alternating("hi my name is john and i am learning python")
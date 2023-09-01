#შექმენით ფუნქცია, რომელსაც გადაეცემა კვადრატის გვერდი და დაპრინტავს მის ფართობს და პერიმეტრს.

gverdi = int(input("sheiyvanet kvadratis gverdi : "))

def kvadrati(square):                                    #კვადრატის პერიმეტრი
    print("kvadratis perimetria :" ,square * 4)

kvadrati(gverdi)



sigrdze = int(input("sheiyvanet martkutxedis sigrdze : "))
sigane = int(input("sheiyvanet martkutxedis sigane : "))

def martkutxedi(sigrdze , sigane):
    print("kvadratis fartobia :" , sigrdze * sigane)

martkutxedi(sigrdze , sigane)

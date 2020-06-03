import math

#Constants and Input Prompts

print("\nHello There, This is a program to calculate the different"
      " SAR values for various tissues of the human body\n")
while True:
    Band = input("Which Radio Frequency technology are we calculating for?\n A. GSM 800/900 \n B. GSM 1800/1900 \n C. 3G: \n")
    if Band == "A":
        print("Calculations for GSM 800/900 technology: \n")
        l_cond = 0.17
        freq1 = 880
        freq2 = 915
    elif Band == "B":
        print("Calculations for GSM 1800/1900 technology: \n")
        l_cond = 0.26
        freq1 = 1710
        freq2 = 1785
    elif Band == "C":
        print("Calculations for 3G technology: \n")
        l_cond = 0.26
        freq1 = 1920
        freq2 = 1980
    break



Choice = input("Enter the tissue name and details to be analysed:   {Skin, Fat, Bone, Brain}")
impedance = float(input("Enter impedance of tissue: "))
conduc = float(input("Enter conductivity of tissue: " ))
density = float(input("Enter density of tissue: " ))
distance = float(input("Enter distance from the tissue surface in meters: " ))

permitv = float((8.84194)*(10**(-9)))
print("Value of permittivity:", permitv)
permeab = float((1.256637)*(10**-6))
print("Value of permeability:", permeab)

print("Lowest conductivity: ", l_cond)
print('\n')

Gt = 1 #Gain at transmitter

if Choice == "Brain":
    Pt = 0.09167
else:
    Pt = float(2/8) #Power transmitted

#calculate center frequency
f1 = float(freq1*(10**6))
f2 = float(freq2*(10**6))
c_freq = float((f1 + f2)/2)
print("LowerBand frequency is: ", f1, "Hz")
print("UpperBand frequency is: ", f2, "Hz")
print("The centre frequency is:", c_freq, "Hz")

#calculate skin depth (using lowest conductivity)
if Choice == "Brain":
    sk_depth = 0.08C1
else:
    sk_depth = float(1/(math.sqrt(c_freq*l_cond*permeab*math.pi)))

print("Skin depth is: ", "%.6f" %sk_depth, "Meters")

#Calculate power density
d = float(sk_depth + distance)
S = float((Pt*Gt)/(4*math.pi*pow(d, 2)))
print("Power Density: ", "%.3f" %S, " W/m^2")

#Calculate Electric field Intensity
E_square = float(S * impedance)
print("Value of electric field intensity is :", "%.3f" %E_square)

#Compute the SAR
Sar = float((conduc*E_square)/(2*density))
print("The SAR of ", Choice," is: ","%.3f" %Sar ," W/Kg")
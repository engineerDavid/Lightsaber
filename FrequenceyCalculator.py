#Fill to calculate the frequnecy based on R1, R2, and C

#Values needed
R1 = float(input("What is R1?"))
R2= float(input("What is R2?"))
C1 = float(input("What is C1 in uf?"))

C1 = C1*(10**-6)


T1H = 0.693*(R1+R2)*C1

T1L = 0.693*(R2)*C1

T = T1H + T1L

#frequencey
f = 1/T

print(f"The Frequency is {f} seconds")
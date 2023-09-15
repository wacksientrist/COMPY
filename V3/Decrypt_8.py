import math
import itertools

# Define Functions

# get input
def Factor(Input, V0, V1):
  D = 0
  for b in range(len(Input)):
   
    # process input
   
    if Input[b] == "0":
      D = D + math.log(V0[b])
    if Input[b] == "1":
      D = D + math.log(V1[b])
 
  return D
def Nsplit(string, length):
    return " ".join(string[i:i+length] for i in range(0,len(string),length))
# Define Variables
i=1
i1=0
i2=0
 
Val_bin_1 = []
Val_bin_0 = []
Binarys = ["0000", "1000", "0100", "1100", "0010", "1010", "0110", "1110", "0001", "1001", "0101", "1101", "0011", "1011", "0111", "1111", "0000", "1000", "0100", "1100", "0010", "1010", "0110", "1110", "0001", "1001", "0101", "1101", "0011", "1011", "0111", "1111", "0000", "1000", "0100", "1100", "0010", "1010", "0110", "1110", "0001", "1001", "0101", "1101", "0011", "1011", "0111", "1111", "0000", "1000", "0100", "1100", "0010", "1010", "0110", "1110", "0001", "1001", "0101", "1101", "0011", "1011", "0111", "1111"]
print(Binarys)
Data = 0

File2 = open("DATA", "r")
Input = File2.read().removesuffix(" ")
Input = Nsplit(Input, 3)
Input = Input.split(" ")
File2.close()


CP1 = [23.2636, 24.6857, 25.0512] #8 bit


# get primes list
Primes = open("primes2.txt").read()
Primes = Primes.replace("\n", " ")
Primes = Primes.split(None)
Primes.append(0)
 
# split into two lists
while i < 70:
  Val_bin_1.append(int(Primes[i+1]))
  i=i+2
i=1
while i < 70:
  Val_bin_0.append(int(Primes[i]))
  i=i+2

# Decrypt
Data1=""
Data2=""
Data3=""
file = open("DATA", "w")
for G in range(len(Input)):
    Data = Input[G]
    i2 = 0
    while i2 < 64:
                Data1=""
                Data2=""
                Data3=""
                i3 = Factor(Binarys[i2], Val_bin_0, Val_bin_1)
                i3 = str(i3).split(".")
                Data2 = i3[1]
                for i in range(2):
                  Data1 = Data1+Data2[i]
                Data3 = str(i3[0])+Data1
                i3 = Data3
                print(Data1)

                
                if i3 == Data:
                    
                    i3 = Binarys[i2]
                    print(str(i3)+";")
                    file.write(str(i3))
                    
                    i2 = 256
                print(i3)
                i2=i2+1
file.close()
print(Input)
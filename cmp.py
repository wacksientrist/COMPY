import Gen_Lookup
Gen_Lookup.generateAllBinaryStrings(16, [None] * 16, 0)

def Nsplit(string, length):
    return " ".join(string[i:i+length] for i in range(0,len(string),length))

File0 = open("INP", "r")
Input0  = Nsplit(File0.read(), 16).split(None)

for i in range(len(Input0)):
    Input = Input0[i]

    File = open("L_16", "r")
    Bins = File.read()
    File.close()

    File2 = open("OUT", "a")
    File2.write(str(Bins.index(Input))+","+str(len(Input)+Bins.index(Input)))
    File2.close()
File3 = open("L_16", "w")
File3.write("")
File3.close()
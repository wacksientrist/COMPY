import Gen_Lookup
Gen_Lookup.generateAllBinaryStrings(16, [None] * 16, 0)

File = open("L_16", "r")
Bins = File.read()
File.close()

File = open("OUT", "r")
Ads = File.read().split(",")
for i2 in range(int(len(Ads)/2)):
    for i in range(int(Ads[i2]), int(Ads[i2+1]), 1):
        print(Bins[i])
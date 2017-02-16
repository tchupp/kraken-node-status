from subprocess import call
memfile = open("/proc/meminfo", "r")

mem = memfile.readlines()

totalRAM = mem[0].strip("\n").split(" ")[-2]
availableRAM = mem[2].strip("\n").split(" ")[-2]

print(totalRAM)
print(availableRAM)

print (float(availableRAM) / float(totalRAM) * 100)

#for line in memfile:
#	print(line)

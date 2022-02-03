handle = open("mbox.txt",'r')
print(handle)
#for cheese in handle:
#    print(cheese)
#input = handle.read()
#print(input)
#for line in handle:
#    if line.startswith('From'):
#        print(line)
#just stripping off white spaces or new line
for line in handle:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line.upper())

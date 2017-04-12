
entry = raw_input("Please enter your chemical structure....")



mol_database = ["NH4+","COOH","COSH","COSeH","SO3H","SO2H","NH2","NH","NHNH2"]

mol = ""
itr = 0
inc = 0
L = list(entry)
print "Parsed substructures"
while itr < len(entry):
    itr += 1
    L = [entry[i:i + itr] for i in range(0, len(entry), itr)]
    print L
    for  structures in L:
        frag_code = ""
        if structures in mol_database:
            frag_code += "1"
            mol += "1"
            print "STRUCTURES FOUND!: " + structures
        else:
            frag_code += "0"
            mol += "0"
print " Fingerprint for " + entry + ":"
print mol
mol = ""
         
        
    
    
    

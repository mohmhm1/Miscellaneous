print "                       II         II "                        
print "                        II       II    "                      
print "                         II    II    "               
print "                          II II"
print "                          IIII"
print "                         II  II"
print "                      II ======== II"
print "                   II ==============II   "         
print "       ,'|-\  .-. .-. .--.   .-.  .-,-._____   .--. ,---.  ,-|-\   "  
print "       | |\ \ |  \| |/ /\ \  | |/\| |(/___  / / /\ \| .-.\ | |\ \   " 
print "       | | \ \|   | / /__\ \ | /  \ (_)  / /)/ /__\ | `-'/ | | \ \   "
print "       | |  \ | |\  |  __  | |  /\  | | / /(_|  __  |   (  | |  \ \  "
print "       /(|`-' | | |)| |  |)| |(/  \ | |/ /___| |  |)| |\ \ /(|`-' /  "
print "      (__)`--'/(  (_|_|  (_) (_)   \`-(_____/|_|  (_|_| \)(__)`--'   "
print "             (__)                                       (__)             "
print "                  II ================ II          2014 Ahmed Mahmoud "     
print "                  II ================ II"
print "                    II ============= II"
print "                     II ========= II"
print "                        II======II"
print "                            II"
print "                          II  II"
print "                      II ========= II"
print "                    II ==============II"
print "                  II ================ II"
print "                  II ================ II"
print "                    II ============= II"
print "                      II ==========II"
print "                        II=======II"
print "                            II"
print "                          II  II"
print "                        II      II"
print "                      II          II"
print '========================================================================='
print 'Hello welcome to DNA count wizard'
user_input = []
entry = raw_input("Enter text, 'done' on its own line to quit: \n")
while entry != "":
    user_input.append(entry)
    entry = raw_input("")
user_input = ''.join(user_input)
DNA=user_input
print DNA
print '========================================================================='
print '                          Sequence Stats                                 '
print '========================================================================='
print 'lenght of DNA sequence is'
print len(DNA), "Base Pairs Long"
countt = 0
counta = 0
countc = 0
countg = 0
for letter in DNA:
    if letter == 'T':
        countt = countt + 1
print 'Stats Below'
print countt,"total T bases counted", countt/float(len(DNA))*100, "percent in sequence"
for letter in DNA:
    if letter == 'A':
        counta = counta + 1
print counta, "total A bases counted", counta/float(len(DNA))*100, "percent in sequence"
for letter in DNA:
    if letter == 'C':
        countc = countc + 1
print countc, "total C bases counted", countc/float(len(DNA))*100, "percent in sequence"
for letter in DNA:
    if letter == 'G':
        countg = countg + 1
print countg,"total G bases counted", countg/float(len(DNA))*100, "percent in sequence"
print 'percentage of GC regions are'
print (countg+countc)/float(len(DNA))*100 
print '========================================================================='
def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)
def revcom(s):
    return complement(s[::-1])
print "complement"
print(complement(DNA[::1]))
print "reverse complement"
print(revcom(DNA))
def RNA(s):
    RNACONV = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'} 
    letters = list(s) 
    letters = [RNACONV[base] for base in letters] 
    return ''.join(letters)
print "RNA conversion"
print (RNA(DNA)) 
print '========================================================================='
print '                         Amino Acid Stats                                '
print '========================================================================='
codon1 =[]
for start in range( 0, len( DNA), 3 ) :
  codon1.append( DNA[ start : start + 3 ] )
print "1 frame", len(codon1), 'Amino acids long'
print codon1 
codon2 = []
for start in range( 1, len( DNA), 3 ) :
  codon2.append( DNA[ start : start + 3 ] )
print "+2 frame", len(codon2), 'Amino acids long'
print codon2
codon3 = [ ]
for start in range( 2, len( DNA), 3 ) :
  codon3.append( DNA[ start : start + 3 ] )
print "+3 frame", len(codon3), 'Amino acids long'
print codon3 
DNA_table = {
    'TTT': '-Phe', 'TCT': '-Ser', 'TAT': '-Tyr', 'TGT': '-Cys',
    'TTC': '-Phe', 'TCC': '-Ser', 'TAC': '-Tyr', 'TGC': '-Cys',
    'TTA': '-Leu', 'TCA': '-Ser', 'TAA': '-Stop', 'TGA': '-Stop',
    'TTG': '-Leu', 'TCG': '-Ser', 'TAG': '-Stop', 'TGG': '-Trp',
    'CTT': '-Leu', 'CCT': '-Pro', 'CAT': '-His', 'CGT': '-Arg',
    'CTC': '-Leu', 'CCC': '-Pro', 'CAC': '-His', 'CGC': '-Arg',
    'CTA': '-Leu', 'CCA': '-Pro', 'CAA': '-Gln', 'CGA': '-Arg',
    'CTG': '-Leu', 'CCG': '-Pro', 'CAG': '-Gln', 'CGG': '-Arg',
    'ATT': '-Ile', 'ACT': '-Thr', 'AAT': '-Asn', 'AGT': '-Ser',
    'ATC': '-Ile', 'ACC': '-Thr', 'AAC': '-Asn', 'AGC': '-Ser',
    'ATA': '-Ile', 'ACA': '-Thr', 'AAA': '-Lys', 'AGA': '-Arg',
    'ATG': '-Met', 'ACG': '-Thr', 'AAG': '-Lys', 'AGG': '-Arg',
    'GTT': '-Val', 'GCT': '-Ala', 'GAT': '-Asp', 'GGT': '-Gly',
    'GTC': '-Val', 'GCC': '-Ala', 'GAC': '-Asp', 'GGC': '-Gly',
    'GTA': '-Val', 'GCA': '-Ala', 'GAA': '-Glu', 'GGA': '-Gly',
    'GTG': '-Val', 'GCG': '-Ala', 'GAG': '-Glu', 'GGG': '-Gly'
}
DNA1=DNA[1:]
DNA2=DNA[2:]
def translate_DNA(codon):
    return DNA_table[codon]
   
def translate(DNA):
    translation = ''
    for n in range(0,len(DNA)-(len(DNA)%3),3):
        translation += translate_DNA(DNA[n:n+3])
    return translation
print
print 'Aminoacid  seq 1 Frame: ',translate(DNA)

def translate_DNA(codon):
    return DNA_table[codon]
   
def translate1(DNA):
    translation = ''
    for n in range(0,len(DNA1)-(len(DNA1)%3),3):
        translation += translate_DNA(DNA1[n:n+3])
    return translation
print
print 'Aminoacid  +2 Frame seq: ',translate1(DNA)
def translate2(DNA):
    translation = ''
    for n in range(0,len(DNA2)-(len(DNA2)%3),3):
        translation += translate_DNA(DNA2[n:n+3])
    return translation
print
print 'Aminoacid +3 Frame  seq: ',translate2(DNA)
main=str(translate(DNA))
codec=len(codon1)
jem=float(codec)

print "---------------------------------------------------------------------------------------------------------------------------------------------------"
print "Amino acid characteristics on +1 ORF"

print main.count('Gly') + main.count('Ala')+ main.count('Val') + main.count('Leu')+ main.count('Met')+ main.count('Ile'),'Nonpolar Aliphatic Amino Acids'

print main.count('Ser') + main.count('Thr')+ main.count('Cys') + main.count('Pro')+ main.count('Asn')+ main.count('Gln'),'Polar Uncharged Amino Acids'

print main.count('Lys')+ main.count('Arg')+ main.count('His'), 'Positively charged Amino Acids'

print main.count('Asp') + main.count('Glu'), 'Negatively charged Amino Acids'

print main.count('Phe') + main.count('Tyr')+ main.count('Trp'), 'Nonpolar aromatic Amino Acids'

hydrophobic= main.count('Phe') + main.count('Ala')+ main.count('Val') + main.count('Leu')+ main.count('Ile')+ main.count('Pro')+ main.count('Gly')
print hydrophobic/float(len(codon1))*100, "% Hydrophobic frequency" 

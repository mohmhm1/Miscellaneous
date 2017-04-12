
"""
 
This is an example to implement Needleman-Wunsch sequence algorithm using python

"""
 
### Set up the alignment score scheme
matchScore, mismatchScore, gapScore = 4, -10,-4 # high mismatchscore will generally yield more stringent single bp substitutions. Higher gapscore will yield better indel results
 
### Two testing string for alingment
seq1 = raw_input("enter reference")
seq2 = raw_input("enter seq")
 

cellMap = {}
 

globalBestCellScore = [None, -100000]
 
 
 
def getAnAlignCell(x, y, seq1, seq2):
  
 
    def alnCell():
 
        global globalBestCellScore
        global cellMap
 
        b1, b2 = seq1[x], seq2[y] 
        mx, my = len(seq1), len(seq2)
 
        cellData = []
 
        if x == 0 or y == 0:
            cellId, s = yield
            cellData.append( (cellId, s) )
        else:
            cellId, s = yield
            cellData.append( (cellId, s) )
            cellId, s = yield
            cellData.append( (cellId, s) )
            cellId, s = yield
            cellData.append( (cellId, s) )
 
        # find the best cell that gives the best alignment score
        cellData.sort( key=lambda x: -x[1] )
        bestCell, bestScore = cellData[0]
 
        if bestScore > globalBestCellScore[1]:
            globalBestCellScore = [ (x,y), bestScore ]
 
        # pass the new alignment score to (x+1, y+1)
        if x+1 < mx and y+1 < my:
            # generate the cell at (x+1, y+1) if necessary
            if (x+1, y+1) not in cellMap:
                cellMap[ (x+1, y+1) ] = getAnAlignCell( x+1, y+1, seq1, seq2 )()
                cellMap[ (x+1, y+1) ].next() 
            if b1 == b2: # a match, seq1[x] == seq[2], new_score = bestScore + matchScore
                cellMap[ (x+1, y+1) ].send( ((x,y), bestScore + matchScore) ) # pass the new score to cell (x+1, y+1)
            else: # a mismatch, seq1[x] != seq[2], new_score = bestScore + mismatchScore
                cellMap[ (x+1, y+1) ].send( ((x,y), bestScore + mismatchScore) ) # pass the new score to cell (x+1, y+1)
        # pass the new alignment score to (x+1, y), namely, the base seq1[x] is aligned to a gap
        if x+1 < mx:
            # generate the cell at (x+1, y) if necessary
            if (x+1, y) not in cellMap:
                cellMap[ (x+1, y) ] = getAnAlignCell( x+1, y, seq1, seq2 )()
                cellMap[ (x+1, y) ].next() 
            cellMap[ (x+1, y) ].send( ((x,y), bestScore + gapScore) )
        # pass the new alignment score to (x, y+1), namely, the base seq2[y] is aligned to a gap
        if y+1 < my:
            # generate the cell at (x, y+1) if necessary
            if (x, y+1) not in cellMap:
                cellMap[ (x, y+1) ] = getAnAlignCell( x, y+1, seq1, seq2 )()
                cellMap[ (x, y+1) ].next() 
            cellMap[ (x, y+1) ].send( ((x,y), bestScore + gapScore) )
             
        path = yield # wait, if the cell is on the best path, the co-routine will resume 
 
 
        # generate the alignment pair according the best alinged cells
        if bestCell[0] >= 0 and bestCell[1] >=0 :
            if path == None:
                path = []
             
            if bestCell[0] - x == 0:
                c1 = "-"
            else:
                c1 = seq1[x-1]
            if bestCell[1] - y == 0:
                c2 = "-"
            else:
                c2 = seq2[y-1]
            path.extend( [ (c1, c2) ] )
             
            # send calculated partial path to the best alingment cell to this cell
            cellMap[ bestCell ].send(  path   )
         
        # return the best path if bestCell[0] = -1 or bestCell[1] = -1
        yield path
 
    return alnCell
 
 

cellMap[ (0,0) ] = getAnAlignCell( 0, 0, seq1, seq2 )()
# prime it
cellMap[(0,0)].next()

cellMap[(0,0)].send( ( (-1, -1), 0 ) )
 

bestCell = globalBestCellScore[0]
 

bestPath = cellMap[bestCell].next()
bestPath.reverse()
 
# some simple mechinary to print out the alignment path
alnRes = zip(*bestPath)
ref = "".join(alnRes[0])
seq = "".join(alnRes[1])
siteref=ref.find("-")
siteref1=ref.count("-")
siteseq=seq.find("-")
siteseq1=seq.count("-")
print (ref)
print (seq)

    

print "you have a ", siteref1,"base pair",ref[(siteref-siteref1)],">",seq[(siteseq+siteseq1)]," change  starting at position",(siteref-siteref1)



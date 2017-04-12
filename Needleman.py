# author Ahmed Mahmoud
#
# Copyright (C) 2014 by Ahmed Mahmoud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
 
"""
 
This is an example to implement Needleman-Wunsch sequence algorithm using python

 
-Ahmed Mahmoud, 12/8/2014

"""
 
### Set up the alignment score scheme
matchScore, mismatchScore, gapScore = 4, -10,-4 # high mismatchscore will generally yield more stringent single bp substitutions. Higher gapscore will yield better indel results
 
### Two testing string for alingment
seq1 = raw_input("enter reference")
seq2 = raw_input("enter seq")
 
### cellMap is a dictionary that maps integer pairs to the co-routines
cellMap = {}
 
### For tracking the global best alignment cell
globalBestCellScore = [None, -100000]
 
 
 
def getAnAlignCell(x, y, seq1, seq2):
    """
    This function returns a co-routine the represents an alignment cell at position
    x and y.  The alignment strings are passed explicilty for simplicity.
    """
 
    def alnCell():
 
        """
        This is the co-routine for an alignment cell. A alignment cell co-routine is
        excuted in roughly two stage. The first stage it collects the alignment score
        from the cells at (x-1,y-1), (x-1,y), and (x, y-1) and calculate the best 
        alignment score. Depending the alignment path through the alignment cell, a new
        alignment score is generated and passed to the cells at (x+1, y+1), 
        (x+1,y), and (x, y+1). If any of those cell has not be generated, it will 
        generate the co-routine and regisiter them with the cellMap dictionary. After 
        this it waits for the backtracking caculation.  If a cell is in the best alignment
        path, it will pass the best alignment pair to next cell in the best alignment
        path.
        """
 
        global globalBestCellScore
        global cellMap
 
        b1, b2 = seq1[x], seq2[y] 
        mx, my = len(seq1), len(seq2)
 
        cellData = []
 
        #if the cells are at the very top of the matrix (nothing above them) or left(nothing to their left
        # they will wait for another cell to generate an alignment score. all other cells willget scores from (x-1,y), (x,y-1), and (x-1, y-1)
        # (top column-1 row down to row 1, 1st row - 1 cell with the first column and then to the actual cell).
        # before they can do any calculation.
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
 
 
# initialize the cell at (0,0)
cellMap[ (0,0) ] = getAnAlignCell( 0, 0, seq1, seq2 )()
# prime it
cellMap[(0,0)].next()
# start the whole execution by sending in the initial score to cell at (0,0)
cellMap[(0,0)].send( ( (-1, -1), 0 ) )
 
# get the best global cell
bestCell = globalBestCellScore[0]
 
# continue to excute the best cell co-routine to get the alignment path
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





import itertools
import networkx



def generate_all_digraphs(n):

    nodes = range(1,n+1)
    pairs = tuple((x,y) for x in nodes for y in nodes)
    print "nodes", nodes
    print "pairs", pairs

    count = 0
    for x in itertools.product(*[[0,1]]*len(pairs)):
        count+=1
    print "graphs:", count
    
    

if __name__=="__main__":

    generate_all_digraphs(5)

        

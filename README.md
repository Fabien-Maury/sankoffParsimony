Sankoff algorithm for solving minimum weighted parsimony problem on a given tree with genetic sequences


 * ARGUMENTS : 
 
    - newickTree : a tree described with Newick format
    
    - costMatrix : a list of list, containing the cost of changing from one character to another e.g. : for DNA nucleotides 'A', 'C', 'G', 'T' : costMatrix = [[0, 3, 4, 9], [3, 0, 2, 4], [4, 2, 0, 4], [9, 4, 4, 0]]

    - leavesDic : a dictionnary containing the nodes' names as keys, and their label as values; for the leaves (bottom nodes of the tree). E.g. : for the value of a specific nucleotide in different species, dic = {'species1 : 'A', 'species2' : 'T, ...}


 * OUTPUT :
  a tuple containing :
  
      - the minimum parsimony score of the tree
      
      - the labelled tree as a dictionnary formatted as : {'node1' : 'A', 'node2' : 'G', ...}

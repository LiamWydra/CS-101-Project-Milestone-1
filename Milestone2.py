#def shared_motif(dna_list) - carlie
def shared_motif(dna_list):
    find=[] 
    check=dna_list[0]
    for a in range(len(check)):
        for t in range (1,len(check)-a):
            subcheck=check[a:(a+t)+1]
            for n in range(1,len(dna_list)):
                if dna_list[n].find(subcheck)==-1:
                    continue
                else:
                    find.append(subcheck)
    if find==[]:
        return ''
    else:
        count_find=[]
        for a in range(len(find)):
            count_find.append(find.count(find[a]))
        substrings=[]
        for a in range(len(find)):
            if count_find[a] == (len(dna_list))-1:
                substrings.append(find[a])
        len_substrings=[]
        for a in range(len(substrings)):
            len_substrings.append(len(substrings[a]))
        max_len=max(len_substrings)
        max_substrings=[]
        for a in range(len(substrings)):
            if len(substrings[a])==max_len:
                max_substrings.append(substrings[a])
    return max_substrings[0]

#def get_edges(dna_dict) - Liam
def get_edges(dna_dict):
    n=0
    z=0
    anws = []
    p = len(dna_dict)
    for i in range (p):
        z=n+1
        for i in range (p):
            if list(dna_dict.values())[n][-3:]==list(dna_dict.values())[z%(len(dna_dict))][0:3] and z%(len(dna_dict))!=n:
                anws+=[(list(dna_dict.keys())[n],list(dna_dict.keys())[z%(len(dna_dict))])]
                z=z+1
            else:
                z=z+1
                continue
        n=n+1
    print (anws)
#def assemble_genome(dna_list) - Liam

#def perfect_match(rna) - Liam
def perfect_match(rna):
    if rna.count("U")==rna.count("A") and rna.count("G")==rna.count("C"):
        import math
        a = math.factorial(rna.count("C"))
        b = math.factorial(rna.count("A"))
        return a*b
    else:
        return 0

#def random_genome(dna, gc_content) - Adin

#def rev_palindrome(dna) - Eleni

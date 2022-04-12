#def find_splice(dna_motif, dna) - Carlie
def find_splice(dna_motif, dna):
    result = []
    count = 0
    for i in range(len(dna_motif)):
        while dna[count] != dna_motif[i]:
            count += 1
        result.append(count)
        count += 1
    return result

print(find_splice("GTCTAAAAC","TGCATGCATGCACCCA")) 

#def shared_motif(dna_list) - carlie

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

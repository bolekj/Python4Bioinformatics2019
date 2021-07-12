#!/usr/bin/env python
gene_names = []
def gene_name_extractor(file):
    
    with open(file,"r") as myfile:
        lines = myfile.readlines()
        for i, line in enumerate(lines):
            if i >35:
                sp_line = line.split()
                field = sp_line[0]
                if field.startswith("-"):
                        break
                names=''.join(field)
                gene_names.append(names)
              
               
    return (gene_names)  

def gene_writer(gene_list,output_file):
    with open (output_file,'w') as outfile:
        outfile.write('GENE_names2 \n')
        for names in gene_names:
            outfile.write (names + '\n')
            
if __name__ == "__ main __":
    import sys
    humchrx_file = sys.argv[1]
    #gene_list = sys.argv [2]
    gene_list_file = sys.argv[2]
    
    #work flow
    print("extracting gene_names from humchrx.txt file")
    genes = gene_name_extractor(humchrx_file)
    print("writing gene_names to an output file")
    gene_writer(genes,gene_list_file)
        
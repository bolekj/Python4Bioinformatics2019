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
                #print(names)
               
    return (gene_names)   
def gene_writer(gene_list,output_file):
    with open (output_file,'w') as outfile:
        outfile.write('gene_names \n')
        for names in gene_names:
            outfile.write (names + '\n')
            
if __name__ == "__main__":
    import sys
    #define inputs
    humchrx = sys.argv[1]
    gene_list = sys.argv[2]
    #work flow
    print("Extracting gene names from humchrx")
    genes= gene_name_extractor(humchrx)
    print("Writing gene names in output file")
    gene_writer(genes,gene_list)
    
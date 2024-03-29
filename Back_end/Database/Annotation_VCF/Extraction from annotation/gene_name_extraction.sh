#Below is the code I used to extract the gene names that the SNPs would be acting upon: 

#decompression and processing of the annotated VCF file (2 commands separated by |) 
zcat annotatedg38.vcf.gz | awk -F'\t' 'BEGIN {                   #zcat decompresses the file 
    OFS="\t"     #output will have lines tab separated lines     # this part of the code (second command after | is preparing the output document and prints the header for the output 
    print "#CHROM\tPOS\tID\tREF\tALT\tGENE_NAMES"                #this is the header for the output document 
}                                                               
!/^#/ { #checks that line doesn't start with a hashtag
    split($8, infoFields, ";")      #this splits the info field which is the 8th column  
    delete geneNamesArr 
    geneNames = "" #empty field called geneNames 
    for (i in infoFields) { #iteration in the elements of the info column 
        if (infoFields[i] ~ /^ANN=/) { #Looks for ANN field in the info column 
            split(infoFields[i], annFields, ",") #splits ann field into an array called annFields 
            for (j in annFields) { #iterating through 
                split(annFields[j], annDetail, "|")  #:splits each annFields[j] into an array called annDetail using the pipe to separate
                if (!(annDetail[4] in geneNamesArr)) { #checks that the element 4 in the array is not present in the gene_names 
                    if (geneNames != "") geneNames = geneNames ","#checks that the string isn't empty, if it's not empty a comma is used to separated 
                    geneNames = geneNames annDetail[4] #Appends the new gene name 
                    geneNamesArr[annDetail[4]] 
                }
            }
        }
    }
    print $1, $2, $3, $4, $5, geneNames
}' > simplified_file.vcf

echo "Simplified VCF file 'simplified_file.vcf' has been created."

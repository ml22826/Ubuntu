#use zcat to extract data from the compressed VCF file, pipe it into awk for processing
zcat ../extracted_variants.vcf.gz | awk 'BEGIN { OFS = "\t" } #set output field separator to tab

#for the first file (extracted_variants.vcf.gz):
NR == FNR { 
    #store rsid values in an array indexed by position, ref, and alt
    rsid[$2,$4,$5] = $3; 
    next 
}

#the second file (simplified_file38.vcf):
{
    #extraction of data fields
    chrom = $1;
    pos = $2;
    id = $3;
    ref = $4;
    alt = $5;
    gene_names = $6;  

    # Determine the refID based on the rsid array, set to "." if not found
    refID = (rsid[pos,ref,alt] == "" ? "." : rsid[pos,ref,alt]);

    #print output fields
print chrom, pos, id, ref, alt, gene_names, refID;
}' - > output_file.csv  #redirection of the output to output_file.csv


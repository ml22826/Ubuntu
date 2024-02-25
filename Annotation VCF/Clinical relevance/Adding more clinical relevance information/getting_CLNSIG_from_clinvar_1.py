import pandas as pd 
import vcf 

vcf_reader=vcf.Reader(open('clinvar_chr1.vcf','r')) # this file comes from the clinvar website using this command on bash "wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_chr1.vcf.gz"
vcf_writer=vcf.Writer(open('filtered3_output.vcf','w'),vcf_reader)

for record in vcf_reader:
    record.INFO={'CLNSIG':record.INFO['CLNSIG']} if 'CLNSIG' in record.INFO else {}
    vcf_writer.write_record(record)
    

vcf_writer.close()



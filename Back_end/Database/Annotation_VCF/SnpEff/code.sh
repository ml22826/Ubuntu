wget http://sourceforge.net/projects/snpeff/files/snpEff_latest_core.zip #Download of snpEff
unzip snpEff_latest_core.zip
java -jar snpEff.jar GRCh38.p7.RefSeq chr1.vcf.gz > output.an2n.vcf #Annotation of file


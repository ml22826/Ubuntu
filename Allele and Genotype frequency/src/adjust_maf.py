#function used to determine the alternate allele frequency based on the plink minor allele frequency file generated using plink v.1.9
#This is necessary as plink v.1.9 calculates the minor allele frequency which is usually the alternate allele but can sometimes be the reference allele. 
def adjust_maf(row):
    '''Function which determines whether the minor allele is the alternate or reference allele for each SNP.
    Keeps the MAF (Minor Allele Frequency) score as the alternate allele frequency if the minor allele=alternate allele . 
    Changes the alternate allele frequency to 1-MAF if minor allele=reference allele.'''
    
    #initialize variable which contains the alternate allele
    alternate_allele = row['ALT']
    
    #check if the alternate allele is the minor allele
    if alternate_allele == row['A1']:
        return row['MAF']  #if it's the same as A1 the score remains the same 
    #if the alternate allele isn't the minor allele check if it's the dominant allele
    elif alternate_allele == row['A2']:
        #counter but don't need this anymore
        adjustment_counter += 1  # 
        return 1 - row['MAF']  #change the score 
    else:
        return row['MAF']  #if neither condition is met (in case score is nan)

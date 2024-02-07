CREATE DATABASE ubuntu4;
USE ubuntu4;

CREATE TABLE Sample (
    SampleID int PRIMARY KEY,
    PopulationCode VARCHAR(50),
    FOREIGN KEY (PopulationCode) REFERENCES Population (PopulationCode)  
);


CREATE TABLE Population (
    PopulationCode VARCHAR(255) PRIMARY KEY,
    PopulationName VARCHAR(255),
    SuperpopulationCode VARCHAR(50),
    SuperpopulationName VARCHAR(255)
);


CREATE TABLE SNP_INFO (
	CHROM int,
    POS int,
    SNP_ID VARCHAR(255),
    REF VARCHAR(255),
    ALT VARCHAR(255),
    GENES VARCHAR(500),
    Clinical_impact VARCHAR(10000),
    PRIMARY KEY(POS,SNP_ID)
    
);
ALTER TABLE SNP_INFO ADD UNIQUE INDEX idx_snp_id (SNP_ID);

CREATE TABLE ALLELE (
    SNP_ID VARCHAR(255),
    REFERENCE_ALLELE INT,
    ALTERNATE_ALLELE INT,
    PopulationCode VARCHAR(255),
    FOREIGN KEY (SNP_ID) REFERENCES SNP_INFO (SNP_ID),
    foreign key (PopulationCode) references Population (PopulationCode)
);

CREATE TABLE GENOTYPES (
    SNP_ID VARCHAR(255),
    GEN_1 INT,
    GEN_2 INT,
    GEN_3 INT,
    PopulationCode VARCHAR(255),
    FOREIGN KEY (SNP_ID) REFERENCES SNP_INFO (SNP_ID),
    foreign key (PopulationCode) references Population (PopulationCode)
);
	

CREATE TABLE GENES (
	GENE VARCHAR(255) PRIMARY KEY,
    POS_START INT,
    POS_END INT,
    foreign key (POS_START) REFERENCES SNP_INFO (POS),
    FOREIGN KEY(POS_END) REFERENCES SNP_INFO (POS)

);





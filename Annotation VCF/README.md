# Annotation Folder README

## SnpEff

**Description:** SnpEff is used here for annotating the VCF file. The annotation primarily focuses on extracting gene names associated with SNPs.

## Linking VCF SNP IDs to dbSNP IDs

**Description:** This section focuses on the linking of the SNP_IDs of the VCF to their corresponding dbSNP IDs.

## Clinical Implications Annotation

**Description:** This folder looks into the various methodologies which were used to establish links between SNPs and potential clinical implications or traits. Information from GWAS websites and ClinVar is used to explore and find clinical associations.


```mermaid
%%{init: {'themeVariables': {'fontSize': '100px'}}}%%
flowchart LR
    A("chr1.vcf.gz") -->|Annotation using snpEff| B("annotated38.vcf.gz")
    B --> C("simplified_file38.vcf.gz");
    C --> D("output_file.csv")
    D -->|Linking SNPs to their dbSNP IDs| E("filtered_2_draft.csv")
    E --> F("complete_snp_info.csv")

    B -->|Cleaning up the annotated VCF| C
    D -->|Adding Clinical relevance information to the VCF| E
    E -->|Adding more clinical info and cleaning up file| F


```mermaid
graph TD
start[<font size=6>附一电子报销流程]-->a1[<font size=6>1.发票检验]
a1-->b1[<font size=6>发票税号正确]
b1--<font size=6>是-->c1[<font size=6>发票下方盖公司有效印章]
c1-->d1[<font size=6>发票背面填写项目]
d1-->e1[<font size=6>项目名称]
d1-->e2[<font size=6>项目负责人签名]
d1-->e3[<font size=6>报销人签名]
d1-->e4[<font size=6>审核人签名]
start-->a2[<font size=6>2.填写报销单]
a2-->b2[<font size=6>项目负责人审核通过]
b2-->c3[<font size=6>打印报销单]
start-->a3[<font size=6>3.获取入库单]
a3-->a3b1[<font size=6>锐竞平台下单]
a3b1-->a3c1[<font size=6>...]
a3c1-->a3d1[<font size=6>在结算页面打印入库单]
b1--<font size=6>否-->c2[<font size=6>发票退回发票源更正]
c2-->a1
classDef className fill:#f9f,stroke:#333,stroke-width:4px
class start,a1,a2,a3 className;

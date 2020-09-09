import allel
callset = allel.read_vcf('clinvar_20200830.vcf', fields = '*')
#callset is defined to read the vcf file from the allel library; takes two arguments: file name and the desired fields; if you want all desired fields, indicate with '*'

sorted(callset.keys())
#displays all columns of the vcf file able to parse

df = allel.vcf_to_dataframe('clinvar_20200830.vcf', fields = ['variants/CHROM', 'variants/POS', 'variants/ID', 'variants/REF', 'variants/ALT', 'variants/MC', 'variants/CLNHGVS'])
#converts the vcf file to a dataframe for data processing; choose desired fields to display, indicate '*' if all fields are retained

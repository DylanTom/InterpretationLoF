import allel
callset = allel.read_vcf('clinvar_20200830.vcf', fields = '*')
sorted(callset.keys())
df = allel.vcf_to_dataframe('clinvar_20200830.vcf', fields = ['variants/CHROM', 'variants/POS', 'variants/ID', 'variants/REF', 'variants/ALT', 'variants/MC', 'variants/CLNHGVS'])

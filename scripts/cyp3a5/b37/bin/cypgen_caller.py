#!/usr/bin/env python3

import os
import sys
import subprocess
from snv_def_modules import *


print("--------------------------------------------\n")

print("CYP3A5 Star Allele Calling with CypGen\n")

print("--------------------------------------------\n")



database = sys.argv[1]
infile = sys.argv[2]
infile_full = sys.argv[3]
infile_full_gt = sys.argv[4]
infile_spec = sys.argv[5]


cn = 2


supp_core_vars = get_core_variants(infile, cn)

print("\nSample core variants:")

if supp_core_vars == None:
    print('rs776746')

else:
    print(supp_core_vars)


snv_def_calls = cand_snv_allele_calling(database, infile, infile_full, infile_full_gt, infile_spec, cn)


snv_cand_alleles = snv_def_calls[0]

print("\nCandidate alleles:")
print(snv_cand_alleles)


snv_def_alleles = snv_def_calls[-1]

dip_variants = get_all_vars_gt(infile_full_gt)


print("\nResult:")

print(snv_def_alleles)

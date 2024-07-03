#!/bin/bash

pub_dir="$HOME/downloads/test_pub"

#nist_pubs=(
#  "800-204C"
#  "800-53Ar5"
#)

nist_pubs=(
  # 800-53
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53B.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53Ar5.pdf"
  # 800-204
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204A.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204B.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204C.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-204D.pdf"
  #800-207
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf"
  "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf"
  # FIPS 199
  "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf"
)

aws_docs=(
  "https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf"  
)

for i in "${nist_pubs[@]}"; do
  pub_name=$(echo $i | cut -d '/' -f6 | cut -d '.' -f1-3 | sed 's/\./\ /g')
  echo "Downloading $pub_name ..."
  wget $i -P $pub_dir -o /dev/null
  sleep 2
done

echo "Downloading AWS Well Architected Framework ..."
for i in "${aws_docs[@]}"; do
  wget $i -P $pub_dir
done

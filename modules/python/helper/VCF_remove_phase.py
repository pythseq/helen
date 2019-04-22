import argparse
import pysam
from collections import defaultdict


def fix_vcf(input_vcf, output_vcf):
    vcf_in = pysam.VariantFile(input_vcf)
    vcf_out = pysam.VariantFile(output_vcf, 'w', header=vcf_in.header)
    records = vcf_in.fetch()
    PS_dictionary = defaultdict(int)
    PS_value = 100

    for record in records:
        for sample in record.samples:
            input_ps = str(record.samples[sample]['PS'])

            if input_ps not in PS_dictionary:
                PS_dictionary = PS_value
                PS_value += 50

            record.samples[sample]['PS'] = str(PS_value)
            vcf_out.write(record)


if __name__ == '__main__':
    '''
    Processes arguments and performs tasks.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_vcf",
        type=str,
        required=True,
        help="H5PY file generated by HELEN."
    )
    parser.add_argument(
        "--output_vcf",
        type=str,
        required=True,
        help="H5PY file generated by HELEN."
    )

    FLAGS, unparsed = parser.parse_known_args()
    fix_vcf(FLAGS.input_vcf, FLAGS.output_vcf)

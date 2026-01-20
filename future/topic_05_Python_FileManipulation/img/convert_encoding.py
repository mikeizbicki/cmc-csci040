#!/bin/python3

# process command line arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('input_file')
parser.add_argument('input_encoding')
parser.add_argument('output_file')
parser.add_argument('output_encoding')
args = parser.parse_args()

# perform the conversion
with open(args.input_file, 'rt', encoding=args.input_encoding) as fin:
    with open(args.output_file, 'wt', encoding=args.output_encoding, errors='ignore') as fout:
        fout.write(fin.read())

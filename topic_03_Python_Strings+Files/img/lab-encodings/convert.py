#!/usr/bin/python3

'''
A simple script for converting a file from one encoding to another.
'''

def convert_encoding(in_file, in_encoding, out_file, out_encoding):
    '''
    '''

    with open(in_file, encoding=in_encoding) as fin:
        text = fin.read()

    with open(out_file, 'w', encoding=out_encoding, errors='replace') as fout:
    #with open(out_file, 'w', encoding=out_encoding) as fout:
        fout.write(text)


if __name__ == '__main__':
    # process command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_file', required=True)
    parser.add_argument('--out_file', required=True)
    parser.add_argument('--in_encoding', required=True)
    parser.add_argument('--out_encoding', required=True)
    args = parser.parse_args()

    # call the main function
    convert_encoding(args.in_file, args.in_encoding, args.out_file, args.out_encoding)


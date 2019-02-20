#!/usr/bin/python
# noinspection PyUnresolvedReferences
import sys
import re
import textwrap

sp_list = []
def amino_list_creator(filename):
    with open(filename, 'r') as in_file:
        text = in_file.read().replace('\n', '').replace('>', '\n>').replace(']', '] ')
        tuples = re.findall(r'(>)(\d+)(\D)(.*)(\[)((\D+)(\w{1,10}))(.*)(\s)(\w+)', text)
        for tuple in tuples:
            values = [tuple[5], textwrap.fill(tuple[10], 50), tuple[1], tuple[3], ' ']
            sp_list.append(values)


def nucl_list_creator(filename):
    with open(filename, 'r') as in_file:
        text = in_file.read().replace('\n', '').replace('>', '\n>')
        tuples = re.findall(r'(>)(\d+)(\D)(.*)(\[)((\D+)(\S{1,10}))()(\s)(.*)(\])(\s)((.*)(strand))(\w+)', text)
        for tuple in tuples:
            values = [tuple[5], textwrap.fill(tuple[16], 50), tuple[1], tuple[3], tuple[13]]
            sp_list.append(values)


def gene_name():
    gene = input('Please enter gene name: ')
    return gene


def main():
    try:
        if len(sys.argv) != 4:
            print('usage: ./Fasta_edit.py choose edit option : -1, -2, -3, -4, -5; -aa or -na and a file')
            sys.exit(1)
        args = sys.argv[1]
        option = sys.argv[2]
        filename = sys.argv[3]
        if option == '-aa':
            amino_list_creator(filename)
        elif option == '-na':
            nucl_list_creator(filename)
        if option == '-aa' and sp_list[0][1][0] != 'M':
            print('Be sure to specify -aa(amino acids) or -nc(nucleic acids) based on fasta file \n' 
                  'Alternatively, be sure that you use fasta file provided by img.jgi.doe.gov web site!')
            sys.exit(1)
        elif option == '-na' and len(sp_list) == 0:
            print('Be sure to specify -aa(amino acids) or -nc(nucleic acids) based on fasta file \n'
                  'Alternatively, be sure that you use fasta file provided by img.jgi.doe.gov web site!')
            sys.exit(1)
        else:
            out_file = open('edit_' + filename, 'w')
            if args == '-1':
                for i in sp_list:
                    output = ('>{}\n{}\n\n'.format(i[0], i[1]))
                    print(output)
                    out_file.write(output)
            elif args == '-2':
                gene = gene_name()
                for i in sp_list:
                    output = ('>{} {}\n{}\n\n'.format(i[0], gene, i[1]))
                    print(output)
                    out_file.write(output)
            elif args == '-3':
                gene = gene_name()
                for i in sp_list:
                    output = ('>{} {} ID {}\n{}\n\n'.format(i[0], gene, i[2], i[1]))
                    print(output)
                    out_file.write(output)
            elif args == '-4':
                gene = gene_name()
                for i in sp_list:
                    output = ('>{} {} ID {}\n{}\n{}\n\n'.format(i[0], gene, i[2], i[3], i[1]))
                    print(output)
                    out_file.write(output)
            elif args == '-5':
                gene = gene_name()
                for i in sp_list:
                    output = ('>{} {} ID {}\n{}{}\n{}\n\n'.format(i[0], gene, i[2], i[3], i[4], i[1]))
                    print(output)
                    out_file.write(output)
            else:
                print('Unknown option: {}, please read Readme.txt'.format(args))
                sys.exit(1)
    except FileNotFoundError as e:
        print('Please be sure to enter script name, one of the options (-1 through -5) and filename. Error:', e)
        return False


if __name__ == '__main__':
    main()
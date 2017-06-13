import argparse
import os
import numpy as np

parser = argparse.ArgumentParser(description='number of citations crawler')
parser.add_argument('-field', type=str, default='NLP')
parser.add_argument('-conf', type=str, default='ACL2015')
args = parser.parse_args()

def main():

    input_file = args.field + '/' + args.conf + '/citations.txt' 
    with open(input_file, 'r') as f:
        lines = f.readlines()[0:]  

    num_papers = len(lines)
    citations_dict = {}


    f_out = open(args.field + '/' + args.conf + '/README.md', 'w')
    f_out.write('# ' + args.conf + ' papers\n')
    for i in range(num_papers):
        tmp = lines[i].strip().split('\t')
        title = tmp[0]
        citations = int(tmp[1])
        citations_dict[title] = citations

    sorted_by_citations = sorted(citations_dict.items(), key=lambda x:-x[1])       
    for i in range(num_papers):    
        f_out.write('- [ ] ' + sorted_by_citations[i][0]  + '          ' + str(sorted_by_citations[i][1]) + '\n')
    f_out.close()    
        
if __name__ == "__main__":
    main()

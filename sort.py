import argparse
import os
import numpy as np

parser = argparse.ArgumentParser(description='number of citations crawler')
parser.add_argument('-input_file', type=str, default='NLP/ACL2016/citations.txt')
args = parser.parse_args()

def main():

    with open(args.input_file, 'r') as f:
        lines = f.readlines()[0:]  

    num_papers = len(lines)
    citations_dict = {}


    f_out = open('NLP/ACL2016/README.md', 'w')
    f_out.write('# ' + 'ACL2016' + ' papers\n')
    for i in range(num_papers):
        tmp = lines[i].strip().split('\t')
        title = tmp[0]
        citations = int(tmp[1])
        citations_dict[title] = citations

    sorted_by_citations = sorted(citations_dict.items(), key=lambda x:-x[1])       
    for i in range(num_papers):    
        f_out.write('- [ ] ' + sorted_by_citations[i][0]  + '          ' + str(sorted_by_citations[i][1]) + '\n')
    f_out.close()    
        

    '''  
    titles = ['A CALL system for learning preposition usage', 'A Character-level Decoder without Explicit Segmentation for Neural Machine Translation']

    for title in titles:
        query.set_phrase(title)
        querier.send_query(query)
        articles = querier.articles
        print articles[0].attrs['num_citations'][0]
    '''
if __name__ == "__main__":
    main()

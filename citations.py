import scholar
import argparse
import os
import urllib2
import time
import numpy as np

parser = argparse.ArgumentParser(description='number of citations crawler')
parser.add_argument('-input_file', type=str, default='ML/ICML2016/paperlist.txt')
parser.add_argument('-start_line', type=int, default=0)
#parser.add_argument('-end_line', type=int, default=-1)
args = parser.parse_args()

def main():
    settings = scholar.ScholarSettings()
    settings.set_citation_format(scholar.ScholarSettings.CITFORM_BIBTEX)
    querier = scholar.ScholarQuerier()
    querier.apply_settings(settings)
    query = scholar.SearchScholarQuery()
    query.set_scope(True)
    query.set_num_page_results(scholar.ScholarConf.MAX_PAGE_RESULTS)


    with open(args.input_file, 'r') as f:
        lines = f.readlines()[args.start_line:]  
    folder_name = args.input_file.split('.')[0]

    #if not os.path.exists(folder_name):
    #    os.makedirs(folder_name)    
    #f_out = open(folder_name + '/README.md', 'w')

    num_papers = len(lines) / 2
    citations = {}

    #f_out.write('# ' + folder_name + ' papers\n')
    for i in range(num_papers):
        num_citations = 0
        title = lines[i * 2].strip()
        citations[title] = -1
        query.set_phrase(title)
        querier.send_query(query)
        articles = querier.articles
        if len(articles) > 0: 
            citations[title] += int(articles[0].attrs['num_citations'][0]) + 1
        print title + '\t' + str(citations[title])
        #time.sleep(max(0, np.random.normal(300, 50, 1)[0]))

    #sorted_by_citations = sorted(citations.items(), key=lambda x:x[1])       
    #for i in range(num_papers):    
    #    f_out.write('- [ ] ' + sorted_by_citations[i][0]  + '          ' + str(sorted_by_citations[i][1]) + '\n')
    #f_out.close()    
        

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

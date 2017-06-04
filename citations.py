import scholar
import argparse
import os

parser = argparse.ArgumentParser(description='number of citations crawler')
parser.add_argument('-input_file', type=str, default='ACL2016.txt')
args = parser.parse_args()

def main():
    settings = scholar.ScholarSettings()
    settings.set_citation_format(scholar.ScholarSettings.CITFORM_BIBTEX)
    querier = scholar.ScholarQuerier()
    querier.apply_settings(settings)
    query = scholar.SearchScholarQuery()
    query.set_num_page_results(scholar.ScholarConf.MAX_PAGE_RESULTS)


    with open(args.input_file, 'r') as f:
        lines = f.readlines()  
    folder_name = args.input_file.split('.')[0]

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)    
    f_out = open(folder_name + '/README.md', 'w')

    num_papers = len(lines) / 2
    f_out.write('# ' + folder_name + 'papers\n')
    for i in range(num_papers):
        num_citations = 0
        title = lines[i * 2].strip()
        f_out.write('- [ ] ' + title  + '           ' + str(num_citations) + '\n')
        #query.set_phrase(title)
        #querier.send_query(query)
        #articles = querier.articles
        #num_citations = articles[0].attrs['num_citations'][0]
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
import re
import json

def classify_predicted_type(predicted_str):
    pass
    
def extract_snippet_info(log_file_path):
    snippet_info = {}

    with open(log_file_path, 'r') as file:
        log = file.readlines()

        start_idxs = []
        for (i, line) in enumerate(log):
            if m := re.search(r'Snippet#: (\d+)_(\d+)$|Total errors at the beginning:', line):
                if m.group(1) is not None and m.group(2) is not None:
                    start_idxs.append((i, m.group(1)+"_"+m.group(2)))
                else:
                    start_idxs.append((i, '-1_-1'))
        
        for i in range(len(start_idxs)-1):
            snippet_no = start_idxs[i][1]
            snippet_log = log[start_idxs[i][0]:start_idxs[i+1][0]]
            final_snippet = []

            for line in reversed(snippet_log):
                if 'original_start_marker'in line:
                    break
                elif 'Moxecution' in line or '==========================================' in line or len(line.strip()) == 0:
                    continue
                
                final_snippet.append(line)
            final_snippet = ''.join(reversed(final_snippet))

            print(final_snippet)

            for line in snippet_log:
                if m := re.search(r'TBD0: {\'deductions\': \[.*\], \'type\': \'(\S+)\', \'base_classes\': \[.*\]}', line):
                    snippet_info[snippet_no] = m.group(1)
            
    # return snippet_info

chunk_num = 'chunk100'
def save_snippets_info(snippets_info, output_file_path='snippets_info_{}_incompleter.json'.format(chunk_num)):
    with open(output_file_path, 'w') as file:
        json.dump(snippets_info, file, indent=4)

def main():
    log_file_path = '../new_all/logs/incompleter/{}/log.txt'.format(chunk_num)
    snippets_info = extract_snippet_info(log_file_path)
    save_snippets_info(snippets_info)

if __name__ == "__main__":
    main()

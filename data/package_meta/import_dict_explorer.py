import pickle
import json
import ast

if __name__ == '__main__':
    # with open('top_pypi.json', 'r') as top_file, open('popular_packages_list.pickle', 'wb') as top_list_file:
    #     top_json = json.loads(top_file.read())
    #     top_list = [top['project'] for top in top_json['rows']]

    #     pickle.dump(top_list, top_list_file)

    with open('popular_packages_list.pickle', 'rb') as top_list_file:
        top_list = pickle.load(top_list_file)

        print(top_list)
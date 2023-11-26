import pickle
import ast

if __name__ == '__main__':
    with open('import_dict.pickle', 'rb') as import_dict_file:
        import_dict = pickle.load(import_dict_file)

        print(ast.dump(import_dict['pd'], indent=2))
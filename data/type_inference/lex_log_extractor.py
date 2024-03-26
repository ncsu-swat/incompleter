import re
import json

def classify_predicted_type(predicted_str):
    '''
    Matches specific types from coarse grained lexecutor model
    '''
    if "None" in predicted_str:
        return "NoneType"
    elif "True" in predicted_str or "False" in predicted_str:
        return "bool"
    elif "-1.0" == predicted_str or "0.0" == predicted_str or "1.0" == predicted_str:
        return "float"
    elif "-1" == predicted_str or "0" == predicted_str or "1" == predicted_str:
        return "int"
    elif "a" == predicted_str or "" == predicted_str: 
        return "str"
    elif "[<" in predicted_str or "[]" in predicted_str:
        return "list"
    elif "{<" in predicted_str:
        return "set"
    elif "{'a'" in predicted_str:
        return "dict"
    elif "(<" in predicted_str:
        return "tuple"
    elif "<class 'lexecutor.ValueAbstraction.DummyObject'>" in predicted_str:
        return "callable"
    elif "<lexecutor.ValueAbstraction.DummyObject" in predicted_str:
        return "object"
    elif "<lexecutor.ValueAbstraction.DummyResource" in predicted_str:
        return "resource"
    else:
        raise ValueError(f"Unknown type detected: {predicted_str}")

def extract_snippet_info(log_file_path):
    '''
    Creates json dict of variable predictions for lexecutor and creates a spot for the unmocker to fill in as it runs
    '''
    with open(log_file_path, 'r') as file:
        log_content = file.read()

    # snippet_pattern = re.compile(r"LExecuting file: snippet_(\d+)\.py.*?(?=(LExecuting file: snippet_|$))", re.DOTALL)
    snippet_pattern = re.compile(r"LExecuting file: snippet_(\d+)-(\d+)\.py.*?(?=(LExecuting file: snippet_|$))", re.DOTALL)
    # prediction_pattern = re.compile(r": Predicting for (name|attribute) (.*?):\s*([^\r\n]*)")
    prediction_pattern = re.compile(r": Predicting for (name|attribute) (.*?):(.*)")


    snippets_info = []

    for snippet_match in snippet_pattern.finditer(log_content):
        # snippet_no = snippet_match.group(1)
        snippet_no = snippet_match.group(1) + "-" + snippet_match.group(2)

        snippet_text = snippet_match.group(0)
        predictions = prediction_pattern.findall(snippet_text)

        snippet_dict = {"snippet_no": snippet_no, "identifiers": {}}

        for prediction_type, identifier, predicted_raw_type in predictions:
            # print(f"Matched prediction for '{identifier}': '{predicted_raw_type}'")
            try:
                predicted_type = classify_predicted_type(predicted_raw_type.strip())
            except ValueError as e:
                print(f"Error in snippet {snippet_no} for identifier '{identifier}': {str(e)}")
                continue

            snippet_dict["identifiers"][identifier] = {
                "lexecutor_predicted_type": predicted_type,
                "incompleter_predicted_type": "todo"
            }

        snippets_info.append(snippet_dict)

    return snippets_info

chunk_num = 'chunk100'
def save_snippets_info(snippets_info, output_file_path="snippets_info_{}.json".format(chunk_num)):
    with open(output_file_path, 'w') as file:
        json.dump(snippets_info, file, indent=4)

def main():
    log_file_path = '../new_all/logs/lexecutor/{}/log.txt'.format(chunk_num)
    snippets_info = extract_snippet_info(log_file_path)
    save_snippets_info(snippets_info)

if __name__ == "__main__":
    main()

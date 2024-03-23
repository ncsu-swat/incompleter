import os
import re

# Path to dir
directory = "./ProblemSolutionsPython"

windows_path_pattern = re.compile(r'"[a-zA-Z]:\\\\[^"]*?"|\'[a-zA-Z]:\\\\[^\']*?\'')

def find_windows_paths(line):
    return windows_path_pattern.findall(line)

total_removed = 0

# Look through all lines for windows pathing
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):  
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            matches = []
            for line in lines:
                match = find_windows_paths(line.strip())
                if match:
                    matches.extend(match)
            
            if matches:
                os.remove(filepath)
                print(f"Removed {file}, containing Windows paths:")
                for match in matches:
                    match_cleaned = match.strip('\"').strip('\'')
                    print(f"  - {match_cleaned}")

                total_removed += 1

print(f"Total count of removed files: {total_removed}")

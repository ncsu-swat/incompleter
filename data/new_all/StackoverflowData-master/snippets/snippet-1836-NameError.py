#Source: https://stackoverflow.com/questions/51282756/typeerror-bufsize-must-be-an-integer
    #! /usr/local/bin/python3 python

import os, sys, re, subprocess


def read_txt(filepath, suffix=".txt"):
    """
    Reads and returns the contents of a MCMakeProblem compatible text file,
    after replacing "#filename"-line in the contents.
    :param filepath:
    :param suffix:
    :return:
    """
    filename = filepath.split("/")[-1][:-len(suffix)]  # The filename without the suffix and the preceding path
    print(filename)
    with open(f"{filepath}", 'r') as f:
        filecontents = f.read()
        filecontents = re.sub(r"#filename (.*)\n", f"#filename {filename}\n", filecontents)
    # print(filecontents)
    return filecontents


def create_HTML_folder(directory="./HTMLfiles"):
    """
    Creates a directory for a HTML file if it doesn't already exist.
    :param directory:
    :return:
    """
    try:
        print("Attempting to create a folder for the HTML files...")
        os.mkdir(directory)
    except:
        print("The folder already exists. Moving along...")


def redirect_HTML(htmlfile, destination="./HTMLfiles"):
    """
    This is for cleaning purposes. Moves a give HTML file to a sub-directory.
    :param htmlfile:
    :param destination:
    :return:
    """
    os.rename(htmlfile, f"{destination}/{htmlfile}")


def feed_txt_to_MakeProblem(filecontents):
    """
    Feeds the contents of a text file WITH A SINGLE PROBLEM to the MCMakeProblem-script.
    :param filecontents:
    :return:
    """
    print(f"\nFile contents:\n"
          f"--------------\n"
          f"{filecontents}\n\n")
    try:
        print("Feeding the contents of a text file to MCMakeProblem...")
        subprocess.run(["./MCMakeProblem"], filecontents, encoding="UTF8")
    except:
        print("... aaaand something went wrong")
        raise


def read_html_for_assignments(htmlfile, suffix=".html"):
    """
    Reads and returns the assignment text and MathCheck-code from a MakeProblem-generated HTML-file.
    :param htmlfile:
    :param suffix:
    :return:
    """
    assignments = re.findall("<tr><td class=ifrl>[\s\S]+?\d+.[\s\S]+?</textarea>", htmlfile)
    assignment = "".join(re.findall(r'\d+\.(?:(?:\s+)?[A-Ö][\s\S]+?[.?])+', assignments))
    mccode = re.findall("verbose_off\s*[\s\S]*?</textarea>", assignment)[0][:-len("\n</textarea>"):]

    return assignment, mccode


def write_txt(contents, destination):
    """
    Writes the given contents to a destination file.
    :param contents:
    :param destination:
    :return:
    """
    with open(destination, "w") as f:
        f.write(contents)
    return


def generate(filename, destination):
    print("\nGenerating a problem...\n")
    # filename = str(filename)
    filecontents = read_txt(filename)
    create_HTML_folder()
    feed_txt_to_MakeProblem(filecontents)  # A html-file is put out by this line
    create_HTML_folder()
    redirect_HTML(f"./{filename}1.html")  # The created html-file is moved to a sub-folder
    assignment, mccode = read_html_for_assignments(f"./HTMLfiles/{filename}1.html")

    write_txt(assignment, f"{destination}/instructions.txt")
    write_txt(mccode, f"{destination}/mccode.txt")
    print("... done.")


testfile = "./TxtFiles/testi.txt"
testdest = "./tehtavat/testi/00/"

print()
print()
filename = testfile  # sys.argv[1]
print(filename)
destination = testdest  # sys.argv[2]
print(destination)
generate(filename, destination)
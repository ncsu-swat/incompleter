#Source: https://stackoverflow.com/questions/34621505/python-csv-reader-typeerror-string-pattern-on-bytes-object
def parse(filename):
        parsedFile = []
        with open(filename, 'rb') as csvfile:
                dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=';,|')
                csvfile.seek(0)
                reader = csv.reader(csvfile, dialect)

                for line in reader:
                    parsedFile.append(line)
                return(parsedFile)

def selectFile():
        print('start selectFile method')
        localPath = os.getcwd() + '\Files'
        print(localPath)
        for fileA in os.listdir(localPath):
                print (fileA)

        test = False
        while test == False:
                fileB = input('which file would you like to DeID? \n')
                conjoinedPath = os.path.join(localPath, fileB)
                test = os.path.isfile(conjoinedPath)


        userInput = input('Please enter the number corresponding to which client ' + fileB + ' belongs to. \n\nAcceptable options are: \n1.A \n2.B \n3.C \n4.D \n5.E \n')
        client = ''
        if (userInput == '1'):
                client = 'A'
        elif (userInput == '2'):
                client = 'B'
        elif (userInput == '3'):
                client = 'CServices'
        elif (userInput == '4'):
                client = 'D'
        elif (userInput == '5'):
                client = 'E'
        return(client, conjoinedPath)



def main():
       x, y = selectFile() 
       parse(y)


if __name__ == '__main__':
        main()
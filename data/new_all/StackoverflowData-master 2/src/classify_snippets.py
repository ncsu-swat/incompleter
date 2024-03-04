from db import CONN
import math
import openpyxl
import langid
import ast

class ClassifySnippets:
    def __init__(self):
        self.count = 1
        self.Errros = ['TypeError', 'NameError','AttributeError','FileNotFoundError','ModuleNotFoundError']
        self.total_post_number = self.get_total_post_number()
        self.chunk_size = 20
        print(self.total_post_number)
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.long_executeable = [146,151, 175, 180, 182, 186, 237, 286, 295, 305, 324, 385, 395, 494, 523, 528,
                                 604, 722, 817, 844, 845, 890, 918, 940,969, 1034, 1078, 1085, 1089, 1108, 1143,
                                 1147, 1285, 1292, 1449, 1486,1493, 1494, 1949, 3666, 6640, 1353, 1475, 1497,1509,
                                 1518, 1520, 1521, 1540, 1544, 1554, 1608,1668, 1694, 1705, 1617, 1714, 1765, 1836, 1872,
                                 1928, 1715, 1938, 1954, 1972, 2002, 2013, 2017, 2088,2066, 2077, 2080, 2113, 2121, 2122,
                                 2103, 2164, 2189, 2198, 2237, 2334, 2377, 2383, 2198, 2208, 2391, 2536, 2198,2464, 2416,
                                 2432, 2434, 2447,2452, 2467, 2565, 2198, 2394, 2416, 2437,2441, 2568, 2416, 2446, 2617, 2661,
                                 2722,2773, 2198, 2279,3115, 2694, 2797,2801, 6697,7185,2839, 2912, 2964, 2833,3352, 2853,
                                 2862, 2920, 2939,2948, 2967, 2970, 2993, 3024, 3006, 3111,3087,3125, 3184, 3185, 3186, 3189,3208,
                                 3228, 3276, 3293, 3326, 3347, 3348, 3376,3405, 3540, 3545, 3546, 3547,4797, 3554, 3575, 3578,
                                 3614, 3645, 3761, 3804,3905, 3924,4086, 4372, 4382, 4265, 4391, 4459, 4517, 4742, 4802,5372,
                                 5373, 5492,5519, 5525, 5565,5589, 5596, 7458, 5673,5676, 5792, 5751, 5816, 5823, 5910, 6109,
                                 6141, 6143, 6303, 6482, 6485, 6486, 6488, 6569, 6626, 6629, 6923, 7037, 7102, 7383, 7384, 7397, 2697,
                                 3668, 7380]

    def classify_snippets(self):

        for i in range(1, math.ceil(self.total_post_number/self.chunk_size)):
            posts = self.get_posts_chunk(i)
            for post in posts:
                print("----"+str(post[0]))
                if post[0] in self.long_executeable:
                    continue
                for snippet in post[5]:
                    language, confidence = self.calculateLanguageScore(snippet)
                    post_link = self.getPostLink(post[1])
                    is_parseable = self.check_syntax(snippet)
                    ErrorFound = "Not Parsable"
                    if is_parseable:
                        ErrorFound = self.run_code(snippet)
                        if ErrorFound is None:
                            ErrorFound = "NoError"
                        if ErrorFound in self.Errros:
                            self.writeinFile(snippet,ErrorFound,post_link)

                    self.sheet.append([snippet, ErrorFound, post_link])
            self.workbook.save('example.xlsx')

    def writeinFile(self, snippet, error, post_link):
            file_path = 'snippets/snippet-' + str(self.count) + '-' + error + '.py'
            with open(file_path, 'x') as file:
                file.write("#Source: "+ post_link+"\n")
                file.write(snippet)
            self.count += 1
    def getPostLink(self,post_id):
        with CONN.cursor() as cursor:
            query = "SELECT post_link FROM posts WHERE post_id = %s"
            cursor.execute(query, (post_id,))
            result = cursor.fetchone()  # Use fetchall() if you expect multiple rows
        if result:
            post_link = result[0]
            return post_link
        else:
            print("Post not found.")
            return None
    def run_code(self, code):
        try:
            exec(code)
        except NameError as ne:
            return "NameError"
        except AttributeError as ve:
            return "AttributeError"
        except FileNotFoundError as e:
            return "FileNotFoundError"
        except TypeError as e:
            return "TypeError"
        except ModuleNotFoundError as e:
            return "ModuleNotFoundError"
        except Exception as e:
            return "OtherError"
    def check_syntax(self,code):
        try:
            ast.parse(code)
            return True
        except SyntaxError as e:
            return False
    def calculateLanguageScore(self, snippet):
        language, confidence = langid.classify(snippet)
        return language, confidence

    def get_posts_chunk(self, page_number):
        with CONN.cursor() as cursor:
            query = "SELECT * FROM post_details LIMIT %s OFFSET %s"
            cursor.execute(query, (self.chunk_size, self.chunk_size*(page_number-1)))
            results = cursor.fetchall()
            return results
    def get_total_post_number(self):
        with CONN.cursor() as cursor:
            cursor.execute("SELECT count(*) FROM post_details")
            total_number_of_posts = cursor.fetchone()[0]
            if total_number_of_posts is None:
                total_number_of_posts = 0
            return total_number_of_posts


# Instantiate the class
classify_snippets_instance = ClassifySnippets()
classify_snippets_instance.classify_snippets()

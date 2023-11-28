Moxecution (mock+execution) Progress: 100% 439/439 [23:04<00:00,  3.15s/it] 
|                                                                
| 
| ==========================================
|  Total errors at the beginning: 439
| ==========================================
| 
| 
| 
| ==========================================
|  TABLE I. Cumulative Metrics:
| ==========================================
| 
| This table shows a cumulative measure of full executability, statement coverage, and branch coverage from one iteration to the next.
| 
| | iter#   |   exec(cnt) |   stmt(%) |   br(%) |
| |---------|-------------|-----------|---------|
| | Iter#0  |         414 |        75 |      73 |
| | Iter#1  |         461 |        75 |      73 |
| | Iter#2  |         482 |        75 |      73 |
| | Iter#3  |         494 |        87 |      86 |
| | Iter#4  |         500 |        93 |      92 |
| | Iter#5  |         505 |        96 |      96 |
| | Iter#6  |         505 |        98 |      97 |
| | Iter#7  |         505 |        98 |      98 |
| | Iter#8  |         506 |        99 |      99 |
| | Iter#9  |         506 |        99 |      99 |
| | Iter#10 |         507 |        99 |      99 |
| 
| 
| 
| ====================================
|  TABLE II. Error Type vs. Iteration:
| ====================================
| 
| This table shows a list of error types and the number of times they occur at each iteration. This table shows the gradual resolution of certain error types and the gradual appearance of others. The gradual appearance of other error types can be attributed to side-effects from some prior applied action pattern. Or, if an action pattern was able to execute a previously erroneous statement, other error types could originate from the following statements in the code.
| 
| | error-type                                                                                          |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |
| |-----------------------------------------------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| | NameError                                                                                           | 174 |  42 |  18 |   6 |   6 |   1 |   1 |   1 |   1 |   1 |    1 |
| | TypeError                                                                                           |   6 |  48 |  63 |  57 |  55 |  55 |  56 |  56 |  56 |  57 |   56 |
| | KeyError                                                                                            |   2 |   2 |   6 |   8 |   9 |   7 |   7 |   7 |   5 |   5 |    5 |
| | AttributeError                                                                                      |   3 |  38 |  16 |  16 |  11 |  12 |  11 |  11 |  12 |  11 |   11 |
| | ModuleNotFoundError                                                                                 |  10 |  20 |  21 |  22 |  21 |  21 |  21 |  21 |  21 |  21 |   21 |
| | IndexError                                                                                          |   2 |   3 |   5 |   6 |   6 |   6 |   6 |   6 |   6 |   6 |    6 |
| | FileNotFoundError                                                                                   |  19 |   7 |   4 |   4 |   4 |   4 |   4 |   4 |   4 |   4 |    4 |
| | ImportError                                                                                         |   5 |   7 |   9 |   9 |   9 |   9 |   9 |   9 |   9 |   9 |    9 |
| | ValueError                                                                                          |   7 |   9 |  12 |  12 |  12 |  13 |  13 |  13 |  13 |  13 |   13 |
| | OSError                                                                                             |   0 |   0 |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | ZeroDivisionError                                                                                   |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | pytz.exceptions.UnknownTimeZoneError                                                                |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | requests.exceptions.HTTPError                                                                       |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | _csv.Error                                                                                          |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | SyntaxError                                                                                         |   1 |   3 |   4 |   5 |   6 |   6 |   6 |   6 |   6 |   6 |    6 |
| | [/Users/adminuser/Documents/Work/PartialExecution/incompleter/data/tmp/snippet_704.py.orig] - Error |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| | pandas._config.config.OptionError                                                                   |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| 
| 
| 
| =========================================
|  TABLE III. Action Pattern vs. Iteration:
| =========================================
| 
| This table shows a list of action patterns and the number of times they had been applied at each iteration. This metric could be a proxy for the impact of an action pattern since an action pattern is likely to be impactful if it has been applied a large number of times.
| 
| | action-pattern                |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |
| |-------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| | DefineVar                     | 104 |  63 |  26 |  18 |  12 |  10 |   9 |   9 |  10 |   9 |    9 |
| | AddImport                     |  61 |  10 |   2 |   1 |   2 |   0 |   0 |   0 |   0 |   0 |    0 |
| | DefineFunc                    |  12 |   4 |   3 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |
| | DefineIterableOrSubscriptable |   1 |  22 |   7 |   7 |   2 |   1 |   1 |   1 |   1 |   1 |    1 |
| | DefineKey                     |   2 |   2 |   6 |   8 |   9 |   7 |   7 |   7 |   5 |   5 |    5 |
| | DefineCallable                |   1 |   3 |  22 |  14 |  13 |  11 |  12 |  12 |  12 |  13 |   12 |
| | InstallModule                 |  10 |  20 |  21 |  22 |  21 |  21 |  21 |  21 |  21 |  21 |   21 |
| | NoneType                      |  22 |  54 |  73 |  78 |  83 |  87 |  87 |  87 |  87 |  87 |   87 |
| | CreateFile                    |  19 |   7 |   4 |   4 |   4 |   4 |   4 |   4 |   4 |   4 |    4 |
| 
| 
| 
| ==================================
|  TABLE IV. Action Pattern Impact:
| ==================================
| 
| This table shows the impact of each action pattern. The column f-exec represents the number of snippets where a certain action pattern contributed towards full executability. Let's define an action sequence as the sequence of action patterns that had been applied to a snippet. If a certain action pattern was part of the action sequence for a fully executable sequence, we increment f-exec by 1 (regardless of how many times the action pattern appears in the action sequence). On the other hand, p-exec (partial executability) represents the number of times a certain action pattern advanced the execution beyond a previously erroneous statement. However, p-exec has no association with full executability.
| 
| | action-pattern                |   f-exec |   p-exec |
| |-------------------------------|----------|----------|
| | DefineVar                     |       55 |      194 |
| | AddImport                     |       25 |       76 |
| | DefineFunc                    |        9 |       19 |
| | DefineIterableOrSubscriptable |       17 |       34 |
| | DefineKey                     |        3 |       14 |
| | DefineCallable                |       18 |       22 |
| | InstallModule                 |        0 |        2 |
| | NoneType                      |        0 |        0 |
| | CreateFile                    |       14 |       19 |
| 
| 
| 
| ==================================
|  TABLE V. UNRESOLVED ERRORS:
| ==================================
| 
|   ------------------------------------------------
|    KeyErrors (5 count):
|   ------------------------------------------------
|      0. 'BUSINESS_ID' (snippet_338.py.orig)
|      1. 'Mycol' (snippet_735.py.orig)
|      2. 3 (snippet_335.py.orig)
|      3. 'ret' (snippet_642.py.orig)
|      4. 'count' (snippet_722.py.orig)
| 
|   ------------------------------------------------
|    TypeErrors (56 count):
|   ------------------------------------------------
|      0. 'TBD1' object is not callable (snippet_770.py.orig)
|      1. stat: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_126.py.orig)
|      2. unsupported operand type(s) for +: 'TBD0' and 'TBD1' (snippet_716.py.orig)
|      3. 'TBD1' object is not callable (snippet_748.py.orig)
|      4. check_type() takes 2 positional arguments but 3 were given (snippet_90.py.orig)
|      5. float() argument must be a string or a real number, not 'ellipsis' (snippet_744.py.orig)
|      6. unsupported operand type(s) for *: 'function' and 'int' (snippet_355.py.orig)
|      7. 'TBD2' object is not callable (snippet_698.py.orig)
|      8. Object of type TBD0 is not JSON serializable (snippet_788.py.orig)
|      9. unsupported operand type(s) for -: 'TBD0' and 'TBD1' (snippet_431.py.orig)
|      10. 'TBD1' object is not callable (snippet_740.py.orig)
|      11. 'module' object is not callable (snippet_623.py.orig)
|      12. unsupported operand type(s) for +: 'TBD0' and 'int' (snippet_797.py.orig)
|      13. TBD0.__init__() takes 1 positional argument but 4 were given (snippet_271.py.orig)
|      14. close() argument must be a Figure, an int, a string, or None, not <class '__main__.TBD0'> (snippet_382.py.orig)
|      15. object of type 'TBD0' has no len() (snippet_682.py.orig)
|      16. 'builtin_function_or_method' object is not subscriptable (snippet_515.py.orig)
|      17. 'TBD2' object is not callable (snippet_812.py.orig)
|      18. 'str' object cannot be interpreted as an integer (snippet_354.py.orig)
|      19. unsupported operand type(s) for +=: 'TBD0' and 'int' (snippet_251.py.orig)
|      20. 'TBD1' object cannot be interpreted as an integer (snippet_774.py.orig)
|      21. '<' not supported between instances of 'TBD1' and 'int' (snippet_12.py.orig)
|      22. unsupported operand type(s) for +: 'TBD2' and 'TBD3' (snippet_518.py.orig)
|      23. 'TBD1' object is not callable (snippet_452.py.orig)
|      24. unsupported operand type(s) for -: 'str' and 'str' (snippet_421.py.orig)
|      25. object of type 'NoneType' has no len() (snippet_505.py.orig)
|      26. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_123.py.orig)
|      27. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_779.py.orig)
|      28. expected string or bytes-like object, got 'TBD0' (snippet_362.py.orig)
|      29. 'TBD1' object does not support item assignment (snippet_158.py.orig)
|      30. utime: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_638.py.orig)
|      31. 'TBD1' object is not callable (snippet_817.py.orig)
|      32. 'foo' is an invalid keyword argument for print() (snippet_743.py.orig)
|      33. expected string or bytes-like object, got 'TBD0' (snippet_650.py.orig)
|      34. '<=' not supported between instances of 'int' and 'TBD0' (snippet_490.py.orig)
|      35. 'TBD0' object does not support item assignment (snippet_660.py.orig)
|      36. cannot unpack non-iterable PathCollection object (snippet_793.py.orig)
|      37. unsupported operand type(s) for |=: 'TBD0' and 'TBD2' (snippet_583.py.orig)
|      38. 'TBD1' object is not callable (snippet_426.py.orig)
|      39. unsupported operand type(s) for +: 'TBD1' and 'int' (snippet_175.py.orig)
|      40. 'TBD3' object is not callable (snippet_507.py.orig)
|      41. remove: path should be string, bytes or os.PathLike, not TBD0 (snippet_481.py.orig)
|      42. read_csv() got an unexpected keyword argument 'error_bad_lines' (snippet_586.py.orig)
|      43. encoding without a string argument (snippet_140.py.orig)
|      44. int() argument must be a string, a bytes-like object or a real number, not 'TBD1' (snippet_536.py.orig)
|      45. cannot unpack non-iterable TBD0 object (snippet_516.py.orig)
|      46. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_632.py.orig)
|      47. the JSON object must be str, bytes or bytearray, not TBD0 (snippet_678.py.orig)
|      48. 'TBD0' object is not callable (snippet_601.py.orig)
|      49. listdir: path should be string, bytes, os.PathLike, integer or None, not TBD0 (snippet_287.py.orig)
|      50. initial_value must be str or None, not TBD0 (snippet_692.py.orig)
|      51. expected string or bytes-like object, got 'TBD0' (snippet_681.py.orig)
|      52. chdir: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_405.py.orig)
|      53. unsupported operand type(s) for +: 'TBD0' and 'str' (snippet_772.py.orig)
|      54. 'TBD0' object is not callable (snippet_36.py.orig)
|      55. unsupported operand type(s) for >>: 'builtin_function_or_method' and '_io.TextIOWrapper'. Did you mean "print(<message>, file=<output_stream>)"? (snippet_98.py.orig)
| 
|   ------------------------------------------------
|    ModuleNotFoundErrors (21 count):
|   ------------------------------------------------
|      0. No module named 'TestPy' (snippet_15.py.orig)
|      1. No module named 'models' (snippet_492.py.orig)
|      2. No module named 'parallel_sync' (snippet_206.py.orig)
|      3. No module named 'DataFrame' (snippet_332.py.orig)
|      4. No module named 'text' (snippet_593.py.orig)
|      5. No module named 'foo' (snippet_115.py.orig)
|      6. No module named 'test.b' (snippet_381.py.orig)
|      7. No module named 'parliaments' (snippet_466.py.orig)
|      8. No module named 'file' (snippet_467.py.orig)
|      9. No module named 'urlparse' (snippet_321.py.orig)
|      10. No module named 'speed_testpy' (snippet_105.py.orig)
|      11. No module named 'request' (snippet_479.py.orig)
|      12. No module named 'file_name' (snippet_233.py.orig)
|      13. No module named 'Desktop' (snippet_322.py.orig)
|      14. No module named 'session' (snippet_823.py.orig)
|      15. No module named 'foo' (snippet_804.py.orig)
|      16. No module named 'text' (snippet_318.py.orig)
|      17. No module named 'vehicle_parts' (snippet_24.py.orig)
|      18. No module named 'file' (snippet_548.py.orig)
|      19. No module named 'xrange' (snippet_339.py.orig)
|      20. No module named 'mymodule' (snippet_669.py.orig)
| 
|   ------------------------------------------------
|    IndexErrors (6 count):
|   ------------------------------------------------
|      0. list index out of range (snippet_763.py.orig)
|      1. list index out of range (snippet_746.py.orig)
|      2. list index out of range (snippet_718.py.orig)
|      3. list index out of range (snippet_712.py.orig)
|      4. list index out of range (snippet_125.py.orig)
|      5. list index out of range (snippet_160.py.orig)
| 
|   ------------------------------------------------
|    ImportErrors (9 count):
|   ------------------------------------------------
|      0. attempted relative import with no known parent package (snippet_350.py.orig)
|      1. cannot import name 'app' from 'app' (/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/app/__init__.py) (snippet_151.py.orig)
|      2. cannot import name 'key' from 'secrets' (/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/secrets.py) (snippet_48.py.orig)
|      3. cannot import name 'Model' from 'mysql' (/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/mysql/__init__.py) (snippet_268.py.orig)
|      4. cannot import name 'variable_in__init__py' from 'tmp' (unknown location) (snippet_131.py.orig)
|      5. attempted relative import with no known parent package (snippet_341.py.orig)
|      6. cannot import name 'ifilterfalse' from 'itertools' (unknown location) (snippet_261.py.orig)
|      7. attempted relative import with no known parent package (snippet_121.py.orig)
|      8. cannot import name 'B' from 'b' (/opt/hostedtoolcache/Python/3.11.6/x64/lib/python3.11/site-packages/b.py) (snippet_582.py.orig)
| 
|   ------------------------------------------------
|    AttributeErrors (11 count):
|   ------------------------------------------------
|      0. 'function' object has no attribute 'tzlocal' (snippet_359.py.orig)
|      1. module 'matplotlib' has no attribute 'pyplot' (snippet_39.py.orig)
|      2. 'str' object has no attribute 'descendants' (snippet_478.py.orig)
|      3. 'dict' object has no attribute 'foo' (snippet_445.py.orig)
|      4. 'builtin_function_or_method' object has no attribute 'equal' (snippet_780.py.orig)
|      5. type object 'User' has no attribute 'objects' (snippet_764.py.orig)
|      6. 'list' object has no attribute 'next' (snippet_565.py.orig)
|      7. 'function' object has no attribute 'getPumps' (snippet_792.py.orig)
|      8. 'str' object has no attribute 'decode'. Did you mean: 'encode'? (snippet_685.py.orig)
|      9. module 'sys' has no attribute 'exc_clear' (snippet_571.py.orig)
|      10. 'function' object has no attribute 'glob' (snippet_100.py.orig)
| 
|   ------------------------------------------------
|    ValueErrors (13 count):
|   ------------------------------------------------
|      0. Should be run as sudo user on linux (snippet_181.py.orig)
|      1. cannot reshape array of size 0 into shape (100,100,100) (snippet_563.py.orig)
|      2. Invalid email address. (snippet_324.py.orig)
|      3. can't have unbuffered text I/O (snippet_118.py.orig)
|      4. Index Unnamed: 0 invalid (snippet_392.py.orig)
|      5. could not convert string 'column1' to float64 at row 0, column 1. (snippet_569.py.orig)
|      6. Expected object or value (snippet_647.py.orig)
|      7. Currency formatting is not possible using the 'C' locale. (snippet_197.py.orig)
|      8. No objects to concatenate (snippet_379.py.orig)
|      9. If using all scalar values, you must pass an index (snippet_679.py.orig)
|      10. can't have unbuffered text I/O (snippet_454.py.orig)
|      11. creationflags is only supported on Windows platforms (snippet_7.py.orig)
|      12. min() arg is an empty sequence (snippet_413.py.orig)
| 
|   ------------------------------------------------
|    OSErrors (1 count):
|   ------------------------------------------------
|      0. No file or directory found at my_model.h5 (snippet_447.py.orig)
| 
|   ------------------------------------------------
|    ZeroDivisionErrors (1 count):
|   ------------------------------------------------
|      0. division by zero (snippet_391.py.orig)
| 
|   ------------------------------------------------
|    FileNotFoundErrors (4 count):
|   ------------------------------------------------
|      0. [Errno 2] No such file or directory: '/Users/tedfuller/Desktop/prank/' (snippet_768.py.orig)
|      1. [Errno 2] No such file or directory: 'C:\\Users\\System-Pc\\Desktop\\ybear.jpg' (snippet_485.py.orig)
|      2. [Errno 2] No such file or directory: 'C:\\Python27\\Lib\\genericpath.py' (snippet_406.py.orig)
|      3. [Errno 2] No such file or directory: 'C:\\Users\\Bob\\SecretPasswordFile.txt' (snippet_798.py.orig)
| 
|   ------------------------------------------------
|    pytz.exceptions.UnknownTimeZoneErrors (1 count):
|   ------------------------------------------------
|      0. 'Asia/India' (snippet_17.py.orig)
| 
|   ------------------------------------------------
|    NameErrors (1 count):
|   ------------------------------------------------
|      0. name 'abc' is not defined. Did you mean: 'abs'? (snippet_738.py.orig)
| 
|   ------------------------------------------------
|    requests.exceptions.HTTPErrors (1 count):
|   ------------------------------------------------
|      0. 404 Client Error: Not Found for url: http://lorempixel.com/400/200 (snippet_620.py.orig)
| 
|   ------------------------------------------------
|    _csv.Errors (1 count):
|   ------------------------------------------------
|      0. iterable expected, not TBD0 (snippet_417.py.orig)
| 
|   ------------------------------------------------
|    SyntaxErrors (6 count):
|   ------------------------------------------------
|      0. duplicate argument 'arg0' in function definition (snippet_209.py.orig)
|      1. invalid syntax (snippet_435.py.orig)
|      2. from __future__ imports must occur at the beginning of the file (snippet_785.py.orig)
|      3. multiple exception types must be parenthesized (snippet_303.py.orig)
|      4. multiple exception types must be parenthesized (snippet_813.py.orig)
|      5. duplicate argument 'arg0' in function definition (snippet_274.py.orig)
| 
|   ------------------------------------------------
|    [/Users/adminuser/Documents/Work/PartialExecution/incompleter/data/tmp/snippet_704.py.orig] - Errors (1 count):
|   ------------------------------------------------
|      0. Your Python interpreter must be 2.7 or greater (within major version 2) (snippet_704.py.orig)
| 
|   ------------------------------------------------
|    pandas._config.config.OptionErrors (1 count):
|   ------------------------------------------------
|      0. No such keys(s): 'display.height' (snippet_196.py.orig)
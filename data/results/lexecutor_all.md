/Users/adminuser/Documents/Work/PartialExecution/incompleter




==========================================
 Total errors at the beginning: 242
==========================================



==========================================
 TABLE I. Cumulative Metrics:
==========================================

| iter#   |   exec(cnt) |   stmt(%) |   br(%) |
|---------|-------------|-----------|---------|
| Iter#0  |          16 |        51 |      73 |
| Iter#1  |          61 |        52 |      73 |
| Iter#2  |          81 |        53 |      76 |
| Iter#3  |          93 |        54 |      77 |
| Iter#4  |          99 |        55 |      77 |
| Iter#5  |         104 |        55 |      78 |
| Iter#6  |         104 |        55 |      78 |
| Iter#7  |         104 |        55 |      78 |
| Iter#8  |         105 |        60 |      84 |
| Iter#9  |         105 |        63 |      87 |
| Iter#10 |         106 |        64 |      89 |



====================================
 TABLE II. Error Type vs. Iteration:
====================================

| error-type                                                                                          |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |
|-----------------------------------------------------------------------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| NameError                                                                                           | 171 |  40 |  17 |   5 |   5 |   0 |   0 |   0 |   0 |   0 |    0 |
| TypeError                                                                                           |   6 |  47 |  61 |  56 |  54 |  54 |  55 |  55 |  55 |  56 |   55 |
| AttributeError                                                                                      |   3 |  37 |  16 |  16 |  11 |  12 |  11 |  11 |  12 |  11 |   11 |
| ModuleNotFoundError                                                                                 |  10 |  20 |  21 |  21 |  21 |  21 |  21 |  21 |  21 |  21 |   21 |
| ValueError                                                                                          |   5 |   7 |  10 |  10 |  10 |  11 |  11 |  11 |  11 |  11 |   11 |
| FileNotFoundError                                                                                   |  19 |  10 |   7 |   7 |   7 |   7 |   7 |   7 |   7 |   7 |    7 |
| ImportError                                                                                         |  11 |  13 |  15 |  15 |  15 |  15 |  15 |  15 |  15 |  15 |   15 |
| IndexError                                                                                          |   3 |   4 |   6 |   7 |   7 |   7 |   7 |   7 |   7 |   7 |    7 |
| OSError                                                                                             |   2 |   2 |   2 |   2 |   2 |   2 |   2 |   2 |   2 |   2 |    2 |
| KeyError                                                                                            |   2 |   2 |   6 |   8 |   9 |   7 |   7 |   7 |   5 |   5 |    5 |
| ZeroDivisionError                                                                                   |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| pytz.exceptions.UnknownTimeZoneError                                                                |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| pandas._config.config.OptionError                                                                   |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| _csv.Error                                                                                          |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |
| SyntaxError                                                                                         |   0 |   2 |   3 |   5 |   5 |   5 |   5 |   5 |   5 |   5 |    5 |
| [/Users/adminuser/Documents/Work/PartialExecution/incompleter/data/tmp/snippet_704.py.orig] - Error |   0 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |   1 |    1 |



=========================================
 TABLE III. Action Pattern vs. Iteration:
=========================================

| action-pattern                |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |
|-------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| DefineVar                     | 102 |  61 |  25 |  17 |  11 |   9 |   8 |   8 |   9 |   8 |    8 |
| DefineIterableOrSubscriptable |   1 |  22 |   7 |   7 |   2 |   1 |   1 |   1 |   1 |   1 |    1 |
| DefineCallable                |   1 |   3 |  21 |  14 |  13 |  11 |  12 |  12 |  12 |  13 |   12 |
| NoneType                      |  27 |  58 |  77 |  82 |  86 |  90 |  90 |  90 |  90 |  90 |   90 |
| AddImport                     |  61 |   9 |   2 |   1 |   2 |   0 |   0 |   0 |   0 |   0 |    0 |
| InstallModule                 |  10 |  20 |  21 |  21 |  21 |  21 |  21 |  21 |  21 |  21 |   21 |
| CreateFile                    |  19 |  10 |   7 |   7 |   7 |   7 |   7 |   7 |   7 |   7 |    7 |
| DefineKey                     |   2 |   2 |   6 |   8 |   9 |   7 |   7 |   7 |   5 |   5 |    5 |
| DefineFunc                    |  11 |   4 |   3 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |



==================================
 TABLE IV. Action Pattern Impact:
==================================

| action-pattern                |   f-exec |   p-exec |
|-------------------------------|----------|----------|
| DefineVar                     |       55 |      191 |
| DefineIterableOrSubscriptable |       17 |       34 |
| DefineCallable                |       18 |       21 |
| NoneType                      |        0 |        0 |
| AddImport                     |       24 |       75 |
| InstallModule                 |        0 |        0 |
| CreateFile                    |       12 |       16 |
| DefineKey                     |        3 |       14 |
| DefineFunc                    |        8 |       18 |



==================================
 TABLE V. UNRESOLVED ERRORS:
==================================

  -------------------------
   TypeErrors (55 count):
  -------------------------
     0. 'TBD3' object is not callable (snippet_507.py.orig)
     1. float() argument must be a string or a real number, not 'ellipsis' (snippet_744.py.orig)
     2. 'TBD1' object is not callable (snippet_817.py.orig)
     3. unsupported operand type(s) for +: 'TBD0' and 'str' (snippet_772.py.orig)
     4. unsupported operand type(s) for +=: 'TBD0' and 'int' (snippet_251.py.orig)
     5. check_type() takes 2 positional arguments but 3 were given (snippet_90.py.orig)
     6. the JSON object must be str, bytes or bytearray, not TBD0 (snippet_678.py.orig)
     7. chdir: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_405.py.orig)
     8. unsupported operand type(s) for +: 'TBD0' and 'int' (snippet_797.py.orig)
     9. cannot unpack non-iterable TBD0 object (snippet_516.py.orig)
     10. unsupported operand type(s) for >>: 'builtin_function_or_method' and '_io.TextIOWrapper'. Did you mean "print(<message>, file=<output_stream>)"? (snippet_98.py.orig)
     11. 'TBD0' object does not support item assignment (snippet_660.py.orig)
     12. remove: path should be string, bytes or os.PathLike, not TBD0 (snippet_481.py.orig)
     13. unsupported operand type(s) for -: 'str' and 'str' (snippet_421.py.orig)
     14. unsupported operand type(s) for -: 'TBD0' and 'TBD1' (snippet_431.py.orig)
     15. 'TBD0' object is not callable (snippet_601.py.orig)
     16. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_779.py.orig)
     17. 'builtin_function_or_method' object is not subscriptable (snippet_515.py.orig)
     18. object of type 'NoneType' has no len() (snippet_505.py.orig)
     19. unsupported operand type(s) for |=: 'TBD0' and 'TBD2' (snippet_583.py.orig)
     20. 'TBD1' object is not callable (snippet_452.py.orig)
     21. close() argument must be a Figure, an int, a string, or None, not <class '__main__.TBD0'> (snippet_382.py.orig)
     22. 'TBD1' object is not callable (snippet_770.py.orig)
     23. '<=' not supported between instances of 'int' and 'TBD0' (snippet_490.py.orig)
     24. expected string or bytes-like object, got 'TBD0' (snippet_650.py.orig)
     25. int() argument must be a string, a bytes-like object or a real number, not 'TBD1' (snippet_536.py.orig)
     26. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_632.py.orig)
     27. 'foo' is an invalid keyword argument for print() (snippet_743.py.orig)
     28. object of type 'TBD0' has no len() (snippet_682.py.orig)
     29. initial_value must be str or None, not TBD0 (snippet_692.py.orig)
     30. read_csv() got an unexpected keyword argument 'error_bad_lines' (snippet_586.py.orig)
     31. Object of type TBD0 is not JSON serializable (snippet_788.py.orig)
     32. unsupported operand type(s) for *: 'function' and 'int' (snippet_355.py.orig)
     33. TBD0.__init__() takes 1 positional argument but 4 were given (snippet_271.py.orig)
     34. unsupported operand type(s) for +: 'TBD1' and 'int' (snippet_175.py.orig)
     35. 'TBD0' object is not callable (snippet_36.py.orig)
     36. 'str' object cannot be interpreted as an integer (snippet_354.py.orig)
     37. expected string or bytes-like object, got 'TBD0' (snippet_362.py.orig)
     38. 'module' object is not callable (snippet_623.py.orig)
     39. unsupported operand type(s) for +: 'TBD2' and 'TBD3' (snippet_518.py.orig)
     40. unsupported operand type(s) for +: 'TBD0' and 'TBD1' (snippet_716.py.orig)
     41. 'TBD1' object cannot be interpreted as an integer (snippet_774.py.orig)
     42. expected string or bytes-like object, got 'TBD0' (snippet_681.py.orig)
     43. 'TBD1' object is not callable (snippet_740.py.orig)
     44. utime: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_638.py.orig)
     45. 'TBD1' object is not callable (snippet_426.py.orig)
     46. listdir: path should be string, bytes, os.PathLike, integer or None, not TBD0 (snippet_287.py.orig)
     47. 'TBD1' object does not support item assignment (snippet_158.py.orig)
     48. 'TBD2' object is not callable (snippet_698.py.orig)
     49. '<' not supported between instances of 'TBD1' and 'int' (snippet_12.py.orig)
     50. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_123.py.orig)
     51. 'TBD1' object is not callable (snippet_748.py.orig)
     52. cannot unpack non-iterable PathCollection object (snippet_793.py.orig)
     53. 'TBD2' object is not callable (snippet_812.py.orig)
     54. encoding without a string argument (snippet_140.py.orig)

  -----------------------------
   AttributeErrors (11 count):
  -----------------------------
     0. 'list' object has no attribute 'next' (snippet_565.py.orig)
     1. 'str' object has no attribute 'decode'. Did you mean: 'encode'? (snippet_685.py.orig)
     2. module 'matplotlib' has no attribute 'pyplot' (snippet_39.py.orig)
     3. 'function' object has no attribute 'glob' (snippet_100.py.orig)
     4. 'function' object has no attribute 'tzlocal' (snippet_359.py.orig)
     5. 'str' object has no attribute 'descendants' (snippet_478.py.orig)
     6. 'builtin_function_or_method' object has no attribute 'equal' (snippet_780.py.orig)
     7. type object 'User' has no attribute 'objects' (snippet_764.py.orig)
     8. module 'sys' has no attribute 'exc_clear' (snippet_571.py.orig)
     9. 'function' object has no attribute 'getPumps' (snippet_792.py.orig)
     10. 'dict' object has no attribute 'foo' (snippet_445.py.orig)

  ----------------------------------
   ModuleNotFoundErrors (21 count):
  ----------------------------------
     0. No module named 'xrange' (snippet_339.py.orig)
     1. No module named 'file_name' (snippet_233.py.orig)
     2. No module named 'parliaments' (snippet_466.py.orig)
     3. No module named 'models' (snippet_492.py.orig)
     4. No module named 'test.b' (snippet_381.py.orig)
     5. No module named 'file' (snippet_467.py.orig)
     6. No module named 'mymodule' (snippet_669.py.orig)
     7. No module named 'urlparse' (snippet_321.py.orig)
     8. No module named 'foo' (snippet_804.py.orig)
     9. No module named 'TestPy' (snippet_15.py.orig)
     10. No module named 'parallel_sync' (snippet_206.py.orig)
     11. No module named 'Desktop' (snippet_322.py.orig)
     12. No module named 'DataFrame' (snippet_332.py.orig)
     13. No module named 'file' (snippet_548.py.orig)
     14. No module named 'session' (snippet_823.py.orig)
     15. No module named 'text' (snippet_593.py.orig)
     16. No module named 'text' (snippet_318.py.orig)
     17. No module named 'request' (snippet_479.py.orig)
     18. No module named 'foo' (snippet_115.py.orig)
     19. No module named 'speed_testpy' (snippet_105.py.orig)
     20. No module named 'vehicle_parts' (snippet_24.py.orig)

  -------------------------
   ValueErrors (11 count):
  -------------------------
     0. can't have unbuffered text I/O (snippet_118.py.orig)
     1. Expected object or value (snippet_647.py.orig)
     2. If using all scalar values, you must pass an index (snippet_679.py.orig)
     3. Index Unnamed: 0 invalid (snippet_392.py.orig)
     4. min() arg is an empty sequence (snippet_413.py.orig)
     5. cannot reshape array of size 0 into shape (100,100,100) (snippet_563.py.orig)
     6. can't have unbuffered text I/O (snippet_454.py.orig)
     7. No objects to concatenate (snippet_379.py.orig)
     8. Invalid email address. (snippet_324.py.orig)
     9. creationflags is only supported on Windows platforms (snippet_7.py.orig)
     10. could not convert string 'column1' to float64 at row 0, column 1. (snippet_569.py.orig)

  --------------------------
   ImportErrors (15 count):
  --------------------------
     0. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_657.py.orig)
     1. cannot import name 'key' from 'secrets' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/secrets.py) (snippet_48.py.orig)
     2. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_351.py.orig)
     3. attempted relative import with no known parent package (snippet_341.py.orig)
     4. cannot import name 'B' from 'b' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/site-packages/b.py) (snippet_582.py.orig)
     5. attempted relative import with no known parent package (snippet_350.py.orig)
     6. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_376.py.orig)
     7. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_447.py.orig)
     8. cannot import name 'ifilterfalse' from 'itertools' (unknown location) (snippet_261.py.orig)
     9. cannot import name 'Model' from 'mysql' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/site-packages/mysql/__init__.py) (snippet_268.py.orig)
     10. attempted relative import with no known parent package (snippet_121.py.orig)
     11. cannot import name 'variable_in__init__py' from 'tmp' (unknown location) (snippet_131.py.orig)
     12. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_750.py.orig)
     13. cannot import name 'app' from 'app' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/site-packages/app/__init__.py) (snippet_151.py.orig)
     14. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_620.py.orig)

  ------------------------
   IndexErrors (7 count):
  ------------------------
     0. list index out of range (snippet_763.py.orig)
     1. list index out of range (snippet_718.py.orig)
     2. list index out of range (snippet_160.py.orig)
     3. list index out of range (snippet_746.py.orig)
     4. list index out of range (snippet_712.py.orig)
     5. list index out of range (snippet_125.py.orig)
     6. list index out of range (snippet_645.py.orig)

  ------------------------
   OSErrors (2 count):
  ------------------------
     0. [Errno 30] Read-only file system: '/my' (snippet_126.py.orig)
     1. [Errno 49] Can't assign requested address (snippet_403.py.orig)

  ------------------------
   KeyErrors (5 count):
  ------------------------
     0. 'BUSINESS_ID' (snippet_338.py.orig)
     1. 'Mycol' (snippet_735.py.orig)
     2. 'count' (snippet_722.py.orig)
     3. 'ret' (snippet_642.py.orig)
     4. 3 (snippet_335.py.orig)

  -------------------------------
   ZeroDivisionErrors (1 count):
  -------------------------------
     0. division by zero (snippet_391.py.orig)

  -------------------------------
   FileNotFoundErrors (7 count):
  -------------------------------
     0. [Errno 2] No such file or directory: '/path/to/file/on/local/machine' (snippet_520.py.orig)
     1. [Errno 2] No such file or directory: '/Users/tedfuller/Desktop/prank/' (snippet_768.py.orig)
     2. [Errno 2] No such file or directory: 'C:\\Python27\\Lib\\genericpath.py' (snippet_406.py.orig)
     3. [Errno 2] No such file or directory: '/path/to/somefile.py' (snippet_738.py.orig)
     4. [Errno 2] No such file or directory: 'C:\\Users\\System-Pc\\Desktop\\ybear.jpg' (snippet_485.py.orig)
     5. [Errno 2] No such file or directory: 'C:\\Users\\Bob\\SecretPasswordFile.txt' (snippet_798.py.orig)
     6. [Errno 2] No such file or directory: '/pythonwork/thefile_subset11.csv' (snippet_409.py.orig)

  ------------------------
   pytz.exceptions.UnknownTimeZoneErrors (1 count):
  ------------------------
     0. 'Asia/India' (snippet_17.py.orig)

  ------------------------
   pandas._config.config.OptionErrors (1 count):
  ------------------------
     0. No such keys(s): 'display.height' (snippet_196.py.orig)

  ------------------------
   _csv.Errors (1 count):
  ------------------------
     0. iterable expected, not TBD0 (snippet_417.py.orig)

  -------------------------
   SyntaxErrors (5 count):
  -------------------------
     0. duplicate argument 'arg0' in function definition (snippet_274.py.orig)
     1. invalid syntax (snippet_435.py.orig)
     2. multiple exception types must be parenthesized (snippet_813.py.orig)
     3. multiple exception types must be parenthesized (snippet_303.py.orig)
     4. duplicate argument 'arg0' in function definition (snippet_209.py.orig)

  ------------------------
   [/Users/adminuser/Documents/Work/PartialExecution/incompleter/data/tmp/snippet_704.py.orig] - Errors (1 count):
  ------------------------
     0. Your Python interpreter must be 2.7 or greater (within major version 2) (snippet_704.py.orig)



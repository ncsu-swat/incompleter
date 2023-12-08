==========================================
 Total errors at the beginning: 241
==========================================



==========================================
 TABLE I. Cumulative Metrics:
==========================================

This table shows a cumulative measure of full executability, statement coverage, and branch coverage from one iteration to the next.

| iter#   |   exec(cnt) |   stmt(%) |   br(%) |
|---------|-------------|-----------|---------|
| Iter#1  |          48 |        52 |      73 |
| Iter#2  |          64 |        53 |      76 |
| Iter#3  |          86 |        54 |      77 |
| Iter#4  |         105 |        55 |      77 |
| Iter#5  |         113 |        55 |      78 |
| Iter#6  |         117 |        55 |      78 |
| Iter#7  |         119 |        55 |      78 |
| Iter#8  |         123 |        60 |      84 |
| Iter#9  |         124 |        63 |      87 |
| Iter#10 |         126 |        64 |      89 |
| Iter#11 |         127 |        65 |      90 |
| Iter#12 |         129 |        65 |      90 |
| Iter#13 |         129 |        65 |      90 |
| Iter#14 |         129 |        65 |      90 |
| Iter#15 |         129 |        65 |      91 |
| Iter#16 |         129 |        65 |      91 |
| Iter#17 |         130 |        65 |      91 |
| Iter#18 |         131 |        65 |      91 |
| Iter#19 |         131 |        65 |      91 |



====================================
 TABLE II. Error Type vs. Iteration:
====================================

This table shows a list of error types and the number of times they occur at each iteration. This table shows the gradual resolution of certain error types and the gradual appearance of others. The gradual appearance of other error types can be attributed to side-effects from some prior applied action pattern. Or, if an action pattern was able to execute a previously erroneous statement, other error types could originate from the following statements in the code.

| error-type                           |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |   11 |   12 |   13 |   14 |   15 |   16 |   17 |   18 |   19 |
|--------------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|
| NameError                            | 171 |  36 |  21 |   8 |  10 |   1 |   0 |   1 |   2 |   0 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| TypeError                            |   6 |  43 |  54 |  39 |  17 |  14 |  10 |   8 |   3 |   7 |    3 |    5 |    0 |    2 |    1 |    2 |    2 |    1 |    0 |    0 |
| AttributeError                       |   3 |  66 |  24 |  17 |  13 |  13 |   7 |   5 |   5 |   3 |    4 |    0 |    2 |    1 |    2 |    1 |    1 |    0 |    0 |    0 |
| ModuleNotFoundError                  |  10 |   2 |   2 |   0 |   0 |   0 |   2 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| ValueError                           |   5 |   2 |   3 |   0 |   0 |   0 |   0 |   1 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| FileNotFoundError                    |  19 |   2 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| ImportError                          |  10 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| IndexError                           |   3 |   0 |   2 |   1 |   1 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| OSError                              |   2 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| KeyError                             |   2 |   0 |   5 |   4 |   4 |   2 |   2 |   2 |   1 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| ZeroDivisionError                    |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| pytz.exceptions.UnknownTimeZoneError |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| pandas._config.config.OptionError    |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| _csv.Error                           |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| SyntaxError                          |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |



=========================================
 TABLE III. Action Pattern vs. Iteration:
=========================================

This table shows a list of action patterns and the number of times they had been applied at each iteration. This metric could be a proxy for the impact of an action pattern since an action pattern is likely to be impactful if it has been applied a large number of times.

| action-pattern                |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |   10 |   11 |   12 |   13 |   14 |   15 |   16 |   17 |   18 |   19 |
|-------------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|------|------|------|------|------|
| DefineVar                     | 140 |  95 |  42 |  23 |  20 |  14 |   7 |   6 |   6 |   3 |    4 |    0 |    3 |    1 |    2 |    1 |    1 |    0 |    0 |    0 |
| DefineIterableOrSubscriptable |   1 |  23 |   7 |  10 |   1 |   1 |   0 |   3 |   0 |   1 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |    0 |    0 |
| DefineCallable                |   1 |   2 |  36 |  25 |  11 |   9 |   9 |   5 |   3 |   5 |    2 |    5 |    0 |    2 |    0 |    2 |    1 |    1 |    0 |    0 |
| NoneType                      |  26 |  24 |  17 |   5 |   6 |   4 |   1 |   1 |   0 |   1 |    1 |    0 |    0 |    0 |    0 |    0 |    1 |    0 |    0 |    0 |
| AddImport                     |  17 |   2 |   0 |   2 |   2 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| DefineFunc                    |  17 |   4 |   3 |   0 |   1 |   0 |   0 |   0 |   1 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| RemoveImport                  |  10 |   2 |   1 |   0 |   0 |   0 |   2 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| CreateFile                    |  19 |   2 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| DefineKey                     |   2 |   0 |   5 |   4 |   4 |   2 |   2 |   2 |   1 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |
| InstallModule                 |   0 |   0 |   1 |   0 |   0 |   0 |   0 |   0 |   0 |   0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |    0 |



==================================
 TABLE IV. Action Pattern Impact:
==================================

This table shows the impact of each action pattern. The column f-exec represents the number of snippets where a certain action pattern contributed towards full executability. Let's define an action sequence as the sequence of action patterns that had been applied to a snippet. If a certain action pattern was part of the action sequence for a fully executable sequence, we increment f-exec by 1 (regardless of how many times the action pattern appears in the action sequence). On the other hand, p-exec (partial executability) represents the number of times a certain action pattern advanced the execution beyond a previously erroneous statement. However, p-exec has no association with full executability.

| action-pattern                |   f-exec |   p-exec |
|-------------------------------|----------|----------|
| DefineVar                     |       97 |      361 |
| DefineIterableOrSubscriptable |       27 |       45 |
| DefineCallable                |       56 |      118 |
| NoneType                      |        0 |        0 |
| AddImport                     |        7 |       23 |
| DefineFunc                    |       15 |       26 |
| RemoveImport                  |       10 |       14 |
| CreateFile                    |       11 |       15 |
| DefineKey                     |        4 |       17 |
| InstallModule                 |        0 |        1 |



==================================
 TABLE V. UNRESOLVED ERRORS:
==================================

  ------------------------------------------------
   TypeErrors (54 count):
  ------------------------------------------------
     0. 'zip' object is not subscriptable (snippet_507.py.orig)
     1. float() argument must be a string or a real number, not 'ellipsis' (snippet_744.py.orig)
     2. 'TBD2' object cannot be interpreted as an integer (snippet_817.py.orig)
     3. unsupported operand type(s) for +: 'TBD0' and 'str' (snippet_772.py.orig)
     4. unsupported operand type(s) for +=: 'TBD0' and 'int' (snippet_251.py.orig)
     5. check_type() takes 2 positional arguments but 3 were given (snippet_90.py.orig)
     6. Input string must be text, not bytes (snippet_678.py.orig)
     7. chdir: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_405.py.orig)
     8. unsupported operand type(s) for +: 'TBD0' and 'int' (snippet_797.py.orig)
     9. cannot unpack non-iterable TBD0 object (snippet_516.py.orig)
     10. unsupported operand type(s) for >>: 'builtin_function_or_method' and 'TBD1'. Did you mean "print(<message>, file=<output_stream>)"? (snippet_98.py.orig)
     11. 'TBD0' object does not support item assignment (snippet_660.py.orig)
     12. 'type' object does not support item deletion (snippet_48.py.orig)
     13. unsupported operand type(s) for -: 'str' and 'str' (snippet_421.py.orig)
     14. unsupported operand type(s) for -: 'TBD0' and 'TBD1' (snippet_431.py.orig)
     15. unsupported operand type(s) for >>: 'DataFrame' and 'TBD0' (snippet_274.py.orig)
     16. stat: path should be string, bytes, os.PathLike or integer, not list (snippet_206.py.orig)
     17. object of type 'TBD1' has no len() (snippet_332.py.orig)
     18. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_779.py.orig)
     19. 'builtin_function_or_method' object is not subscriptable (snippet_515.py.orig)
     20. object of type 'TBD0' has no len() (snippet_548.py.orig)
     21. float() argument must be a string or a real number, not 'TBD1' (snippet_499.py.orig)
     22. TBD14.__call__() takes 2 positional arguments but 3 were given (snippet_823.py.orig)
     23. can only concatenate list (not "str") to list (snippet_593.py.orig)
     24. unsupported operand type(s) for |=: 'TBD0' and 'TBD2' (snippet_583.py.orig)
     25. '<=' not supported between instances of 'int' and 'TBD0' (snippet_490.py.orig)
     26. expected string or bytes-like object, got 'TBD0' (snippet_650.py.orig)
     27. int() argument must be a string, a bytes-like object or a real number, not 'TBD1' (snippet_536.py.orig)
     28. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_632.py.orig)
     29. 'foo' is an invalid keyword argument for print() (snippet_743.py.orig)
     30. initial_value must be str or None, not TBD0 (snippet_692.py.orig)
     31. read_csv() got an unexpected keyword argument 'error_bad_lines' (snippet_586.py.orig)
     32. Object of type TBD0 is not JSON serializable (snippet_788.py.orig)
     33. unsupported operand type(s) for *: 'TBD0' and 'int' (snippet_355.py.orig)
     34. unsupported operand type(s) for +: 'TBD1' and 'int' (snippet_175.py.orig)
     35. 'str' object cannot be interpreted as an integer (snippet_354.py.orig)
     36. expected string or bytes-like object, got 'TBD0' (snippet_362.py.orig)
     37. 'module' object is not callable (snippet_623.py.orig)
     38. unsupported operand type(s) for +: 'TBD2' and 'TBD3' (snippet_518.py.orig)
     39. unsupported operand type(s) for +: 'TBD0' and 'TBD1' (snippet_716.py.orig)
     40. package must be a string (snippet_131.py.orig)
     41. 'TBD1' object cannot be interpreted as an integer (snippet_774.py.orig)
     42. expected string or bytes-like object, got 'TBD0' (snippet_681.py.orig)
     43. unsupported operand type(s) for /: 'TBD2' and 'int' (snippet_740.py.orig)
     44. utime: path should be string, bytes, os.PathLike or integer, not TBD0 (snippet_638.py.orig)
     45. listdir: path should be string, bytes, os.PathLike, integer or None, not TBD0 (snippet_287.py.orig)
     46. 'TBD1' object does not support item assignment (snippet_158.py.orig)
     47. unsupported operand type(s) for -: 'int' and 'TBD2' (snippet_653.py.orig)
     48. '<' not supported between instances of 'TBD1' and 'int' (snippet_12.py.orig)
     49. isinstance() arg 2 must be a type, a tuple of types, or a union (snippet_123.py.orig)
     50. unsupported operand type(s) for /: 'TBD0' and 'TBD4' (snippet_748.py.orig)
     51. cannot unpack non-iterable PathCollection object (snippet_793.py.orig)
     52. 'function' object is not iterable (snippet_812.py.orig)
     53. encoding without a string argument (snippet_140.py.orig)

  ------------------------------------------------
   AttributeErrors (8 count):
  ------------------------------------------------
     0. 'list' object has no attribute 'next' (snippet_565.py.orig)
     1. 'str' object has no attribute 'decode'. Did you mean: 'encode'? (snippet_685.py.orig)
     2. 'dict' object has no attribute 'iteritems' (snippet_339.py.orig)
     3. module 'matplotlib' has no attribute 'pyplot' (snippet_39.py.orig)
     4. 'function' object has no attribute 'glob' (snippet_100.py.orig)
     5. 'builtin_function_or_method' object has no attribute 'equal' (snippet_780.py.orig)
     6. 'function' object has no attribute 'getPumps' (snippet_792.py.orig)
     7. 'dict' object has no attribute 'foo' (snippet_445.py.orig)

  ------------------------------------------------
   ValueErrors (11 count):
  ------------------------------------------------
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

  ------------------------------------------------
   ModuleNotFoundErrors (1 count):
  ------------------------------------------------
     0. No module named 'library' (snippet_492.py.orig)

  ------------------------------------------------
   ImportErrors (11 count):
  ------------------------------------------------
     0. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_657.py.orig)
     1. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_351.py.orig)
     2. attempted relative import with no known parent package (snippet_341.py.orig)
     3. cannot import name 'B' from 'b' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/site-packages/b.py) (snippet_582.py.orig)
     4. attempted relative import with no known parent package (snippet_350.py.orig)
     5. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_447.py.orig)
     6. cannot import name 'ifilterfalse' from 'itertools' (unknown location) (snippet_261.py.orig)
     7. attempted relative import with no known parent package (snippet_121.py.orig)
     8. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_750.py.orig)
     9. cannot import name 'app' from 'app' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/site-packages/app/__init__.py) (snippet_151.py.orig)
     10. cannot import name 'Mapping' from 'collections' (/Users/adminuser/miniconda3/envs/incompleter/lib/python3.11/collections/__init__.py) (snippet_620.py.orig)

  ------------------------------------------------
   IndexErrors (7 count):
  ------------------------------------------------
     0. list index out of range (snippet_763.py.orig)
     1. list index out of range (snippet_160.py.orig)
     2. list index out of range (snippet_746.py.orig)
     3. list index out of range (snippet_712.py.orig)
     4. list index out of range (snippet_770.py.orig)
     5. list index out of range (snippet_125.py.orig)
     6. list index out of range (snippet_645.py.orig)

  ------------------------------------------------
   OSErrors (2 count):
  ------------------------------------------------
     0. [Errno 30] Read-only file system: '/my' (snippet_126.py.orig)
     1. [Errno 49] Can't assign requested address (snippet_403.py.orig)

  ------------------------------------------------
   KeyErrors (5 count):
  ------------------------------------------------
     0. 'BUSINESS_ID' (snippet_338.py.orig)
     1. 'Mycol' (snippet_735.py.orig)
     2. 'count' (snippet_722.py.orig)
     3. 'ret' (snippet_642.py.orig)
     4. 3 (snippet_335.py.orig)

  ------------------------------------------------
   ZeroDivisionErrors (1 count):
  ------------------------------------------------
     0. division by zero (snippet_391.py.orig)

  ------------------------------------------------
   FileNotFoundErrors (6 count):
  ------------------------------------------------
     0. [Errno 2] No such file or directory: '/path/to/file/on/local/machine' (snippet_520.py.orig)
     1. [Errno 2] No such file or directory: 'C:\\Python27\\Lib\\genericpath.py' (snippet_406.py.orig)
     2. [Errno 2] No such file or directory: '/path/to/somefile.py' (snippet_738.py.orig)
     3. [Errno 2] No such file or directory: 'C:\\Users\\System-Pc\\Desktop\\ybear.jpg' (snippet_485.py.orig)
     4. [Errno 2] No such file or directory: 'C:\\Users\\Bob\\SecretPasswordFile.txt' (snippet_798.py.orig)
     5. [Errno 2] No such file or directory: '/pythonwork/thefile_subset11.csv' (snippet_409.py.orig)

  ------------------------------------------------
   pytz.exceptions.UnknownTimeZoneErrors (1 count):
  ------------------------------------------------
     0. 'Asia/India' (snippet_17.py.orig)

  ------------------------------------------------
   pandas._config.config.OptionErrors (1 count):
  ------------------------------------------------
     0. No such keys(s): 'display.height' (snippet_196.py.orig)

  ------------------------------------------------
   _csv.Errors (1 count):
  ------------------------------------------------
     0. iterable expected, not TBD0 (snippet_417.py.orig)

  ------------------------------------------------
   SyntaxErrors (1 count):
  ------------------------------------------------
     0. invalid syntax (snippet_435.py.orig)





==================================
 TABLE VI. VENN DIAGRAM STATISTICS:
==================================

This table shows the venn diagram statistics between LExecutor and incompleter.

| Set                |   snippet_cnt(%) |
|--------------------|------------------|
| (only) lexecutor   |             0.16 |
| (only) incompleter |             0.17 |
| (both) common      |             0.38 |
| (none) unsolved    |             0.29 |
#Source: https://stackoverflow.com/questions/67284067/sqlalchemy-pymysql-attributeerror-module-socket-has-no-attribute-af-unix
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})
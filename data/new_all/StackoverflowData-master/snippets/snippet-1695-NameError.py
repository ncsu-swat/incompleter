#Source: https://stackoverflow.com/questions/62610636/django-typeerror-not-enough-arguments-for-format-string
Summary = myTable.objects.raw("SELECT FROM_UNIXTIME (unixtime, '%Y/%m/%d') AS ndate, count(id) AS query_count FROM myTable GROUP BY ndate ORDER BY query_count DESC")
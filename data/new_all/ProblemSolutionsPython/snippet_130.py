import arrow
utc = arrow.utcnow()
print("utc:")
print(utc)
print("\nutc to local:")
print(utc.to('local'))
print("\nlocal to utc:")
print(utc.to('local').to('utc'))
print("\nutc to specific location:")
print(utc.to('US/Pacific'))
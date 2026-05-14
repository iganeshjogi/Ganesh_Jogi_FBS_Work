#Convert the time entered in hh,min and sec into seconds.

hh = int(input('Enter the time hours:'))
mm = int(input('Enter the time minutes:'))
sec = int(input('Enter the time seconds:'))

hh_sec = hh * 3600
mm_sec = mm *  60

total_sec = hh_sec + mm_sec + sec
print (f'Total number of seconds in {hh} hour, {mm} minutes and {sec} seconds are {total_sec}')

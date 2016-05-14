from time import gmtime, strftime
import time
from shutil import move

while(1):
  with open('sample.xml', 'r') as input_file, open('new_sample.xml', 'w') as output_file:
    for line in input_file:
      if "<description>" in line:
        output_file.write(strftime("<description>%B %d, %H:%M:%S</description>\n", gmtime()))
      else:
        output_file.write(line)
  time.sleep(1)
  move('new_sample.xml','sample.xml')

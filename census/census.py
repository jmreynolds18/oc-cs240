data = file('census.txt', 'r')
for line in data:
    line = line.strip()
    if '%' not in line:
        continue
    blacklist = ['Region', 'Division', 'Table', 'UNITED STATES', 'population']
   
    if 'Region' in line or 'Division' in line  or 'UNITED STATES' in line:
        continue

    print line
    print line[:27].strip()
    print line[27:38].strip()
    print line[86:96].strip()
    print line[144:154].strip()
    
    
    

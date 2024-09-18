def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            c = 0
            res = row.rstrip().split(',')
            for i in res:
                c += int(i)
            row = row.rstrip() + ',' + str(c) + '\n'
            yield row

def process(path):
    with open('ans.csv', 'w') as cf:
        for row in csv_reader(path):
            cf.write(row)

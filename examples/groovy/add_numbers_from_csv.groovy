@Grab('com.xlson.groovycsv:groovycsv:1.3')
import static com.xlson.groovycsv.CsvParser.parseCsv

fh = new File('examples/data/distance.csv')
def csv_content = fh.getText('utf-8')

def data_iterator = parseCsv(csv_content, readFirstLine: true)

def sum = 0
for (line in data_iterator) {
    sum += line[2] as Integer
}

println sum

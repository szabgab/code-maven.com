@Grab('com.xlson.groovycsv:groovycsv:1.3')
import static com.xlson.groovycsv.CsvParser.parseCsv

fh = new File('examples/data/process_csv_file.csv')
def csv_content = fh.getText('utf-8')

def data_iterator = parseCsv(csv_content, separator: ';', readFirstLine: true)
// println data_iterator.getClass()  // class com.xlson.groovycsv.CsvIterator

def sum = 0
for (line in data_iterator) {
    sum += line[2] as Integer
}

println sum


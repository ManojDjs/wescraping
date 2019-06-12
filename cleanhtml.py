from html.parser import HTMLParser
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    string=''
    def handle_starttag(self, tag, attrs):
        tag=tag.replace('<head>','')
        print(tag)
        print("Encountered a start tag:", tag)
        string=" ".join((tag))
    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)
        string=' '.join((tag))

    def handle_data(self, data):
        print("Encountered some data  :", data)
        string=' '.join((data))

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
l='<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'
parser.feed(l)



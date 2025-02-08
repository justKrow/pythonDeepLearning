#
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphCount = 0


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position: ", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Encountered start tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0], " position: ", pos[1])
        global paragraphCount
        if tag == "p":
            paragraphCount += 1
        if len(attrs) > 0:
            print("Attributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered data: ", data)
        pos = self.getpos()
        print("At line: ", pos[0], " position: ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()

    f = open("Internet Data/samplehtml.html")
    if f.mode == "r":
        contents = f.read()  # read the entire file
        parser.feed(contents)
    print("Number of paragraphs: ", paragraphCount)


if __name__ == "__main__":
    main()

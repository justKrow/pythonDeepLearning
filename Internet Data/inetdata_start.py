#
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#
import urllib.request


def main():
    webUrl = urllib.request.urlopen("http://www.google.com")
    print("Result code: ", webUrl.getcode())
    data = webUrl.read()
    print(data)


if __name__ == "__main__":
    main()

from optparse import OptionParser

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-s",
                      dest="size",
                      default="2",
                      help="input matrix size")
    (options, args) = parser.parse_args()

    print(options.size)
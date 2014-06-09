def parse_input_file(f):
    # parses file data into a dictionary with restaraunts as keys and ratings
    # as values
    ratings = {}
    contents = f.readlines()

    for line in contents:
        line = line.strip()
        split_line = line.split(":")
        ratings[split_line[0]] = split_line[1]
    return ratings

def sort_and_print_restaurants(ratings):
    # create a list, names, to sort restaurants alphabetically    
    names = sorted(ratings.keys())
    for name in names:
        print "Restauant %s is rated at %d" % (name, int(ratings[name]))

def main():
    with open("scores.txt") as f:
        sort_and_print_restaurants(parse_input_file(f))
    f.close()

if __name__ == "__main__":
    main()
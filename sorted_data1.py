import operator 

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
    # create sorted_values to sort restaurants by rating     
    sorted_values = sorted(ratings.iteritems(), key = operator.itemgetter(1))

    for i in sorted_values:
        restaurant = i[0]
        rating = i[1]

        print "Restauant %s is rated at %s" % (restaurant, rating)

def main():
    with open("scores.txt") as f:
        sort_and_print_restaurants(parse_input_file(f))
    f.close()

if __name__ == "__main__":
    main()
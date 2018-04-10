"""Restaurant rating lister."""
def ratings_lister(my_file):
    restaurant_ratings = {}
    name_list = []
    restaurant_name = open(my_file)

    for line in restaurant_name:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        restaurant_ratings[restaurant] = int(rating)
    return restaurant_ratings


def ordered_restuarant(ordered_res):
    for new_rest, new_rate in (sorted(ordered_res.items())):
        print "{} is rated at {}".format(new_rest, new_rate)

# ordered_res =  ratings_lister("scores.txt")
# ordered_restuarant (ordered_res)

def prompt_user(ordered_res):
    user_input = raw_input("Please enter a restauarant name: ")
    user_rating = int(raw_input("Enter rating for restaurant: "))
    ordered_res[user_input] = user_rating
    final_print = ordered_restuarant(ordered_res)
    return final_print

ordered_res = ratings_lister("scores.txt")
ordered_restuarant(ordered_res)
prompt_user(ordered_res)

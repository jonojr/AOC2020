
def generate_bag_mapping(bag_rules):
    bag_mapping = {}

    for bag_group in bag_rules:
        base_bag, internal_bags = bag_group.split("s contain ")

        internal_bags = [bag.split()[:-1] for bag in
                         internal_bags.strip('.').replace('no other bags',
                                                          '').split(', ')]

        processed_bags = []
        for bag in internal_bags:
            if bag:
                bag_count = int(bag[0])
                bag_names = ' '.join(bag[1:]) + " bag"

                processed_bags.append((bag_count, bag_names))

        bag_mapping[base_bag] = processed_bags
    return bag_mapping


def child_bags(bag_mapping, parent_bag):
    result = {parent_bag}
    for bag in bag_mapping[parent_bag]:
        result |= child_bags(bag_mapping, bag[1])

    return result


def number_bags_containing(bag_mapping, requested_bag):
    valid_bag_count = 0
    for parent_bag in bag_mapping.keys():
        if parent_bag != requested_bag:
            if requested_bag in child_bags(bag_mapping, parent_bag):
                valid_bag_count += 1

    return valid_bag_count


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        bag_rules = input_file.read().split("\n")

    bag_mapping = generate_bag_mapping(bag_rules)

    print(number_bags_containing(bag_mapping, "shiny gold bag"))

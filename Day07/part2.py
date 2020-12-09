
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


def merge_dicts(dict1, dict2):
    result = dict1
    for key, value in dict2.items():
        current = result.get(key, 0)
        result[key] = current + value

    return result


def child_bags(bag_mapping, parent_bag):
    parent_bag_name = parent_bag[1]
    parent_bag_count = parent_bag[0]
    result = {parent_bag_name: parent_bag_count}
    for bag in bag_mapping[parent_bag_name]:
        child_contents = child_bags(bag_mapping, bag)

        merge_dicts(result, {k: v*parent_bag_count for (k, v) in child_contents.items()})

    return result


def number_bags_contained(bag_mapping, requested_bag):
    result = child_bags(bag_mapping, requested_bag)

    return sum(result.values()) - 1


if __name__ == "__main__":
    with open("input.txt", 'r') as input_file:
        bag_rules = input_file.read().split("\n")

    bag_mapping = generate_bag_mapping(bag_rules)

    print(number_bags_contained(bag_mapping, (1, "shiny gold bag")))

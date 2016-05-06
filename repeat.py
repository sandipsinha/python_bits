def repeatArray(the_array):
        sorted(the_array)
        floor = 1
	ceiling = len(the_array)  - 1
	while (floor < ceiling):
            mid_point = floor + (ceiling - floor)/2
            lower_range_floor, lower_range_ceiling = floor, mid_point
            upper_range_floor, upper_range_ceiling = mid_point + 1, ceiling
            num_distinct_integers = 0
            for items in the_array:
                if items >= lower_range_floor and items <= lower_range_ceiling:
                    num_distinct_integers += 1

            num_possible_integers_in_lower_range = lower_range_ceiling - lower_range_floor + 1

            if num_distinct_integers > num_possible_integers_in_lower_range:
                floor, ceiling = lower_range_floor, lower_range_ceiling
            else:
                floor, ceiling = upper_range_floor, upper_range_ceiling
        return floor


if __name__ == 'main':
    some_array = raw_input("Enter a array : ")

    print 'The duplicate number is ', repeatArray(some_array)

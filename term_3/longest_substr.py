def length_of_longest_substring(string: str) -> int:
    if not string:
        return 0 # if the length of the string is 0, return 0 as there are no substrings

    # set longest substring to 1 as default value for now
    longest_substring = 1
    # set window start and end to the start of the string
    window_start, window_end = 0, 0

    # slowly increase the end of the window until it has reached the length of the string
    # once it is the length of the string
    while window_end < len(string):
        # create a substring using list slicing which is the size of the window
        substring = string[window_start : window_end + 1]
        # check that the substring has no duplicate characters
        if len(set(list(substring))) == len(substring):
            # set longest_substring to current length if it is higher than the previous longest substring
            longest_substring = max(longest_substring, window_end - window_start + 1)
            # increase the window length by one to test if that substring will contain duplicates
            window_end += 1
            continue
        # increase the start of the window by one
        window_start += 1
    return longest_substring

def repeatstr(times_to_repeatit: int, string_to_repeat: str):
        return string_to_repeat * times_to_repeatit  # can also do it with for-range with empty result and result += string


to_be_repeated: str = input()
repeats: int = int(input())
print(repeatstr(repeats, to_be_repeated))

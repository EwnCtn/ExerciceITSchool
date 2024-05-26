from typing import List, Tuple, Dict

class WrongTupleSizeException(Exception):
    pass

def list_of_tuples_to_dict(tuples: List[Tuple[object, object]]) -> Dict[object, object]:
    result_dict = {}
    for t in tuples:
        if len(t) != 2:
            raise WrongTupleSizeException(f"Tuple {t} n'are 2 elemente.")
        result_dict[t[0]] = t[1]
    return result_dict

try:
    tuples_list = [(1, 'a'), (2, 'b'), (3, 'c')]
    result = list_of_tuples_to_dict(tuples_list)
    print(result)
except WrongTupleSizeException as e:
    print(f"Error: {e}")

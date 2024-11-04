from typing import Dict, List


def get_mean_scores(scores_dict_list: List[Dict[str, float]]) -> Dict[str, float]:
    final_dict: Dict[str, float] = {}
    for scores_dict in scores_dict_list:
        for key in scores_dict.keys():
            final_dict[key] = final_dict.get(key, 0) + scores_dict[key]
    for key in final_dict.keys():
        final_dict[key] = final_dict[key] / len(scores_dict_list)
    return final_dict
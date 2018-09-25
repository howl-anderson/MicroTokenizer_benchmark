import os
from tokenizer_tools.evaluate_by_files import evaluate_by_files_at_token_level

current_dir_path = os.path.dirname(os.path.abspath(__file__))


def evaluate_by_files(corpus, tokenizer_name):
    if corpus == 'pd':
        gold_file = os.path.join(current_dir_path, "data/people_daily/test_gold.utf8")
    else:
        gold_file = os.path.join(current_dir_path, "data/icwb2-data/gold/{}_test_gold.utf8".format(corpus))
        alternative_gold_file = os.path.join(current_dir_path, "data/icwb2-data/gold/{}_testing_gold.utf8".format(corpus))
        if not os.path.exists(gold_file):  # for fix some gold corpus such as AS uising testing in file name instead of test
            gold_file = alternative_gold_file

    test_file = os.path.join(current_dir_path, "workspace/{}-{}.txt".format(corpus, tokenizer_name))

    score = evaluate_by_files_at_token_level(test_file, gold_file)

    metrics = {
        "RECALL": round(score["RECALL"], 3),
        "PRECISION": round(score["PRECISION"], 3),
        "F1-MEASURE": round(score["F1-MEASURE"], 3)
    }

    return metrics


if __name__ == "__main__":
    score = evaluate_by_files('msr', 'MicroTokenizer_with_custom_CRF_model')
    # score = evaluate_by_files('msr', 'jieba')

    print(score)

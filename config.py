from tokenizers import (
    tokenizer_MicroTokenizer_with_custom_HMM,
    tokenizer_MicroTokenizer_with_custom_DAG,
    tokenizer_MicroTokenizer_with_CRF,
    tokenizer_MicroTokenizer_with_custom_CRF,
    tokenizer_MicroTokenizer_with_custom_joint_model,
    tokenizer_MicroTokenizer_with_custom_max_match_forward,
    tokenizer_MicroTokenizer_with_custom_max_match_backward,
    tokenizer_MicroTokenizer_with_custom_max_match_bidirectional
)


tokenizer_registry = {
        'MicroTokenizer_with_HMM': tokenizer_MicroTokenizer_with_custom_HMM,
        'MicroTokenizer_with_DAG': tokenizer_MicroTokenizer_with_custom_DAG,
        'MicroTokenizer_with_CRF': tokenizer_MicroTokenizer_with_custom_CRF,
        'MicroTokenizer_with_full_feature_CRF': tokenizer_MicroTokenizer_with_CRF,
        'MicroTokenizer_with_joint_model': tokenizer_MicroTokenizer_with_custom_joint_model,
        'MicroTokenizer_with_max_match_forward': tokenizer_MicroTokenizer_with_custom_max_match_forward,
        'MicroTokenizer_with_max_match_backward': tokenizer_MicroTokenizer_with_custom_max_match_backward,
        'MicroTokenizer_with_max_match_bidirectional': tokenizer_MicroTokenizer_with_custom_max_match_bidirectional
    }

# TODO: likely to be over-design
corpus_registry = {
    "PD": 'pd'
}

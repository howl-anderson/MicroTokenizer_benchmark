本文件记录已知的语料库 BUG

* msr_test_gold.utf8 442 行 行尾多了一个字符 `“` 实际属于 下一行的行首，导致和 msr_test.utf8 这两行的语料不一致
* 多行数据不一致类似这种情况，按照行的方式进行评估的方案行不通。
# MicroTokenizer 分词软件基准测试

## 评测目标
本项目测试各个常见分词算法在分词效果上的表现，比较各个分词方法和理论的实际效果，对分词速度也做了简单的考核。

## 分词算法
选用了 MicroTokenizer 自带的所有算法

## 测试数据集
采用人民日报数据集，按照 9：1 的比例分割成训练集和测试集。使用基于词的评判标准。

## 测试方法
使用了 tokenizer_tools 提供的评估工具


## 测试过程
### 安装依赖
```bash
pip install -r ./requirements.txt
```

如果 Mac OS 下安装 `pyltp` 出现 `MACOSX_DEPLOYMENT_TARGET` 相关的问题，请参考 [pyltp 安装](https://github.com/HIT-SCIR/pyltp#%E5%AE%89%E8%A3%85) 和 `install_pyltp_under_macos.bash`

### 训练模型
```bash
python ./train_MicroTokenizer.py
```

和

```bash
python ./train_full_feature_CRF.py
```

### 执行测试程序
```bash
python ./main.py
```

### 渲染可视化结果
```bash
python ./render_readme.py
```

渲染结果为 `README.md`

## 测试结果
### 模型性能
{% for item in test_result %}
#### {{ item.title }}
{{ item.markdown_table }}
{% endfor %}

### 分词速度
#### 测试结果
TODO
#### 测试硬件
{{ sysinfo }}
#### 测试语料
{{ big_corpus }}
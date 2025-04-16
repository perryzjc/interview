---
tags: [topic/fundamentals, concept/vector, type/definition, domain/math, domain/ai_ml]
aliases: [Vector, 向量定义]
---
# 向量 (Vector)

## 概述

在数学和计算机科学（尤其是在 AI/ML 领域）中，向量 (Vector) 是一个**有序的数字列表**，通常用来表示空间中的一个点或一个方向。列表中的每个数字代表向量在某个维度上的分量或坐标。

例如，一个二维向量可以表示为 `(x, y)`，一个三维向量可以表示为 `(x, y, z)`。在 [[../AI & ML/Core Technologies/嵌入 (Embedding)|机器学习嵌入]]中，向量的维度通常非常高（例如几百甚至上千维），表示为 `(d1, d2, d3, ..., dn)`，其中 n 是向量的维度。

## 向量在 AI/ML 中的意义

向量是 AI/ML 中表示和处理数据的基本方式，特别是对于非结构化数据（如文本、图像）：

1.  **表示语义**: 通过 [[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]] 技术，可以将单词、句子、商品等转换为向量。这些向量能够**捕捉输入的语义信息**。
2.  **量化相似性**: 在向量空间中，可以通过计算向量之间的**距离**（如[[../AI & ML/Information Retrieval/欧氏距离|欧氏距离]]）或**夹角**（如[[../AI & ML/Information Retrieval/余弦相似度|余弦相似度]]）来**量化它们之间的相似性**。距离越近或夹角越小，通常表示语义越相似。
3.  **模型输入**: 向量是[[../AI & ML/Core Technologies/Transformer 模型|深度学习模型]]（如 Transformer）能够处理的数学对象。模型通过对输入向量进行计算来学习模式和进行预测。

> [!info] 示例
> * `国王` 可能被表示为向量 `(0.8, 0.7, 0.6, ..., -0.2)`
> * `女王` 可能被表示为向量 `(0.7, 0.8, 0.5, ..., -0.1)`
>  * `香蕉` 可能被表示为向量 `(-0.9, -0.8, 0.6, ..., 0.5)`
> * 可以看到 `国王` 和 `女王` 的向量表示（在所有维度上）会比它们与 `香蕉` 的向量表示更相似。

## 关键操作

*   **向量加减**: 可以进行向量运算，有时能揭示语义关系 (如 `国王 - 男人 + 女人 ≈ 女王`)。
*   **[[../AI & ML/Information Retrieval/相似性搜索|相似度计算]]**: 计算两个向量的[[../AI & ML/Information Retrieval/余弦相似度|余弦相似度]]或[[../AI & ML/Information Retrieval/欧氏距离|欧氏距离]]。

## 总结

向量是将现实世界中的对象（尤其是文本）转化为机器可理解、可计算形式的关键桥梁。理解向量及其相似性计算是理解 [[../AI & ML/Core Technologies/嵌入 (Embedding)|Embedding]]、[[../AI & ML/Core Technologies/向量数据库|向量数据库]] 和 [[../AI & ML/Information Retrieval/相似性搜索|语义搜索]] 的基础。

## 相关概念

*   [[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]
*   [[向量空间]]
*   [[维度 (Dimension)]]
*   [[../AI & ML/Information Retrieval/相似性搜索|相似性搜索]]
*   [[../AI & ML/Information Retrieval/余弦相似度|余弦相似度]]
*   [[../AI & ML/Information Retrieval/欧氏距离|欧氏距离]]
*   [[../AI & ML/Core Technologies/向量数据库|向量数据库]]

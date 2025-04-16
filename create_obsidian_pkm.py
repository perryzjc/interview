import os
import textwrap

# --- Configuration ---
TARGET_ROOT_DIRECTORY = '.' # Base directory for creating files/folders
OVERWRITE_EXISTING = True # Set to False to avoid overwriting existing files

# --- Helper Function ---
def write_file(filepath, content):
    """Creates directories and writes content to a file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully wrote: {filepath}")
    except IOError as e:
        print(f"Error writing file {filepath}: {e}")

# --- Knowledge Base Content Definitions (Part 5 - AI Core Tech & Model Landscape) ---

# Concepts/AI & ML/Core Technologies
ai_ml_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML')
ai_core_tech_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Core Technologies')
llm_path = os.path.join(ai_ml_folder, '大型语言模型 (LLM).md')

transformer_path = os.path.join(ai_core_tech_folder, 'Transformer 模型.md')
transformer_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/transformer, type/architecture, technology]
    aliases: [Transformer Architecture, Transformer架构]
    ---
    # Transformer 模型架构

    [[../00 - AI 与机器学习概览|返回 AI 概览]] | [[../大型语言模型 (LLM)|LLM 基础]]

    ## 概述

    Transformer 是一种**深度学习模型架构**，由 Google 在 2017 年的论文《Attention Is All You Need》中提出。它最初用于机器翻译任务，但其核心机制——**自注意力 (Self-Attention)**——被证明在处理各种序列数据（尤其是自然语言文本）方面非常强大，从而**彻底改变了[[../大型语言模型 (LLM)|自然语言处理 (NLP)]]领域**。

    **几乎所有现代的[[../大型语言模型 (LLM)|大型语言模型 (LLM)]]（如 GPT、BERT、LLaMA、Claude 等）都是基于 Transformer 架构构建的。** 理解 Transformer 的核心思想有助于理解 LLM 为何如此强大。

    ## 核心思想：注意力机制 (Attention Mechanism)

    在 Transformer 出现之前，处理序列数据（如句子）的主流模型是 RNN (循环神经网络) 和 LSTM/GRU (长短期记忆网络/门控循环单元)。这些模型按顺序处理单词，难以捕捉句子中**相距较远的词语之间的依赖关系**（例如，“法律” 和 “规定” 在长句中的关联），并且难以**并行计算**（必须处理完前一个词才能处理下一个）。

    Transformer 架构通过**注意力机制 (Attention Mechanism)**，特别是**自注意力 (Self-Attention)**，解决了这些问题：

    1.  **同时关注所有词**: 对于句子中的**每一个词**，自注意力机制会计算它与句子中**所有其他词**（包括它自己）的**相关性或“注意力权重”**。
    2.  **加权表示**: 基于这些权重，模型为每个词生成一个新的表示 (Representation)，这个表示融合了句子中所有与之相关词语的信息。**相关性越强的词，其信息对当前词新表示的贡献越大。**
    3.  **捕捉长距离依赖**: 由于模型可以直接计算任意两个词之间的相关性，无论它们在句子中相距多远，因此能够有效捕捉长距离依赖关系。
    4.  **并行计算**: 每个词的新表示可以**独立并行计算**，大大提高了训练效率。

    ```mermaid
     graph LR
        subgraph "传统 RNN/LSTM (顺序处理)"
            direction LR
            W1 --> W2 --> W3 --> W4 --> Output1
        end

        subgraph "Transformer (自注意力机制 - 并行处理)"
            direction TB
            Input["输入句子<br/>(Word1, Word2, Word3, Word4)"] --> Attention{"自注意力层<br/>(计算所有词之间的相关性)"};
            Attention -- "融合相关词信息" --> Repr["每个词的新表示<br/>(Rep1, Rep2, Rep3, Rep4)"];
            Repr --> Output2["后续处理/输出"];

            Word1_In[Word1] --> Attention;
            Word2_In[Word2] --> Attention;
            Word3_In[Word3] --> Attention;
            Word4_In[Word4] --> Attention;

            Attention --> Word1_Repr[Rep1];
            Attention --> Word2_Repr[Rep2];
            Attention --> Word3_Repr[Rep3];
            Attention --> Word4_Repr[Rep4];

            style Input fill:#eee,stroke:#333
            style Repr fill:#ccf,stroke:#333
        end

        W1 --- Word1_In;
        W2 --- Word2_In;
        W3 --- Word3_In;
        W4 --- Word4_In;

        linkStyle default interpolate basis
    ```
    [!info] 直观理解
    想象一下你在阅读一个长句子：“**苹果**公司昨天发布了新款 **iPhone**，它具有更强的**处理器**和改进的**摄像头**。” 当模型处理 “iPhone” 这个词时，自注意力机制能让它同时关注到 “苹果”（知道是谁发布的）、“处理器”和“摄像头”（知道是 iPhone 的特性），即使这些词语在句子中位置不同。

    ## Transformer 的主要组成部分 (简化)

    *   **[[../Core Technologies/嵌入 (Embedding)|词嵌入 (Embeddings)]]**: 将输入的单词转换为向量表示。
    *   **位置编码 (Positional Encoding)**: 由于 Transformer 并行处理，本身没有顺序信息，需要加入位置编码来告诉模型单词在句子中的位置。
    *   **多头自注意力 (Multi-Head Self-Attention)**: 同时从不同角度（不同的“头”）计算注意力权重，捕捉更丰富的依赖关系。
    *   **前馈神经网络 (Feed-Forward Networks)**: 在注意力层之后对每个位置的表示进行进一步处理。
    *   **层归一化 (Layer Normalization) & 残差连接 (Residual Connections)**: 帮助模型训练更稳定、更深入。
    *   **编码器 (Encoder) & 解码器 (Decoder)**:
        *   原始 Transformer 包含编码器（理解输入序列）和解码器（生成输出序列），适用于机器翻译等 Seq2Seq 任务。
        *   许多 LLM（如 GPT 系列）主要使用**解码器**部分 (Decoder-only)，专注于根据前面的文本生成后续文本。
        *   有些模型（如 BERT）主要使用**编码器**部分 (Encoder-only)，专注于理解文本，适用于文本分类、命名实体识别等任务。

    ## 对产品经理的意义

    *   **理解能力基础**: Transformer 的注意力机制是 LLM 能够理解上下文、把握语义关系、处理长文本的关键。
    *   **生成能力基础**: 基于 Transformer 的解码器架构使得 LLM 能够流畅地生成连贯的文本。
    *   **效率与规模**: Transformer 的并行计算能力使得训练更大规模的模型成为可能，从而带来了能力的涌现。
    *   **局限性提示**: 理解其基于模式匹配和概率生成，有助于理解[[../模型幻觉 (Hallucination)|幻觉]]等局限性的来源（它不具备真正的逻辑推理或世界模型）。

    ## 总结

    Transformer 架构及其核心的自注意力机制是理解现代 [[../大型语言模型 (LLM)|LLM]] 工作原理的基础。产品经理不需要深入了解其数学细节，但理解其**核心思想（如何通过注意力捕捉依赖关系）**以及**它带来的优势（处理长距离依赖、并行计算）**，对于理解 LLM 的能力边界、评估相关技术方案非常有帮助。

    ## 相关概念

    *   [[../大型语言模型 (LLM)|大型语言模型 (LLM)]]
    *   [[注意力机制]]
    *   [[自注意力]]
    *   [[../Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]
    *   [[自然语言处理 (NLP)]]
    *   [[深度学习]]
    *   [[编码器-解码器架构]]
""")

embedding_path = os.path.join(ai_core_tech_folder, '嵌入 (Embedding).md')
embedding_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/embedding, type/technique, technology]
    aliases: [Embedding, 词嵌入, 文本嵌入, 向量表示]
    ---
    # 嵌入 (Embedding)

    [[../00 - AI 与机器学习概览|返回 AI 概览]]

    ## 概述

    嵌入 (Embedding) 是一种在机器学习（特别是自然语言处理 NLP 和推荐系统）中广泛使用的技术，指的是将**离散的、高维的输入（如单词、句子、用户、商品）表示为低维的、稠密的、连续的向量 (Vector)**。

    这个向量被称为**嵌入向量 (Embedding Vector)**，其核心思想是**捕捉输入的语义信息**。在向量空间中，**语义上相似的输入，其对应的嵌入向量在空间中的距离也更近**。

    [!info] 直观理解
    想象一个巨大的多维空间（远超三维）。Embedding 技术就像给每个词（或句子、商品）在这个空间里找到一个坐标点。意思相近的词（比如“国王”和“女王”）它们的坐标点会很接近；而意思不同的词（比如“国王”和“香蕉”）坐标点会离得很远。甚至可以通过向量运算体现一些关系，比如 `Vector("国王") - Vector("男人") + Vector("女人")` 在空间中可能非常接近 `Vector("女王")`。

    ## 为什么需要 Embedding？

    *   **让机器理解语义**: 计算机无法直接理解文本。通过将词语或句子转换为向量，机器学习模型（如 [[../大型语言模型 (LLM)|LLM]]）才能对其进行数学运算和处理，从而理解语义关系。
    *   **降维**: 将原本高维稀疏的表示（例如 one-hot 编码，维度等于词表大小）转换为低维稠密的向量，减少计算复杂度，提高模型效率。
    *   **捕捉相似性**: 可以方便地计算不同输入之间的语义相似度（例如通过计算向量之间的[[余弦相似度]]或[[欧氏距离]]）。这对于[[../检索增强生成 (RAG)|信息检索]]、[[推荐系统]]、[[聚类]]等任务至关重要。
    *   **作为模型输入**: 嵌入向量通常作为[[../Core Technologies/Transformer 模型|Transformer]]等深度学习模型的初始输入层。

    ## Embedding 的类型

    *   **词嵌入 (Word Embedding)**: 为词汇表中的每个单词生成一个向量。经典算法包括 Word2Vec, GloVe, FastText。缺点是无法处理未登录词 (OOV)，且无法很好地表达一词多义。
    *   **句子/文本嵌入 (Sentence/Text Embedding)**: 为整个句子或段落生成一个向量表示。常用的方法包括：
        *   对词嵌入进行平均或加权平均。
        *   使用 [[../Core Technologies/Transformer 模型|Transformer]] 的编码器（如 BERT, Sentence-BERT）直接生成句子级别的向量。这通常效果更好，能捕捉更复杂的语义。

    ## Embedding 的应用

    *   **[[../大型语言模型 (LLM)|LLM]] 的输入**: LLM 的第一步通常就是将输入的文本转换为嵌入向量。
    *   **[[../检索增强生成 (RAG)|检索增强生成 (RAG)]]**: 将知识库中的文档块和用户查询都转换为嵌入向量，通过在[[../Core Technologies/向量数据库|向量数据库]]中进行相似度搜索，快速找到最相关的上下文信息。**这是 RAG 的核心机制之一。**
    *   **语义搜索**: 用户输入查询，系统将其转换为向量，在索引好的文档向量库中查找最相似的文档。
    *   **[[推荐系统]]**: 将用户和物品（如商品、电影）都嵌入到同一个向量空间，通过计算用户向量与物品向量的相似度来进行推荐。
    *   **文本分类/聚类**: 将文本转换为嵌入向量后，再输入给分类或聚类模型。

    ## 对产品经理的意义

    *   **理解 AI 能力基础**: 了解 Embedding 是机器理解语言语义的关键一步。
    *   **理解 RAG 核心**: 明白 Embedding 和[[../Core Technologies/向量数据库|向量数据库]]是实现高效[[../检索增强生成 (RAG)|语义检索]]以支持 RAG 的基础。
    *   **评估技术方案**: 在讨论语义搜索、推荐系统、RAG 等方案时，能理解 Embedding 在其中的作用和重要性。
    *   **数据考量**: 知道生成高质量 Embedding 需要大量的训练数据，并且可能需要针对特定领域进行微调。

    ## 总结

    Embedding 是将文本等离散输入转化为机器可理解的、包含语义信息的向量表示的关键技术。它是 [[../大型语言模型 (LLM)|LLM]]、[[../检索增强生成 (RAG)|RAG]]、语义搜索和推荐系统等众多 AI 应用的基石。产品经理理解其基本概念和应用价值，有助于更好地设计 AI 产品和评估相关技术方案。

    ## 相关概念

    *   [[向量 (Vector)]]
    *   [[向量空间]]
    *   [[语义相似度]]
    *   [[余弦相似度]]
    *   [[Word2Vec]], [[GloVe]] (词嵌入算法)
    *   [[BERT]], [[Sentence-BERT]] (文本嵌入模型)
    *   [[../大型语言模型 (LLM)|大型语言模型 (LLM)]]
    *   [[../检索增强生成 (RAG)|检索增强生成 (RAG)]]
    *   [[../Core Technologies/向量数据库|向量数据库]]
    *   [[自然语言处理 (NLP)]]
""")

vector_db_path = os.path.join(ai_core_tech_folder, '向量数据库.md')
vector_db_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/vector_database, type/database, technology]
    aliases: [Vector Database, 向量库]
    ---
    # 向量数据库 (Vector Database)

    [[../00 - AI 与机器学习概览|返回 AI 概览]] | [[../Core Technologies/嵌入 (Embedding)|相关: 嵌入 (Embedding)]] | [[../检索增强生成 (RAG)|相关: RAG]]

    ## 概述

    向量数据库是一种**专门设计用于存储、索引和高效查询高维[[../Core Technologies/嵌入 (Embedding)|嵌入向量 (Embedding Vectors)]]** 的数据库。

    随着[[../Core Technologies/嵌入 (Embedding)|Embedding]]技术在 AI 领域的广泛应用（用于表示文本、图像、音频等的语义信息），如何快速地在海量向量中找到与给定查询向量**最相似**的向量（即[[近似最近邻搜索 (Approximate Nearest Neighbor, ANN)]]）成为了一个关键需求。传统的关系型数据库或文档数据库并不擅长处理这种高维向量的相似性搜索。向量数据库应运而生，填补了这一空白。

    ## 核心功能：相似性搜索

    向量数据库的核心能力是**高效的相似性搜索 (Similarity Search)**。当给定一个查询向量时（例如，用户问题的[[../Core Technologies/嵌入 (Embedding)|嵌入]]），向量数据库能够快速地从数百万甚至数十亿的向量中，找出在向量空间中与其**距离最近**（即语义最相似）的 K 个向量（K-Nearest Neighbors, KNN）。

    常用的相似度/距离度量包括：
    *   **[[余弦相似度 (Cosine Similarity)]]**: 衡量向量方向的相似性，常用于文本嵌入。
    *   **[[欧氏距离 (Euclidean Distance)]]**: 衡量向量空间中的直线距离。
    *   **点积 (Dot Product)**

    为了实现**快速**搜索，向量数据库通常采用**[[近似最近邻搜索 (ANN)]]** 算法（如 HNSW, LSH, IVF 等），这些算法能在可接受的精度损失范围内，极大地提升搜索速度。

    ## 为什么需要向量数据库？(尤其对于 RAG)

    向量数据库是实现高效[[../检索增强生成 (RAG)|检索增强生成 (RAG)]]系统的**关键基础设施**：

    1.  **存储知识库向量**: [[../检索增强生成 (RAG)|RAG]] 需要将外部知识库（文档、网页等）分割成块 (Chunks)，并将每个块转换为[[../Core Technologies/嵌入 (Embedding)|嵌入向量]]存储起来。向量数据库提供了存储这些海量向量的场所。
    2.  **快速语义检索**: 当用户提问时，RAG 需要将用户问题也转换为[[../Core Technologies/嵌入 (Embedding)|嵌入向量]]，然后在知识库向量中快速找到语义最相关的几个文档块作为[[../检索增强生成 (RAG)|上下文]]。向量数据库的 ANN 搜索能力使得这一步非常高效。
    3.  **可扩展性**: 能够处理不断增长的向量数据。
    4.  **元数据过滤**: 通常支持在向量搜索的同时，根据元数据（如文档来源、时间戳、类别标签）进行过滤，提高检索的精确性。

    ```mermaid
    graph TD
        subgraph RAG 流程中的向量数据库
            direction LR
            A[知识库文档] --> B(文本分块);
            B --> C{文本嵌入<br/>([[../Core Technologies/嵌入 (Embedding)|Embedding]]);
            C --> D[(向量数据库<br/>存储文档向量)];

            E[用户查询] --> F{查询嵌入<br/>([[../Core Technologies/嵌入 (Embedding)|Embedding]]);
            F -- "查询向量" --> G{向量数据库<br/>(ANN 搜索)};
            D -- "被搜索" --> G;
            G -- "Top-K 相似向量<br/>(对应相关文档块)" --> H[检索到的上下文];
            H --> I[[[../大型语言模型 (LLM)|LLM]] 生成];
        end
        style D fill:#f9f, stroke:#333
        style G fill:#f9f, stroke:#333
    ```

    ## 常见的向量数据库

    *   **专用向量数据库**: Pinecone, Weaviate, Milvus, Qdrant, Chroma DB 等。它们专门为向量存储和搜索而设计优化。
    *   **现有数据库扩展**: PostgreSQL (通过 pgvector 扩展), Elasticsearch, Redis 等也增加了向量搜索功能，但可能在性能和功能上与专用库有差异。

    ## 对产品经理的意义

    *   **理解 RAG 技术栈**: 知道向量数据库是实现高效 RAG 的关键组件。
    *   **评估技术方案**: 在讨论需要语义搜索或 RAG 功能的产品时，能够理解引入向量数据库的必要性和相关考量（如选型、成本、性能）。
    *   **数据管理考量**: 考虑知识库的构建、[[../Core Technologies/嵌入 (Embedding)|Embedding]] 生成、向量数据库的维护和更新策略。
    *   **性能与成本权衡**: 不同的向量数据库或 ANN 算法在搜索速度、精度、内存消耗、成本等方面有不同的权衡。

    ## 总结

    向量数据库是 AI 应用（特别是涉及[[../Core Technologies/嵌入 (Embedding)|Embedding]]和语义相似性搜索的应用，如[[../检索增强生成 (RAG)|RAG]]）的重要基础设施。它使得在大规模向量数据中进行快速、高效的相似性搜索成为可能。产品经理理解其作用和价值，有助于更好地规划和设计依赖语义理解和检索能力的 AI 产品。

    ## 相关概念

    *   [[../Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]
    *   [[向量 (Vector)]]
    *   [[相似性搜索]]
    *   [[近似最近邻搜索 (ANN)]]
    *   [[../检索增强生成 (RAG)|检索增强生成 (RAG)]]
    *   [[信息检索]]
    *   [[数据库]]
    *   [[机器学习]]
""")

# Concepts/AI & ML/Models
ai_models_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Models')

llama_path = os.path.join(ai_models_folder, 'LLaMA 模型系列.md')
llama_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/llm, model/llama, type/open_source_model]
    aliases: [LLaMA, Llama 2, Llama 3]
    ---
    # LLaMA 模型系列

    [[主流 LLM 模型概览|返回 模型概览]] | [[../开源 vs 闭源模型|开源模型]]

    ## 概述

    LLaMA (Large Language Model Meta AI) 是由 **Meta AI (Facebook 的 AI 研究部门)** 开发的一系列**[[../大型语言模型 (LLM)|大型语言模型]]**。LLaMA 系列以其**开源**的特性（特别是 Llama 2 和 Llama 3 对商业使用也相对友好）和**强大的性能**（在同等参数规模下通常表现优异）而备受关注，极大地推动了[[../开源 vs 闭源模型|开源 LLM]]生态的发展。

    ## 主要版本与特点

    *   **LLaMA (原始版本)**: 2023 年初发布，最初仅供研究用途，但权重意外泄露，引发了开源社区的热潮。展示了在相对较小参数规模（7B, 13B, 33B, 65B）下也能达到接近[[../Models/GPT 模型系列|GPT-3]]等更大闭源模型性能的可能性。
    *   **Llama 2**: 2023 年中发布，是 LLaMA 的重大升级。
        *   **性能提升**: 在更多数据上训练，性能显著提升。
        *   **开源且可商用**: 允许商业使用（有一定限制条件，如月活用户超 7 亿需申请许可），极大地促进了其应用落地。
        *   **不同规模**: 提供 7B, 13B, 70B 等参数规模的模型。
        *   **Chat 版本**: 提供了经过指令微调和 RLHF (人类反馈强化学习) 优化的对话版本 (Llama 2-Chat)，更擅长遵循指令和进行对话。
    *   **Llama 3**: 2024 年 4 月发布，是 Llama 系列的最新一代。
        *   **性能再次飞跃**: 在多个基准测试上表现出色，被认为是当前最强的开源模型之一，尤其在 8B 和 70B 参数级别上，性能可与 [[../Models/GPT 模型系列|GPT-3.5]] 甚至 [[../Models/Gemini 模型系列|Gemini Pro]] 等闭源模型媲美。
        *   **改进的预训练**: 使用了更大、更高质量的数据集（超过 15T token），并改进了训练方法。
        *   **更长的上下文窗口**: 支持更长的输入文本。
        *   **更好的指令遵循能力**: 对话版本 (Llama 3 Instruct) 在理解和遵循复杂指令方面有显著提升。
        *   **多语言能力提升**: (未来版本会更强)
        *   **开源可商用**: 延续了 Llama 2 的开放政策。

    ## LLaMA 系列的影响

    *   **推动开源生态**: 为研究人员和开发者提供了强大的、可自由访问和修改的基础模型，催生了大量基于 LLaMA 的微调模型和应用。
    *   **降低使用门槛**: 使得中小型企业和个人开发者也能用上高性能的 LLM，而无需完全依赖昂贵的闭源 API。
    *   **促进竞争与创新**: 对闭源模型厂商构成了竞争压力，加速了整个 LLM 领域的发展。
    *   **数据隐私优势**: [[../开源 vs 闭源模型|允许本地部署]]，满足了对数据隐私要求高的场景。

    ## 对产品经理的意义

    *   **技术选型考量**: 在进行 [[../技术选型|技术选型]] 时，LLaMA 系列是[[../开源 vs 闭源模型|开源路径]]上的重要选项。需要评估其性能、部署成本、维护难度与特定产品需求的匹配度。
    *   **了解能力边界**: 关注 LLaMA 系列的最新进展和评测报告，了解当前顶级开源模型的真实能力和局限性。
    *   **社区价值**: 认识到开源社区的存在可以提供丰富的微调模型、工具和解决方案，但也需要评估社区贡献的质量和可靠性。
    *   **与闭源模型的权衡**: 能够清晰地阐述选择 LLaMA（开源）而非 GPT/Claude（闭源）的理由（或反之），参见 [[../开源 vs 闭源模型]]。

    ## 总结

    LLaMA 系列是 Meta 推出的高性能开源 LLM，对 AI 领域产生了深远影响。了解 LLaMA 的基本情况、版本迭代和核心优势，对于需要进行 LLM 技术选型的 AI 产品经理来说非常重要。它代表了开源 LLM 的重要力量，是闭源 API 之外的一个关键选择。

    ## 相关概念

    *   [[../大型语言模型 (LLM)|大型语言模型 (LLM)]]
    *   [[../开源 vs 闭源模型|开源 vs 闭源模型]]
    *   [[Meta AI]]
    *   [[微调 (Fine-tuning)]]
    *   [[RLHF]] (人类反馈强化学习)
    *   [[参数规模]]
    *   [[基准测试 (Benchmark)]]
    *   [[主流 LLM 模型概览]]
""")

mainstream_llms_path = os.path.join(ai_models_folder, '主流 LLM 模型概览.md')
mainstream_llms_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/llm, type/overview, model/comparison]
    aliases: [LLM Landscape, 主流大模型]
    ---
    # 主流 LLM 模型概览

    [[../00 - AI 与机器学习概览|返回 AI 概览]] | [[../大型语言模型 (LLM)|LLM 基础]]

    ## 概述

    当前[[../大型语言模型 (LLM)|大型语言模型 (LLM)]]领域发展迅速，涌现了众多来自不同公司和研究机构的模型。了解主流模型的名称、开发者、主要特点以及[[../开源 vs 闭源模型|开放性]]，对于 AI 产品经理进行技术选型和评估非常有帮助。

    以下列举一些当前（截至编写时，技术发展很快，请关注最新信息）比较知名和有影响力的 LLM 系列：

    ## 主流模型系列简介

    | 模型系列        | 主要开发者     | 主要特点/定位                                     | 开放性 ([[../开源 vs 闭源模型|Open/Closed]]) | 备注/知名版本举例                                    |
    | :-------------- | :------------- | :------------------------------------------------ | :------------------------------------ | :--------------------------------------------------- |
    | **[[GPT 模型系列|GPT 系列]]** | OpenAI         | **通用能力强**，引领多轮对话和指令遵循，API 易用 | **闭源 (API)**                      | GPT-3, GPT-3.5 (ChatGPT), GPT-4, GPT-4o              |
    | **[[Claude 模型系列|Claude 系列]]** | Anthropic      | 强调**安全性、伦理**和“宪法 AI”，长文本处理能力强 | **闭源 (API)**                      | Claude, Claude 2, Claude 3 (Haiku, Sonnet, Opus) |
    | **[[Gemini 模型系列|Gemini 系列]]** | Google DeepMind | **多模态能力** (原生支持文本、图像、音频、视频)，与 Google 生态集成 | **闭源 (API)** / 部分小模型[[../Models/Gemma 模型系列|开源 (Gemma)]] | Gemini Pro, Gemini Ultra, Gemini Flash             |
    | **[[LLaMA 模型系列|Llama 系列]]** | Meta AI        | **高性能开源**，推动开源生态发展，允许商用      | **开源**                            | Llama 2 (7B, 13B, 70B), Llama 3 (8B, 70B)           |
    | **[[Mistral 模型系列|Mistral 系列]]**| Mistral AI     | **高性能开源**，尤其在中等规模模型上表现优异，注重效率 | **开源** / 部分模型闭源 (API)       | Mistral 7B, Mixtral 8x7B (MoE), Mistral Large (API) |
    | **Falcon 系列** | TII (阿联酋)   | 早期重要的高性能开源模型                          | **开源**                            | Falcon 40B, Falcon 180B                            |
    | **(国内示例)**    | 如百度、阿里、智谱AI、月之暗面等 | 各具特色，中文能力通常较强，部分开源或提供 API | **混合** (部分开源，部分闭源 API) | 文心一言, 通义千问, ChatGLM, Kimi 等                 |

    **说明:**
    *   "B" 通常指 Billion (十亿) 参数。参数规模是衡量模型大小的一个指标，但不完全等同于性能。
    *   模型的性能通常通过各种[[基准测试 (Benchmark)]]来评估，但实际应用效果还需结合具体场景测试。
    *   [[开源 vs 闭源模型|开放性]]可能随时间变化，需关注官方发布。
    *   MoE (Mixture of Experts) 是一种模型架构，可以在保持较低计算成本的同时实现大规模参数的效果。

    ## 产品经理需要了解多深？

    这是一个常见问题，尤其对于非技术背景的 PM。参见 [[../核心技能/PM 对 LLM 的理解深度|PM 对 LLM 的理解深度]]。

    **核心观点**: PM **不需要**深入理解模型的算法细节或数学原理，但需要：

    1.  **理解核心概念**: 懂 [[../大型语言模型 (LLM)|LLM]], [[../Core Technologies/Transformer 模型|Transformer]], [[../Core Technologies/嵌入 (Embedding)|Embedding]], [[../检索增强生成 (RAG)|RAG]], [[../提示工程 (Prompt Engineering)|Prompt]], [[../模型幻觉 (Hallucination)|幻觉]], [[../模型鲁棒性 (Robustness)|鲁棒性]], [[../开源 vs 闭源模型|开源/闭源]] 等基本概念的含义和作用。
    2.  **了解能力边界**: 知道当前主流模型能做什么、不能做什么，它们的优势和局限性是什么。
    3.  **把握技术趋势**: 关注行业发展，了解不同模型的演进方向（例如：多模态、更长上下文、更高效率）。
    4.  **评估与选型**: 能够基于产品需求，与技术团队讨论并参与模型选型的决策，理解不同选择（如开源 vs. 闭源, 不同模型 API）在**成本、性能、定制化、隐私、风险**等方面的权衡。
    5.  **有效沟通**: 能够用相对准确的语言与工程师、算法科学家沟通需求和产品逻辑。

    [!tip] 面试建议
    面试时，展现你对主流模型的**了解广度**（知道有哪些主要玩家和它们的特点）和对**核心概念的理解深度**（能解释 RAG、幻觉等并讨论其影响），比深入某个具体模型的算法细节更重要。强调你如何基于这些理解来做产品决策。

    ## 总结

    LLM 领域百花齐放，了解主流模型的概况和特点，有助于 AI 产品经理把握行业动态，做出更明智的技术选型和产品规划。关键在于理解概念、能力边界和商业影响，而非钻研底层算法。

    ## 相关概念

    *   [[../大型语言模型 (LLM)|大型语言模型 (LLM)]]
    *   [[../开源 vs 闭源模型|开源 vs 闭源模型]]
    *   [[GPT 模型系列]] (Placeholder Link)
    *   [[Claude 模型系列]] (Placeholder Link)
    *   [[Gemini 模型系列]] (Placeholder Link)
    *   [[LLaMA 模型系列]]
    *   [[Mistral 模型系列]] (Placeholder Link)
    *   [[Gemma 模型系列]] (Placeholder Link)
    *   [[参数规模]]
    *   [[基准测试 (Benchmark)]]
    *   [[API (应用程序接口)]]
    *   [[../核心技能/PM 对 LLM 的理解深度|PM 对 LLM 的理解深度]]
""")

# Concepts/Product Management/核心技能
core_skills_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '核心技能')

pm_llm_depth_path = os.path.join(core_skills_folder, 'PM 对 LLM 的理解深度.md')
pm_llm_depth_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, skill/technical_literacy, type/soft_skill, domain/ai_ml]
    aliases: [产品经理需要懂多少AI技术, PM技术深度]
    ---
    # PM 对 LLM 的理解深度

    [[../../AI & ML/主流 LLM 模型概览|返回 模型概览]]

    ## 问题背景

    一个常见的疑问是：“作为 AI 产品经理，我需要理解像 [[../../AI & ML/Models/LLaMA 模型系列|LLaMA]]、[[../../AI & ML/Core Technologies/Transformer 模型|Transformer]] 这些技术到什么程度？” 尤其对于非技术背景出身的 PM 来说，把握合适的学习深度很重要。

    ## 核心原则：聚焦Why和What，理解How的影响

    产品经理的核心职责是定义**“Why”（为什么要做）**和**“What”（做什么）**，而技术团队负责**“How”（如何实现）**。但这并不意味着 PM 可以完全不懂技术。对于 AI PM，尤其需要理解“How”对“What”和“Why”的影响。

    **PM 不需要成为 AI 算法专家或工程师，不需要能够编写代码或推导数学公式。**

    **但是，PM 需要达到以下理解层次：**

    1.  **理解核心概念与原理 (Conceptual Understanding)**:
        *   **懂术语**: 能准确理解和使用 [[../../AI & ML/大型语言模型 (LLM)|LLM]], [[../../AI & ML/Core Technologies/Transformer 模型|Transformer]], [[../../AI & ML/Core Technologies/嵌入 (Embedding)|Embedding]], [[../../AI & ML/检索增强生成 (RAG)|RAG]], [[../../AI & ML/提示工程 (Prompt Engineering)|Prompt Engineering]], [[../../AI & ML/模型幻觉 (Hallucination)|幻觉]], [[../../AI & ML/模型鲁棒性 (Robustness)|鲁棒性]], [[../../AI & ML/微调 (Fine-tuning)|微调]], [[../../AI & ML/开源 vs 闭源模型|开源/闭源]] 等核心术语的**含义、作用和基本原理**。
        *   **知其然，知其所以然 (Why it works)**: 对关键技术（如 [[../../AI & ML/Core Technologies/Transformer 模型|Transformer]] 的注意力机制为何能处理长依赖，[[../../AI & ML/检索增强生成 (RAG)|RAG]] 为何能缓解幻觉）有**直觉性、概念性**的理解。

    2.  **了解能力边界与局限性 (Capabilities & Limitations)**:
        *   知道当前 AI 技术（特别是 LLM）擅长什么（文本生成、理解、摘要等），不擅长什么（严格逻辑推理、事实绝对准确性、实时感知物理世界等）。
        *   理解 [[../../AI & ML/模型幻觉 (Hallucination)|幻觉]]、[[../../AI & ML/模型偏见|偏见]]、[[../../AI & ML/模型鲁棒性 (Robustness)|鲁棒性]]差等是现有技术的固有局限性，需要在产品设计中考虑缓解策略。

    3.  **把握技术趋势 (Technology Trends)**:
        *   关注 AI 领域的主要发展方向（如多模态、更长上下文、Agent 化、效率优化等）。
        *   了解[[../../AI & ML/Models/主流 LLM 模型概览|主流模型]]的演进和能力差异。

    4.  **评估技术方案与权衡 (Evaluate Solutions & Trade-offs)**:
        *   能够参与技术选型的讨论，理解不同方案（如 [[../../AI & ML/开源 vs 闭源模型|API vs. 开源模型]]、不同 RAG 策略、是否需要[[../../AI & ML/微调 (Fine-tuning)|微调]]）在**成本、性能、开发周期、可控性、数据隐私、风险**等方面的利弊权衡 (Trade-offs)。
        *   能够基于产品需求，向技术团队提出合理的技术要求（例如：对[[../../AI & ML/模型幻觉 (Hallucination)|幻觉率]]的容忍度、响应[[../../AI & ML/大型语言模型 (LLM)|延迟]]要求）。

    5.  **有效沟通与协作 (Effective Communication & Collaboration)**:
        *   能够用**相对准确的技术语言**与工程师、算法科学家顺畅沟通产品需求、用户场景和业务逻辑。
        *   能够理解技术团队反馈的技术难点、风险和限制。

    ## 类比：产品经理 vs. 汽车设计师

    [!info] 类比
    想象一位汽车设计师（产品经理）。他/她不需要精通发动机的内部构造或流体力学计算（工程师/科学家的领域），但是：
    *   需要知道不同类型的发动机（汽油、电动、混合动力）的**基本原理、优缺点、适用场景**（核心概念）。
    *   需要了解当前发动机技术的**能力边界**（无法无限加速、有排放限制等）（局限性）。
    *   需要关注电池技术、自动驾驶等**发展趋势**。
    *   需要在设计时**权衡**动力、油耗/续航、成本、空间、安全性等因素（评估与权衡）。
    *   需要能与工程师沟通设计意图，并理解工程师提出的结构或制造方面的限制（沟通协作）。

    ## 如何学习？

    *   **阅读科普文章和博客**: 关注 AI 领域的知名媒体、技术博客和专家解读。
    *   **学习在线课程**: Coursera, Udacity, Fast.ai 等平台有许多面向非专业人士的 AI/ML 入门课程。
    *   **阅读产品案例分析**: 学习其他 AI 产品是如何应用技术的。
    *   **与技术同事交流**: 主动请教，参加技术分享会。
    *   **动手实践**: 尝试使用 ChatGPT 等工具，体验不同的 Prompt 和功能；如果可能，参与一些简单的 AI 项目。
    *   **聚焦概念而非细节**: 优先理解“是什么”、“为什么”、“有什么用”、“有什么风险”，而不是死抠算法细节。

    ## 总结

    AI 产品经理需要的是**技术素养 (Technical Literacy)**，而不是技术专精 (Technical Expertise)。关键在于**理解技术的核心概念、能力边界和商业影响，能够基于此进行产品决策，并与技术团队有效沟通协作**。不必为不懂算法细节而焦虑，持续学习，聚焦于技术如何服务于用户和业务价值即可。

    ## 相关概念

    *   [[技术素养]]
    *   [[../完整框架/04 - 技术与实现|技术与实现 (完整框架)]]
    *   [[../../AI & ML/00 - AI 与机器学习概览|AI 与机器学习概览]]
    *   [[../../AI & ML/Models/主流 LLM 模型概览|主流 LLM 模型概览]]
    *   [[权衡 (Trade-offs)]]
    *   [[沟通技巧]]
    *   [[学习能力]]
""")


# --- Modify existing LLM content to include new links ---
# NOTE: In a real update scenario, you'd read the existing file first.
# Here, we redefine the content string with added links for simplicity in this script.
llm_content_updated = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/llm, type/definition, technology]
    aliases: [LLM, Large Language Model]
    ---
    # 大型语言模型 (Large Language Model - LLM)

    [[00 - AI 与机器学习概览|返回 AI 概览]]

    ## 概述

    大型语言模型 (LLM) 是一种基于**[[深度学习]]**（特别是 [[Core Technologies/Transformer 模型|Transformer]] 架构）的人工智能模型，它通过在**海量文本数据**上进行训练，学习语言的模式、结构和知识，从而能够**理解和生成**类似人类的自然语言文本。

    LLM 是当前许多先进 AI 应用（包括 AI 聊天机器人、内容创作工具、代码生成器以及像 Amazon Rufus 这样的 AI 购物助手）的核心驱动力。理解其基础有助于理解 [[Core Technologies/Transformer 模型|Transformer]] 和 [[Core Technologies/嵌入 (Embedding)|Embedding]] 等相关技术。

    ## LLM 的核心能力

    *   **文本生成 (Text Generation)**: 创作文章、故事、邮件、代码等。
    *   **问答 (Question Answering)**: 基于其内部知识或结合外部信息回答问题。
    *   **文本摘要 (Summarization)**: 将长文本压缩成关键信息。
    *   **翻译 (Translation)**: 在不同语言之间进行翻译。
    *   **情感分析 (Sentiment Analysis)**: 判断文本所表达的情感倾向。
    *   **对话系统 (Conversational AI)**: 进行多轮对话交互。
    *   **代码生成/理解 (Code Generation/Understanding)**: 根据自然语言描述生成代码或解释代码。

    ## LLM 的工作原理 (简化理解)

    1.  **训练 (Training)**:
        *   LLM 在包含互联网文本、书籍、代码等的大规模数据集上进行**预训练 (Pre-training)**。
        *   目标是学习预测文本序列中的下一个词 (Next Token Prediction) 或填补文本中的空白 (Masked Language Modeling)。通过这个过程，模型学习语法、语义、常识知识等。输入文本首先会被转换为 [[Core Technologies/嵌入 (Embedding)|嵌入向量]]。
        *   这个阶段计算量巨大，成本高昂。
    2.  **[[微调 (Fine-tuning)|微调 (Fine-tuning)]]**: (可选但常见)
        *   为了让模型在特定任务（如问答、摘要、特定领域对话）上表现更好，可以使用**更小、更具体**的数据集对预训练好的模型进行微调。
        *   例如，可以用电商领域的问答数据微调 LLM，使其更擅长回答购物相关问题。
    3.  **推理/推断 (Inference)**:
        *   当用户输入一个**[[提示工程 (Prompt Engineering)|提示 (Prompt)]]**（例如一个问题）时，模型会根据其学到的模式和知识，**预测最可能**接在后面的词语序列，从而生成回答。
        *   生成过程通常是**概率性**的，可以通过调整参数（如 Temperature）来控制输出的随机性和创造性。

    ```mermaid
    graph LR
        A["海量文本数据<br/>(互联网, 书籍等)"] --> B("文本->[[Core Technologies/嵌入 (Embedding)|Embedding]]") --> C(预训练 Pre-training<br/>(基于 [[Core Technologies/Transformer 模型|Transformer]])<br/>学习语言模式);
        C --> D["预训练 LLM<br/>(基础模型)"];
        F["特定任务数据<br/>(如电商问答)"] --> G(微调 Fine-tuning<br/>优化特定能力);
        D --> G;
        G --> H["微调后 LLM<br/>(针对性优化)"];
        I["用户[[提示工程 (Prompt Engineering)|提示]] (Prompt)<br/>(例如: '这件衣服有其他颜色吗?')"] --> J(推理 Inference<br/>预测后续文本);
        D --> J;
        H --> J;
        J --> K["模型输出 (Output)<br/>(例如: '有的, 这件衣服还有蓝色和...')"];

        style D fill:#eee,stroke:#333
        style H fill:#ccf,stroke:#333
    ```

    ## LLM 的关键考量 (产品角度)

    *   **[[模型幻觉 (Hallucination)|幻觉 (Hallucination)]]**: LLM 可能生成看似合理但实际上是错误的或无中生有的信息。这是 LLM 应用中的核心挑战。
    *   **[[模型鲁棒性 (Robustness)|鲁棒性]]**: 模型在面对不同类型、甚至略有干扰的输入时，表现是否稳定？
    *   **[[提示工程 (Prompt Engineering)|提示工程]]**: 如何设计有效的提示来引导模型产生期望的输出？
    *   **知识更新**: LLM 的知识截止于其训练数据。如何让它获取并使用最新的信息？（[[检索增强生成 (RAG)|RAG]] 是常用方法）
    *   **成本 (Cost)**: 训练和运行 LLM（尤其是大型模型）的计算成本很高。API 调用也需要付费。
    *   **延迟 (Latency)**: 模型生成响应需要时间，对于实时交互应用需要考虑延迟问题。
    *   **[[开源 vs 闭源模型|开源 vs. 闭源]]**: 如何选择合适的模型？（见 [[开源 vs 闭源模型]]）
    *   **[[模型偏见|偏见]]与伦理 (Bias & Ethics)**: 训练数据中可能存在的偏见会被模型学到，导致输出带有歧视性或不公平。需要进行风险评估和缓解。
    *   **[[../技术相关/数据隐私|数据隐私]]**: 用户输入的数据如何处理？是否会被用于再训练？

    ## 与 AI 购物助手 (Rufus) 的关联

    Rufus 类助手很可能利用 LLM 来：
    *   理解用户的自然语言查询（商品咨询、比较、售后问题等）。
    *   生成自然的、对话式的回答。
    *   可能结合 [[检索增强生成 (RAG)|RAG]] 技术，从亚马逊庞大的商品目录、评论、订单信息等实时数据库中检索信息，以提供准确、最新的答案，减少[[模型幻觉 (Hallucination)|幻觉]]。
    *   通过[[提示工程 (Prompt Engineering)|精心设计的提示]]和可能的[[微调 (Fine-tuning)|微调]]，确保回答符合品牌调性、聚焦于购物场景。

    ## 总结

    LLM 是驱动现代 AI 应用（如 AI 助手）的关键技术。产品经理需要理解其基本原理、能力、优势和局限性（特别是[[模型幻觉 (Hallucination)|幻觉]]、成本、[[模型鲁棒性 (Robustness)|鲁棒性]]等），以便在产品设计、技术选型和风险管理中做出明智的决策。

    ## 相关概念

    *   [[00 - AI 与机器学习概览|AI 与机器学习概览]]
    *   [[深度学习]]
    *   [[Core Technologies/Transformer 模型|Transformer]]
    *   [[Core Technologies/嵌入 (Embedding)|Embedding]]
    *   [[提示工程 (Prompt Engineering)|提示工程 (Prompt Engineering)]]
    *   [[模型幻觉 (Hallucination)|模型幻觉 (Hallucination)]]
    *   [[模型鲁棒性 (Robustness)|模型鲁棒性 (Robustness)]]
    *   [[检索增强生成 (RAG)|检索增强生成 (RAG)]]
    *   [[开源 vs 闭源模型|开源 vs 闭源模型]]
    *   [[微调 (Fine-tuning)]]
    *   [[AI 伦理]]
    *   [[../Product Management/完整框架/04 - 技术与实现|技术与实现 (完整框架)]]
    *   [[Models/主流 LLM 模型概览|主流 LLM 模型概览]]
    *   [[../Product Management/核心技能/PM 对 LLM 的理解深度|PM 对 LLM 的理解深度]]
""")


# --- Main Script Logic ---
def main():
    print("Starting Obsidian Knowledge Base Generation (Part 6 - AI Core Tech & Models)...")
    print(f"Target Root Directory: {os.path.abspath(TARGET_ROOT_DIRECTORY)}")
    print(f"Overwrite Existing Files: {OVERWRITE_EXISTING}")

    # Prioritized based on user request: Transformer intuition, LLaMA/models, PM understanding depth
    files_to_create = {
        # AI Core Technologies (Intuition focused)
        transformer_path: transformer_content,
        embedding_path: embedding_content,
        vector_db_path: vector_db_content, # Essential for RAG understanding
        # AI Models Landscape (Addressing LLaMA & comparison)
        llama_path: llama_content,
        mainstream_llms_path: mainstream_llms_content,
        # Core Skills (Addressing PM's required depth)
        pm_llm_depth_path: pm_llm_depth_content,
        # Update existing LLM file content with new links
        llm_path: llm_content_updated, # Use the updated content string
    }

    # Create necessary base directories if they don't exist
    os.makedirs(ai_core_tech_folder, exist_ok=True)
    os.makedirs(ai_models_folder, exist_ok=True)
    os.makedirs(core_skills_folder, exist_ok=True)
    # Ensure the base AI/ML folder exists for the updated LLM file path
    os.makedirs(os.path.dirname(llm_path), exist_ok=True)
    print("Base directories ensured.")

    for filepath, content in files_to_create.items():
        if not OVERWRITE_EXISTING and os.path.exists(filepath):
            print(f"Skipping existing file: {filepath}")
            continue
        write_file(filepath, content)

    print("\nObsidian Knowledge Base Generation (Part 6) Complete.")
    print("Focus was on core AI technologies (Transformer, Embedding, VectorDB), LLM landscape (LLaMA, comparison), and PM's required technical depth.")

if __name__ == "__main__":
    main()
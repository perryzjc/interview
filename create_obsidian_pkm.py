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

# --- Knowledge Base Content Definitions (Part 9 - Foundational & IR Concepts) ---

# --- Concepts/Fundamentals ---
# (Creating this new folder for foundational concepts)
fundamentals_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Fundamentals')

vector_path = os.path.join(fundamentals_folder, '向量 (Vector).md')
vector_content = textwrap.dedent("""\
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

    [!info] 示例
    *   `国王` 可能被表示为向量 `(0.8, 0.7, 0.6, ..., -0.2)`
    *   `女王` 可能被表示为向量 `(0.7, 0.8, 0.5, ..., -0.1)`
    *   `香蕉` 可能被表示为向量 `(-0.9, -0.8, 0.6, ..., 0.5)`
    *   可以看到 `国王` 和 `女王` 的向量表示（在所有维度上）会比它们与 `香蕉` 的向量表示更相似。

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
""")

database_path = os.path.join(fundamentals_folder, '数据库.md')
database_content = textwrap.dedent("""\
    ---
    tags: [topic/fundamentals, concept/database, type/definition, domain/computer_science]
    aliases: [Database, DB]
    ---
    # 数据库 (Database)

    ## 概述

    数据库 (Database, DB) 是一个**结构化的、持久化存储的数据集合**，通常由数据库管理系统 (Database Management System, DBMS) 进行管理。数据库使得数据的存储、检索、更新和管理更加高效和有组织。

    ## 数据库的主要类型

    根据数据组织方式和特点，数据库可以分为多种类型：

    1.  **关系型数据库 (Relational Database)**:
        *   **特点**: 基于**关系模型**，将数据存储在具有**行和列的二维表 (Table)** 中，表之间可以通过**键 (Key)** 建立关联。使用 **[[SQL (结构化查询语言)|SQL]]** 进行查询和操作。
        *   **优势**: 结构清晰，[[事务处理 (Transaction)]] (ACID特性) 成熟可靠，数据一致性高。
        *   **劣势**: 模式 (Schema) 相对固定，不易扩展，处理非结构化数据或超大规模数据可能效率不高。
        *   **代表**: MySQL, PostgreSQL, Oracle, SQL Server, SQLite。
    2.  **NoSQL 数据库 (Not Only SQL)**:
        *   **特点**: 通常**不遵循严格的关系模型和固定的表结构**，设计用于大规模、高并发、模式灵活的应用场景。包含多种子类型：
            *   **键值存储 (Key-Value Store)**: 数据以简单的键值对形式存储。(如: Redis, Memcached)
            *   **文档数据库 (Document Database)**: 数据以类似 [[JSON]] 或 BSON 的**文档**形式存储，模式灵活。(如: MongoDB, Couchbase)
            *   **列式数据库 (Column-Family Store)**: 数据按列族存储，适合大规模聚合查询。(如: Cassandra, HBase)
            *   **图形数据库 (Graph Database)**: 专注于存储**节点和边**，高效处理实体间的复杂关系。(如: Neo4j, Nebula Graph)
        *   **优势**: 高可扩展性，高性能读写，模式灵活，适合半结构化和非结构化数据。
        *   **劣势**: 通常牺牲了部分一致性（遵循 BASE 原则而非 ACID），事务支持较弱。
    3.  **[[../AI & ML/Core Technologies/向量数据库|向量数据库 (Vector Database)]]**:
        *   **特点**: **专门用于存储和高效查询高维[[向量 (Vector)|向量]]**，核心功能是[[../AI & ML/Information Retrieval/相似性搜索|相似性搜索]]（特别是[[../AI & ML/Information Retrieval/近似最近邻搜索 (ANN)|ANN]]）。
        *   **优势**: 在海量向量中进行快速语义相似性检索。
        *   **劣势**: 通常不适合存储和查询传统的结构化数据，功能相对专一。
        *   **代表**: Pinecone, Milvus, Weaviate, Qdrant, Chroma DB (以及带向量扩展的传统数据库如 PostgreSQL+pgvector)。
    4.  **其他类型**: 时间序列数据库 (Time-Series DB), 搜索数据库 (Search Engine DB, 如 Elasticsearch) 等。

    ```mermaid
    graph TD
        A["数据库 (Database)"] --> B["关系型数据库 (Relational)<br/>(表格, SQL, ACID)"];
        A --> C["NoSQL 数据库<br/>(模式灵活, 高扩展性, BASE)"];
        A --> D["[[../AI & ML/Core Technologies/向量数据库|向量数据库 (Vector)]]<br/>(向量存储, [[../AI & ML/Information Retrieval/相似性搜索|相似性搜索]])"];
        A --> E["其他 (时间序列等)"];

        C --> C1["键值存储 (Key-Value)"];
        C --> C2["文档数据库 (Document)"];
        C --> C3["列式数据库 (Column-Family)"];
        C --> C4["图形数据库 (Graph)"];

        subgraph 传统数据存储
            B; C1; C2; C3; C4; E;
        end
        subgraph AI/向量数据存储
            D;
        end

        style D fill:#ccf, stroke:#333
    ```

    ## 对产品经理的意义

    *   **理解数据存储基础**: 知道数据是如何被组织和存储的。
    *   **参与技术选型**: 能够与工程师讨论不同数据库类型在特定场景下的优劣势（例如：需要强一致性事务用关系型，需要灵活存储用户信息用文档型，需要语义搜索用向量型）。
    *   **考虑数据需求**: 在设计功能时，考虑需要存储哪些数据，数据的结构如何，对查询性能的要求等。
    *   **理解技术限制**: 了解不同数据库在扩展性、一致性、查询能力等方面的限制。

    ## 总结

    数据库是现代应用的基础设施。了解不同数据库类型的特点和适用场景，有助于产品经理更好地理解系统架构，参与技术决策，并设计出能够有效利用数据的功能。特别是[[../AI & ML/Core Technologies/向量数据库|向量数据库]]，在当前 AI 应用（尤其是 [[../AI & ML/检索增强生成 (RAG)|RAG]]）中扮演着越来越重要的角色。

    ## 相关概念

    *   [[数据 (Data)]]
    *   [[数据库管理系统 (DBMS)]]
    *   [[关系模型]]
    *   [[表 (Table)]]
    *   [[SQL (结构化查询语言)|SQL]]
    *   [[事务处理 (Transaction)]] (ACID vs BASE)
    *   [[NoSQL]]
    *   [[JSON]]
    *   [[../AI & ML/Core Technologies/向量数据库|向量数据库]]
    *   [[技术架构]]
""")

ml_path = os.path.join(fundamentals_folder, '机器学习 (ML).md')
ml_content = textwrap.dedent("""\
    ---
    tags: [topic/fundamentals, concept/ml, type/definition, domain/ai_ml]
    aliases: [ML, Machine Learning, 机器学习定义]
    ---
    # 机器学习 (Machine Learning - ML)

    [[../AI & ML/00 - AI 与机器学习概览|返回 AI 概览]]

    ## 概述

    机器学习 (Machine Learning, ML) 是人工智能 (AI) 的一个核心子领域，专注于研究如何让计算机系统**利用数据来提高其在特定任务上的性能，而无需进行显式编程**。简单来说，就是让机器具备从经验（数据）中“学习”的能力。

    传统编程是人告诉机器**如何**做（明确的规则和指令），而机器学习是人给机器提供**数据**和**目标**，让机器自己**学习如何**做。

    ## 机器学习的基本流程 (简化)

    ```mermaid
    graph LR
        A[1. 数据收集与准备<br/>(采集, 清洗, 标注)] --> B[2. 特征工程<br/>(选择/提取/转换特征)];
        B --> C[3. 模型选择<br/>(选择合适的算法)];
        C --> D[4. 模型训练<br/>(用训练数据学习参数)];
        D --> E[5. 模型评估<br/>(用测试数据评估性能)];
        E -- "性能达标?" --> F(6. 模型部署<br/>(上线应用));
        E -- "否" --> C;
        F --> G(7. 模型监控与迭代);
        G --> A;

        subgraph 机器学习流程
            direction LR
            A ~~~ B ~~~ C ~~~ D ~~~ E ~~~ F ~~~ G
        end
    ```

    1.  **数据收集与准备**: 获取相关数据，进行清洗（处理缺失值、异常值）、标注（如果需要监督学习）。
    2.  **特征工程**: 从原始数据中选择、提取或转换出对模型学习有帮助的特征 (Features)。(在[[../AI & ML/Core Technologies/深度学习|深度学习]]中，特征工程的重要性有所降低，模型能自动学习特征)。
    3.  **模型选择**: 根据任务类型（分类、回归、聚类等）和数据特点，选择合适的机器学习算法（如[[线性回归]]、[[逻辑回归]]、[[决策树]]、[[支持向量机 (SVM)]]、[[神经网络]]等）。
    4.  **模型训练**: 将准备好的训练数据输入给选定的模型算法，算法会自动调整内部参数，以最小化预测错误或达成特定目标。
    5.  **模型评估**: 使用未参与训练的测试数据来评估模型的性能，常用的[[../AI & ML/Evaluation/评估指标 (Evaluation Metrics)|评估指标]]包括准确率、精确率、召回率、F1 分数、AUC 等（取决于任务）。
    6.  **模型部署**: 将训练好的、性能达标的模型部署到实际应用中，对外提供预测或决策服务。
    7.  **模型监控与迭代**: 持续监控模型在线上的表现，收集新数据，根据需要重新训练或更新模型。

    ## 机器学习的主要类型

    根据学习方式和数据类型的不同，机器学习主要分为：

    1.  **监督学习 (Supervised Learning)**:
        *   **特点**: 使用**带有标签 (Labeled)** 的数据进行训练。模型学习从输入特征到已知输出标签之间的映射关系。
        *   **任务**:
            *   **分类 (Classification)**: 预测输入属于哪个预定义的类别（例如：判断邮件是否为垃圾邮件，识别图像中的猫或狗）。
            *   **回归 (Regression)**: 预测一个连续的数值（例如：预测房价，预测股票价格）。
    2.  **无监督学习 (Unsupervised Learning)**:
        *   **特点**: 使用**没有标签**的数据进行训练。模型需要自己发现数据中的结构、模式或关系。
        *   **任务**:
            *   **聚类 (Clustering)**: 将相似的数据点分组（例如：用户分群）。
            *   **降维 (Dimensionality Reduction)**: 减少数据的特征数量，同时保留重要信息（例如：[[主成分分析 (PCA)]]）。
            *   **关联规则挖掘**: 发现数据项之间的关联性（例如：“购买啤酒的人也倾向于购买尿布”）。
    3.  **强化学习 (Reinforcement Learning - RL)**:
        *   **特点**: 模型（称为智能体 Agent）通过与**环境 (Environment)** 互动来学习。智能体执行**动作 (Action)**，环境给出**奖励 (Reward)** 或惩罚，智能体的目标是学习一个**策略 (Policy)** 来最大化累积奖励。
        *   **应用**: [[游戏 AI]] (如 AlphaGo), [[机器人控制]], [[推荐系统]] 优化等。RLHF (人类反馈强化学习) 被用于[[../微调 (Fine-tuning)|微调]] [[../大型语言模型 (LLM)|LLM]] 以更好地遵循指令。

    ```mermaid
    graph TD
        A["机器学习 (ML)"] --> B["监督学习<br/>(有标签数据)"];
        A --> C["无监督学习<br/>(无标签数据)"];
        A --> D["强化学习<br/>(与环境互动学习)"];

        B --> B1["分类 (类别预测)"];
        B --> B2["回归 (数值预测)"];

        C --> C1["聚类 (数据分组)"];
        C --> C2["降维 (特征压缩)"];
        C --> C3["关联规则"];

        D --> D1["策略学习 (最大化奖励)"];
    ```

    ## 对产品经理的意义

    *   **理解 AI 能力来源**: 知道机器学习是当前 AI 能力的主要来源，是数据驱动的。
    *   **评估可行性**: 对一个 AI 功能需求，能初步判断它属于哪种机器学习任务，大致了解其实现难度和对数据的要求（例如，监督学习需要大量标注数据）。
    *   **数据重要性**: 深刻理解数据质量和数量对机器学习模型效果的决定性作用（Garbage In, Garbage Out）。
    *   **沟通协作**: 能与数据科学家、ML 工程师就模型目标、评估指标、数据需求等进行有效沟通。
    *   **关注模型评估与迭代**: 理解模型需要持续评估和优化。

    ## 总结

    机器学习是让机器从数据中学习的核心技术。理解其基本流程、主要类型（监督、无监督、强化）及其典型任务，有助于产品经理更好地理解 AI 产品的底层逻辑，评估需求可行性，并认识到数据在 AI 产品开发中的关键作用。

    ## 相关概念

    *   [[人工智能 (AI)]]
    *   [[../AI & ML/Core Technologies/深度学习|深度学习]] (ML 的一个分支)
    *   [[数据 (Data)]]
    *   [[特征工程]]
    *   [[模型训练]]
    *   [[模型评估]]
    *   [[../AI & ML/Evaluation/评估指标 (Evaluation Metrics)|评估指标]]
    *   [[监督学习]]
    *   [[无监督学习]]
    *   [[强化学习 (RL)]]
    *   [[分类 (Classification)]]
    *   [[回归 (Regression)]]
    *   [[聚类 (Clustering)]]
""")

# --- Concepts/AI & ML/Core Technologies ---
# (Moving Deep Learning here as it's a core tech under ML)
ai_core_tech_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Core Technologies')

deep_learning_path = os.path.join(ai_core_tech_folder, '深度学习.md')
deep_learning_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/deep_learning, type/definition, domain/ml]
    aliases: [Deep Learning, DL, 深度神经网络]
    ---
    # 深度学习 (Deep Learning - DL)

    [[../00 - AI 与机器学习概览|返回 AI 概览]] | [[../../Fundamentals/机器学习 (ML)|从属于: 机器学习]]

    ## 概述

    深度学习 (Deep Learning, DL) 是[[../../Fundamentals/机器学习 (ML)|机器学习 (ML)]]的一个**特定分支**，其核心是使用包含**多个处理层（因此称为“深度”）的人工神经网络 (Artificial Neural Networks, ANN)** 来学习数据的复杂模式和表示。

    与传统的机器学习方法相比，深度学习的一个关键优势在于其**自动特征学习**能力。传统 ML 通常需要领域专家进行复杂的[[../../Fundamentals/机器学习 (ML)|特征工程]]来提取有效特征，而深度学习模型可以直接从原始数据（如图像像素、文本词语）中逐层学习越来越抽象、越来越复杂的特征表示。

    深度学习在许多领域取得了突破性进展，尤其是在**计算机视觉 (Computer Vision)**、**[[../Core Technologies/自然语言处理 (NLP)|自然语言处理 (NLP)]]** 和**语音识别 (Speech Recognition)** 等方面。

    ## 核心构成：人工神经网络 (ANN)

    深度学习的基础是人工神经网络，其结构受到人脑神经元连接方式的启发：

    *   **神经元 (Neuron)**: 基本计算单元，接收输入，进行加权求和和[[激活函数]]处理，产生输出。
    *   **层 (Layer)**: 神经元按层组织。
        *   **输入层 (Input Layer)**: 接收原始数据。
        *   **隐藏层 (Hidden Layers)**: 位于输入层和输出层之间，负责进行特征提取和转换。**“深度”学习指的就是隐藏层数量多**。
        *   **输出层 (Output Layer)**: 产生最终的预测结果（如分类概率、回归值）。
    *   **连接与权重 (Connections & Weights)**: 层与层之间的神经元通过带权重的连接进行信息传递。模型训练的过程就是调整这些权重，以使模型能够做出准确的预测。
    *   **[[激活函数]] (Activation Function)**: 引入非线性，使得神经网络能够学习复杂模式（否则多层线性网络等效于单层）。常用如 ReLU, Sigmoid, Tanh。

    ```mermaid
    graph TD
        subgraph "人工神经网络 (示意)"
            direction LR
            subgraph Input Layer
                I1(Input 1)
                I2(Input 2)
                I3(...)
            end
            subgraph Hidden Layer 1
                 H11(Node)
                 H12(Node)
                 H13(...)
            end
             subgraph Hidden Layer 2 (更多层 = '深度')
                 H21(Node)
                 H22(Node)
                 H23(...)
             end
             subgraph Output Layer
                 O1(Output 1)
                 O2(...)
             end

            Input Layer -- "连接权重" --> Hidden Layer 1;
            Hidden Layer 1 -- "连接权重" --> Hidden Layer 2;
            Hidden Layer 2 -- "连接权重" --> Output Layer;
        end
    ```

    ## 常见的深度学习架构

    除了基本的多层感知机 (MLP)，还有一些针对特定数据类型设计的特殊神经网络架构：

    *   **卷积神经网络 (Convolutional Neural Networks, CNN)**: 特别擅长处理**网格状数据**，如**图像**。通过卷积层提取局部特征，池化层降维。在图像识别、目标检测等领域非常成功。
    *   **循环神经网络 (Recurrent Neural Networks, RNN)**: 设计用于处理**序列数据**（如文本、时间序列），具有“记忆”能力，能考虑先前的信息。变体如 LSTM, GRU 解决了 RNN 的梯度消失/爆炸问题。
    *   **[[../Core Technologies/Transformer 模型|Transformer]]**: **当前 NLP 领域的主流架构**。基于[[自注意力]]机制，能有效捕捉长距离依赖并支持并行计算。是 [[../大型语言模型 (LLM)|LLM]] 的基础。

    ## 深度学习的优势

    *   **强大的特征学习能力**: 能够自动从原始数据中学习复杂、抽象的特征表示。
    *   **处理非结构化数据**: 在图像、文本、语音等非结构化数据上表现优异。
    *   **性能卓越**: 在许多复杂的 AI 任务上达到了 SOTA (State-of-the-Art) 水平。
    *   **端到端学习**: 可以直接从输入到输出进行学习，减少了对传统特征工程的依赖。

    ## 深度学习的挑战

    *   **需要大量数据**: 通常需要比传统 ML 方法更多的（通常是标注好的）数据才能达到良好性能。
    *   **计算成本高**: 训练深度模型需要强大的计算资源（如 GPU/TPU）和较长时间。
    *   **可解释性差 (黑箱问题)**: 模型内部决策过程复杂，难以直观理解为什么模型会做出某个预测。
    *   **调参复杂**: 模型架构和训练过程涉及众多超参数，需要经验和实验来优化。
    *   **对数据质量敏感**: 对噪声和偏差数据比较敏感。

    ## 对产品经理的意义

    *   **理解 AI 技术前沿**: 知道深度学习是驱动当前许多最先进 AI 功能（图像识别、NLP、LLM）的核心技术。
    *   **认识数据和算力需求**: 理解深度学习项目通常需要大量数据和计算资源，影响项目规划和预算。
    *   **关注可解释性问题**: 对于需要高透明度和可信度的应用（如金融、医疗），需要考虑深度学习模型的“黑箱”特性带来的挑战。
    *   **评估技术方案**: 了解 CNN、RNN、Transformer 等不同架构的适用场景（例如，处理图像用 CNN，处理文本序列用 Transformer）。

    ## 总结

    深度学习是机器学习中一个强大的分支，通过构建深层神经网络，实现了在图像、文本、语音等复杂数据上的卓越表现，是当前 AI 革命的核心引擎。产品经理需要理解其基本原理、优势、挑战以及对数据和算力的要求，以便更好地与技术团队合作，规划和评估基于深度学习的 AI 产品。

    ## 相关概念

    *   [[../../Fundamentals/机器学习 (ML)|机器学习 (ML)]]
    *   [[人工智能 (AI)]]
    *   [[人工神经网络 (ANN)]]
    *   [[神经元]]
    *   [[隐藏层]]
    *   [[激活函数]]
    *   [[卷积神经网络 (CNN)]]
    *   [[循环神经网络 (RNN)]]
    *   [[../Core Technologies/Transformer 模型|Transformer 模型]]
    *   [[特征学习]]
    *   [[../../Fundamentals/数据 (Data)|数据]]
    *   [[算力]]
    *   [[可解释性 AI (Explainable AI)]]
""")


# --- Concepts/AI & ML/Information Retrieval ---
# (Creating this new folder)
ir_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Information Retrieval')

similarity_search_path = os.path.join(ir_folder, '相似性搜索.md')
similarity_search_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/similarity_search, type/technique, domain/ir, domain/vector_database]
    aliases: [Similarity Search, 语义搜索, 向量搜索]
    ---
    # 相似性搜索 (Similarity Search)

    [[../Core Technologies/向量数据库|相关: 向量数据库]] | [[信息检索|返回 信息检索]]

    ## 概述

    相似性搜索，在 AI/ML 领域通常特指**基于[[../Core Technologies/嵌入 (Embedding)|嵌入向量]]的语义相似性搜索**，其目标是在一个大规模的[[../../Fundamentals/向量 (Vector)|向量]]集合中，找到与给定查询向量**最相似**（即在向量空间中距离最近）的一个或多个向量。

    与传统的基于关键词匹配的搜索不同，相似性搜索能够理解查询和目标内容的**语义含义**，即使它们使用的具体词语不同，只要意思相近，也能被匹配到。

    ## 核心原理

    1.  **[[../Core Technologies/嵌入 (Embedding)|向量化]]**: 将需要被搜索的内容（如文档、图片、商品）和用户的查询都使用**相同的**[[../Core Technologies/嵌入 (Embedding)|嵌入模型]]转换为高维[[../../Fundamentals/向量 (Vector)|向量]]。
    2.  **[[../Core Technologies/向量数据库|索引与存储]]**: 将内容向量存储在[[../Core Technologies/向量数据库|向量数据库]]或专门的索引结构中，以便快速检索。
    3.  **[[距离/相似度计算]]**: 定义一个度量标准来衡量向量之间的相似性，常用的是[[余弦相似度]]（衡量方向相似性）或[[欧氏距离]]（衡量空间距离）。
    4.  **[[近邻搜索]]**: 当给定一个查询向量时，在索引中搜索与其相似度最高（或距离最近）的 K 个向量（[[K近邻 (KNN)]]）。为了效率，通常使用[[近似最近邻搜索 (ANN)]]算法。

    [!info] 示例
    用户搜索“适合夏天穿的透气跑鞋”，即使数据库中的某个商品描述是“轻量化网面运动鞋，夏季跑步优选”，由于它们的[[../Core Technologies/嵌入 (Embedding)|嵌入向量]]在语义空间中距离很近，相似性搜索也能将其匹配出来，而传统的关键词搜索可能就无法匹配。

    ## 应用场景

    *   **[[../检索增强生成 (RAG)|检索增强生成 (RAG)]]**: 核心步骤！根据用户问题向量，在知识库向量中搜索最相关的上下文。
    *   **语义文本搜索**: 比关键词搜索更智能的文档/网页搜索。
    *   **图像/视频检索**: 以图搜图，以视频搜视频。
    *   **[[推荐系统]]**: 查找与用户兴趣向量或用户看过的物品向量相似的其他物品。
    *   **重复内容检测**: 查找相似的文档或图片。
    *   **异常检测**: 正常数据的向量通常聚集在一起，远离这些聚类的向量可能是异常点。

    ## 关键技术

    *   **[[../Core Technologies/嵌入 (Embedding)|嵌入模型 (Embedding Models)]]**: 生成高质量、能够准确反映语义的向量至关重要。
    *   **[[距离/相似度度量]]**: 选择合适的度量标准（[[余弦相似度]], [[欧氏距离]]等）。
    *   **[[近似最近邻搜索 (ANN)]] 算法**: HNSW, LSH, IVF 等，用于在速度和精度之间做权衡，实现快速搜索。
    *   **[[../Core Technologies/向量数据库|向量数据库]]**: 提供存储、索引和查询向量的基础设施。

    ## 对产品经理的意义

    *   **理解智能搜索基础**: 知道相似性搜索是实现超越关键词匹配的语义理解搜索的核心。
    *   **评估 RAG 可行性**: 理解[[../检索增强生成 (RAG)|RAG]] 依赖于高效的相似性搜索来查找相关上下文。
    *   **定义产品需求**: 在设计需要“智能搜索”、“相关推荐”、“问答”等功能时，可以考虑相似性搜索方案。
    *   **关注性能与精度**: 了解[[近似最近邻搜索 (ANN)|ANN]] 带来的速度与精度的权衡，需要在产品层面设定合理的预期。

    ## 总结

    相似性搜索（特别是基于向量的语义搜索）是现代 AI 应用中的一项关键技术，它使得机器能够理解内容的深层含义并进行智能匹配。它是[[../检索增强生成 (RAG)|RAG]]、语义搜索、智能推荐等功能的技术基石。

    ## 相关概念

    *   [[../../Fundamentals/向量 (Vector)|向量 (Vector)]]
    *   [[../Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]
    *   [[../Core Technologies/向量数据库|向量数据库]]
    *   [[近似最近邻搜索 (ANN)]]
    *   [[K近邻 (KNN)]]
    *   [[余弦相似度]]
    *   [[欧氏距离]]
    *   [[信息检索]]
    *   [[../检索增强生成 (RAG)|检索增强生成 (RAG)]]
""")

ann_search_path = os.path.join(ir_folder, '近似最近邻搜索 (ANN).md')
ann_search_content = textwrap.dedent("""\
    ---
    tags: [topic/ai_ml, concept/ann_search, type/algorithm, domain/ir, domain/vector_database]
    aliases: [ANN Search, Approximate Nearest Neighbor Search, ANN算法]
    ---
    # 近似最近邻搜索 (Approximate Nearest Neighbor - ANN)

    [[相似性搜索|返回 相似性搜索]] | [[../Core Technologies/向量数据库|相关: 向量数据库]]

    ## 概述

    近似最近邻搜索 (Approximate Nearest Neighbor, ANN) 是一种在高维[[../../Fundamentals/向量 (Vector)|向量]]空间中**快速查找**与查询向量**近似**相似（距离最近）的邻居的算法。

    与精确的 K 近邻 (Exact K-Nearest Neighbor, KNN) 搜索（需要计算查询向量与数据库中所有向量的距离，找到绝对最近的 K 个）相比，ANN 算法通过牺牲一定的**精度 (Accuracy)** 来换取极大的**速度 (Speed)** 提升和更低的**资源消耗**（内存、计算量）。

    在处理[[../Core Technologies/向量数据库|向量数据库]]中数百万甚至数十亿级别的海量高维向量时，精确 KNN 搜索的计算成本过高，无法满足实时查询的需求，因此 ANN 成为了**实际应用中的标准方法**。

    ## 为什么需要 ANN？

    *   **高维灾难 (Curse of Dimensionality)**: 在高维空间中，所有点之间的距离趋向于变得很大且相近，传统的空间索引结构（如 KD-Tree）效率急剧下降。精确查找所有点的距离变得非常耗时。
    *   **数据规模**: 现代 AI 应用（如 [[../检索增强生成 (RAG)|RAG]] 的知识库）可能包含海量向量，无法对每个向量都进行精确计算。
    *   **实时性要求**: 许多应用（如在线搜索、推荐、问答）需要毫秒级的响应速度。

    ## ANN 的核心思想：速度与精度的权衡

    ANN 算法的核心思想是**避免全局搜索**，通过某种策略快速缩小搜索范围，找到“足够近”的邻居，而不是“绝对最近”的邻居。这种权衡通常是值得的，因为在很多应用场景下，找到语义上非常相似的几个结果通常就足够了，不一定非要找到理论上最相似的那一个。

    ```mermaid
    graph LR
        A[精确 KNN 搜索] -- 特点 --> B(保证找到<br/>**绝对**最近邻);
        A -- 缺点 --> C(计算量大<br/>速度慢<br/>资源消耗高);

        D[近似 ANN 搜索] -- 特点 --> E(快速找到<br/>**大概率**是最近邻的结果);
        D -- 优势 --> F(速度快<br/>资源消耗低);
        D -- 代价 --> G(牺牲少量精度<br/>可能错过绝对最近邻);

        H{实际应用<br/>(大规模/高维/实时)} -- 通常选择 --> D;

        style H fill:#ccf, stroke:#333
    ```

    ## 常见的 ANN 算法类型

    存在多种不同的 ANN 算法，各有优劣：

    *   **基于树的方法 (Tree-based)**: 如 KD-Tree, Annoy。通过构建树状结构划分空间。在高维时效果下降。
    *   **基于哈希的方法 (Hashing-based)**: 如 [[局部敏感哈希 (LSH)]]。通过设计哈希函数，让相似的向量有更高概率映射到同一个“桶”里，然后在同一个桶内搜索。
    *   **基于图的方法 (Graph-based)**: 如 **HNSW (Hierarchical Navigable Small World)**。构建一个多层的邻近图，搜索时从顶层粗粒度的图开始，逐步导航到底层精细的图，找到最近邻。**HNSW 是当前非常流行且性能优异的 ANN 算法之一**。
    *   **基于量化的方法 (Quantization-based)**: 如 IVF (Inverted File Index), PQ (Product Quantization)。通过聚类或向量压缩来减少需要比较的向量数量。IVF 将向量空间划分为多个区域（聚类中心），搜索时只查找查询向量所在区域及其附近区域的向量。

    ## 对产品经理的意义

    *   **理解技术现实**: 知道在大规模向量搜索中，追求绝对精确通常不现实，ANN 是工程实践中的常用方案。
    *   **关注性能指标**: 理解 ANN 涉及**速度（查询延迟 QPS）、精度（召回率 Recall）、内存占用**等多个指标的权衡。在定义产品需求时，需要考虑对这些指标的要求。
    *   **评估技术方案**: 了解不同的 ANN 算法有不同的特点和适用场景，可以参与关于[[../Core Technologies/向量数据库|向量数据库]]或 ANN 算法选型的讨论。
    *   **设定合理预期**: 向[[../沟通协作/利益相关者管理|利益相关者]]解释为什么搜索结果是“近似”相关的，而不是绝对完美的。

    ## 总结

    ANN 是解决大规模高维向量[[相似性搜索|相似性搜索]]效率问题的关键技术。它通过牺牲少量精度换取速度和效率，是现代[[../Core Technologies/向量数据库|向量数据库]]和许多 AI 应用（如 [[../检索增强生成 (RAG)|RAG]]）的核心引擎。产品经理理解 ANN 的基本原理和其速度-精度的权衡，有助于设定合理的产品预期和评估相关技术方案。

    ## 相关概念

    *   [[相似性搜索]]
    *   [[K近邻 (KNN)]]
    *   [[../Core Technologies/向量数据库|向量数据库]]
    *   [[高维灾难]]
    *   [[精度 (Accuracy/Recall)]]
    *   [[速度 (Latency/QPS)]]
    *   [[HNSW]], [[LSH]], [[IVF]] (具体 ANN 算法)
    *   [[权衡 (Trade-offs)]]
""")

information_retrieval_path = os.path.join(ir_folder, '信息检索.md')
information_retrieval_content = textwrap.dedent("""\
    ---
    tags: [topic/fundamentals, concept/ir, type/definition, domain/computer_science]
    aliases: [IR, Information Retrieval, 信息检索系统]
    ---
    # 信息检索 (Information Retrieval - IR)

    ## 概述

    信息检索 (Information Retrieval, IR) 是计算机科学的一个领域，专注于**从大规模的信息资源集合（通常是非结构化的，如文本文档、网页、图像）中查找满足用户特定信息需求的资料**的过程。

    简单来说，IR 系统就是帮助用户**找到他们想要的信息**的系统。我们日常使用的**搜索引擎**（如 Google, Baidu）就是最典型的 IR 系统。

    ## IR 系统的核心任务

    1.  **信息表示 (Representation)**: 如何将文档和用户查询表示成计算机可以处理的形式？
        *   传统方法：[[词袋模型 (Bag-of-Words)]], [[TF-IDF]] 向量。
        *   现代方法：[[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入向量 (Embeddings)]] (来自 [[../AI & ML/大型语言模型 (LLM)|LLM]] 或其他模型)。
    2.  **索引 (Indexing)**: 如何组织和存储这些表示，以便能够快速查找？
        *   传统方法：[[倒排索引 (Inverted Index)]] (用于关键词搜索)。
        *   现代方法：[[../AI & ML/Core Technologies/向量数据库|向量数据库]] / [[../AI & ML/Information Retrieval/近似最近邻搜索 (ANN)|ANN 索引]] (用于语义搜索)。
    3.  **查询处理 (Query Processing)**: 如何理解用户的查询意图，并将其转换为可用于检索的形式？
        *   [[查询扩展]], [[查询重写]]。
        *   将查询文本转换为[[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入向量]]。
    4.  **匹配与排序 (Matching & Ranking)**: 如何根据查询找到相关的文档，并按照相关性对结果进行排序？
        *   传统方法：基于关键词匹配度（如 BM25 算法）。
        *   现代方法：基于[[../AI & ML/Information Retrieval/相似性搜索|向量相似度计算]]（如[[../AI & ML/Information Retrieval/余弦相似度|余弦相似度]]）。
        *   通常会结合多种信号进行[[学习排序 (Learning to Rank)]]。
    5.  **评估 (Evaluation)**: 如何衡量 IR 系统的性能？
        *   常用指标：[[精确率 (Precision)]], [[召回率 (Recall)]], F1-Score, MAP (Mean Average Precision), NDCG (Normalized Discounted Cumulative Gain)。

    ```mermaid
    graph TD
        A[用户信息需求] --> B(用户查询 Query);
        B --> C{查询处理};
        C --> D{匹配与排序};

        E[信息资源集合<br/>(文档/网页/向量等)] --> F(信息表示);
        F --> G{索引构建};
        G -- 索引 --> D;

        D -- 排序后的结果 --> H[呈现给用户];

        subgraph IR 系统核心流程
            direction LR
            B --> C --> D --> H;
            E --> F --> G;
        end

        I(评估 Evaluation<br/>(Precision, Recall等)) -- 反馈优化 --> C & D & G;

    ```

    ## IR 与 [[../AI & ML/检索增强生成 (RAG)|RAG]] 的关系

    [[../AI & ML/检索增强生成 (RAG)|RAG]] 中的“检索 (Retrieval)”步骤，本质上就是一个**信息检索**过程。它利用 IR 技术（特别是基于[[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入]]的[[../AI & ML/Information Retrieval/相似性搜索|相似性搜索]]和[[../AI & ML/Core Technologies/向量数据库|向量数据库]]）从外部知识库中找到与用户输入最相关的信息片段，作为[[../AI & ML/大型语言模型 (LLM)|LLM]] 生成回答的上下文。

    可以说，**高效、精准的 IR 是 RAG 系统成功的关键前提**。

    ## 对产品经理的意义

    *   **理解搜索与问答基础**: 了解用户查找信息的基本过程和技术原理。
    *   **评估 RAG 方案**: 明白 RAG 系统的效果很大程度上取决于其底层 IR 组件的性能（检索的准确性、召回率、速度）。
    *   **定义搜索/问答需求**: 能够更清晰地描述对搜索结果相关性、排序逻辑、召回范围等方面的要求。
    *   **关注评估指标**: 了解衡量搜索或问答系统好坏的关键指标（如精确率、召回率）。

    ## 总结

    信息检索 (IR) 是查找相关信息的核心技术领域，是搜索引擎、问答系统、[[../AI & ML/检索增强生成 (RAG)|RAG]] 等应用的基础。理解 IR 的基本概念和流程，有助于产品经理更好地设计和评估需要信息查找功能的产品。

    ## 相关概念

    *   [[搜索引擎]]
    *   [[../AI & ML/检索增强生成 (RAG)|检索增强生成 (RAG)]]
    *   [[../AI & ML/Information Retrieval/相似性搜索|相似性搜索]]
    *   [[../AI & ML/Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]
    *   [[../AI & ML/Core Technologies/向量数据库|向量数据库]]
    *   [[倒排索引]]
    *   [[TF-IDF]]
    *   [[BM25]]
    *   [[精确率 (Precision)]]
    *   [[召回率 (Recall)]]
    *   [[学习排序 (Learning to Rank)]]
""")


# --- Main Script Logic ---
def main():
    print("Starting Obsidian Knowledge Base Generation (Part 9 - Foundational & IR Concepts)...")
    print(f"Target Root Directory: {os.path.abspath(TARGET_ROOT_DIRECTORY)}")
    print(f"Overwrite Existing Files: {OVERWRITE_EXISTING}")

    # Files prioritized by user request: Vector, Sim Search, ANN, IR, DB, ML, DL
    files_to_create = {
        # Fundamentals
        vector_path: vector_content,
        database_path: database_content,
        ml_path: ml_content,
        # AI Core Technologies (Moving DL here)
        deep_learning_path: deep_learning_content,
        # Information Retrieval Concepts
        similarity_search_path: similarity_search_content,
        ann_search_path: ann_search_content,
        information_retrieval_path: information_retrieval_content,
    }

    # Create necessary base directories if they don't exist
    os.makedirs(fundamentals_folder, exist_ok=True)
    os.makedirs(ai_core_tech_folder, exist_ok=True) # Already exists, but safe to call again
    os.makedirs(ir_folder, exist_ok=True)
    print("Base directories ensured.")

    for filepath, content in files_to_create.items():
        if not OVERWRITE_EXISTING and os.path.exists(filepath):
            print(f"Skipping existing file: {filepath}")
            continue
        write_file(filepath, content)

    print("\nObsidian Knowledge Base Generation (Part 9) Complete.")
    print("Focus was on foundational concepts (Vector, DB, ML, DL) and Information Retrieval concepts (Sim Search, ANN, IR).")

if __name__ == "__main__":
    main()
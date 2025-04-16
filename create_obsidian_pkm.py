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

# --- Knowledge Base Content Definitions (Part 15 - Study Plan) ---

# --- Interview Simulation/Product Manager Interview/Preparation Guide ---
# (Using the existing folder)
prep_guide_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Preparation Guide')

# --- Define path and content for the new Study Plan file ---
study_plan_path = os.path.join(prep_guide_folder, '01 - AI PM 面试冲刺学习计划 (推荐顺序).md')
study_plan_content = textwrap.dedent("""\
    ---
    tags: [topic/interview, type/guide, process/preparation, skill/planning, roadmap/learning]
    aliases: [AI PM学习路线图, 面试准备顺序]
    ---
    # AI PM 面试冲刺学习计划 (推荐顺序)

    [[00 - 面试准备指南与行动计划|返回 准备指南]]

    ## 概述

    本计划为你提供一个**推荐的学习和练习顺序**，旨在帮助你**高效地**利用本知识库准备 AI 产品经理面试，特别是针对涉及 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]] 和类似 [[../../Concepts/Product Management/应用案例 - AI 助手/00 - AI 购物助手案例分析 (Rufus 启发)|AI 购物助手]] 的岗位。

    **核心原则**:
    *   **先基础，后深入**: 先掌握 PM 和 AI 的核心概念。
    *   **理论与实践结合**: 将概念学习与案例分析、模拟面试结合。
    *   **聚焦重点**: 优先学习与 AI 产品经理面试最相关的知识和技能。
    *   **迭代学习**: 这不是一次性过程，根据需要回顾和加深理解。

    [!tip] Agile Mindset
    > 这只是一个推荐顺序。请根据你**自身的知识背景**和**面试时间安排**灵活调整。如果你对某个领域已经很熟悉，可以快速跳过或深入特定环节。

    ## 推荐学习与练习步骤 (Step-by-Step)

    **Phase 1: 奠定基础 (Foundation Building)**

    *   **目标**: 快速回顾产品管理核心流程与思维，并建立对 AI/ML 领域的基本认知。
    *   **行动项**:
        *   `[ ]` **理解产品管理框架**:
            *   `[[../../Concepts/Product Management/MVP 框架/00 - MVP 框架概览|概览 MVP 框架]]`: 理解其核心思想和 4 个步骤。
            *   `[[../../Concepts/Product Management/完整框架/00 - 完整产品管理框架概览|概览完整 PM 框架]]`: 了解更全面的 7 个步骤。
        *   `[ ]` **掌握核心 PM 概念**: 至少浏览一遍，确保理解：
            *   用户与需求: `[[../../Concepts/Product Management/基础概念/用户画像|用户画像]]`, `[[../../Concepts/Product Management/基础概念/痛点|痛点]]`, `[[../../Concepts/Product Management/用户研究/00 - 用户研究概览|用户研究]]`, `[[../../Concepts/Product Management/用户研究/用户访谈|用户访谈]]`, `[[../../Concepts/Product Management/用户研究/用户反馈|用户反馈]]`
            *   战略与规划: `[[../../Concepts/Product Management/产品战略与规划/价值主张|价值主张]]`, `[[../../Concepts/Product Management/市场与行业分析/市场定位|市场定位]]`, `[[../../Concepts/Product Management/市场与行业分析/竞品分析|竞品分析]]`, `[[../../Concepts/Product Management/产品战略与规划/产品路线图|产品路线图]]`
            *   设计与决策: `[[../../Concepts/Product Management/产品设计/功能优先级排序|功能优先级排序]]` (`[[../../Concepts/Product Management/产品设计/MoSCoW 方法|MoSCoW]]`, `[[../../Concepts/Product Management/产品设计/RICE 模型|RICE]]`), `[[../../Concepts/Product Management/产品设计/用户体验 (UX)|用户体验 (UX)]]`, `[[../../Concepts/Product Management/产品设计/可用性|可用性]]`
            *   数据与衡量: `[[../../Concepts/Product Management/数据分析与实验/00 - 数据分析概览|数据分析概览]]`, `[[../../Concepts/Product Management/数据分析与实验/KPI|KPI]]`, `[[../../Concepts/Product Management/数据分析与实验/OKR|OKR]]`, `[[../../Concepts/Product Management/数据分析与实验/A_B 测试|A/B 测试]]`, `[[../../Concepts/Product Management/数据分析与实验/转化率|转化率]]`, `[[../../Concepts/Product Management/数据分析与实验/留存率|留存率]]`, `[[../../Concepts/Product Management/数据分析与实验/北极星指标|北极星指标]]`
            *   协作与文档: `[[../../Concepts/Product Management/沟通协作/跨职能团队|跨职能团队]]`, `[[../../Concepts/Product Management/沟通协作/利益相关者管理|利益相关者管理]]`, `[[../../Concepts/Product Management/文档与交付物/PRD 产品需求文档|PRD]]`
        *   `[ ]` **建立 AI/ML 基础认知**:
            *   `[[../../Concepts/AI & ML/00 - AI 与机器学习概览|阅读 AI 与 ML 概览]]`
            *   理解 `[[../../Concepts/Fundamentals/机器学习 (ML)|机器学习 (ML)]]` 的基本概念和类型。
            *   理解 `[[../../Concepts/AI & ML/Core Technologies/深度学习|深度学习 (DL)]]` 是 ML 的一个分支及其优势。
            *   了解 `[[../../Concepts/AI & ML/Core Technologies/自然语言处理 (NLP)|自然语言处理 (NLP)]]` 的目标和任务。

    **Phase 2: 深入 AI 核心技术 (AI Core Tech Deep Dive)**

    *   **目标**: 重点理解与 [[../../Concepts/Product Management/应用案例 - AI 助手/00 - AI 购物助手案例分析 (Rufus 启发)|AI 助手]] 强相关的核心技术概念，特别是回答你关于 Rufus 如何工作的疑问。
    *   **行动项**:
        *   `[ ]` **LLM 核心**:
            *   深入学习 `[[../../Concepts/AI & ML/大型语言模型 (LLM)|大型语言模型 (LLM)]]`：它是如何工作的（简化原理）？它的核心能力和局限性是什么？
            *   理解 `[[../../Concepts/AI & ML/Core Technologies/Transformer 模型|Transformer 模型]]` 的**核心思想**（注意力机制），明白它为何是 LLM 的基石。
        *   `[ ]` **RAG 与相关技术 (回答 Rufus 如何处理细节/实时信息)**:
            *   **重点理解**: `[[../../Concepts/AI & ML/检索增强生成 (RAG)|检索增强生成 (RAG)]]` 的**工作原理、优势（缓解幻觉、知识更新）和挑战**。这是理解 Rufus 类助手的关键。
            *   理解支撑 RAG 的技术: `[[../../Concepts/AI & ML/Core Technologies/嵌入 (Embedding)|嵌入 (Embedding)]]` (如何表示语义？) -> `[[../../Concepts/Fundamentals/向量 (Vector)|向量]]` -> `[[../../Concepts/AI & ML/Core Technologies/向量数据库|向量数据库]]` (如何存储和检索向量？) -> `[[../../Concepts/AI & ML/Information Retrieval/相似性搜索|相似性搜索]]` (如何找到相关信息？) -> `[[../../Concepts/AI & ML/Information Retrieval/近似最近邻搜索 (ANN)|近似最近邻搜索 (ANN)]]` (如何在海量数据中快速搜索？)。
        *   `[ ]` **与 LLM 交互和优化**:
            *   学习 `[[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|提示工程 (Prompt Engineering)]]` 的基本技巧和策略（如何更好地“指挥”LLM？如何结合 RAG 的结果？）。
            *   理解 `[[../../Concepts/AI & ML/微调 (Fine-tuning)|微调 (Fine-tuning)]]` 的概念、目的以及它与 Prompt/RAG 的区别与联系。
        *   `[ ]` **理解核心挑战**:
            *   深入思考 `[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|模型幻觉]]` 的成因、风险和缓解策略 (RAG 是主要手段)。
            *   理解 `[[../../Concepts/AI & ML/模型鲁棒性 (Robustness)|模型鲁棒性]]` 的重要性及提升方法。

    **Phase 3: 把握技术选型与评估 (Tech Landscape & Evaluation)**

    *   **目标**: 了解当前主流 LLM 格局，理解模型选型的考量因素，并知道如何评估模型效果。解答你关于 LLaMA 是否“太高级”以及 PM 需要懂多深的问题。
    *   **行动项**:
        *   `[ ]` **模型选型权衡**:
            *   学习 `[[../../Concepts/AI & ML/开源 vs 闭源模型|开源 vs. 闭源模型]]` 的核心差异和利弊权衡。
            *   浏览 `[[../../Concepts/AI & ML/Models/主流 LLM 模型概览|主流 LLM 模型概览]]`，了解主要玩家 (`[[../../Concepts/AI & ML/Models/GPT 模型系列|GPT]]`, `[[../../Concepts/AI & ML/Models/Claude 模型系列|Claude]]`, `[[../../Concepts/AI & ML/Models/Gemini 模型系列|Gemini]]`, `[[../../Concepts/AI & ML/Models/LLaMA 模型系列|Llama]]` 等) 的特点和定位。
        *   `[ ]` **PM 的技术理解深度**:
            *   **重点阅读**: `[[../../Concepts/Product Management/核心技能/PM 对 LLM 的理解深度|PM 对 LLM 的理解深度]]`，明确学习的目标和边界。
        *   `[ ]` **模型评估**:
            *   了解 `[[../../Concepts/AI & ML/Evaluation/基准测试 (Benchmark)|基准测试 (Benchmark)]]` 的作用及其**重要局限性**。知道不能唯 Benchmark 论。
            *   思考在实际产品中应如何评估模型效果（结合领域测试集、A/B 测试、人工评估、业务指标等）。

    **Phase 4: 应用与案例分析 (Application & Case Study)**

    *   **目标**: 将前面学习的 PM 框架和 AI 概念应用到具体的 AI 购物助手案例中，融会贯通。
    *   **行动项**:
        *   `[ ]` **深入研究案例**:
            *   仔细阅读 `[[../../Concepts/Product Management/应用案例 - AI 助手/01 - Rufus 类助手 MVP 框架应用|AI 助手 MVP 框架应用]]`。
            *   仔细阅读 `[[../../Concepts/Product Management/应用案例 - AI 助手/02 - Rufus 类助手完整框架应用|AI 助手完整框架应用]]`。
        *   **关联思考**: 在阅读案例时，主动思考：
            *   这里体现了哪些 PM 框架的步骤？
            *   涉及了哪些 AI 技术概念？（LLM, RAG, Prompt...）
            *   技术选型（例如 RAG）是如何解决产品问题的（例如信息准确性）？
            *   PM 在每个环节需要考虑的关键风险和指标是什么？

    **Phase 5: 面试技巧与模拟实战 (Interview Skills & Simulation)**

    *   **目标**: 掌握面试技巧，并通过模拟练习将知识转化为流畅、结构化的表达。
    *   **行动项**:
        *   `[ ]` **掌握核心技巧**:
            *   学习并准备 `[[../技巧与方法/STAR 原则|STAR 原则]]` 故事库。
            *   回顾 `[[../技巧与方法/行为面试问题|常见行为面试问题类型]]`。
            *   理解产品设计题的回答框架（参考 `[[../Product Design Simulation/03 - 产品设计问题模拟 (AI 购物助手)|产品设计模拟]]` 中的框架提示）。
            *   学习 `[[../技巧与方法/面试技巧|通用面试技巧]]`。
        *   `[ ]` **准备个性化内容**:
            *   打磨 `[[../Self Introduction/01 - 自我介绍准备 (PM - AI方向)|自我介绍]]`。
            *   准备 `[[../Asking Questions/05 - 提问面试官环节准备|向面试官提问的问题]]`。
        *   `[ ]` **开始模拟练习 (反复进行!)**:
            *   **口头练习**: 打开 `[[../Simulation Scenarios/00 - 模拟面试场景入口|模拟面试场景入口]]`。
            *   **先练 MVP 版**: `[[../Simulation Scenarios/01 - AI 助手面试模拟 (MVP 快速版)|AI 助手 MVP 模拟]]`，练习快速抓住核心。
            *   **再练深入版**: `[[../Simulation Scenarios/02 - AI 助手面试模拟 (综合深入版)|AI 助手综合深入版模拟]]`，练习应对追问和复杂思考。
            *   **专项练习**: 针对性地练习 `[[../Behavioral Simulation/02 - 行为面试问题模拟 (STAR 练习)|行为问题]]`、`[[../Technical Simulation/04 - AI 技术理解问题模拟|技术理解问题]]`。
            *   **计时 + 录音/录像 + 复盘**: 这是提升的关键！

    **Phase 6: 查漏补缺与最终准备 (Review & Final Prep)**

    *   **目标**: 回顾知识体系，针对薄弱环节进行加强，调整心态。
    *   **行动项**:
        *   `[ ]` 快速回顾整个知识库的结构和重点笔记。
        *   `[ ]` 针对模拟练习中发现的不足，重点复习相关的概念笔记。
        *   `[ ]` 再次检查对目标公司和职位JD的理解。
        *   `[ ]` 调整作息，放松心态，自信应对！

    ---

    祝你学习高效，面试成功！
""")


# --- Main Script Logic ---
def main():
    print("Starting Obsidian Knowledge Base Generation (Part 15 - Study Plan)...")
    print(f"Target Root Directory: {os.path.abspath(TARGET_ROOT_DIRECTORY)}")
    print(f"Overwrite Existing Files: {OVERWRITE_EXISTING}")

    # Define path for the new Study Plan file
    # (Assuming prep_guide_folder is correctly defined based on previous context)
    prep_guide_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Preparation Guide')

    study_plan_path = os.path.join(prep_guide_folder, '01 - AI PM 面试冲刺学习计划 (推荐顺序).md')

    # Files to create/update in this run
    files_to_create = {
        study_plan_path: study_plan_content,
    }

    # Create necessary base directories if they don't exist
    os.makedirs(prep_guide_folder, exist_ok=True)
    # Add checks for other potentially referenced folders if necessary, although this file primarily links
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', 'MVP 框架'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '完整框架'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '基础概念'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '用户研究'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '产品战略与规划'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '市场与行业分析'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '产品设计'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '数据分析与实验'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '沟通协作'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '文档与交付物'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '核心技能'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '应用案例 - AI 助手'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Core Technologies'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Models'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Evaluation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Infrastructure'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Information Retrieval'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Fundamentals'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Self Introduction'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Behavioral Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Product Design Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Technical Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Asking Questions'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Simulation Scenarios'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Technical Deep Dive'), exist_ok=True)


    print("Base directories ensured.")

    for filepath, content in files_to_create.items():
        if not OVERWRITE_EXISTING and os.path.exists(filepath):
            print(f"Skipping existing file: {filepath}")
            continue
        write_file(filepath, content)

    print("\nObsidian Knowledge Base Generation (Part 15) Complete.")
    print("Focus was on creating a detailed, actionable Study and Preparation Plan.")

if __name__ == "__main__":
    main()
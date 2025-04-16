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

# --- Knowledge Base Content Definitions (Part 14 - Enhanced Conversational Simulations) ---

# --- Interview Simulation/Product Manager Interview/Simulation Scenarios ---
# (Creating this new subfolder for realistic, conversational simulations)
simulation_scenarios_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Simulation Scenarios')

# --- Entry point for Simulation Scenarios ---
# DEFINE THE PATH VARIABLE
sim_entry_point_path = os.path.join(simulation_scenarios_folder, '00 - 模拟面试场景入口.md')
# DEFINE THE CONTENT VARIABLE (This was missing)
sim_entry_point_content = textwrap.dedent("""\
    ---
    tags: [topic/interview, type/simulation, process/practice]
    aliases: [面试模拟场景, PM面试实战]
    ---
    # 模拟面试场景入口

    [[../Preparation Guide/00 - 面试准备指南与行动计划|返回 准备指南]]

    ## 概述

    欢迎来到模拟面试实战场景！这里的目标是提供更接近真实面试体验的对话式模拟。我们为你准备了不同难度和侧重点的模拟场景，帮助你将之前学习的概念和框架应用到接近真实的对话中。

    **核心练习目标**:
    *   练习自然的对话表达。
    *   在压力下结构化地思考和回答。
    *   灵活运用 [[../../Concepts/Product Management/核心技能/STAR 原则|STAR 原则]]、产品设计框架等。
    *   将 AI/LLM 知识自然地融入产品讨论。
    *   适应不同的面试官风格和追问。

    ## 模拟场景列表

    1.  **[[01 - AI 助手面试模拟 (MVP 快速版)|AI 助手面试模拟 (MVP 快速版)]]**
        *   **适合**: 面试初期准备，或针对节奏较快、更侧重核心 PM 技能和潜力的面试轮次（例如针对实习生）。
        *   **特点**: 对话相对直接，问题更侧重于 [[../../Concepts/Product Management/MVP 框架/00 - MVP 框架概览|MVP]] 思维、核心[[../../Concepts/Product Management/核心技能/沟通技巧|沟通]]与[[../../Concepts/Product Management/核心技能/解决问题能力|解决问题]]能力、基础[[../../Concepts/Product Management/核心技能/PM 对 LLM 的理解深度|AI 概念理解]]。
    2.  **[[02 - AI 助手面试模拟 (综合深入版)|AI 助手面试模拟 (综合深入版)]]**
        *   **适合**: 面试后期准备，或针对需要展现深度思考、技术理解和处理复杂性能力的面试轮次。
        *   **特点**: 对话可能更深入，包含更多追问，涉及[[../../Concepts/Product Management/完整框架/00 - 完整产品管理框架概览|完整框架]]思考、技术[[../../Concepts/Product Management/技术选型|选型权衡]]、[[../../Concepts/Product Management/基础概念/风险管理|风险管理]]、[[../../Concepts/Product Management/产品战略与规划/产品战略|战略思考]]等。

    ## 如何使用这些模拟场景？

    [!exercise] 练习建议
    > 1. **选择场景**: 根据你的准备阶段和目标选择一个场景开始。
    > 2. **扮演角色**: 大声朗读“面试官”的问题，然后**口头回答**“候选人 (你)”的部分。**不要只是阅读！**
    > 3. **运用框架和知识**: 在回答时，积极思考并尝试运用 [[../../Concepts/Product Management/核心技能/STAR 原则|STAR]]、产品设计框架，并引用相关的[[../../Concepts/AI & ML/00 - AI 与机器学习概览|AI]]和[[../../Concepts/Product Management/00 - 产品管理框架概览|产品管理]]概念。
    > 4. **注意引导提示**: 留意 `[!tip]` 或 `[!info]` 中的提示，它们会指导你的思考方向或建议使用的概念。
    > 5. **计时练习**: (可选) 为自己设定回答时间限制，模拟真实面试的压力。
    > 6. **录音复盘**: (强烈推荐) 录下你的回答，回听评估流畅度、逻辑性、内容深度和时间控制。
    > 7. **反复练习**: 对同一个场景进行多次练习，尝试不同的表述方式和侧重点。

    开始你的模拟面试吧！
""")


# --- UPDATED MVP Level Simulation Content ---
sim_mvp_path = os.path.join(simulation_scenarios_folder, '01 - AI 助手面试模拟 (MVP 快速版).md')
sim_mvp_content_updated = textwrap.dedent("""\
    ---
    tags: [topic/interview, type/simulation, level/mvp, domain/ai_assistant, process/practice]
    aliases: [AI助手MVP面试模拟, 详细对话模拟MVP]
    ---
    # AI 助手面试模拟 (MVP 快速版 - 详细对话示例)

    [[00 - 模拟面试场景入口|返回 模拟入口]]

    **场景设定**: 你正在面试某大型电商平台的 AI 产品经理实习生岗位。面试官看起来比较亲和，语速适中，注重考察你的基本素质和潜力。

    ---

    **面试官**: "你好，[你的名字]！很高兴见到你。我们简单开始，能先请你做个自我介绍吗？大概 1-2 分钟就好。"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   遵循 [[../Self Introduction/01 - 自我介绍准备 (PM - AI方向)|自我介绍结构]]：开场 -> 核心经历 (PM基础+AI关联) -> 技能总结 -> 动机。
    > *   重点突出与岗位的匹配度、学习能力和热情。
    > *   语速自然，带有停顿思考，避免像背书。

    > **(示例回答)**:
    > “您好面试官，非常荣幸能有这次面试机会。我叫[你的名字]，是[学校]主修[专业，例如数据科学/计算机科学/经济学]的大二学生。我对利用技术，特别是 AI，来解决实际问题、提升用户体验非常感兴趣，尤其关注 AI 在电商领域的应用，了解到贵公司在这方面有很多前沿探索，所以我对 AI 产品经理实习生这个岗位非常向往。”
    >
    > “虽然我目前还没有直接的 AI 产品管理经验，但在学习和实践中，我一直努力培养相关的基础能力。比如，在[课程名称/项目名称]项目中，我负责了[[../../Concepts/Product Management/用户研究/00 - 用户研究概览|用户调研]]和需求分析部分，通过访谈和问卷定义了目标[[../../Concepts/Product Management/基础概念/用户画像|用户画像]]，并梳理了核心[[../../Concepts/Product Management/基础概念/痛点|痛点]]。我也对[[../../Concepts/Product Management/数据分析与实验/00 - 数据分析概览|数据分析]]很感兴趣，掌握了 [工具/语言，如 SQL, Python]，并尝试在项目中通过数据来验证假设。”
    >
    > “同时，我对 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]] 等 AI 技术保持着浓厚的兴趣，主动学习了像 [[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]、[[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|提示工程]] 这些核心概念，也一直在思考它们如何在电商场景下创造价值，比如优化商品发现、智能问答等。我认为我的优势在于**快速学习能力**、**用户导向的思维**以及**初步的数据分析能力**。”
    >
    > “我非常希望能加入贵团队，在实际项目中学习如何将 AI 技术落地为优秀的产品，贡献自己的力量。以上是我的自我介绍，谢谢！”

    ---

    **面试官**: "听起来不错，你对 AI 很有热情。我们最近在关注像 Amazon Rufus 这样的 AI 购物助手，觉得这个方向很有潜力。假设让你来负责设计一个类似产品的 MVP 版本，你会怎么入手？你的思路是什么？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   明确提出将使用 [[../../Concepts/Product Management/MVP 框架/00 - MVP 框架概览|MVP 框架]]。
    > *   按照框架步骤清晰阐述，每一步都要有具体思考。
    > *   语言自然，带有思考的连接词。

    > **(示例回答)**:
    > “好的，面试官。对于设计 AI 购物助手的 MVP 版本，我会遵循[[../../Concepts/Product Management/MVP 框架/00 - MVP 框架概览|精益创业 (Lean Startup)]] 的思路，采用 MVP 框架来入手，目标是尽快验证核心[[../../Concepts/Product Management/产品战略与规划/价值主张|价值假设]]并获取用户反馈。”
    >
    > “**第一步，是明确[[../../Concepts/Product Management/MVP 框架/01 - 用户痛点价值 (MVP)|用户、痛点和核心价值]]。** 在 MVP 阶段，我会聚焦于最大、最高频的痛点。我认为当前电商用户，特别是**有明确购物意图**的用户，普遍存在两大痛点：一是在海量信息中**查找具体商品信息效率低**，比如想快速知道某件衣服的材质或者某个电子产品的兼容性；二是遇到**常见购物问题**（像物流、退换货政策）时，现有自助渠道不方便或找不到，联系人工客服又需要等待。所以，我们 MVP 的核心价值假设就是：通过 AI 助手提供**即时、准确**的单品信息问答和常见问题解答，可以显著**提升用户的信息获取效率**，节省时间。”
    >
    > “**第二步，基于这个价值假设，设计[[../../Concepts/Product Management/MVP 框架/02 - MVP 解决方案|MVP 解决方案]]。** 核心是‘最小可行’。我会包含两个核心功能：**1. 单品页智能问答**，用户在商品详情页可以直接问关于这个商品的问题；**2. 平台通用 FAQ 问答**，处理物流、退换货等常见咨询。我们需要明确 MVP **不做**什么，比如暂时不做跨商品比较、不做[[个性化]]推荐。技术实现上，为了保证回答的准确性，尤其是商品信息的实时性，我认为需要采用 **[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 技术**，结合我们平台的商品数据库和 FAQ 知识库，再利用 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]] 生成自然回答。当然，[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉]]控制会是一个挑战，需要通过 [[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|Prompt 工程]]和 RAG 策略来重点应对。”
    >
    > “**第三步，定义[[../../Concepts/Product Management/MVP 框架/03 - MVP 数据验证|数据指标和验证计划]]。** 我们需要知道这个 MVP 是否有效。我会关注几个核心指标：**助手使用率**（多少人用了）、**问题解决率**（AI 是否给出了相关回答）、以及**用户满意度 (CSAT)**（通过回答后的简单反馈收集）。同时，我们也会观察对应场景的**人工客服咨询量**是否有所下降。验证方式上，我会建议采用**小范围[[../../Concepts/Product Management/数据分析与实验/灰度发布|灰度发布]]或 [[../../Concepts/Product Management/数据分析与实验/A_B 测试|A/B 测试]]**，将 MVP 功能推送给部分用户，对比实验组和对照组的数据表现。”
    >
    > “**第四步，就是[[../../Concepts/Product Management/MVP 框架/04 - MVP 迭代优化|快速迭代优化]]。** 根据收集到的数据和[[../../Concepts/Product Management/用户研究/用户反馈|用户反馈]]，分析哪些问题回答得好，哪些不好，用户最关心什么。基于这些洞察，决定下一步是**优化现有功能**（比如提升某个品类问题的回答准确率），还是根据用户反馈和数据表现，**探索新的高优先级方向**（比如用户问得很多的跨商品比较功能）。这是一个持续的 Build-Measure-Learn 循环。”
    >
    > “总的来说，这就是我设计 AI 购物助手 MVP 的一个初步思路框架。”

    ---

    **面试官**: "嗯，思路比较清晰。你提到了用 RAG 技术来提高准确性，减少幻觉。你能用简单的语言解释一下什么是 [[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 吗？它大概是怎么工作的？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   使用简洁明了的语言，避免过多技术术语。
    > *   用生活化的类比帮助理解。
    > *   强调 RAG 的核心价值：结合外部知识。

    > **(示例回答)**:
    > “当然可以。[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]，您可以把它想象成给 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]] 这个‘博学的通才’配备了一个‘专属领域知识库’和‘实时检索引擎’。”
    >
    > “工作流程大致是这样的：当用户提出一个问题，比如‘这双鞋防水吗？’，系统**不会**直接让 LLM ‘猜’答案。而是**第一步**，拿着用户的问题，去我们的商品数据库这个‘知识库’里**查找**与‘这双鞋’和‘防水’相关的信息，可能会找到‘防水等级：IPX7’这样的具体信息。”
    >
    > “**第二步**，系统把找到的这个‘IPX7’信息，连同用户的问题一起，‘喂’给 LLM，同时给 LLM 一个指令，大概意思是：‘请根据这个信息（IPX7）来回答用户关于防水的问题’。这就像我们写报告时引用参考资料一样。”
    >
    > “**最后**，LLM 就基于这个可靠的信息，生成一个自然语言的回答，比如‘是的，这款鞋的防水等级达到了 IPX7 标准’。”
    >
    > “所以，RAG 的核心就是**先检索外部可靠信息，再让 LLM 基于这些信息来生成回答**，这样就能大大提高回答的**准确性**和**实时性**，有效减少 LLM ‘凭空捏造’也就是[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉]]的情况，尤其对于需要精确信息的购物场景非常关键。”

    ---

    **面试官**: "明白了。那你觉得，在开发这个 MVP 版本的 AI 助手时，可能会遇到哪些主要的挑战或[[../../Concepts/Product Management/基础概念/风险管理|风险]]？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   展现全面思考，从不同维度分析。
    > *   结合 MVP 的特性（快速、聚焦）。

    > **(示例回答)**:
    > “嗯，即使是 MVP 版本，挑战和风险也不少。我主要想到几个方面：”
    >
    > “**技术层面**，最大的挑战可能还是**保证回答质量**。首先是 **[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 的检索效果**，能不能总能准确、快速地找到用户需要的那一小段信息？如果检索错了，LLM 的回答也就错了。其次是 **[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉控制]]**，虽然 RAG 能缓解，但可能无法完全消除，如何设计[[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|提示]]和校验机制来进一步把关？还有就是模型的**[[../../Concepts/AI & ML/模型鲁棒性 (Robustness)|鲁棒性]]**，用户提问的方式千奇百怪，模型能不能稳定理解？最后是**[[../../Concepts/AI & ML/大型语言模型 (LLM)|成本和延迟]]**，如果选用 API，调用成本如何控制？响应速度能不能满足用户实时交互的需求？”
    >
    > “**产品层面**，主要的挑战在于 **[[../../Concepts/Product Management/产品设计/功能优先级排序|范围界定]]**。MVP 很容易做着做着就想加功能，如何保持聚焦，确保我们优先验证了核心价值假设？另外，如何设计**有效的[[../../Concepts/Product Management/数据分析与实验/KPI|衡量指标]]** 也很关键，比如‘问题解决率’，怎么定义才算‘解决’？用户的[[../../Concepts/Product Management/数据分析与实验/NPS CSAT评分|CSAT]]评分如何设计才能获得真实有效的反馈？”
    >
    > “**用户层面**，一个挑战是**冷启动和用户教育**。如何让用户知道我们有这个新功能，并且愿意去尝试和信任一个 AI 助手？这需要好的[[../../Concepts/Product Management/用户引导 (Onboarding)|引导设计]]。另外，还需要**管理用户的预期**，让他们明白 MVP 阶段 AI 的能力是有限的，避免过高的期望带来失望。”
    >
    > “我觉得识别并提前考虑这些挑战，有助于我们在开发过程中制定应对策略，提高 MVP 成功的几率。”

    ---

    **面试官**: "最后一个问题，你平时会关注哪些 AI 或者电商领域的信息来源？你对这个领域未来的发展有什么看法吗？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   真诚分享，展现主动学习的态度。
    > *   结合具体例子，避免泛泛而谈。
    > *   对未来的看法可以结合自身兴趣和职位方向。

    > **(示例回答)**:
    > “我平时会关注几个方面的信息来源。技术动态方面，我会看一些像 **[具体技术博客/社区，如 Hugging Face Blog, AI Explained 频道]** 的内容，了解[[../../Concepts/AI & ML/Models/主流 LLM 模型概览|主流模型]]的进展和新发布。行业应用方面，我会关注 **[行业媒体/报告，如 TechCrunch AI, CB Insights]** 以及像贵公司这样的**头部电商平台发布的 AI 相关功能和新闻**。我也会在 **[社交平台/社区，如 Twitter/X 上的 AI 研究者, Reddit 的 r/MachineLearning]** 上看大家的讨论。”
    >
    > “对于 AI 在电商领域的未来，我个人非常看好。我觉得短期内，像我们讨论的 **AI 购物助手会越来越普及**，它会变得更懂用户，从简单的问答进化到更主动、更[[个性化]]的导购，比如能根据我的风格和需求，直接帮我搭配一整套衣服。中期来看，**[[../../Concepts/AI & ML/多模态 AI|多模态]]能力**会更重要，用户可能直接拍一张照片问‘有没有类似款式的商品？’，或者 AI 能理解商品视频里的细节。长期而言，我觉得 AI 可能会成为一种**无处不在的购物基础设施**，深度融入搜索、推荐、[[虚拟试穿]]、售后等各个环节，让整个购物体验更加智能、高效和个性化。当然，这其中也会伴随着[[../../Concepts/AI & ML/AI 伦理|伦理]]、[[../../Concepts/AI & ML/模型偏见|偏见]]和[[../../Concepts/AI & ML/技术相关/数据隐私|隐私]]等挑战需要我们持续关注和解决。我对参与到这个变革中感到非常兴奋。”

    ---

    **面试官**: "好的，了解了。时间差不多了，你有什么问题想问我吗？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   准备1-2个真诚且有思考的问题。
    > *   避免问薪资福利等（除非面试官主动提）。

    > **(示例回答)**:
    > “谢谢您！我的确有几个问题想请教。第一个是，对于 AI 产品经理实习生这个角色，团队在日常工作中，会更侧重于让我们参与哪些环节？是偏向[[../../Concepts/Product Management/用户研究/00 - 用户研究概览|用户研究]]多一些，还是[[../../Concepts/Product Management/数据分析与实验/00 - 数据分析概览|数据分析]]，或者是和工程师一起打磨[[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|Prompt]]和评估模型效果呢？”
    >
    > “(如果时间允许) 第二个问题是，您个人觉得在贵公司做电商领域的 AI 产品，最有挑战性但也最有意思的地方是什么？”

    ---
    **(模拟结束)**
""")

# --- UPDATED Comprehensive Level Simulation Content ---
sim_comprehensive_path = os.path.join(simulation_scenarios_folder, '02 - AI 助手面试模拟 (综合深入版).md')
sim_comprehensive_content_updated = textwrap.dedent("""\
    ---
    tags: [topic/interview, type/simulation, level/comprehensive, domain/ai_assistant, process/practice]
    aliases: [AI助手综合面试模拟, 详细对话模拟深入]
    ---
    # AI 助手面试模拟 (综合深入版 - 详细对话示例)

    [[00 - 模拟面试场景入口|返回 模拟入口]]

    **场景设定**: 你正在面试某大型电商平台的 AI 产品经理岗位（可能是全职或有经验的实习生）。面试官可能是资深 PM 或技术负责人，注重考察你的思考深度、技术理解力、战略眼光和处理复杂问题的能力。面试官语速可能较快，追问较多。

    ---

    **面试官**: "你好，[你的名字]。我看过你的简历，我们今天来深入聊聊。先简单做个自我介绍，重点讲讲你认为自己最匹配我们这个 AI 产品经理岗位的经历和能力吧。"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   相比 MVP 面试，这里的自我介绍可以更侧重于**展现深度和成果**。
    > *   使用 [[../../Concepts/Product Management/核心技能/STAR 原则|STAR 法则]] 概括关键项目时，务必突出**量化成果**和你在其中**应对的挑战**。
    > *   更明确地连接你的经验与 **AI PM 所需的核心能力**。

    > **(示例回答)**:
    > “您好面试官，感谢您给我面试机会。我叫[你的名字]，在[上一家公司/学校项目]主要负责[你的职责范围，例如某电商功能模块的产品管理]。我今天面试的是 AI 产品经理岗位，因为我深信 AI 技术将重塑电商体验，并渴望在这个领域做出有影响力的产品。”
    >
    > “在之前的经历中，我有两方面积累比较契合这个岗位。**一方面是扎实的产品管理基本功**。例如，在负责[具体项目名称]时，面对[[../../Concepts/Product Management/数据分析与实验/KPI|关键指标]] [指标名称] 下滑的问题 (Situation)，我的任务是找出原因并提升该指标 (Task)。我主导了[[../../Concepts/Product Management/用户研究/用户访谈|用户访谈]]和[[../../Concepts/Product Management/数据分析与实验/00 - 数据分析概览|用户行为数据分析]]，定位到核心[[../../Concepts/Product Management/基础概念/痛点|痛点]]在于[具体痛点]。基于此，我设计了 [具体方案]，并通过 [[../../Concepts/Product Management/数据分析与实验/A_B 测试|A/B 测试]] 验证了效果，最终将该指标提升了 [量化结果，例如 15%] (Action & Result)。这个过程锻炼了我的[[../../Concepts/Product Management/核心技能/用户洞察|用户洞察]]、[[../../Concepts/Product Management/核心技能/数据分析能力|数据分析]]和[[../../Concepts/Product Management/核心技能/决策能力|产品决策]]能力。”
    >
    > “**另一方面是我对 AI 技术的持续关注和应用思考**。虽然之前的项目并非纯粹的 AI 项目，但我一直在积极学习 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]]、[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 等技术，并思考它们如何赋能电商。例如，我注意到 [之前项目中遇到的某个问题或效率瓶颈]，当时我就设想如果能引入类似[[../../Concepts/AI & ML/Core Technologies/自然语言处理 (NLP)|NLP]]的技术来自动[做什么事]，可能会带来[什么价值]。我还利用业余时间学习了[相关课程或工具]，并搭建了一个简单的 Demo 来验证 [某个 AI 应用想法] 的可行性。这让我对 AI 产品的潜力、挑战（如[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉]]、[[../../Concepts/AI & ML/模型鲁棒性 (Robustness)|鲁棒性]]）以及 PM 在其中需要扮演的角色有了更深的理解。”
    >
    > “总结来说，我认为自己具备**以用户为中心的产品设计能力**、**数据驱动的决策习惯**，以及**对 AI 技术原理和应用场景的浓厚兴趣与快速学习能力**。我非常希望能将这些能力运用到贵公司 AI 购物助手这样富有挑战和价值的产品上。”
    >
    > “以上是我的介绍，谢谢！”

    ---

    **面试官**: "你提到了对 AI 购物助手的思考。我们这个方向对标 Amazon Rufus，希望能打造行业领先的产品。如果让你来负责这个产品的长期规划，你会如何思考产品的[[../../Concepts/Product Management/产品战略与规划/产品战略|战略]]和[[../../Concepts/Product Management/产品战略与规划/产品路线图|路线图]]？请展开谈谈。"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   展现战略思考高度，运用框架但避免生搬硬套。
    *   思考“长期”意味着什么？(例如：3-5 年？)
    *   强调差异化和核心竞争力。
    *   将技术趋势与产品演进结合。

    > **(示例回答)**:
    > “思考 AI 购物助手的长期规划，我会从[[../../Concepts/Product Management/基础概念/产品愿景|产品愿景]]出发，结合市场、用户和自身优势来制定战略和[[../../Concepts/Product Management/产品战略与规划/产品路线图|路线图]]。”
    >
    > “**首先，[[../../Concepts/Product Management/基础概念/产品愿景|愿景]]层面**，我认为 AI 购物助手不应仅仅是一个被动的问答工具，它的终极形态应该是成为每个用户的**‘私人智能购物顾问’**，能够深度理解用户的个性化需求，主动提供有价值的建议，无缝融入购物全链路，让购物变得更智能、更省心、甚至更有趣。”
    >
    > “**其次，基于这个愿景，进行[[../../Concepts/Product Management/完整框架/01 - 行业与市场认知|市场与用户分析]]**。我们需要看[[../../Concepts/Product Management/市场与行业分析/竞品分析|竞争对手]]（如 Rufus）做得怎么样，他们的优势和不足在哪里？同时要深入理解不同[[../../Concepts/Product Management/基础概念/用户画像|用户群体]]（新手、专家、特定品类爱好者）在不同购物阶段（发现、研究、决策、售后）的核心[[../../Concepts/Product Management/基础概念/痛点|痛点]]和未被满足的需求。例如，跨品类复杂决策、个性化风格搭配、可持续消费选择等可能是现有方案覆盖不足的地方。”
    >
    > “**第三，明确我们的[[../../Concepts/Product Management/产品战略与规划/价值主张|核心价值定位]]和[[../../Concepts/Product Management/市场与行业分析/差异化|差异化]]战略**。依托我们平台海量的用户行为数据和商品知识图谱，我认为我们的核心优势在于实现**极致的[[个性化]]理解和精准推荐**。差异化可以体现在：**1. 更懂用户的个性化导购**: 不仅回答问题，更能基于用户风格、历史、场景主动提供搭配建议、替代品推荐等。**2. 全链路无缝体验**: 将助手能力深度整合到搜索、推荐流、购物车、订单、售后等各个环节。**3. 建立信任与专业性**: 通过可靠的[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]和对[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉]]的严格控制，在用户心中建立专业、可信赖的形象。”
    >
    > “**第四，规划[[../../Concepts/Product Management/产品战略与规划/产品路线图|阶段性的路线图主题 (Roadmap Themes)]]**。这需要一个演进的过程：
    >     *   **近期 (0-1年)**: **夯实基础，提升核心体验**。重点是优化核心问答的准确率 ([[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]优化)、覆盖度、[[../../Concepts/AI & ML/模型鲁棒性 (Robustness)|鲁棒性]]，并提升[[../../Concepts/Product Management/产品设计/用户体验 (UX)|交互体验]]（如响应速度）。[[../../Concepts/Product Management/数据分析与实验/KPI|衡量指标]]关注用户满意度 (CSAT)、问题解决率、使用渗透率。
    >     *   **中期 (1-3年)**: **深化智能，驱动转化增长**。重点发展**[[个性化]]推荐和导购能力**（例如，‘帮我找类似风格但更便宜的’、‘这件上衣配什么裤子好看？’），实现更强的**多轮对话**和上下文理解，开始探索**[[../../Concepts/AI & ML/多模态 AI|多模态]]输入**（如以图搜同款/搭配）。[[../../Concepts/Product Management/数据分析与实验/KPI|衡量指标]]重点关注 [[../../Concepts/Product Management/数据分析与实验/转化率|转化率]]、[[../../Concepts/Product Management/数据分析与实验/客单价|客单价]]、用户参与度。
    >     *   **长期 (3年以上)**: **主动智能，无缝融入生态**。探索**主动服务**（如基于用户需求预测，主动推送相关信息或优惠），实现更自然的**语音/多模态交互**，将助手能力**平台化/API化**赋能商家或第三方开发者，最终实现成为‘私人智能购物顾问’的[[../../Concepts/Product Management/基础概念/产品愿景|愿景]]。[[../../Concepts/Product Management/数据分析与实验/KPI|衡量指标]]关注 [[../../Concepts/Product Management/数据分析与实验/用户生命周期价值 (LTV)|LTV]] 提升、[[../../Concepts/Product Management/数据分析与实验/北极星指标|北极星指标]]（如 AI 驱动的 GMV 占比）。
    >
    > “**最后，设定[[../../Concepts/Product Management/数据分析与实验/北极星指标|北极星指标]]** 来指引方向，例如‘AI 助手驱动的用户购物成功率’（结合了效率、转化和满意度）。”
    >
    > “当然，这个规划需要根据技术发展、市场反馈和业务优先级进行动态调整。”

    ---

    **面试官**: "你提到了 RAG 对于保证信息准确性的重要性。但在实际应用中，[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 的检索效果本身可能就不完美，比如检索到了不相关或过时的信息。你认为作为 PM，应该如何与技术团队一起应对‘检索不准’带来的问题？你觉得这个问题有多严重？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   先评估问题的严重性，展现风险意识。
    > *   再给出多层次的解决方案，体现系统性思考。
    > *   强调 PM 的推动和协调作用。

    > **(示例回答)**:
    > “您提的这个问题非常关键，我认为‘检索不准’是 [[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]] 系统中的**核心挑战之一**，其严重性非常高。因为对于电商场景，用户对商品信息（价格、库存、规格）、政策等的准确性要求极高，错误的检索结果直接导致 [[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]] 产生错误的回答，这会严重损害用户信任，甚至引发交易纠纷，可以说是 RAG 系统能否成功的**关键瓶颈**。”
    >
    > “应对这个问题，需要 PM 和技术团队紧密合作，从多个层面入手：”
    >
    > “**首先是源头治理，即优化‘检索 (Retrieve)’环节本身**：
    > > 1.  **提升知识库质量**: 我们需要确保 RAG 依赖的[[../../Concepts/AI & ML/检索增强生成 (RAG)|外部知识库]]（商品库、FAQ 等）本身的**准确性、完整性和时效性**。这需要建立良好的数据治理流程。
    > > 2.  **优化[[../../Concepts/AI & ML/Core Technologies/嵌入 (Embedding)|Embedding 模型]]**: 可能需要针对电商领域的特定术语和语义，[[../../Concepts/AI & ML/微调 (Fine-tuning)|微调]] Embedding 模型，让它能更好地理解商品相关的查询和文档。
    > > 3.  **改进检索策略**: 不能只依赖单一的[[../../Concepts/AI & ML/Information Retrieval/相似性搜索|语义相似度]]。可以探索**混合搜索 (Hybrid Search)**，结合传统的[[../../Concepts/AI & ML/Information Retrieval/关键词搜索|关键词搜索]]（如 BM25）和[[../../Concepts/AI & ML/Information Retrieval/相似性搜索|向量搜索]]；引入**重排 (Re-ranking)** 模型，对初步检索到的结果进行二次排序，提高头部结果的相关性；优化[[../../Concepts/AI & ML/Core Technologies/向量数据库|向量数据库]]的[[../../Concepts/AI & ML/Information Retrieval/近似最近邻搜索 (ANN)|ANN]] 索引参数，在速度和召回率之间找到最佳平衡点。
    > > 4.  **查询理解与改写**: 对于用户模糊或复杂的查询，先进行意图识别和查询改写，生成更利于检索的标准化查询。
    >
    > “**其次是过程监控和干预**：
    > > 5.  **检索结果相关性评估**: 建立机制评估检索返回的 Top-K 个文档块与用户问题的相关性。如果相关性普遍很低，可以考虑不将这些信息传递给 LLM，或者降低 LLM 回答的置信度。
    > > 6.  **LLM 的判断与[[../../Concepts/AI & ML/提示工程 (Prompt Engineering)|提示]]**: 在 Prompt 中明确指示 LLM，如果发现提供的上下文信息与问题不符或不足以回答，应如何响应（例如，说明信息不足，或请求用户澄清），而不是强行回答。
    >
    > “**最后是下游补救和反馈闭环**：
    > > 7.  **答案的后处理与校验**: 对于涉及价格、库存等关键信息的回答，增加校验逻辑或规则进行检查。
    > > 8.  **清晰的来源追溯**: 如果可能，在回答中提供信息的来源链接（例如商品页面、帮助文档），增加透明度，也方便用户自行核实。
    > > 9.  **用户反馈机制**: 这是非常重要的一环。设计方便用户标记‘回答不准确’的机制，收集这些 Bad Case 用于持续优化检索算法、Embedding 模型和知识库内容。[[../../Concepts/Product Management/用户研究/用户反馈闭环|用户反馈闭环]]
    > >10. **优雅降级与转人工**: 设计好当 AI 无法可靠回答时的[[../../Concepts/Product Management/产品设计/容错设计|容错逻辑]]，例如引导用户换个问法，或者提供清晰便捷的转人工客服入口。
    >
    > “作为 PM，我会**推动建立衡量检索质量和最终回答准确率的[[../../Concepts/Product Management/数据分析与实验/KPI|指标]]**，与技术团队一起**设定目标**，并**协调资源**投入到上述各个环节的优化中，持续迭代改进。”

    ---

    **面试官**: "我们来讨论一个具体的场景。假设用户问 AI 助手：‘我想买一台适合打游戏和视频剪辑的笔记本电脑，预算 1 万左右，有什么推荐？’ 你会期望 AI 助手如何响应？这背后需要哪些技术能力和产品设计考量？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   展现处理复杂、开放性需求的能力。
    *   强调多轮交互、个性化和可解释性的重要性。
    *   深入讨论技术挑战和产品细节。

    > **(示例回答)**:
    > “这是一个非常典型但也比较复杂的导购场景，因为它涉及用户的**复合需求、预算约束以及主观偏好**。我期望的 AI 助手响应流程，不仅仅是给出一个简单的列表，而应该是一个**引导式、个性化、且透明可信**的交互过程。”
    >
    > “**第一步：深入理解与澄清需求。** LLM 需要首先准确识别用户的核心意图（寻求推荐）和关键约束（品类：笔记本，用途：游戏+视频剪辑，预算：1万左右）。但‘适合打游戏和视频剪辑’仍然比较模糊，所以**关键的第一反应应该是进行智能追问**，以获取更具体的需求。例如，AI 可以问：
    > > *   ‘好的，为了更好地为您推荐，能具体说说您主要玩哪些游戏吗？对屏幕刷新率有特别要求吗？’
    > > *   ‘视频剪辑方面，主要是处理 1080P 还是 4K 素材？常用的剪辑软件是什么？’
    > > *   ‘除了性能和预算，您对品牌、重量、续航或者外观有什么特别的偏好吗？’
    > 这背后需要强大的[[../../Concepts/AI & ML/Core Technologies/自然语言处理 (NLP)|NLU]]能力来理解初始需求，以及良好的[[对话管理]]能力来设计和执行有效的澄清流程。”
    >
    > “**第二步：基于精确需求进行检索与匹配。** 在获取更具体的需求后（比如用户回答了常玩的游戏类型和对内存的要求），系统需要结合[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]和**结构化数据库查询**。一方面，可能需要通过[[../../Concepts/AI & ML/Information Retrieval/相似性搜索|语义搜索]]理解‘适合玩XX游戏’意味着对显卡的什么要求；另一方面，需要根据明确的预算、内存、品牌等条件进行**精确的属性筛选**。这需要检索系统能够支持混合查询。”
    >
    > “**第三步：融入[[个性化]]推荐。** 在筛选出符合硬性条件的候选商品后，系统应该结合该用户的**历史行为**（浏览、购买、收藏）、**用户画像标签**（如价格敏感度、品牌偏好）以及**平台上相似用户的偏好**，对候选商品进行**个性化排序或推荐**。这需要[[推荐系统]]算法的支持。”
    >
    > “**第四步：生成结构化、可解释的推荐结果。** 我不建议直接推荐单一‘最佳’选项，因为用户偏好是多样的。更好的方式是**推荐 2-3 款各有侧重的电脑**，并**清晰地展示做出推荐的理由**。例如：
    > > *   **呈现**: 使用卡片或其他可视化形式展示每款电脑的关键信息（图片、名称、价格、核心配置如 CPU/GPU/RAM/存储/屏幕、用户评分）。
    > > *   **解释**: 对每款推荐，用简洁的语言说明**为什么它符合用户的需求**。例如：‘**推荐 A**：这款的 **RTX 4060 显卡**能流畅运行您提到的游戏，性价比高；**推荐 B**：这款虽然略超预算，但它的 **CPU 性能**和**高色准屏幕**更适合您的视频剪辑工作；**推荐 C**：这款非常**轻薄便携**，如果您经常需要携带的话...’ 这需要 LLM 具备良好的**总结、对比和解释能力**，并且这些解释需要基于真实的商品特性 ([[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]的重要性再次体现)。[[可解释性 AI]]
    > > *   **行动引导**: 提供明确的下一步操作按钮，如 ‘查看详情’、‘加入对比’、‘不喜欢，换一批’、‘我想再问问关于[某款电脑]的…’。”
    >
    > “**技术能力要求总结**: 这需要一个融合了[[../../Concepts/AI & ML/Core Technologies/自然语言处理 (NLP)|NLU]]、[[对话管理]]、[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]（混合搜索）、[[推荐系统]]和[[../../Concepts/AI & ML/大型语言模型 (LLM)|LLM]]生成/解释能力的复杂系统。
    > **产品设计考量**: 核心在于如何设计**自然的澄清交互**，如何**有效组织和呈现复杂的比较信息**，如何**平衡个性化与多样性**，以及如何在整个流程中**建立和维持用户的信任**。”

    ---

    **面试官**: "如果让你在 [[../../Concepts/AI & ML/Models/LLaMA 模型系列|Llama 3]] 开源模型和 [[../../Concepts/AI & ML/Models/GPT 模型系列|GPT-4o]] API 之间为我们的 AI 助手选择一个基础模型，你会主要考虑哪些因素？并给出你的初步倾向和理由。"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   展现对技术选型复杂性的理解，强调没有银弹。
    > *   系统性地列出权衡维度，并结合业务场景分析。
    > *   给出有逻辑支撑的倾向性结论，并保留调整空间。

    > **(示例回答)**:
    > “这是一个非常关键的技术选型决策，我会从多个维度来系统性地评估和权衡：”
    >
    > “**1. 性能与特定能力**: [[../../Concepts/AI & ML/Models/GPT 模型系列|GPT-4o]] 作为顶尖的[[../../Concepts/AI & ML/开源 vs 闭源模型|闭源模型]]，在通用的[[../../Concepts/AI & ML/Core Technologies/自然语言处理 (NLP)|自然语言理解]]、[[推理]]和特别是[[../../Concepts/AI & ML/多模态 AI|多模态]]能力上可能具有优势，API 调用也相对成熟。[[../../Concepts/AI & ML/Models/LLaMA 模型系列|Llama 3]] 是目前最强的[[../../Concepts/AI & ML/开源 vs 闭源模型|开源模型]]之一，虽然通用能力可能略有差距（差距在缩小），但它的**优势在于开放性**，允许我们针对电商领域的特定术语、对话风格和海量商品知识进行深度**[[../../Concepts/AI & ML/微调 (Fine-tuning)|微调]]**，理论上可以在**特定领域达到甚至超过**通用闭源模型的表现。对于购物助手来说，领域适配性可能非常重要。”
    >
    > “**2. 成本**: [[../../Concepts/AI & ML/Infrastructure/API (应用程序接口)|API]] 调用是按量付费，对于我们这样用户量巨大的电商平台，如果助手使用率很高，长期来看 API 成本可能会非常高昂。[[../../Concepts/AI & ML/开源 vs 闭源模型|开源模型]]虽然需要前期投入硬件（GPU 服务器）、部署和维护的人力成本，但**边际成本较低**，长期大规模使用可能更经济。”
    >
    > “**3. 数据隐私与安全**: 这是电商平台的核心生命线。使用 [[../../Concepts/AI & ML/Infrastructure/API (应用程序接口)|API]] 意味着用户的对话数据、甚至可能间接关联到的购物行为数据需要传输给第三方。尽管有隐私协议，但这始终是一个潜在风险点。[[../../Concepts/AI & ML/开源 vs 闭源模型|开源模型]]允许我们**完全在自己的基础设施内运行**，对数据有完全的掌控权，隐私和安全性更高。”
    >
    > “**4. 定制化与控制权**: [[../../Concepts/AI & ML/开源 vs 闭源模型|开源模型]]提供了最大的灵活性。我们可以自由地进行[[../../Concepts/AI & ML/微调 (Fine-tuning)|微调]]，调整模型行为，甚至修改模型结构。而 [[../../Concepts/AI & ML/Infrastructure/API (应用程序接口)|API]] 的定制化能力通常非常有限，我们也会受制于 API 提供商的更新节奏、价格策略甚至服务中断风险。”
    >
    > “**5. 开发速度与生态**: [[../../Concepts/AI & ML/Infrastructure/API (应用程序接口)|API]] 无疑能让我们**更快地启动项目**和进行 MVP 验证。[[../../Concepts/AI & ML/开源 vs 闭源模型|开源模型]]的部署、优化和维护需要更强的技术团队和更长的周期。不过，Llama 的开源社区非常活跃，有很多工具和预训练资源可以利用。”
    >
    > “**权衡与初步倾向**:
    > 综合来看，考虑到我们平台**对数据隐私的极高要求**，以及电商场景对**领域知识深度适配和长期成本控制**的需求，我**初步更倾向于深入评估基于 [[../../Concepts/AI & ML/Models/LLaMA 模型系列|Llama 3]] 等高性能开源模型进行自建和[[../../Concepts/AI & ML/微调 (Fine-tuning)|微调]]的方案**。这能给我们带来长期的技术自主权、数据安全性和成本优势。
    >
    > 当然，这需要我们具备相应的技术投入能力。在项目初期，我们**也可以考虑先使用 [[../../Concepts/AI & ML/Models/GPT 模型系列|GPT-4o]] API 进行快速原型验证和核心功能迭代**，同时并行地探索和构建基于开源模型的能力，未来再根据实际效果和成本进行迁移。最终决策需要基于更详细的技术评测 (PoC) 和成本效益分析。”

    ---

    **面试官**: "好的，今天的交流非常有收获。你有什么问题想问我吗？"

    **候选人 (你)**:
    > [!tip] 回答策略
    > *   问与刚才讨论相关、或更能展现你思考深度的问题。
    *   可以结合面试官的背景提问。

    > **(示例回答)**:
    > “非常感谢您今天深入的交流！我确实有两个问题想请教：”
    >
    > “第一个是，刚才我们讨论了很多 AI 助手的技术挑战，比如[[../../Concepts/AI & ML/模型幻觉 (Hallucination)|幻觉]]控制和[[../../Concepts/AI & ML/检索增强生成 (RAG)|RAG]]优化。从您的角度看，在将这类 AI 技术真正落地到大规模电商平台的复杂业务中，**除了技术本身，您认为最大的组织性或流程性挑战是什么？**”
    >
    > “第二个问题是，对于 AI 产品经理这个角色，除了技术理解和产品能力，您认为**未来 3-5 年，还需要培养哪些关键的新能力或素质**才能保持竞争力？”
    >
    > “再次感谢您的时间！”

    ---
    **(模拟结束)**
""")


# --- Main Script Logic ---
def main():
    print("Starting Obsidian Knowledge Base Generation (Part 14 - Enhanced Simulations)...")
    print(f"Target Root Directory: {os.path.abspath(TARGET_ROOT_DIRECTORY)}")
    print(f"Overwrite Existing Files: {OVERWRITE_EXISTING}")

    # Define paths for the simulation files (ensure these variables match those used below)
    # Need to define the missing variable from the traceback
    sim_entry_point_path = os.path.join(simulation_scenarios_folder, '00 - 模拟面试场景入口.md')
    sim_entry_point_content = textwrap.dedent("""\
    ---
    tags: [topic/interview, type/simulation, process/practice]
    aliases: [面试模拟场景, PM面试实战]
    ---
    # 模拟面试场景入口

    [[../Preparation Guide/00 - 面试准备指南与行动计划|返回 准备指南]]

    ## 概述

    欢迎来到模拟面试实战场景！这里的目标是提供更接近真实面试体验的对话式模拟。我们为你准备了不同难度和侧重点的模拟场景，帮助你将之前学习的概念和框架应用到接近真实的对话中。

    **核心练习目标**:
    *   练习自然的对话表达。
    *   在压力下结构化地思考和回答。
    *   灵活运用 [[../../Concepts/Product Management/核心技能/STAR 原则|STAR 原则]]、产品设计框架等。
    *   将 AI/LLM 知识自然地融入产品讨论。
    *   适应不同的面试官风格和追问。

    ## 模拟场景列表

    1.  **[[01 - AI 助手面试模拟 (MVP 快速版)|AI 助手面试模拟 (MVP 快速版)]]**
        *   **适合**: 面试初期准备，或针对节奏较快、更侧重核心 PM 技能和潜力的面试轮次（例如针对实习生）。
        *   **特点**: 对话相对直接，问题更侧重于 [[../../Concepts/Product Management/MVP 框架/00 - MVP 框架概览|MVP]] 思维、核心[[../../Concepts/Product Management/核心技能/沟通技巧|沟通]]与[[../../Concepts/Product Management/核心技能/解决问题能力|解决问题]]能力、基础[[../../Concepts/Product Management/核心技能/PM 对 LLM 的理解深度|AI 概念理解]]。
    2.  **[[02 - AI 助手面试模拟 (综合深入版)|AI 助手面试模拟 (综合深入版)]]**
        *   **适合**: 面试后期准备，或针对需要展现深度思考、技术理解和处理复杂性能力的面试轮次。
        *   **特点**: 对话可能更深入，包含更多追问，涉及[[../../Concepts/Product Management/完整框架/00 - 完整产品管理框架概览|完整框架]]思考、技术[[../../Concepts/Product Management/技术选型|选型权衡]]、[[../../Concepts/Product Management/基础概念/风险管理|风险管理]]、[[../../Concepts/Product Management/产品战略与规划/产品战略|战略思考]]等。

    ## 如何使用这些模拟场景？

    [!exercise] 练习建议
    > 1. **选择场景**: 根据你的准备阶段和目标选择一个场景开始。
    > 2. **扮演角色**: 大声朗读“面试官”的问题，然后**口头回答**“候选人 (你)”的部分。**不要只是阅读！**
    > 3. **运用框架和知识**: 在回答时，积极思考并尝试运用 [[../../Concepts/Product Management/核心技能/STAR 原则|STAR]]、产品设计框架，并引用相关的[[../../Concepts/AI & ML/00 - AI 与机器学习概览|AI]]和[[../../Concepts/Product Management/00 - 产品管理框架概览|产品管理]]概念。
    > 4. **注意引导提示**: 留意 `[!tip]` 或 `[!info]` 中的提示，它们会指导你的思考方向或建议使用的概念。
    > 5. **计时练习**: (可选) 为自己设定回答时间限制，模拟真实面试的压力。
    > 6. **录音复盘**: (强烈推荐) 录下你的回答，回听评估流畅度、逻辑性、内容深度和时间控制。
    > 7. **反复练习**: 对同一个场景进行多次练习，尝试不同的表述方式和侧重点。

    开始你的模拟面试吧！
    """) # End of sim_entry_point_content definition

    # Files to update with enhanced conversational content
    files_to_create = {
        sim_entry_point_path: sim_entry_point_content, # Use the newly defined content variable
        sim_mvp_path: sim_mvp_content_updated, # Use the updated MVP content
        sim_comprehensive_path: sim_comprehensive_content_updated, # Use the updated Comprehensive content
    }

    # Create necessary base directories if they don't exist
    # Need to ensure all potentially referenced parent directories exist
    os.makedirs(simulation_scenarios_folder, exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Preparation Guide'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Self Introduction'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Behavioral Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Product Design Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Technical Simulation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', 'Asking Questions'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', 'MVP 框架'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '完整框架'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '基础概念'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '产品战略与规划'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '产品设计'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '数据分析与实验'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '沟通协作'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '核心技能'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '应用案例 - AI 助手'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Core Technologies'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Models'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Evaluation'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Infrastructure'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'AI & ML', 'Information Retrieval'), exist_ok=True)
    os.makedirs(os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Fundamentals'), exist_ok=True)

    print("Base directories ensured.")

    for filepath, content in files_to_create.items():
        if not OVERWRITE_EXISTING and os.path.exists(filepath):
            print(f"Skipping existing file: {filepath}")
            continue
        write_file(filepath, content)

    print("\nObsidian Knowledge Base Generation (Part 14 - Fixed) Complete.")
    print("Focus was on updating simulation scenarios with detailed, conversational examples.")

if __name__ == "__main__":
    main()
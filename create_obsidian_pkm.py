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

# --- Knowledge Base Content Definitions (Part 4 - Prioritized Gaps: Skills & Core Concepts) ---

# Interview Simulation/Product Manager Interview/技巧与方法
interview_skills_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Interview Simulation', 'Product Manager Interview', '技巧与方法')

behavioral_interview_questions_path = os.path.join(interview_skills_folder, '行为面试问题.md')
behavioral_interview_questions_content = textwrap.dedent("""\
    ---
    tags: [topic/interview, concept/behavioral_questions, type/guide, skill/interviewing]
    aliases: [Behavioral Interview Questions, BI Questions, 行为问题]
    ---
    # 行为面试问题 (Behavioral Interview Questions)

    [[面试技巧|返回 面试技巧]]

    ## 概述

    行为面试问题是面试中非常常见的一类问题，旨在通过了解你**过去的行为**来预测你**未来的表现**。面试官认为，过去的经历是预测未来行为的最佳指标。这类问题通常要求你分享具体的例子来证明你具备某种技能、特质或在特定情况下会如何反应。

    问题的典型开头方式包括：
    *   “请分享一个你...” (Tell me about a time when you...)
    *   “描述一个你曾经...” (Describe a situation where you...)
    *   “举一个例子说明你如何...” (Give me an example of how you...)
    *   “你遇到过...的情况吗？你是怎么处理的？” (Have you ever encountered... How did you handle it?)

    回答行为面试问题的最佳方法是使用 [[STAR 原则|STAR 原则]]。

    ## 常见的行为面试问题类型 (产品经理)

    产品经理面试中的行为问题通常围绕以下核心能力展开：

    1.  **领导力与影响力 (Leadership & Influence)**:
        *   “分享一次你带领团队完成一个困难项目的经历。”
        *   “描述一次你需要在没有直接管理权的情况下，说服[[../Concepts/Product Management/沟通协作/跨职能团队|跨职能团队]]接受你的想法。”
        *   “讲一次你不得不做出一个不受欢迎但正确的决策。”
    2.  **[[../Concepts/Product Management/沟通协作/沟通技巧|沟通与协作]] (Communication & Collaboration)**:
        *   “举例说明你如何向非技术背景的[[../Concepts/Product Management/沟通协作/利益相关者管理|利益相关者]]解释一个复杂的技术概念。”
        *   “描述一次你与难相处的同事或[[../Concepts/Product Management/沟通协作/利益相关者管理|利益相关者]]成功合作的经历。”
        *   “分享一次你的沟通出现误解，以及你是如何解决的。”
        *   “你如何确保[[../Concepts/Product Management/沟通协作/跨职能团队|跨职能团队]]对产品目标保持[[../Concepts/Product Management/沟通协作/团队对齐|对齐]]？”
    3.  **解决问题与决策能力 (Problem Solving & Decision Making)**:
        *   “描述一个你遇到的最复杂的问题，以及你是如何分析和解决的。”
        *   “分享一次你在信息不充分的情况下做出关键决策的经历。”
        *   “讲一次你基于[[../Concepts/Product Management/数据分析与实验/数据驱动决策|数据分析]]做出重要产品决策的例子。”
        *   “当面对多个优先级冲突的需求时，你是如何决策的？（结合[[../Concepts/Product Management/产品设计/功能优先级排序|优先级排序]]框架）”
    4.  **[[../Concepts/Product Management/沟通协作/冲突解决|冲突管理]] (Conflict Management)**:
        *   “分享一次你处理团队成员之间冲突的经历。” ([[../Concepts/Product Management/沟通协作/STAR 原则|STAR 原则]] 示例中已使用)
        *   “描述一次你与[[../Concepts/Product Management/沟通协作/利益相关者管理|利益相关者]]在产品方向上存在分歧，你是如何处理的。”
    5.  **主动性与结果导向 (Initiative & Results Orientation)**:
        *   “分享一次你主动发现并解决了一个重要问题的经历。”
        *   “讲一个你超额完成目标的例子。”
        *   “描述一次你失败的经历，以及你从中吸取了什么教训？” (考察[[../Concepts/Product Management/核心技能/学习能力|学习能力]]和韧性)
    6.  **用户中心思维 (User Centricity)**:
        *   “举例说明你如何将[[../Concepts/Product Management/用户研究/用户反馈|用户反馈]]融入产品决策。”
        *   “描述一次你为了深入理解用户需求所做的努力。”
    7.  **适应性与应对压力 (Adaptability & Handling Pressure)**:
        *   “分享一次项目需求或方向发生重大变化，你是如何应对的。”
        *   “描述一次你在高压或紧迫的时间表下工作的经历。”

    ## 如何准备行为面试问题

    1.  **回顾经历**: 仔细梳理你的项目经验、工作经历、甚至相关的课外活动或个人项目。
    2.  **匹配能力**: 对照目标职位的要求，思考哪些经历可以证明你具备所需的核心能力。
    3.  **准备[[STAR 原则|STAR 故事]]**: 为每个核心能力准备 2-3 个具体的[[STAR 原则|STAR 故事]]。确保故事完整、有细节、突出你的行动和量化结果。
    4.  **练习讲述**: 反复练习用[[STAR 原则|STAR 法则]]清晰、简洁、自信地讲述你的故事。控制时间，突出重点。可以使用[[../Concepts/Product Management/核心技能/讲故事能力|讲故事]]的技巧让你的回答更生动。
    5.  **思考变体**: 思考同一个故事可以用在哪些不同的问题上，或者一个问题可以用哪些不同的故事来回答。

    ## 总结

    行为面试问题是评估候选人软技能和过往经验的关键环节。通过充分准备[[STAR 原则|STAR 故事]]并练习有效表达，你可以自信地应对这类问题，充分展现你的能力和潜力。

    ## 相关概念

    *   [[面试技巧]]
    *   [[STAR 原则]]
    *   [[../Concepts/Product Management/核心技能/沟通技巧|沟通技巧]]
    *   [[../Concepts/Product Management/核心技能/解决问题能力|解决问题能力]]
    *   [[../Concepts/Product Management/核心技能/决策能力|决策能力]]
    *   [[../Concepts/Product Management/核心技能/领导力|领导力]]
    *   [[../Concepts/Product Management/核心技能/冲突解决|冲突解决]]
    *   [[../Concepts/Product Management/核心技能/讲故事能力|讲故事能力]]
""")

# Concepts/Product Management/核心技能
core_skills_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '核心技能')

storytelling_path = os.path.join(core_skills_folder, '讲故事能力.md')
storytelling_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, skill/storytelling, type/soft_skill, skill/communication]
    aliases: [Storytelling, 产品叙事]
    ---
    # 讲故事能力 (Storytelling)

    ## 概述

    讲故事能力 (Storytelling) 对于产品经理来说，是一项非常重要的[[沟通技巧|软技能]]。它指的是**运用叙事的方式来传递信息、激发情感、建立连接、并最终影响他人（如团队成员、[[../沟通协作/利益相关者管理|利益相关者]]、用户）**的能力。

    产品经理需要在各种场合讲故事：
    *   向团队阐述[[../基础概念/产品愿景|产品愿景]]和[[../产品战略与规划/产品战略|战略]]。
    *   向[[../沟通协作/利益相关者管理|利益相关者]]汇报进展、争取资源或解释决策。
    *   在[[../文档与交付物/PRD 产品需求文档|需求文档]]或[[../用户研究/用户故事|用户故事]]中描绘用户场景和价值。
    *   在面试中（尤其是回答[[../../Interview Simulation/Product Manager Interview/技巧与方法/行为面试问题|行为面试问题]]时）生动地展示自己的经历和能力。
    *   向市场和用户传递产品的[[../产品战略与规划/价值主张|价值主向]]。

    一个好的故事比枯燥的数据或指令更能吸引人、更容易被记住、也更有说服力。

    ## 好故事的要素

    一个引人入胜的故事通常包含以下要素：

    1.  **清晰的主题/信息 (Clear Theme/Message)**: 你想通过这个故事传达的核心观点是什么？
    2.  **情境设定 (Setting the Scene)**: 故事发生的背景、时间、地点是什么？帮助听众进入情境。([[../沟通协作/STAR 原则|STAR]] 中的 S)
    3.  **角色 (Characters)**: 故事的主人公是谁？（可能是用户、团队、或者你自己）。让角色有血有肉，有目标和动机。
    4.  **冲突/挑战 (Conflict/Challenge)**: 主人公遇到了什么问题、障碍或[[../基础概念/痛点|痛点]]？这是驱动故事发展的核心。([[../沟通协作/STAR 原则|STAR]] 中的 T)
    5.  **情节/行动 (Plot/Action)**: 主人公为了解决冲突采取了哪些行动？故事是如何发展的？这是故事的主体。([[../沟通协作/STAR 原则|STAR]] 中的 A)
    6.  **高潮/转折点 (Climax/Turning Point)**: 故事中最关键、最紧张或最重要的时刻。
    7.  **结局/结果 (Resolution/Result)**: 冲突最终如何解决？主人公达成了什么目标或获得了什么结果？带来了什么影响？([[../沟通协作/STAR 原则|STAR]] 中的 R)
    8.  **情感连接 (Emotional Connection)**: 好故事能够触动听众的情感，引发共鸣（例如：喜悦、激动、同情、希望）。
    9.  **(可选) 教训/启示 (Lesson/Moral)**: 故事带来了什么启示或值得学习的地方？

    ## 产品经理如何运用讲故事能力？

    *   **阐述[[../基础概念/产品愿景|产品愿景]]**: 不要只说“我们要成为市场领导者”，而是描绘一个用户因为使用了你的产品而生活变得更美好的具体场景和故事。
    *   **解释[[../用户研究/用户故事|用户故事]]**: 让[[../用户研究/用户故事|用户故事]]不仅仅是“作为一个XX，我想要XX，以便XX”，而是围绕这个故事描绘更丰富的用户场景、[[../基础概念/痛点|痛点]]和期望。
    *   **沟通[[../数据分析与实验/00 - 数据分析概览|数据]]**: 不要只罗列数据，而是用数据讲述一个故事。例如，数据变化背后反映了怎样的用户行为变化？这个变化对业务意味着什么？
    *   **进行[[../沟通协作/演示表达|演示汇报]]**: 使用故事来开场或串联你的汇报内容，吸引听众注意力，让信息更容易被理解和记住。
    *   **回答[[../../Interview Simulation/Product Manager Interview/技巧与方法/行为面试问题|行为面试问题]]**: 使用[[../沟通协作/STAR 原则|STAR 法则]]本身就是一种结构化的讲故事方式。在讲述时，加入适当的情感和细节，让你的经历更生动、更有说服力。
    *   **构建[[品牌故事]]**: 与市场团队合作，围绕产品和品牌的核心价值讲述引人入胜的故事。

    ## 提升讲故事能力的技巧

    *   **了解你的听众**: 故事要根据听众的背景、兴趣和关注点进行调整。
    *   **明确核心信息**: 清楚你想通过故事传达的关键点是什么。
    *   **结构清晰**: 遵循经典的叙事结构（开端、发展、高潮、结局）。
    *   **注重细节**: 适当的细节能让故事更真实、更生动。
    *   **注入情感**: 真诚地表达情感，与听众建立连接。
    *   **善用比喻和类比**: 让复杂的概念更容易理解。
    *   **练习，练习，再练习**: 多讲、多听、多观察，不断打磨你的故事。可以录下自己讲故事的过程进行复盘。
    *   **保持简洁**: 避免冗长和无关的细节，抓住重点。

    ## 总结

    讲故事是产品经理的核心[[沟通技巧]]之一。掌握讲故事的能力，能够让你在沟通、协作、影响他人以及面试中更具优势。通过有意识地运用叙事结构和技巧，你可以将信息和想法以更有效、更有影响力的方式传递出去。

    ## 相关概念

    *   [[沟通技巧]]
    *   [[../沟通协作/演示表达|演示表达]]
    *   [[../../Interview Simulation/Product Manager Interview/技巧与方法/行为面试问题|行为面试问题]]
    *   [[../沟通协作/STAR 原则|STAR 原则]]
    *   [[../基础概念/产品愿景|产品愿景]]
    *   [[../用户研究/用户故事|用户故事]]
    *   [[品牌故事]]
    *   [[影响力]]
""")

communication_skills_path = os.path.join(core_skills_folder, '沟通技巧.md')
communication_skills_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, skill/communication, type/soft_skill]
    aliases: [Communication Skills, 产品经理沟通]
    ---
    # 沟通技巧 (Communication Skills)

    ## 概述

    沟通技巧是产品经理**最核心、最基础**的软技能之一。产品经理作为连接[[../沟通协作/跨职能团队|跨职能团队]]、[[../沟通协作/利益相关者管理|利益相关者]]和用户的枢纽，其工作效率和成果在很大程度上取决于有效的沟通。

    有效的沟通不仅仅是信息的传递，更是**理解的建立、共识的达成、关系的维护和影响力的发挥**。它贯穿于产品管理的每一个环节，从[[../完整框架/02 - 用户需求分析|需求挖掘]]、[[../完整框架/03 - 产品设计与方案构思|方案设计]]、[[../完整框架/04 - 技术与实现|技术实现]]到[[../完整框架/06 - 推动与沟通|推动上线]]和[[../完整框架/07 - 迭代与成长|后续迭代]]。

    ## 关键沟通技巧维度

    1.  **清晰表达 (Clarity & Conciseness)**
        *   **结构化思维**: 表达前先组织思路（例如使用金字塔原理、总分总结构）。
        *   **语言精练**: 使用简洁、明确、无歧义的语言，避免行话和术语（除非对方熟悉）。
        *   **突出重点**: 清晰传达核心信息和关键要点。
        *   **书面沟通**: 编写清晰、结构化的[[../文档与交付物/PRD 产品需求文档|文档]]、邮件、报告。

    2.  **积极倾听 (Active Listening)**
        *   **专注**: 全神贯注地听对方讲话，避免打断。
        *   **理解**: 不仅听懂字面意思，更要理解对方的意图、感受和立场。
        *   **确认**: 通过复述、提问（“所以你的意思是...?”）来确认自己理解无误。
        *   **非语言信号**: 注意对方的肢体语言和语气。
        *   **同理心 (Empathy)**: 尝试站在对方的角度思考问题。

    3.  **提问能力 (Questioning)**
        *   **开放式问题**: 鼓励对方详细阐述（“你对这个方案有什么看法？”）。
        *   **封闭式问题**: 用于确认信息或获取具体答案（“这个功能下周能完成吗？”）。
        *   **探究性问题**: 深入挖掘原因和细节（“为什么你认为这个方案更好？” [[../用户研究/5 Whys|5 Whys]]）。
        *   **澄清性问题**: 确保理解一致（“你能再解释一下这个技术难点吗？”）。

    4.  **[[../沟通协作/演示表达|演示与呈现]] (Presentation)**
        *   **逻辑清晰**: 演示内容结构合理，易于理解。
        *   **视觉辅助**: 制作简洁、专业的幻灯片或其他可视化材料。
        *   **[[讲故事能力|讲故事]]**: 运用叙事技巧吸引听众。
        *   **自信表达**: 保持自然的语速、音量和肢体语言。
        *   **互动控场**: 与听众互动，回答问题，把握节奏。

    5.  **书面沟通 (Written Communication)**
        *   **[[../文档与交付物/PRD 产品需求文档|PRD]] 与文档**: 编写结构清晰、内容完整、易于理解的需求文档、[[../产品战略与规划/产品路线图|路线图]]、复盘报告等。
        *   **邮件沟通**: 专业、简洁、重点突出，明确需要对方做什么（如有）。
        *   **即时消息 (IM)**: 适用于快速同步和简单问题，避免长篇大论。复杂问题或正式决策建议使用邮件或会议。

    6.  **[[../沟通协作/冲突解决|冲突管理与谈判]] (Conflict Resolution & Negotiation)**
        *   识别冲突根源，保持冷静客观。
        *   积极倾听各方诉求，寻找共同点。
        *   提出建设性解决方案，寻求[[双赢 (Win-Win)]]。
        *   在必要时进行[[../沟通协作/谈判技巧|谈判]]和妥协。

    7.  **[[../沟通协作/利益相关者管理|向上管理与横向协调]] (Managing Up & Sideways)**
        *   **向上管理**: 主动向领导汇报进展、风险，管理预期，寻求支持。
        *   **横向协调**: 与[[../沟通协作/跨职能团队|其他部门]]同事建立良好关系，有效协作。

    8.  **给予和接收[[../用户研究/用户反馈|反馈]] (Giving & Receiving Feedback)**
        *   **给予反馈**: 具体、及时、对事不对人，关注行为和影响，提出改进建议。
        *   **接收反馈**: 保持开放心态，虚心听取，表示感谢，反思改进。

    ## 提升沟通技巧的建议

    *   **明确沟通目标**: 每次沟通前思考：我想达到什么目的？我想让对方了解什么/做什么？
    *   **了解沟通对象**: 考虑对方的背景、角色、关注点和沟通风格。
    *   **选择合适的渠道**: 根据沟通内容和对象选择最有效的方式（会议、邮件、电话、IM等）。
    *   **练习与反思**: 在实践中不断运用沟通技巧，并反思哪些做得好，哪些可以改进。
    *   **寻求反馈**: 主动向同事、领导或导师寻求关于你沟通方式的反馈。
    *   **观察学习**: 观察优秀的沟通者是如何表达、倾听和互动的。

    ## 总结

    沟通是产品经理的“空气和水”，无处不在且至关重要。持续打磨倾听、表达、提问、写作、呈现等各项沟通技巧，能够极大地提升产品经理的工作效率和影响力，是职业发展的核心竞争力。

    ## 相关概念

    *   [[../完整框架/06 - 推动与沟通|推动与沟通]]
    *   [[积极倾听]]
    *   [[提问技巧]]
    *   [[../沟通协作/演示表达|演示表达]]
    *   [[书面沟通]]
    *   [[../沟通协作/冲突解决|冲突解决]]
    *   [[../沟通协作/谈判技巧|谈判技巧]]
    *   [[../沟通协作/利益相关者管理|利益相关者管理]]
    *   [[../沟通协作/跨职能团队|跨职能团队]]
    *   [[../用户研究/用户反馈|反馈]]
    *   [[同理心]]
    *   [[讲故事能力]]
""")

quantitative_thinking_path = os.path.join(core_skills_folder, '量化思维.md')
quantitative_thinking_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, skill/quantitative_thinking, type/mindset, skill/data_literacy, skill/decision_making]
    aliases: [Quantitative Thinking, 量化分析能力, 数据敏感度]
    ---
    # 量化思维 (Quantitative Thinking)

    ## 概述

    量化思维是指在思考问题、分析情况、做出决策时，**倾向于使用数据、指标和量化分析**来理解、衡量和评估事物的能力和习惯。对于产品经理而言，这是一种重要的思维方式，是实现[[../数据分析与实验/数据驱动决策|数据驱动决策]]的基础。

    具备量化思维的产品经理，不会仅仅依赖直觉或定性描述，而是会主动思考：
    *   这个问题/现象的**规模**有多大？（How big?）
    *   它的**频率**如何？（How often?）
    *   它的**影响程度**如何？（What's the impact?）
    *   我们如何**衡量**成功？（How to measure?）
    *   数据告诉我们什么**趋势**？（What's the trend?）
    *   不同方案的**成本效益**如何？（What's the cost-benefit?）

    ## 量化思维在产品管理中的体现

    1.  **定义[[../数据分析与实验/KPI|目标与指标]]**:
        *   将模糊的产品目标转化为具体的、可衡量的[[../数据分析与实验/KPI|KPI]]或[[../数据分析与实验/OKR|OKR]]的关键结果。
        *   思考如何定义[[../数据分析与实验/北极星指标|北极星指标]]来指引方向。
    2.  **[[../产品设计/功能优先级排序|需求优先级排序]]**:
        *   使用[[../产品设计/RICE 模型|RICE 模型]]等量化框架，评估需求的覆盖面 (Reach)、影响程度 (Impact) 和投入精力 (Effort)。
        *   估算功能上线可能带来的[[../数据分析与实验/KPI|指标]]提升。
    3.  **[[../数据分析与实验/00 - 数据分析概览|数据分析与解读]]**:
        *   能够看懂[[../数据分析与实验/Dashboard|数据报表]]，理解[[../数据分析与实验/KPI|核心指标]]的含义和变化趋势。
        *   运用[[../数据分析与实验/用户分群|同期群分析]]、[[../数据分析与实验/漏斗分析|漏斗分析]]等方法，从数据中发现问题和洞察。
    4.  **[[../数据分析与实验/A_B 测试|实验设计与评估]]**:
        *   设计[[../数据分析与实验/A_B 测试|A/B 测试]]方案，明确要比较的指标和[[../数据分析与实验/统计显著性|统计显著性]]要求。
        *   基于实验数据做出科学决策。
    5.  **评估[[../产品战略与规划/产品战略|方案与决策]]**:
        *   进行[[../技术相关/成本效益分析|成本效益分析]]，评估不同技术方案或产品策略的潜在[[ROI]]。
        *   估算市场规模 ([[../市场与行业分析/TAM SAM SOM|TAM/SAM/SOM]])。
    6.  **[[../沟通协作/沟通技巧|沟通与汇报]]**:
        *   用数据支撑自己的观点和建议，使沟通更有说服力。（例如：在[[../沟通协作/演示表达|汇报]]中展示关键数据和图表）
        *   在回答[[../../Interview Simulation/Product Manager Interview/技巧与方法/行为面试问题|行为面试问题]]时，使用[[../沟通协作/STAR 原则|STAR 法则]]的 R (Result) 部分，尽可能量化成果。

    ## 如何培养量化思维？

    *   **建立[[../数据分析与实验/数据指标体系|数据指标体系]]意识**: 了解你负责的产品有哪些核心指标？它们是如何定义的？正常的范围是多少？
    *   **主动接触数据**: 经常查看产品数据[[../数据分析与实验/Dashboard|看板]]，尝试自己分析数据（即使只是用 Excel）。
    *   **多问“多少”和“如何衡量”**: 在讨论问题或方案时，习惯性地思考量化的问题。
    *   **学习基础统计学知识**: 了解平均数、中位数、百分比、[[../数据分析与实验/统计显著性|显著性]]等基本概念。
    *   **掌握常用分析方法**: 学习[[../数据分析与实验/漏斗分析|漏斗分析]]、[[../数据分析与实验/用户分群|同期群分析]]、[[../数据分析与实验/A_B 测试|A/B 测试]]等基本原理和应用场景。
    *   **关注估算能力 (Estimation)**: 练习对用户量、市场规模、开发工作量等进行快速估算（[[费米问题]]是很好的练习）。
    *   **向数据分析师学习**: 主动与[[../数据分析与实验/数据分析师|数据分析师]]交流，学习他们分析问题的思路和方法。
    *   **保持好奇心和批判性思维**: 对数据结果保持好奇，同时也要思考数据的来源、准确性和可能的偏差。

    ## 量化思维的重要性

    *   **提高决策质量**: 基于数据的决策通常比基于直觉的决策更可靠。
    *   **提升沟通效率**: 数据是通用语言，能够减少主观争论。
    *   **精准定位问题**: 通过量化分析更容易找到问题的关键点。
    *   **有效衡量进展**: 清晰了解目标达成情况。
    *   **增强说服力**: 用数据支撑观点更能赢得信任和支持。

    ## 总结

    量化思维是优秀产品经理的关键特质之一。它并非要求 PM 成为数据科学家，而是要养成一种用数据思考、用数据说话的习惯。通过有意识地培养和实践，你可以提升自己的量化分析能力，从而做出更明智的产品决策。

    ## 相关概念

    *   [[../数据分析与实验/数据驱动决策|数据驱动决策]]
    *   [[../数据分析与实验/00 - 数据分析概览|数据分析]]
    *   [[../数据分析与实验/KPI|KPI]]
    *   [[../数据分析与实验/OKR|OKR]]
    *   [[../数据分析与实验/A_B 测试|A/B 测试]]
    *   [[../数据分析与实验/漏斗分析|漏斗分析]]
    *   [[../数据分析与实验/用户分群|同期群分析]]
    *   [[../数据分析与实验/数据指标体系|数据指标体系]]
    *   [[../产品设计/RICE 模型|RICE 模型]]
    *   [[估算能力]]
    *   [[统计学基础]]
    *   [[../../Interview Simulation/Product Manager Interview/技巧与方法/STAR 原则|STAR 原则]] (Result 量化)
""")

# Concepts/Product Management/用户研究
user_research_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '用户研究')

user_interview_path = os.path.join(user_research_folder, '用户访谈.md')
user_interview_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, process/user_research, type/qualitative_method, skill/user_research]
    aliases: [User Interview, 用户访谈方法]
    ---
    # 用户访谈 (User Interview)

    [[00 - 用户研究概览|返回 用户研究概览]]

    ## 概述

    用户访谈是一种核心的**定性[[00 - 用户研究概览|用户研究]]方法**，通过与目标用户进行**一对一的对话**，深入了解他们的**需求、[[../基础概念/痛点|痛点]]、动机、行为、态度以及使用特定产品或服务的体验**。

    与[[问卷调查]]等定量方法不同，用户访谈更侧重于**深入理解“为什么”**，挖掘用户行为背后的深层原因和潜在需求，获取丰富、生动的细节信息。它是探索性研究、需求挖掘、[[../基础概念/用户画像|用户画像]]构建以及[[../产品设计/可用性|可用性]]问题探究的重要手段。

    ## 用户访谈的目标

    *   **探索用户需求与[[../基础概念/痛点|痛点]]**: 发现用户未被满足的需求和在特定场景下遇到的困难。
    *   **理解用户行为与动机**: 了解用户为什么会做出某种行为？驱动他们决策的因素是什么？
    *   **验证产品假设**: 验证关于用户需求、行为或对某个产品概念的早期假设。
    *   **获取产品反馈**: 了解用户对现有产品或原型的使用体验、满意度和改进建议。
    *   **构建[[../基础概念/用户画像|用户画像]]**: 收集构建典型用户画像所需的素材和细节。
    *   **了解[[用户场景]]**: 深入理解用户在真实世界中使用产品的情境。

    ## 用户访谈的类型

    *   **探索性访谈 (Exploratory Interview)**: 在项目早期进行，目标是广泛了解用户需求、痛点和市场机会，定义问题空间。问题通常非常开放。
    *   **验证性访谈 (Validation Interview)**: 用于验证特定的产品概念、设计方案或[[../产品战略与规划/价值主张|价值主张]]假设。
    *   **[[../产品设计/可用性|可用性]]访谈 (Usability Interview)**: 通常结合[[../用户研究/可用性测试|可用性测试]]进行，在用户完成任务后，深入了解他们遇到的困难、困惑点以及操作思路。
    *   **客户访谈 (Customer Interview)**: 更广泛的概念，可能包含销售、客户成功等目的，但也可用于产品研究。

    ## 用户访谈的流程

    1.  **明确访谈目标 (Define Objectives)**: 清晰定义本次访谈想要了解的核心问题是什么。
    2.  **确定目标用户 (Identify Target Users)**: 根据研究目标，筛选符合[[../基础概念/用户画像|目标用户画像]]特征的访谈对象。
    3.  **设计访谈提纲 (Design Interview Guide)**:
        *   准备一个半结构化的访谈提纲，包含主要问题和追问方向，但保持灵活性。
        *   问题应以**开放式问题**为主（“你通常是如何...?” “能具体讲讲上次...的经历吗？” “你对...有什么看法？”），避免诱导性问题和是非题。
        *   问题顺序通常从**宽泛到具体**，从**背景信息到核心问题**。
        *   包含开场白（介绍自己、目的、保密性、时长、征求同意录音等）和结束语（感谢、询问是否有其他问题）。
    4.  **招募访谈对象 (Recruit Participants)**: 通过用户库、社交媒体、推荐、第三方平台等渠道招募用户。可能需要提供一定的激励（如礼品卡）。
    5.  **执行访谈 (Conduct Interview)**:
        *   **营造轻松氛围**: 让用户感到舒适、放松。
        *   **[[../核心技能/积极倾听|积极倾听]]**: 80% 的时间听，20% 的时间问。鼓励用户多说。
        *   **保持中立**: 不要评判用户的回答，避免表露个人倾向。
        *   **适时追问**: 对感兴趣的点或模糊不清的地方进行追问（“能再多告诉我一些关于...吗？” “当时你的感受是怎样的？”）。
        *   **控制时间**: 按照预定时间进行，尊重用户的时间。
        *   **记录**: 通过录音（需征得同意）和笔记记录关键信息。最好有专门的记录员。
    6.  **整理与分析 (Synthesize & Analyze)**:
        *   访谈结束后尽快整理笔记和录音。
        *   将多个访谈的信息进行汇总、编码、归类（例如使用[[亲和图法]]）。
        *   寻找**模式 (Patterns)**、**共同点 (Common Themes)** 和 **异常点 (Outliers)**。
        *   提炼**关键洞察 (Key Insights)**。
    7.  **产出报告 (Report Findings)**: 将访谈目标、过程、主要发现、洞察和建议总结成报告，与团队分享。可以使用[[../基础概念/用户画像|用户画像]]、[[用户旅程图]]等形式呈现结果。

    ## 用户访谈的技巧

    *   **建立融洽关系 (Build Rapport)**: 开场时进行简单的寒暄，让用户放松。
    *   **从“过去”问起**: 询问用户过去实际发生的具体经历，而不是假设性的未来行为（人们不擅长预测自己）。
    *   **关注行为而非观点**: “你是怎么做的？”通常比“你喜欢什么？”更有价值。
    *   **鼓励[[../核心技能/讲故事能力|讲故事]]**: 让用户分享具体的场景和细节。
    *   **拥抱沉默**: 短暂的沉默可能意味着用户在思考，不要急于填补空白。
    *   **保持好奇心**: 对用户的回答保持真诚的好奇。
    *   **注意非语言信号**: 观察用户的表情和肢体语言。

    ## 优点与缺点

    *   **优点**:
        *   **深度洞察**: 能获取丰富、深入的定性信息，理解“为什么”。
        *   **灵活性**: 可以根据用户的回答调整问题和方向。
        *   **发现意外**: 可能发现意想不到的需求或问题。
        *   **建立用户连接**: 与用户建立更直接的联系。
    *   **缺点**:
        *   **样本量小**: 结果难以推广到全体用户，不具统计代表性。
        *   **耗时耗力**: 招募、执行、分析都需要投入较多时间和精力。
        *   **主观性**: 结果的解读可能受到访谈者主观因素的影响。
        *   **用户偏见**: 用户可能因为记忆偏差、社交期望等因素提供不完全准确的信息。

    ## 总结

    用户访谈是产品经理深入理解用户的有力武器。通过掌握访谈的流程和技巧，你可以获得宝贵的定性洞察，为产品决策提供坚实的基础。在面试中，能够清晰阐述你进行用户访谈的经验和从中获得的洞察，是展现你用户中心思维和研究能力的重要方式。

    ## 相关概念

    *   [[00 - 用户研究概览|用户研究]]
    *   [[定性研究]]
    *   [[../基础概念/用户画像|用户画像]]
    *   [[../基础概念/痛点|痛点]]
    *   [[用户场景]]
    *   [[5 Whys]]
    *   [[访谈提纲]]
    *   [[../核心技能/积极倾听|积极倾听]]
    *   [[../核心技能/提问技巧|提问技巧]]
    *   [[../产品设计/可用性|可用性测试]] (访谈是其中一部分)
    *   [[../完整框架/02 - 用户需求分析|用户需求分析]]
""")

# Concepts/Product Management/开发流程
dev_process_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '开发流程')

product_owner_path = os.path.join(dev_process_folder, '产品负责人 (Product Owner).md')
product_owner_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, concept/product_owner, type/role, framework/scrum]
    aliases: [Product Owner, PO]
    ---
    # 产品负责人 (Product Owner - PO)

    [[Scrum|返回 Scrum 框架]]

    ## 概述

    产品负责人 (Product Owner, PO) 是 **[[Scrum]] 团队**中的一个核心角色。PO 的主要职责是**最大化产品价值**，这些价值是由 [[开发团队 (Development Team)]] 开发出来的。PO 是产品[[../开发流程/产品待办列表|产品待办列表 (Product Backlog)]] 的**唯一负责人**，负责定义、排序和沟通产品需求。

    PO 需要代表**所有[[../沟通协作/利益相关者管理|利益相关者]]（包括用户、客户、业务方等）**的声音，并确保 [[Scrum]] 团队的工作与[[../基础概念/产品愿景|产品愿景]]和[[../产品战略与规划/产品战略|业务目标]]保持一致。

    *注意：在实践中，产品经理 (Product Manager) 常常会承担 [[Scrum]] 团队中产品负责人的角色，但两者的职责范围和侧重点可能略有不同。PM 可能更关注长期的[[../产品战略与规划/产品战略|产品战略]]、[[../市场与行业分析/市场定位|市场定位]]和业务增长，而 PO 更聚焦于具体的 [[Sprint]] 交付和 [[产品待办列表]] 管理。然而，在很多公司，这两个角色是合一的。*

    ## 产品负责人的主要职责

    根据 《[[Scrum 指南]]》，产品负责人的职责主要包括：

    1.  **制定和清晰地沟通[[../开发流程/产品目标|产品目标 (Product Goal)]]**:
        *   定义产品的长期目标和[[../基础概念/产品愿景|愿景]]。
        *   确保 [[Scrum]] 团队和[[../沟通协作/利益相关者管理|利益相关者]]都理解产品目标。
    2.  **创建和清晰地沟通[[产品待办列表项|产品待办列表项 (Product Backlog Items)]]**:
        *   将用户需求、功能、改进、修复等转化为清晰、可理解的[[产品待办列表项]]（通常是[[../用户研究/用户故事|用户故事]]）。
        *   确保每个列表项都包含足够的信息，以便[[开发团队 (Development Team)]]能够理解和实现。
    3.  **对[[产品待办列表项]]进行排序 (Ordering Product Backlog Items)**:
        *   根据[[../产品战略与规划/价值主张|用户价值]]、业务优先级、[[../技术相关/技术依赖|依赖关系]]、[[../技术相关/风险管理|风险]]、[[../开发流程/工作量估算|工作量]]等因素，对[[产品待办列表项]]进行排序。
        *   确保[[开发团队 (Development Team)]]始终在开发最高价值的功能。这是 PO **最核心**的职责之一。常用的排序方法参见[[../产品设计/功能优先级排序|功能优先级排序]]。
    4.  **确保[[产品待办列表]]是透明、可见和可理解的 (Ensuring Transparency, Visibility, and Understanding)**:
        *   [[产品待办列表]]应该是动态的、对所有[[../沟通协作/利益相关者管理|利益相关者]]可见的。
        *   PO 需要清晰地向团队解释列表项的内容和排序理由。

    ## 产品负责人需要具备的能力

    *   **领域知识 (Domain Knowledge)**: 深入理解产品所处的行业、市场和用户。
    *   **[[../产品战略与规划/产品战略|战略思维]]**: 能够制定[[../基础概念/产品愿景|产品愿景]]和[[../产品战略与规划/产品战略|战略]]，并将其分解为可执行的步骤。
    *   **[[../核心技能/决策能力|决策能力]]**: 能够在复杂和不确定的情况下，基于[[../产品战略与规划/价值主张|价值]]和[[../数据分析与实验/数据驱动决策|数据]]做出艰难的优先级决策。
    *   **[[../核心技能/沟通技巧|沟通与协作能力]]**: 能够清晰地与[[开发团队 (Development Team)]]、[[Scrum Master]]、[[../沟通协作/利益相关者管理|利益相关者]]等进行有效沟通，建立良好关系。
    *   **[[../核心技能/影响力|影响力与谈判能力]]**: 能够在没有直接管理权的情况下，说服他人，平衡各方需求。
    *   **[[../开发流程/敏捷开发|敏捷思维]]**: 理解并践行敏捷价值观和原则。

    ## 产品负责人与其他角色的协作

    *   **与[[开发团队 (Development Team)]]**:
        *   澄清需求，回答问题。
        *   参与[[../开发流程/Sprint 计划会|Sprint 计划会]]，解释[[产品待办列表项]]，共同设定 [[Sprint 目标]]。
        *   参与[[../开发流程/Sprint 评审会|Sprint 评审会]]，检视产品增量，提供反馈。
        *   尊重开发团队对技术实现和工作量估算的专业判断。
    *   **与[[Scrum Master]]**:
        *   协作确保 [[Scrum]] 流程顺畅。
        *   [[Scrum Master]] 帮助 PO 理解和使用 [[Scrum]]，辅导 PO 如何有效管理[[产品待办列表]]。
    *   **与[[../沟通协作/利益相关者管理|利益相关者]]**:
        *   收集需求和反馈。
        *   沟通[[../产品战略与规划/产品路线图|产品路线图]]和发布计划。
        *   管理[[../沟通协作/期望管理|期望]]。
        *   演示产品进展（如在[[../开发流程/Sprint 评审会|Sprint 评审会]]上）。

    ## 总结

    产品负责人是 [[Scrum]] 团队中至关重要的角色，对产品的成功负有最终责任。PO 通过有效管理[[产品待办列表]]，确保团队始终聚焦于交付最高价值的产品增量。要成为一名优秀的 PO，需要具备深厚的领域知识、强大的决策能力和卓越的沟通协作技巧。

    ## 相关概念

    *   [[Scrum]]
    *   [[敏捷开发]]
    *   [[产品待办列表 (Product Backlog)]]
    *   [[Sprint]]
    *   [[Sprint 目标]]
    *   [[产品目标 (Product Goal)]]
    *   [[用户故事]]
    *   [[功能优先级排序]]
    *   [[开发团队 (Development Team)]]
    *   [[Scrum Master]]
    *   [[利益相关者管理]]
    *   [[产品经理 (Product Manager)]] (与 PO 的关系)
""")

product_backlog_path = os.path.join(dev_process_folder, '产品待办列表 (Product Backlog).md')
product_backlog_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, concept/product_backlog, type/artifact, framework/scrum]
    aliases: [Product Backlog, 产品待办事项列表, PB]
    ---
    # 产品待办列表 (Product Backlog)

    [[Scrum|返回 Scrum 框架]]

    ## 概述

    产品待办列表 (Product Backlog) 是 [[Scrum]] 框架中的核心**工件 (Artifact)** 之一。它是一个**有序的、动态的需求列表**，包含了所有已知的产品需求，也是产品未来所有可能改动的**唯一来源**。

    这个列表包含了各种类型的待办列表项 (Product Backlog Items, PBI)，例如：
    *   **新功能 (New Features)**
    *   **功能改进 (Enhancements)**
    *   **缺陷修复 (Bug Fixes)**
    *   **技术工作 (Technical Debt / Infrastructure)**
    *   **知识获取 (Spikes / Research)**

    **[[产品负责人 (Product Owner)]] 对产品待办列表的内容、可用性和排序负有全部责任。**

    ## 产品待办列表的特征 (DEEP)

    一个好的产品待办列表通常具备 DEEP 特征：

    *   **D - Detailed Appropriately (适当详细)**: 优先级高的 PBI（近期要做的）应该包含足够的细节，以便 [[开发团队 (Development Team)]] 能够理解和开发；优先级低的 PBI（远期才做的）可以比较粗略。
    *   **E - Estimated (经过估算)**: [[开发团队 (Development Team)]] 会对 PBI 的[[工作量估算|工作量]]（通常使用[[故事点 (Story Points)]]）进行估算，这有助于 [[产品负责人 (Product Owner)]] 进行优先级排序和发布规划。
    *   **E - Emergent (动态涌现)**: 产品待办列表不是一成不变的。随着对产品、用户和市场的理解加深，新的 PBI 会不断涌现，现有的 PBI 可能被修改、移除或重新排序。它是一个“活文档”。
    *   **P - Prioritized (经过排序)**: **这是最重要的特征**。列表中的所有 PBI 都按照优先级进行了排序。[[产品负责人 (Product Owner)]] 根据[[../产品战略与规划/价值主张|价值]]、[[../技术相关/风险管理|风险]]、[[../技术相关/技术依赖|依赖关系]]、[[工作量估算|成本]]等因素进行排序，确保[[开发团队 (Development Team)]] 始终在处理最高优先级的 PBI。

    ## 产品待办列表项 (PBI)

    产品待办列表由一系列的产品待办列表项 (PBI) 组成。PBI 通常包含以下信息：

    *   **描述 (Description)**: 清晰地描述需求是什么。常用的格式是[[../用户研究/用户故事|用户故事]] (“作为一个[角色], 我想要[做某事], 以便[获得某种价值]”)。
    *   **顺序 (Order)**: PBI 在列表中的位置，反映其优先级。
    *   **估算 (Estimate)**: [[开发团队 (Development Team)]] 估算的工作量（如[[故事点 (Story Points)]]）。
    *   **价值 (Value)**: （可选）对业务或用户的价值评估。
    *   **(可选) [[验收标准 (Acceptance Criteria)]]**: 定义 PBI 完成的标准，以便测试和验收。

    ## 产品待办列表梳理 (Product Backlog Refinement)

    产品待办列表梳理（也称为 Backlog Grooming）是一个**持续进行**的活动，[[产品负责人 (Product Owner)]] 和 [[开发团队 (Development Team)]] 会定期（通常占用 [[Sprint]] 中 5-10% 的时间）一起：

    *   **评审和讨论** 即将到来的 PBI。
    *   **澄清需求**，添加细节。
    *   **拆分** 过大的 PBI（例如 [[史诗 (Epic)]] 分解为更小的[[../用户研究/用户故事|用户故事]]）。
    *   **估算** 新的或修改后的 PBI。
    *   **重新排序** PBI。

    这个活动确保了产品待办列表始终处于良好状态 (DEEP)，为后续的 [[Sprint 计划会]]做好准备。

    ## 产品待办列表与 [[Sprint 待办列表 (Sprint Backlog)]]

    *   **产品待办列表 (Product Backlog)**: 包含**所有**已知的产品需求，是产品的长期需求池，由 [[产品负责人 (Product Owner)]] 负责。
    *   **[[Sprint 待办列表 (Sprint Backlog)]]**: 包含为**当前 Sprint** 选定的 PBI 以及交付这些 PBI 所需的任务计划。它是 [[开发团队 (Development Team)]] 在一个 Sprint 内的工作计划，由 [[开发团队 (Development Team)]] 负责管理。

    在 [[Sprint 计划会]]上，[[开发团队 (Development Team)]] 从产品待办列表的顶部选择最高优先级的 PBI，并将其放入 [[Sprint 待办列表 (Sprint Backlog)]] 中。

    ## 总结

    产品待办列表是 [[Scrum]] 框架的核心，是连接[[../基础概念/产品愿景|产品愿景]]与开发执行的桥梁。[[产品负责人 (Product Owner)]] 通过持续维护一个排序良好、细节适当、动态更新的产品待办列表，来指导 [[开发团队 (Development Team)]] 最大化产品价值的交付。

    ## 相关概念

    *   [[Scrum]]
    *   [[工件 (Artifact)]]
    *   [[产品负责人 (Product Owner)]]
    *   [[开发团队 (Development Team)]]
    *   [[产品待办列表项 (PBI)]]
    *   [[用户故事]]
    *   [[功能优先级排序]]
    *   [[工作量估算]]
    *   [[故事点 (Story Points)]]
    *   [[产品待办列表梳理 (Refinement)]]
    *   [[Sprint 待办列表 (Sprint Backlog)]]
    *   [[Sprint 计划会]]
    *   [[DEEP 原则]]
""")

# Concepts/Product Management/核心技能
core_skills_folder = os.path.join(TARGET_ROOT_DIRECTORY, 'Concepts', 'Product Management', '核心技能')

conflict_resolution_path = os.path.join(core_skills_folder, '冲突解决.md')
conflict_resolution_content = textwrap.dedent("""\
    ---
    tags: [topic/product_management, skill/conflict_resolution, type/soft_skill, skill/communication, skill/collaboration]
    aliases: [Conflict Resolution, 冲突管理]
    ---
    # 冲突解决 (Conflict Resolution)

    [[../沟通协作/沟通技巧|返回 沟通技巧]]

    ## 概述

    冲突在团队协作和产品开发过程中是**不可避免**的，甚至在某种程度上是**健康的**（如果处理得当）。不同背景、不同角色的成员（如产品、设计、开发、测试、运营等）对于目标、优先级、方案、资源分配等问题持有不同观点是很自然的。

    冲突解决是指**识别、处理和化解这些分歧和矛盾，以达成建设性结果**的过程。对于产品经理来说，具备良好的冲突解决能力至关重要，因为他们经常处于协调各方、平衡需求的中心位置。有效的冲突管理能够：

    *   防止分歧升级为破坏性对抗。
    *   促进更深入的理解和更好的决策。
    *   增强团队信任和凝聚力。
    *   推动项目顺利进行。

    ## 冲突的常见来源 (产品管理)

    *   **目标不一致**: 不同部门或个人对产品目标、[[../数据分析与实验/KPI|KPI]] 的理解或侧重不同。
    *   **优先级分歧**: 对于[[../产品设计/功能优先级排序|哪些功能应该先做]]存在不同看法。
    *   **方案争议**: 对某个功能的设计方案、技术实现方案有不同意见（例如：[[../沟通协作/STAR 原则|STAR 示例]]中的设计 vs. 前端冲突）。
    *   **资源争夺**: 有限的开发时间、人力、预算等资源的分配。
    *   **角色与职责不清**: 团队成员对各自的职责范围存在模糊或重叠。
    *   **沟通不畅**: 信息不对称、误解导致矛盾。
    *   **个性差异**: 不同成员的工作风格、沟通方式或个性冲突。

    ## 冲突解决的策略/风格 (Thomas-Kilmann 模型)

    Kenneth Thomas 和 Ralph Kilmann 提出了五种常见的冲突处理风格，基于两个维度：**坚持自我 (Assertiveness)** 和 **合作性 (Cooperativeness)**。

    ```mermaid
    graph TD
        subgraph "冲突处理风格 (Thomas-Kilmann)"
            direction TB
            YAxis["坚持自我<br/>(Assertiveness)<br/>高"] --> YAxisLow["低"];
            XAxisLow["合作性<br/>(Cooperativeness)<br/>低"] --> XAxis["高"];

            A(回避 (Avoiding)<br/>低坚持/低合作<br/>推迟/忽视) -- XAxisLow --> B(迁就 (Accommodating)<br/>低坚持/高合作<br/>牺牲自己满足对方);
            C(竞争 (Competing)<br/>高坚持/低合作<br/>坚持己见/赢输) -- XAxisLow --> D(协作 (Collaborating)<br/>高坚持/高合作<br/>共同寻找双赢);
            E(妥协 (Compromising)<br/>中坚持/中合作<br/>各让一步/折中)

            A -- YAxisLow --> C;
            B -- YAxisLow --> D;
            E -- "中/中" --> CenterPoint;


            style A fill:#eee,stroke:#333
            style B fill:#ccf,stroke:#333
            style C fill:#fcc,stroke:#333
            style D fill:#cfc,stroke:#333
            style E fill:#ffc,stroke:#333
            style CenterPoint fill:none, stroke:none

            linkStyle default stroke-width:0px;
        end

    ```

    1.  **竞争 (Competing)**: 高坚持，低合作。坚持自己的立场，力求说服对方，追求“赢”。适用于需要快速决策或原则性问题。风险：可能损害关系。
    2.  **协作 (Collaborating)**: 高坚持，高合作。积极与对方合作，深入挖掘双方需求，共同寻找满足双方利益的“[[双赢 (Win-Win)]]”解决方案。最理想但最耗时。适用于重要且复杂的问题。
    3.  **妥协 (Compromising)**: 中等坚持，中等合作。双方各让一步，寻求一个折中的、双方都能接受的方案。适用于时间有限或暂时无法找到完美方案的情况。风险：可能双方都不完全满意。
    4.  **回避 (Avoiding)**: 低坚持，低合作。选择暂时搁置争议、推迟处理或完全忽视冲突。适用于问题不重要、时机不合适或需要时间冷静的情况。风险：问题可能恶化。
    5.  **迁就 (Accommodating)**: 低坚持，高合作。牺牲自己的需求去满足对方。适用于维护关系更重要、自己不太在意结果或认识到自己错误的情况。风险：可能被利用，长期可能导致不满。

    **没有绝对好坏的风格，需要根据具体情况（问题重要性、时间压力、关系重要性、对方风格等）灵活选择。** 但通常来说，**协作 (Collaborating)** 是最理想的、能带来最佳长期效果的策略。

    ## 冲突解决的步骤 (通用)

    1.  **识别与承认冲突**: 意识到冲突的存在，并承认其需要被处理。不要忽视或回避。
    2.  **创造沟通环境**: 找到一个合适的时间和地点，确保相关方都能参与，营造一个开放、安全、尊重的沟通氛围。
    3.  **倾听与理解各方**: 让每一方都有机会陈述自己的观点、理由、感受和诉求。运用[[../核心技能/积极倾听|积极倾听]]技巧，确保真正理解对方的立场和背后的需求（区分立场 Position 和利益 Interest）。
    4.  **明确核心问题**: 共同定义冲突的真正焦点是什么？要解决的核心问题是什么？
    5.  **寻找共同目标**: 强调团队的共同目标或[[../基础概念/产品愿景|愿景]]，将冲突从“你对我”转变为“我们共同面对问题”。
    6.  **探索解决方案**: 鼓励各方提出可能的解决方案。进行头脑风暴，不要过早评判。
    7.  **评估与选择方案**: 共同评估各种方案的优劣势，选择一个最能满足各方核心需求、最符合共同目标的方案（理想是[[双赢 (Win-Win)]]方案）。可能需要[[../核心技能/谈判技巧|谈判]]和[[妥协]]。
    8.  **确认与执行**: 明确最终达成的协议和下一步行动计划，确保各方都理解并承诺执行。
    9.  **跟进与评估**: 后续跟进执行情况，评估解决方案的效果，必要时进行调整。

    ## 总结

    冲突是协作的常态，有效的冲突解决是产品经理推动工作、建立信任、促进团队成长的关键能力。掌握不同的冲突处理风格和解决步骤，能够在面对分歧时保持冷静、积极应对，将潜在的障碍转化为达成共识、优化方案的机会。

    ## 相关概念

    *   [[../沟通协作/沟通技巧|沟通技巧]]
    *   [[../核心技能/积极倾听|积极倾听]]
    *   [[../核心技能/谈判技巧|谈判技巧]]
    *   [[双赢 (Win-Win)]]
    *   [[妥协]]
    *   [[../沟通协作/利益相关者管理|利益相关者管理]]
    *   [[../沟通协作/跨职能团队|跨职能团队]]
    *   [[团队协作]]
    *   [[情商 (Emotional Intelligence)]]
""")


# --- Main Script Logic ---
def main():
    print("Starting Obsidian Knowledge Base Generation (Part 4 - Skills & Core Concepts)...")
    print(f"Target Root Directory: {os.path.abspath(TARGET_ROOT_DIRECTORY)}")
    print(f"Overwrite Existing Files: {OVERWRITE_EXISTING}")

    # Files prioritized by user request and interview relevance
    files_to_create = {
        # Interview Skills (as requested)
        behavioral_interview_questions_path: behavioral_interview_questions_content,
        # Core Skills (as requested and relevant)
        storytelling_path: storytelling_content,
        communication_skills_path: communication_skills_content,
        quantitative_thinking_path: quantitative_thinking_content,
        conflict_resolution_path: conflict_resolution_content, # Added as a core communication/collaboration skill
        # Core User Research Concept
        user_interview_path: user_interview_content,
        # Core Agile Concepts
        product_owner_path: product_owner_content,
        product_backlog_path: product_backlog_content,

    }

    # Create necessary base directories if they don't exist
    os.makedirs(interview_skills_folder, exist_ok=True)
    os.makedirs(core_skills_folder, exist_ok=True)
    os.makedirs(user_research_folder, exist_ok=True)
    os.makedirs(dev_process_folder, exist_ok=True)

    print("Base directories ensured.")

    for filepath, content in files_to_create.items():
        if not OVERWRITE_EXISTING and os.path.exists(filepath):
            print(f"Skipping existing file: {filepath}")
            continue
        write_file(filepath, content)

    print("\nObsidian Knowledge Base Generation (Part 4) Complete.")

if __name__ == "__main__":
    main()
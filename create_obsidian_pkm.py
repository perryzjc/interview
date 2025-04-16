import os
import textwrap

# --- Configuration ---
# Define the root directory where the script should create folders and files.
# '.' means the current directory where the script is run.
# Adjust this if you want to run it from a different base location.
ROOT_DIR = '.'

# --- Notes Data ---
# Dictionary mapping file paths (relative to ROOT_DIR) to their Markdown content.
# Uses os.path.join for cross-platform compatibility.
# Content is in Chinese and utilizes Obsidian features.

notes_data = {
    # --- Product Management Core Concepts ---
    os.path.join("Concepts", "Product Management", "00 - Product Management Overview.md"): textwrap.dedent("""\
        ---
        tags: [product-management, overview, core-concept]
        aliases: [产品管理, PM]
        ---
        # 產品管理核心概念 (Product Management Core Concepts)

        > [!info] 定义 (Definition)
        > 產品管理是組織內的一個職能，負責產品或產品線的整體成功，從策略制定到市場發布及後續迭代。它連接了業務、技術和用戶體驗 (UX)。

        ## 核心職責 (Core Responsibilities)

        產品經理通常負責以下關鍵領域：

        - **[[03 - Product Strategy|產品策略]]**: 定義產品的願景、目標市場和長期方向。
        - **[[04 - Roadmapping|產品路線圖]]**: 規劃產品的發展路徑和功能發布順序。
        - **[[02 - User Research/User Research Overview|用戶研究]]**: 理解用戶需求、痛點和行為。
        - **[[05 - Prioritization/Prioritization Overview|優先級排序]]**: 決定開發哪些功能以及何時開發。
        - **[[06 - Product Metrics/Product Metrics Overview|產品指標]]**: 定義、追踪和分析產品成功的關鍵指標。
        - **[[07 - Go-to-Market Strategy|上市策略]]**: 規劃和執行產品發布。
        - **[[08 - Stakeholder Management|干系人管理]]**: 與工程、設計、市場、銷售、法務等團隊協調溝通。
        - **[[01 - Product Lifecycle|產品生命週期]]**: 管理產品從概念到退市的整個過程。

        ## 主要知識領域 (Key Knowledge Areas)

        ```mermaid
        graph TD
            A(產品管理) --> B(產品策略);
            A --> C(用戶研究);
            A --> D(產品路線圖);
            A --> E(優先級排序);
            A --> F(產品指標);
            A --> G(上市策略);
            A --> H(干系人管理);
            A --> I(產品生命週期);

            C --> C1(用戶訪談);
            C --> C2(問卷調查);
            C --> C3(可用性測試);

            E --> E1(RICE模型);
            E --> E2(MoSCoW方法);
            E --> E3(Kano模型);

            F --> F1(北極星指標);
            F --> F2(AARRR模型);

            style A fill:#f9f,stroke:#333,stroke-width:2px
        ```

        > [!tip] 延伸閱讀
        > 探索以上每個連結，深入了解各個具體概念。這個知識庫旨在模塊化，方便你按需學習。
        """),

    os.path.join("Concepts", "Product Management", "01 - Product Lifecycle.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, product-lifecycle]
        aliases: [產品生命週期]
        ---
        # 產品生命週期 (Product Lifecycle)

        > [!info] 定义 (Definition)
        > 產品生命週期描述了一個產品從引入市場到最終退出市場的各個階段。理解這些階段有助於制定相應的策略。

        ## 主要階段 (Key Stages)

        ```mermaid
        graph LR
            A[導入期 (Introduction)] --> B(成長期 (Growth));
            B --> C(成熟期 (Maturity));
            C --> D(衰退期 (Decline));

            subgraph 產品生命週期
                direction LR
                A
                B
                C
                D
            end

            style A fill:#cde4ff
            style B fill:#baffc9
            style C fill:#ffffba
            style D fill:#ffb3ba
        ```

        1.  **導入期 (Introduction)**:
            -   新產品推向市場，銷售額低，成本高。
            -   重點：建立市場認知，吸引早期採用者。
            -   相關策略：[[07 - Go-to-Market Strategy|上市策略]]。
        2.  **成長期 (Growth)**:
            -   市場接受度提高，銷售額快速增長，利潤開始出現。
            -   重點：擴大市場份額，建立品牌偏好，應對競爭。
            -   相關策略：功能迭代，渠道擴展。
        3.  **成熟期 (Maturity)**:
            -   銷售額達到頂峰並趨於穩定，市場飽和，競爭激烈。
            -   重點：維持市場份額，差異化，提高效率。
            -   相關策略：優化現有功能，探索細分市場。
        4.  **衰退期 (Decline)**:
            -   銷售額和利潤下降，市場萎縮。
            -   重點：決定是維持、收割還是退出產品。
            -   相關策略：成本控制，產品線簡化。

        > [!tip] 注意
        > 並非所有產品都嚴格遵循此模型，週期長度也因產品和市場而異。

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[03 - Product Strategy|產品策略]]
        """),

    # --- User Research ---
    os.path.join("Concepts", "Product Management", "02 - User Research", "User Research Overview.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, user-research]
        aliases: [用戶研究]
        ---
        # 用戶研究概述 (User Research Overview)

        > [!info] 定义 (Definition)
        > 用戶研究是系統性地了解目標用戶及其需求、行為、動機和痛點的過程。它是以用戶為中心設計的基礎。

        ## 為何重要 (Why is it Important?)

        -   **驗證假設**: 減少基於猜測的決策。
        -   **發現需求**: 找到未被滿足的用戶需求和機會點。
        -   **提升用戶體驗**: 設計出更易用、更有價值的產品。
        -   **降低風險**: 避免開發沒人要的功能或產品。

        ## 主要方法 (Key Methods)

        用戶研究方法多種多樣，可以分為定性和定量兩大類：

        -   **定性研究 (Qualitative)**: 深入理解“為什麼”和“怎麼樣”。
            -   [[User Interviews|用戶訪談]]
            -   [[Usability Testing|可用性測試]]
            -   焦點小組 (Focus Groups)
            -   實境調查 (Ethnographic Studies)
        -   **定量研究 (Quantitative)**: 用數據衡量“多少”和“多頻繁”。
            -   [[Surveys|問卷調查]]
            -   A/B 測試 (A/B Testing)
            -   網站/應用分析 (Analytics)

        > [!example] 如何選擇方法?
        > - 探索早期概念或深入理解動機 -> [[User Interviews|用戶訪談]]
        > - 評估現有設計的易用性 -> [[Usability Testing|可用性測試]]
        > - 收集大量用戶的意見或偏好 -> [[Surveys|問卷調查]]

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[05 - Prioritization/Prioritization Overview|優先級排序]] (用戶研究的發現是排序的重要輸入)
        """),

    os.path.join("Concepts", "Product Management", "02 - User Research", "User Interviews.md"): textwrap.dedent("""\
        ---
        tags: [product-management, user-research, qualitative-method]
        aliases: [用戶訪談]
        ---
        # 用戶訪談 (User Interviews)

        > [!info] 定义 (Definition)
        > 用戶訪談是一種定性研究方法，通過與用戶進行一對一的對話，深入了解他們的經驗、態度、需求和痛點。

        ## 目標 (Goals)

        -   探索用戶行為背後的動機。
        -   驗證或推翻關於用戶需求的假設。
        -   發現未預期的見解和機會。
        -   建立用戶畫像 (Personas)。

        ## 最佳實踐 (Best Practices)

        -   **明確目標**: 每次訪談前確定你想了解的核心問題。
        -   **開放式問題**: 多問 "How", "Why", "Tell me about..."，避免引導性問題。
        -   **積極傾聽**: 不僅聽用戶說什麼，還要觀察他們的語氣和肢體語言。
        -   **保持中立**: 不要評判用戶的回答。
        -   **記錄**: 錄音（經同意）並做筆記。
        -   **尋找模式**: 訪談結束後，整理筆記，尋找跨多個訪談的共同主題。

        > [!warning] 常見陷阱
        > - 不要問用戶他們想要什麼功能 (他們通常不知道或說不清)。要問他們遇到的問題和現在是如何解決的。
        > - 不要只訪談“喜歡”你產品的用戶。

        ---
        關聯概念: [[User Research Overview|用戶研究概述]], [[Usability Testing|可用性測試]] (訪談常用於測試前後)
        """),

    os.path.join("Concepts", "Product Management", "02 - User Research", "Surveys.md"): textwrap.dedent("""\
        ---
        tags: [product-management, user-research, quantitative-method]
        aliases: [問卷調查]
        ---
        # 問卷調查 (Surveys)

        > [!info] 定义 (Definition)
        > 問卷調查是一種定量研究方法，通過向大量用戶分發結構化的問卷來收集數據，了解用戶的偏好、態度、行為頻率等。

        ## 優點 (Pros)

        -   **規模化**: 可以快速觸達大量用戶。
        -   **量化數據**: 易於統計分析，發現趨勢。
        -   **成本相對較低**: 比一對一訪談成本低。

        ## 缺點 (Cons)

        -   **缺乏深度**: 難以理解“為什麼”。
        -   **設計挑戰**: 問題設計不當可能導致誤導性結果。
        -   **回答偏差**: 用戶可能不認真回答或提供社會期望的答案。

        ## 設計技巧 (Design Tips)

        -   **保持簡短**: 問題越少越好。
        -   **問題清晰**: 避免模糊或雙關語。
        -   **選項互斥且窮盡**: 對於選擇題。
        -   **從易到難**: 先問簡單的問題。
        -   **避免引導性問題**: 如 "您難道不喜歡我們的新功能嗎？"。
        -   **預測試 (Pilot Test)**: 在小範圍內測試問卷，發現問題。

        > [!example] 應用場景
        > - 測量用戶滿意度 (如 NPS - Net Promoter Score)。
        > - 了解功能使用頻率。
        > - 收集用戶基本信息。

        ---
        關聯概念: [[User Research Overview|用戶研究概述]], [[06 - Product Metrics/Product Metrics Overview|產品指標]] (NPS 就是一種通過問卷收集的指標)
        """),

    os.path.join("Concepts", "Product Management", "02 - User Research", "Usability Testing.md"): textwrap.dedent("""\
        ---
        tags: [product-management, user-research, qualitative-method, ux]
        aliases: [可用性測試]
        ---
        # 可用性測試 (Usability Testing)

        > [!info] 定义 (Definition)
        > 可用性測試是一種評估產品易用性的方法，通過觀察真實用戶在嘗試完成特定任務時遇到的問題。

        ## 目標 (Goals)

        -   **識別易用性問題**: 發現用戶在哪裡卡頓、困惑或犯錯。
        -   **評估任務完成率**: 用戶能否成功完成關鍵任務？
        -   **衡量效率**: 完成任務需要多長時間？
        -   **收集主觀反饋**: 用戶對使用體驗的感受如何？

        ## 測試流程 (Testing Process)

        1.  **定義目標和任務**: 明確要測試的產品部分和用戶需要完成的關鍵任務。
        2.  **招募參與者**: 尋找代表目標用戶群體的測試者 (通常5-8人就能發現大部分問題)。
        3.  **準備測試環境**: 設置好設備、原型或產品。
        4.  **執行測試**:
            -   向用戶解釋流程，強調測試的是產品而非用戶本人。
            -   讓用戶“放聲思考”(Think Aloud)。
            -   觀察用戶行為，記錄遇到的困難。
            -   主持人盡量少干預。
        5.  **分析結果**: 匯總觀察到的問題，按嚴重程度排序。

        > [!tip] 原型測試
        > 可用性測試可以在產品開發的任何階段進行，甚至在只有低保真原型時就可以開始，這樣可以及早發現問題，降低修改成本。

        ---
        關聯概念: [[User Research Overview|用戶研究概述]], [[User Interviews|用戶訪談]] (測試後常會進行簡短訪談)
        """),

    # --- Product Strategy ---
    os.path.join("Concepts", "Product Management", "03 - Product Strategy.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, strategy]
        aliases: [產品策略]
        ---
        # 產品策略 (Product Strategy)

        > [!info] 定义 (Definition)
        > 產品策略是一個高層次的計劃，描述了產品為實現業務目標將要達成什麼，以及如何達成。它為產品決策提供了框架和方向。

        ## 核心要素 (Key Components)

        一個好的產品策略通常包含：

        1.  **願景 (Vision)**:
            -   產品的長期目標和最終想要達到的狀態。
            -   回答：“我們為什麼要打造這個產品？”
        2.  **目標市場 (Target Audience)**:
            -   我們為誰解決問題？定義清晰的用戶畫像 (Personas)。
            -   相關：[[02 - User Research/User Research Overview|用戶研究]]
        3.  **要解決的問題 (Problems to Solve)**:
            -   產品旨在解決目標用戶的哪些核心痛點？
        4.  **目標與關鍵成果 (Objectives and Key Results - OKRs)**:
            -   如何衡量策略的成功？設定具體、可衡量的目標。
            -   相關：[[06 - Product Metrics/Product Metrics Overview|產品指標]]
        5.  **差異化與定位 (Differentiation & Positioning)**:
            -   我們的產品與競爭對手有何不同？獨特價值主張 (Unique Value Proposition - UVP) 是什麼？
        6.  **商業模式 (Business Model)**:
            -   產品如何創造收入和利潤？

        ## 策略 vs 路線圖 (Strategy vs. Roadmap)

        -   **策略 (Strategy)** 是 **Why** (為什麼做) 和 **What** (做什麼的核心目標)。
        -   **[[04 - Roadmapping|路線圖 (Roadmap)]]** 是 **How** (如何分步實現) 和 **When** (大致的時間規劃)。

        > [!tip] 策略是動態的
        > 市場和用戶需求不斷變化，產品策略也需要定期審視和調整。

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[04 - Roadmapping|產品路線圖]], [[01 - Product Lifecycle|產品生命週期]] (不同生命週期階段需要不同的策略)
        """),

    # --- Roadmapping ---
    os.path.join("Concepts", "Product Management", "04 - Roadmapping.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, planning, roadmap]
        aliases: [產品路線圖, Roadmap]
        ---
        # 產品路線圖 (Roadmapping)

        > [!info] 定义 (Definition)
        > 產品路線圖是一個高層次的視覺化計劃，溝通了產品的發展方向和隨時間推移的主要工作重點 (通常是主題或目標，而非具體功能列表)。

        ## 主要目的 (Key Purposes)

        -   **溝通策略**: 向 [[08 - Stakeholder Management|干系人]] (團隊、管理層、客戶等) 展示產品的 [[03 - Product Strategy|策略]] 和未來方向。
        -   **協調工作**: 幫助不同團隊 (開發、市場、銷售) 了解即將到來的工作，以便協調計劃。
        -   **指導優先級**: 作為 [[05 - Prioritization/Prioritization Overview|優先級排序]] 的依據，確保開發工作與策略一致。

        ## 常見類型 (Common Types)

        -   **基於目標的路線圖 (Goal-Oriented Roadmap)**: 側重於要實現的業務目標或用戶成果 (例如：提高用戶活躍度)。
        -   **基於主題的路線圖 (Theme-Based Roadmap)**: 圍繞高層次的主題組織工作 (例如：改善新手引導、提升性能)。
        -   **基於時間的路線圖 (Time-Based Roadmap)**: 按時間框架 (如季度) 劃分，標注大致的時間預期 (Now, Next, Later 是常見模式)。

        ```mermaid
        gantt
            dateFormat  YYYY-MM-DD
            title 產品路線圖示例 (基於時間)
            excludes    weekends

            section Q3 2024 (Now)
            用戶登錄優化     :a1, 2024-07-01, 30d
            數據分析基礎建設 :a2, 2024-07-15, 45d

            section Q4 2024 (Next)
            新功能模塊A探索  :b1, 2024-10-01, 60d
            性能瓶頸改善     :b2, 2024-10-20, 40d

            section Q1 2025 (Later)
            國際化支持       :c1, 2025-01-10, 90d
            合作夥伴集成     :c2, 2025-02-01, 75d
        ```

        > [!warning] 路線圖不是承諾
        > 路線圖應被視為方向指引，而非功能的精確交付日期承諾。它需要根據市場反饋、[[02 - User Research/User Research Overview|用戶研究]]發現和業務變化保持靈活性和調整空間。

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[03 - Product Strategy|產品策略]], [[05 - Prioritization/Prioritization Overview|優先級排序]]
        """),

    # --- Prioritization ---
    os.path.join("Concepts", "Product Management", "05 - Prioritization", "Prioritization Overview.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, prioritization]
        aliases: [優先級排序, 優先級]
        ---
        # 優先級排序概述 (Prioritization Overview)

        > [!info] 定义 (Definition)
        > 優先級排序是在資源有限（時間、人力、資金）的情況下，決定先做什麼、後做什麼、甚至不做什麼的過程。這是產品經理最關鍵也最具挑戰性的職責之一。

        ## 為何重要 (Why is it Important?)

        -   **聚焦價值**: 確保團隊時間投入到對用戶和業務最有價值的事情上。
        -   **資源優化**: 在限制條件下最大化產出。
        -   **策略對齊**: 保證開發工作符合 [[03 - Product Strategy|產品策略]] 和 [[04 - Roadmapping|路線圖]]。
        -   **管理預期**: 向 [[08 - Stakeholder Management|干系人]] 清晰地溝通決策依據。

        ## 常用框架 (Common Frameworks)

        沒有萬能的框架，通常需要結合多種方法和判斷：

        -   **[[RICE Framework|RICE 模型]]**: 基於 Reach (觸達), Impact (影響), Confidence (信心), Effort (投入) 進行量化評分。
        -   **[[MoSCoW Method|MoSCoW 方法]]**: 將需求分為 Must have, Should have, Could have, Won't have。
        -   **[[Kano Model|Kano 模型]]**: 從用戶滿意度角度區分基本需求、期望需求和興奮需求。
        -   **價值 vs 複雜度矩陣 (Value vs. Complexity Matrix)**: 簡單的二維矩陣，快速分類。
        -   **機會排序法 (Opportunity Scoring)**: 基於用戶對需求的重要性和滿意度打分。

        > [!tip] 輸入來源
        > 優先級排序的決策應基於多方面信息：
        > - [[02 - User Research/User Research Overview|用戶研究]] 的發現
        > - [[06 - Product Metrics/Product Metrics Overview|產品指標]] 數據
        > - 業務目標和 [[03 - Product Strategy|產品策略]]
        > - [[08 - Stakeholder Management|干系人]] 的輸入 (銷售、市場、客服等)
        > - 技術可行性和依賴關係
        > - 市場競爭分析

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[04 - Roadmapping|產品路線圖]], [[RICE Framework|RICE 模型]], [[MoSCoW Method|MoSCoW 方法]], [[Kano Model|Kano 模型]]
        """),

    os.path.join("Concepts", "Product Management", "05 - Prioritization", "RICE Framework.md"): textwrap.dedent("""\
        ---
        tags: [product-management, prioritization, framework, RICE]
        aliases: [RICE模型, RICE]
        ---
        # RICE 模型 (RICE Framework)

        > [!info] 定义 (Definition)
        > RICE 是一種量化的優先級排序框架，旨在通過評估四個維度來幫助決策：Reach (觸達), Impact (影響), Confidence (信心), 和 Effort (投入)。

        ## 計算公式 (Formula)

        ```
        RICE Score = (Reach * Impact * Confidence) / Effort
        ```

        ## 四個維度 (The Four Factors)

        1.  **Reach (觸達範圍)**:
            -   這個功能/項目在一定時間內會影響多少用戶？
            -   *示例*: 每月影響 500 個用戶，Reach = 500。
            -   *度量*: 用戶數、交易數、試用轉化數等。

        2.  **Impact (影響程度)**:
            -   這個功能/項目對每個用戶的影響有多大？（通常對應產品目標，如提高轉化率、滿意度等）
            -   *評分*: 通常使用量級評分，例如：
                -   3 = 巨大影響 (massive impact)
                -   2 = 較大影響 (high impact)
                -   1 = 中等影響 (medium impact)
                -   0.5 = 較小影響 (low impact)
                -   0.25 = 微小影響 (minimal impact)

        3.  **Confidence (信心水平)**:
            -   你對 Reach 和 Impact 的估計有多大把握？（基於數據支撐、研究等）
            -   *評分*: 百分比形式：
                -   100% = 高度信心 (high confidence)
                -   80% = 中等信心 (medium confidence)
                -   50% = 低度信心 (low confidence)
                -   <50% = 猜測 (moonshot) - 需要更多研究

        4.  **Effort (投入成本)**:
            -   實現這個功能/項目需要多少資源？（通常指工程、設計等團隊投入的“人月”或“點數”）
            -   *評分*: 使用相對估算值，例如：
                -   0.5 = 非常小 (幾天)
                -   1 = 小 (1-2週)
                -   2 = 中 (1個月)
                -   3 = 大 (2個月)
                -   5 = 非常大 (一個季度)
            -   *注意*: Effort 在分母，投入越大，得分越低。

        ## 使用步驟 (How to Use)

        1.  列出所有待排序的功能/項目。
        2.  對每個項目，估算 R, I, C, E 四個值。
        3.  計算每個項目的 RICE 分數。
        4.  按 RICE 分數從高到低排序。

        > [!warning] RICE 不是絕對真理
        > - 分數是相對的，用於比較不同選項。
        > - 對於主觀評分 (Impact, Confidence)，需要團隊達成共識。
        > - 策略性項目或基礎設施項目可能得分不高，但仍然重要，需要額外考慮。

        ---
        關聯概念: [[Prioritization Overview|優先級排序概述]]
        """),

    os.path.join("Concepts", "Product Management", "05 - Prioritization", "MoSCoW Method.md"): textwrap.dedent("""\
        ---
        tags: [product-management, prioritization, framework, MoSCoW]
        aliases: [MoSCoW方法, MoSCoW]
        ---
        # MoSCoW 方法 (MoSCoW Method)

        > [!info] 定义 (Definition)
        > MoSCoW 是一種相對簡單的優先級排序方法，將需求或功能分為四個類別，常用於確定特定發布版本 (Release) 或時間盒 (Timebox) 內的範圍。

        ## 四個類別 (The Four Categories)

        1.  **Must have (必須有)**:
            -   **定義**: 核心需求，沒有它們產品就無法發布或不可用。如果發布時沒有包含任何一個 Must have 項，則發布應被視為失敗。
            -   **特徵**: 關鍵功能、法律要求、安全必需品。
            -   *示例*: 電商網站的“添加到購物車”和“結賬”功能。

        2.  **Should have (應該有)**:
            -   **定義**: 重要但非必需的需求。如果沒有它們，產品仍然可用，但價值會降低或用戶體驗不佳。可以嘗試在發布時包含，但如果時間緊張，可以推遲。
            -   **特徵**: 重要的輔助功能、性能改進。
            -   *示例*: 電商網站的“商品篩選”或“多種支付方式”。

        3.  **Could have (可以有)**:
            -   **定義**: 期望但不重要的需求。如果時間和資源允許，可以包含，它們能帶來一些額外價值或用戶愉悅感，但缺少它們影響不大。
            -   **特徵**: “錦上添花”的功能、小的易用性改進。
            -   *示例*: 電商網站的“自定義主題顏色”。

        4.  **Won't have (這次不會有)**:
            -   **定義**: 已被明確排除在當前範圍之外的需求。記錄下來是為了明確共識，避免範圍蔓延。這些需求可能會在未來考慮。
            -   **特徵**: 與當前目標不符、成本過高、或者計劃在後續版本實現的功能。
            -   *示例*: 電商網站初期版本可能決定“暫不做”社交分享功能。

        ## 使用場景 (When to Use)

        -   非常適合與 [[08 - Stakeholder Management|干系人]] 快速就範圍達成共識。
        -   在敏捷開發中，常用於確定 Sprint 或 Release 的目標。
        -   相比 [[RICE Framework|RICE]] 等量化模型，更側重於分類和範圍界定。

        > [!tip] 保持平衡
        > 要警惕將過多的需求歸類為 "Must have"，這會導致範圍過大。通常建議將有限比例 (例如 60% 或更少) 的精力分配給 Must have，為 Should have 和 Could have 留出空間。

        ---
        關聯概念: [[Prioritization Overview|優先級排序概述]]
        """),

    os.path.join("Concepts", "Product Management", "05 - Prioritization", "Kano Model.md"): textwrap.dedent("""\
        ---
        tags: [product-management, prioritization, framework, Kano, user-satisfaction]
        aliases: [Kano模型, Kano]
        ---
        # Kano 模型 (Kano Model)

        > [!info] 定义 (Definition)
        > Kano 模型是一種用戶需求分類和優先級排序的理論，它將產品質量特性與用戶滿意度聯繫起來，幫助理解不同功能對用戶感受的影響。

        ## 核心思想 (Core Idea)

        Kano 模型認為，並非所有功能都能同等地提升用戶滿意度。有些功能缺失會導致極度不滿，但有了也未必帶來高滿意度；而另一些功能即使沒有，用戶也不會太在意，但一旦提供，則可能帶來極大的驚喜和滿意度。

        ## 五種質量特性 (Five Categories of Attributes)

        ```mermaid
        graph LR
            subgraph "Kano 模型"
            direction TB
                A(基本型需求<br>Must-be Quality) -- 不滿足 --> B(極度不滿);
                A -- 滿足 --> C(沒感覺/理所當然);
                D(期望型需求<br>One-dimensional Quality) -- 不滿足 --> E(不滿);
                D -- 滿足 --> F(滿意);
                G(魅力型需求<br>Attractive Quality) -- 不滿足 --> H(沒感覺);
                G -- 滿足 --> I(非常滿意/驚喜);
                J(無差異需求<br>Indifferent Quality) -- 不滿足/滿足 --> K(無所謂);
                L(反向型需求<br>Reverse Quality) -- 不滿足 --> M(滿意);
                L -- 滿足 --> N(不滿);
            end

        style A fill:#ffb3ba
        style D fill:#ffffba
        style G fill:#baffc9
        style J fill:#eeeeee
        style L fill:#cde4ff
        ```

        1.  **基本型需求 (Must-be / Basic Needs)**:
            -   用戶認為產品“必須”具備的功能。
            -   **特點**: 滿足了不會提升滿意度 (因為是理所當然的)，但不滿足會導致極度不滿。
            -   *示例*: 酒店房間有乾淨的床鋪，App 可以正常登錄。
            -   **策略**: 必須優先滿足。

        2.  **期望型需求 (One-dimensional / Performance Needs)**:
            -   用戶期望的功能，滿足程度與滿意度成正比。
            -   **特點**: 提供得越多/越好，用戶越滿意；提供得越少/越差，用戶越不滿。
            -   *示例*: 手機電池續航時間越長越好，網頁加載速度越快越好。
            -   **策略**: 在資源允許下盡力滿足，是競爭的關鍵。

        3.  **魅力型需求 (Attractive / Excitement Needs)**:
            -   用戶未預期到的、帶來驚喜的功能。
            -   **特點**: 沒有也不會引起不滿，但一旦提供，會讓用戶非常滿意，甚至產生口碑效應。
            -   *示例*: 某 App 的一個意想不到的貼心小功能，首次使用降噪耳機的安靜體驗。
            -   **策略**: 是產品差異化和創造忠誠度的來源，可以選擇性投入。

        4.  **無差異需求 (Indifferent Quality)**:
            -   用戶根本不在意的功能。
            -   **特點**: 無論提供與否，用戶滿意度都沒有變化。
            -   **策略**: 避免投入資源。

        5.  **反向型需求 (Reverse Quality)**:
            -   一些用戶喜歡，但另一些用戶討厭的功能。
            -   **特點**: 提供後反而導致一部分用戶不滿。
            -   *示例*: 過於複雜的界面，某些用戶不喜歡的自動播放功能。
            -   **策略**: 需要謹慎處理，可能需要提供選項或避免。

        ## 如何應用 (How to Apply)

        -   通常通過專門設計的 Kano 問卷進行 [[02 - User Research/Surveys|問卷調查]] 來識別功能屬於哪個類別。
        -   問卷會針對每個功能問兩個問題：
            -   如果 **有** 這個功能，您感覺如何？ (正面問題)
            -   如果 **沒有** 這個功能，您感覺如何？ (負面問題)
        -   根據用戶對這兩個問題的回答組合，判斷該功能對該用戶屬於哪個類別。

        > [!tip] 動態變化
        > 需求的類別會隨時間變化。今天的魅力型需求可能變成明天的期望型需求，甚至後天的基本型需求 (例如：手機觸摸屏)。

        ---
        關聯概念: [[Prioritization Overview|優先級排序概述]], [[02 - User Research/User Research Overview|用戶研究]]
        """),

    # --- Product Metrics ---
    os.path.join("Concepts", "Product Management", "06 - Product Metrics", "Product Metrics Overview.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, metrics, data-driven]
        aliases: [產品指標, 指標]
        ---
        # 產品指標概述 (Product Metrics Overview)

        > [!info] 定义 (Definition)
        > 產品指標是用於衡量產品表現、用戶行為和業務成果的可量化數據點。它們幫助產品團隊做出數據驅動的決策，並追蹤實現目標的進展。

        ## 為何重要 (Why are Metrics Important?)

        -   **衡量成功**: 定義和追蹤實現 [[03 - Product Strategy|產品策略]] 和目標的進度。
        -   **識別問題**: 發現產品或用戶體驗中的瓶頸和機會點。
        -   **數據驅動決策**: 為 [[05 - Prioritization/Prioritization Overview|優先級排序]]、功能設計和迭代提供依據。
        -   **溝通效果**: 向 [[08 - Stakeholder Management|干系人]] 展示產品的價值和影響。
        -   **學習與改進**: 驗證假設，了解哪些有效，哪些無效。

        ## 指標類型 (Types of Metrics)

        指標可以從多個維度分類：

        -   **按性質**:
            -   **定量指標 (Quantitative)**: 數字（如：用戶數、轉化率、收入）。
            -   **定性指標 (Qualitative)**: 非數字的反饋（如：用戶訪談、[[02 - User Research/Usability Testing|可用性測試]]發現的問題、NPS 的評論）。
        -   **按焦點**:
            -   **用戶行為指標**: 活躍用戶數 (DAU/MAU)、留存率、功能使用率。
            -   **業務指標**: 收入 (Revenue)、客戶獲取成本 (CAC)、客戶生命週期價值 (LTV)。
            -   **產品質量指標**: Bug 數量、加載時間、崩潰率。
            -   **用戶滿意度指標**: [[North Star Metric|北極星指標]] (可能相關)、淨推薦值 (NPS)、客戶滿意度 (CSAT)。
        -   **按層級**:
            -   **[[North Star Metric|北極星指標 (NSM)]]**: 指引整個產品方向的單一核心指標。
            -   **一級指標 (Tier 1 / Driver Metrics)**: 直接驅動 NSM 的關鍵指標。
            -   **二級指標 (Tier 2 / Diagnostic Metrics)**: 解釋一級指標變化的細分指標。

        ## 選擇好的指標 (Choosing Good Metrics - AARRR Framework Example)

        一個常用的框架是 [[AARRR Framework|AARRR 模型]]（海盜指標），它關注用戶生命週期的關鍵階段：

        -   **Acquisition (獲取)**: 用戶如何找到你？ (流量來源、註冊數)
        -   **Activation (激活)**: 用戶首次體驗是否良好？ (完成關鍵操作、新手引導完成率)
        -   **Retention (留存)**: 用戶是否持續回來？ (日/週/月留存率、流失率)
        -   **Referral (推薦)**: 用戶是否願意推薦？ (NPS、分享率)
        -   **Revenue (收入)**: 你如何賺錢？ (付費轉化率、ARPU、LTV)

        > [!warning] 虛榮指標 (Vanity Metrics)
        > 警惕那些看起來不錯但不能指導實際行動的指標（如：累計註冊用戶數）。關注 **可操作指標 (Actionable Metrics)**，即那些能夠反映真實用戶行為並能指導你改進產品的指標。

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[03 - Product Strategy|產品策略]] (指標衡量策略成功), [[North Star Metric|北極星指標]], [[AARRR Framework|AARRR 模型]]
        """),

    os.path.join("Concepts", "Product Management", "06 - Product Metrics", "North Star Metric.md"): textwrap.dedent("""\
        ---
        tags: [product-management, metrics, strategy, NSM]
        aliases: [北極星指標, NSM]
        ---
        # 北極星指標 (North Star Metric - NSM)

        > [!info] 定义 (Definition)
        > 北極星指標 (NSM) 是一個單一的、能夠最好地體現產品為客戶創造的核心價值的指標。它應該是領先指標 (Leading Indicator)，預示著未來的業務成功（如收入）。

        ## 核心特徵 (Key Characteristics)

        一個好的北極星指標應該：

        1.  **反映用戶價值 (Reflects Customer Value)**: 它衡量了用戶從產品中獲得的核心利益。
        2.  **代表產品願景 (Represents Product Vision)**: 與 [[03 - Product Strategy|產品策略]] 和長期目標一致。
        3.  **領先指標 (Is a Leading Indicator)**: 它的增長預示著未來收入或其他滯後業務指標的增長。
        4.  **可行動 (Is Actionable)**: 團隊的日常工作可以直接或間接地影響這個指標。
        5.  **可衡量 (Is Measurable)**: 可以清晰地定義和追踪。
        6.  **易於理解 (Is Understandable)**: 整個公司都能理解它的含義。
        7.  **非虛榮指標 (Is Not a Vanity Metric)**: 它的增長真正代表了產品的健康發展。

        ## 示例 (Examples)

        -   **Facebook (早期)**: 月活躍用戶數 (MAU) - 反映連接人的核心價值。
        -   **Airbnb**: 預訂間夜數 (Nights Booked) - 反映房東和房客成功匹配的核心價值。
        -   **Spotify**: 聽眾總收聽時長 (Time Spent Listening) - 反映用戶享受音樂/播客的核心價值。
        -   **Slack**: 每週發送消息達到一定數量 (e.g., 2000條) 的團隊數 - 反映團隊協作的核心價值。
        -   **電商平台**: 每週完成購買的用戶數。

        ## 如何找到 NSM (How to Find Your NSM)

        1.  **明確核心價值**: 你的產品為用戶解決的最關鍵問題是什麼？
        2.  **識別關鍵行為**: 哪些用戶行為最能體現他們體驗到了這種價值？
        3.  **量化該行為**: 如何用一個數字來衡量這種行為的頻率或深度？
        4.  **驗證關聯性**: 這個指標的增長是否真的與長期業務成功（如留存、收入）相關？

        > [!tip] NSM 不是唯一的指標
        > NSM 是指引方向的核心，但仍需要 [[Product Metrics Overview|其他一級和二級指標]] 來全面了解產品健康狀況並診斷問題。NSM 也可能隨著產品發展和策略調整而演變。

        ---
        關聯概念: [[Product Metrics Overview|產品指標概述]], [[03 - Product Strategy|產品策略]]
        """),

    os.path.join("Concepts", "Product Management", "06 - Product Metrics", "AARRR Framework.md"): textwrap.dedent("""\
        ---
        tags: [product-management, metrics, framework, AARRR, pirate-metrics]
        aliases: [AARRR模型, 海盜指標, Pirate Metrics]
        ---
        # AARRR 模型 (海盜指標)

        > [!info] 定义 (Definition)
        > AARRR 模型，又稱“海盜指標”(因為發音像海盜的吼聲 "Arrr!")，是一個由 Dave McClure 提出的用戶生命週期分析框架。它將用戶轉化路徑分解為五個關鍵階段，並為每個階段設定核心指標，幫助初創公司和產品團隊了解其增長引擎的健康狀況。

        ## 五個階段 (The Five Stages)

        ```mermaid
        graph TD
            A(獲取 Acquisition) --> B(激活 Activation);
            B --> C(留存 Retention);
            C --> D(收入 Revenue);
            C --> E(推薦 Referral);

            subgraph 用戶生命週期漏斗 (User Lifecycle Funnel)
                direction TB
                A
                B
                C
                D & E
            end
        ```
        *(注意: Revenue 和 Referral 的順序有時會互換，取決於商業模式)*

        1.  **Acquisition (獲取)**:
            -   **問題**: 用戶從哪裡來？如何找到我們？
            -   **核心目標**: 吸引潛在用戶訪問你的產品或網站。
            -   **示例指標**: 網站訪問量、各渠道流量來源、應用下載量、註冊用戶數、每次獲取成本 (CPA)。

        2.  **Activation (激活)**:
            -   **問題**: 用戶是否體驗到了“啊哈時刻”(Aha! Moment)？首次體驗是否愉快？
            -   **核心目標**: 讓用戶體驗到產品的核心價值。
            -   **示例指標**: 完成新手引導的用戶比例、註冊後完成關鍵操作 (如發布第一條內容、添加第一個好友) 的用戶比例、次日留存率 (可視為早期激活信號)。

        3.  **Retention (留存)**:
            -   **問題**: 用戶是否會持續回來使用？
            -   **核心目標**: 讓用戶養成使用習慣，長期留在產品中。
            -   **示例指標**: 日活躍用戶 (DAU) / 月活躍用戶 (MAU) 比例、日/週/月留存率 (Cohort Analysis)、流失率 (Churn Rate)。

        4.  **Referral (推薦)**:
            -   **問題**: 用戶是否願意向他人推薦我們的產品？
            -   **核心目標**: 利用現有用戶帶來新用戶（病毒式增長）。
            -   **示例指標**: 淨推薦值 (NPS)、分享/邀請次數、病毒係數 K (K factor)。

        5.  **Revenue (收入)**:
            -   **問題**: 我們如何從用戶行為中賺錢？
            -   **核心目標**: 將用戶價值轉化為商業價值。
            -   **示例指標**: 付費轉化率、每用戶平均收入 (ARPU)、客戶生命週期價值 (LTV)、總收入。

        ## 應用價值 (Value of Application)

        -   **診斷瓶頸**: 幫助定位用戶流失發生在哪個環節，以便集中資源改進。
        -   **衡量增長**: 提供一個全面的框架來衡量產品的增長健康度。
        -   **設定目標**: 為每個階段設定具體的、可衡量的指標和目標。

        > [!tip] 關注轉化率
        > 除了各階段的絕對數字，更重要的是關注從一個階段到下一個階段的 **轉化率**，這能更清晰地揭示漏斗中的問題所在。

        ---
        關聯概念: [[Product Metrics Overview|產品指標概述]], [[01 - Product Lifecycle|產品生命週期]]
        """),

    # --- Go-to-Market Strategy ---
    os.path.join("Concepts", "Product Management", "07 - Go-to-Market Strategy.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, strategy, marketing, launch]
        aliases: [上市策略, GTM]
        ---
        # 上市策略 (Go-to-Market Strategy - GTM)

        > [!info] 定义 (Definition)
        > 上市策略 (GTM) 是一個行動計劃，詳細說明了公司將如何利用其資源將新產品或服務推向市場，並觸達目標客戶以實現競爭優勢。它涵蓋了從產品定位、定價、銷售渠道到市場營銷的所有方面。

        ## 為何需要 GTM 策略 (Why Need a GTM Strategy?)

        -   **降低風險**: 減少產品上市失敗的可能性。
        -   **明確路徑**: 為所有相關團隊（產品、市場、銷售、客服）提供清晰的行動指南。
        -   **資源協調**: 確保各部門步調一致，有效利用資源。
        -   **加速成功**: 更快地觸達目標市場，實現產品目標。

        ## 核心組成部分 (Key Components)

        一個全面的 GTM 策略通常需要回答以下問題：

        1.  **目標市場 (Target Market)**:
            -   我們要賣給誰？（[[03 - Product Strategy|產品策略]] 中的定義）
            -   市場細分 (Market Segmentation) 和理想客戶畫像 (Ideal Customer Profile - ICP)。
        2.  **價值主張 (Value Proposition)**:
            -   我們的產品為目標客戶提供什麼獨特價值？（[[03 - Product Strategy|產品策略]] 中的定義）
            -   如何清晰地溝通這種價值？（產品定位和信息傳遞）
        3.  **定價策略 (Pricing Strategy)**:
            -   產品如何定價？（基於成本、價值、競爭對手？）
            -   是否有不同的定價層級或模式（如訂閱、按需付費）？
        4.  **銷售渠道 (Sales Channels)**:
            -   我們如何將產品交付給客戶？（直銷、分銷、線上、線下？）
            -   銷售團隊的結構和策略是什麼？
        5.  **市場營銷計劃 (Marketing Plan)**:
            -   如何提高產品知名度並產生潛在客戶？（內容營銷、廣告、SEO、社交媒體、公關等）
            -   品牌建設和信息傳遞策略。
        6.  **客戶支持 (Customer Support)**:
            -   如何幫助客戶成功使用產品並解決他們的問題？
        7.  **預算和資源 (Budget & Resources)**:
            -   執行 GTM 策略需要多少資金和人力？
        8.  **成功指標 (Success Metrics)**:
            -   如何衡量 GTM 策略的成功？（[[06 - Product Metrics/Product Metrics Overview|產品指標]]，如：早期用戶獲取數、轉化率、收入目標達成率）

        > [!tip] GTM 與產品發布 (Launch)
        > 產品發布 (Product Launch) 通常是 GTM 策略中的一個關鍵里程碑事件，但 GTM 是一個更廣泛、更持續的過程，涵蓋了產品進入市場的整個生命週期早期階段。

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[03 - Product Strategy|產品策略]], [[01 - Product Lifecycle|產品生命週期]] (特別是導入期), [[06 - Product Metrics/Product Metrics Overview|產品指標]]
        """),

    # --- Stakeholder Management ---
    os.path.join("Concepts", "Product Management", "08 - Stakeholder Management.md"): textwrap.dedent("""\
        ---
        tags: [product-management, core-concept, communication, collaboration]
        aliases: [干系人管理, 相關方管理]
        ---
        # 干系人管理 (Stakeholder Management)

        > [!info] 定义 (Definition)
        > 干系人管理是指識別所有對產品成功有影響或受產品影響的個人或團體（即干系人），並與他們建立和維護良好關係，以理解他們的需求、管理他們的預期、獲取他們的支持，並最終促進產品成功的過程。

        ## 誰是干系人 (Who are Stakeholders?)

        產品的干系人通常非常廣泛，可以分為內部和外部：

        -   **內部干系人 (Internal)**:
            -   **開發團隊 (Engineering/Development)**: 負責實現產品。
            -   **設計團隊 (Design/UX)**: 負責用戶體驗和界面設計。
            -   **市場團隊 (Marketing)**: 負責 [[07 - Go-to-Market Strategy|上市策略]] 和推廣。
            -   **銷售團隊 (Sales)**: 負責將產品賣給客戶。
            -   **客服團隊 (Customer Support/Success)**: 負責幫助用戶解決問題。
            -   **管理層/高管 (Leadership/Executives)**: 負責公司戰略和資源分配。
            -   **法務團隊 (Legal)**: 負責合規性。
            -   **數據分析團隊 (Data Analytics)**: 提供數據洞察。
            -   其他產品經理 (若有)。
        -   **外部干系人 (External)**:
            -   **客戶/用戶 (Customers/Users)**: 產品的最終使用者。
            -   **合作夥伴 (Partners)**: 合作提供價值。
            -   **投資者 (Investors)**: 關注回報。
            -   **監管機構 (Regulators)**: 關注合規性。
            -   **媒體 (Media)**: 影響公眾認知。

        ## 為何重要 (Why is it Important?)

        -   **獲取支持**: 產品開發需要跨團隊協作，良好的關係是基礎。
        -   **收集信息**: 不同干系人擁有不同的視角和信息，對產品決策至關重要（如銷售反饋市場需求，客服反饋用戶痛點）。
        -   **管理預期**: 確保干系人了解產品的 [[03 - Product Strategy|策略]]、[[04 - Roadmapping|路線圖]] 和 [[05 - Prioritization/Prioritization Overview|優先級]]，避免誤解和衝突。
        -   **建立信任**: 透明、及時的溝通能建立信任。
        -   **減少阻力**: 主動管理可以預防或化解潛在的衝突。

        ## 關鍵技巧 (Key Skills)

        -   **識別 (Identification)**: 繪製干系人地圖，了解誰是關鍵人物。
        -   **分析 (Analysis)**: 理解每個干系人的興趣、權力、影響力、需求和期望。
        -   **溝通 (Communication)**:
            -   針對不同對象調整溝通方式和頻率。
            -   積極傾聽他們的需求和擔憂。
            -   清晰地闡述產品願景、策略和決策依據 (The "Why")。
            -   定期同步進展和變化。
        -   **協商與影響 (Negotiation & Influence)**: 在資源衝突或意見不一時，尋求共贏方案。
        -   **建立關係 (Relationship Building)**: 真誠互動，建立信任。

        > [!example] 溝通頻率示例
        > - 與開發/設計團隊：每日站會、每周迭代計劃會。
        > - 與市場/銷售團隊：每周/每兩週同步會。
        > - 與管理層：每月/每季度匯報。
        > - (根據實際情況調整)

        ---
        關聯概念: [[00 - Product Management Overview|產品管理核心概念]], [[03 - Product Strategy|產品策略]], [[04 - Roadmapping|產品路線圖]], [[05 - Prioritization/Prioritization Overview|優先級排序]] (需要向干系人解釋排序結果)
        """),

    # --- Interview Simulation ---
    os.path.join("Interview Simulation", "Product Manager Interview", "1 - Prioritization Question.md"): textwrap.dedent("""\
        ---
        tags: [interview, product-manager, prioritization]
        ---
        # 面試問題：優先級排序 (Interview Question: Prioritization)

        ## 問題示例 (Example Question)

        > "假設你是某個 SaaS 產品 (例如：項目管理工具) 的產品經理。現在你收到了來自不同渠道的需求：用戶反饋希望增加甘特圖功能，銷售團隊強烈要求開發一個面向大客戶的定制報表功能，工程團隊建議重構一個舊的技術模塊以提高性能。同時，數據顯示用戶留存率近期有所下降。你會如何決定接下來的開發優先級？請闡述你的思考過程。"

        ## 解答思路 (Approach)

        > [!tip] 核心框架：目標 -> 評估 -> 排序 -> 溝通
        > 面試官不僅關心你的 *結論*，更關心你得出結論的 *結構化思考過程*。

        1.  **澄清目標與背景 (Clarify Goals & Context)**:
            *   首先，回顧當前階段的 **[[03 - Product Strategy|產品策略]]** 和 **[[06 - Product Metrics/Product Metrics Overview|產品指標]]** 目標。當前最重要的目標是什麼？是提高留存率？擴展大客戶市場？還是提升用戶滿意度？
            *   確認是否存在既定的 **[[04 - Roadmapping|產品路線圖]]**？這些需求是否與路線圖主題相關？
            *   (反問面試官) "為了更好地回答這個問題，我想先確認一下我們產品現階段的核心目標是什麼？比如，我們是更關注用戶增長、留存，還是收入？"

        2.  **評估每個選項 (Evaluate Each Option)**:
            *   **甘特圖功能 (用戶反饋)**:
                *   **價值**: 提升項目可視化能力，可能提升部分用戶滿意度和使用深度。
                *   **影響**: 會影響多少用戶？(Reach) 對核心指標 (如留存率) 的影響有多大？(Impact)
                *   **依據**: 是否有 [[02 - User Research/User Research Overview|用戶研究]] 支持？有多少用戶提了這個需求？
                *   **成本**: 開發需要多少資源？(Effort)
            *   **定制報表 (銷售驅動)**:
                *   **價值**: 可能贏得大客戶合同，增加收入。
                *   **影響**: 影響客戶數量少，但單個價值高。對整體 [[06 - Product Metrics/AARRR Framework|Revenue]] 可能有顯著影響。
                *   **風險**: 定制化程度多高？是否會影響產品的通用性？維護成本？
                *   **成本**: 開發和後續維護投入？(Effort)
            *   **技術重構 (工程建議)**:
                *   **價值**: 提高性能、穩定性，降低未來開發成本，可能間接改善用戶體驗和留存。
                *   **影響**: 可能影響所有用戶，但影響是間接的。對留存率下降問題可能有幫助。
                *   **緊迫性**: 當前的性能問題有多嚴重？是否阻礙了新功能的開發？
                *   **成本**: 需要多少工程資源？(Effort) 是否會阻塞其他功能開發？
            *   **留存率下降問題 (數據驅動)**:
                *   **根本原因**: 為什麼留存率下降？需要進一步分析數據或做 [[02 - User Research/User Research Overview|用戶研究]] 來定位原因。這可能不是一個單一“功能”能解決的，可能需要一系列改進。

        3.  **運用優先級框架 (Apply Prioritization Framework)**:
            *   可以口頭上應用 [[05 - Prioritization/RICE Framework|RICE]] 或 [[05 - Prioritization/Value vs. Complexity Matrix|價值 vs 複雜度]] 的思路來比較這些選項。
            *   **RICE 思考**:
                *   甘特圖: Reach (中/高?), Impact (中?), Confidence (中?), Effort (高?)
                *   定制報表: Reach (低), Impact (高 - 對特定客戶), Confidence (高 - 如果銷售確認), Effort (中/高?)
                *   技術重構: Reach (高), Impact (中 - 間接), Confidence (高 - 如果工程確認必要性), Effort (高?)
            *   **結合目標**: 如果當前核心目標是 **解決留存率下降**，那麼技術重構或針對導致流失原因的功能改進可能優先級更高。如果目標是 **擴展大客戶市場**，定制報表優先級可能更高。

        4.  **做出初步決策並說明理由 (Make a Preliminary Decision & Justify)**:
            *   沒有唯一正確答案。關鍵是展示權衡過程。
            *   *示例回答方向*: "基於留存率下降這個關鍵問題，我會優先投入資源 **深入分析留存率下降的原因**。這可能涉及數據分析和快速的用戶研究。同時，我會評估 **技術重構** 對穩定性和性能的改善是否能直接緩解部分流失問題。對於 **甘特圖**，雖然用戶有需求，但如果不是導致流失的核心原因，可以考慮放在 'Next'。對於 **定制報表**，需要評估其對整體策略的影響以及資源佔用，看是否可以找到更通用的解決方案滿足部分需求，或者確認其戰略重要性後再排入。"

        5.  **強調溝通與迭代 (Emphasize Communication & Iteration)**:
            *   強調會與 [[08 - Stakeholder Management|干系人]] (銷售、工程、用戶) 溝通這個決策及其背後的原因。
            *   說明這是一個動態過程，會根據後續的數據和反饋進行調整。

        > [!success] 加分項
        > - 展示結構化思維。
        > - 清晰引用產品管理概念和框架 (如 RICE, 策略, 指標)。
        > - 表現出數據敏感度和用戶中心思想。
        > - 強調溝通和協作的重要性。
        > - 能夠進行權衡取捨 (Trade-offs)。
        """),
}

# --- Script Logic ---
def create_notes():
    """Creates the directory structure and .md files based on notes_data."""
    print(f"Starting knowledge base creation in root directory: {os.path.abspath(ROOT_DIR)}")
    created_files = 0
    created_dirs = 0

    for rel_path, content in notes_data.items():
        full_path = os.path.join(ROOT_DIR, rel_path)
        dir_path = os.path.dirname(full_path)

        # Create directories if they don't exist
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path)
                print(f"  Created directory: {dir_path}")
                created_dirs += 1
            except OSError as e:
                print(f"  Error creating directory {dir_path}: {e}")
                continue # Skip file creation if directory failed

        # Create or overwrite the markdown file
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Created/Updated file: {full_path}")
            created_files += 1
        except IOError as e:
            print(f"  Error writing file {full_path}: {e}")

    print("\n--------------------")
    print("Knowledge base creation process finished.")
    print(f"Total directories created: {created_dirs}")
    print(f"Total files created/updated: {created_files}")
    print("--------------------")
    print("\n建議：")
    print("1. 在 Obsidian 中打開包含這些文件的 Vault。")
    print("2. 安裝並啟用 Mermaid 插件以查看圖表。")
    print("3. 探索文件之間的雙向鏈接，體驗知識圖譜的效果。")
    print("4. 根據自己的學習進度，繼續添加和完善筆記內容。")

if __name__ == "__main__":
    # Ensure the root directory exists (optional, useful if ROOT_DIR is not '.')
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)
        print(f"Created root directory: {os.path.abspath(ROOT_DIR)}")
        
    create_notes()
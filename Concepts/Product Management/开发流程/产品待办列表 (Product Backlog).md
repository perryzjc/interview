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
*   **P - Prioritized (经过排序)**: **这是最重要的特征**。列表中的所有 PBI 都按照优先级进行了排序。[[产品负责人 (Product Owner)]] 根据[[价值主张|价值]]、[[技术相关/风险管理|风险]]、[[技术相关/技术依赖|依赖关系]]、[[工作量估算|成本]]等因素进行排序，确保[[开发团队 (Development Team)]] 始终在处理最高优先级的 PBI。

## 产品待办列表项 (PBI)

产品待办列表由一系列的产品待办列表项 (PBI) 组成。PBI 通常包含以下信息：

*   **描述 (Description)**: 清晰地描述需求是什么。常用的格式是[[用户研究/用户故事|用户故事]] (“作为一个[角色], 我想要[做某事], 以便[获得某种价值]”)。
*   **顺序 (Order)**: PBI 在列表中的位置，反映其优先级。
*   **估算 (Estimate)**: [[开发团队 (Development Team)]] 估算的工作量（如[[故事点 (Story Points)]]）。
*   **价值 (Value)**: （可选）对业务或用户的价值评估。
*   **(可选) [[验收标准 (Acceptance Criteria)]]**: 定义 PBI 完成的标准，以便测试和验收。

## 产品待办列表梳理 (Product Backlog Refinement)

产品待办列表梳理（也称为 Backlog Grooming）是一个**持续进行**的活动，[[产品负责人 (Product Owner)]] 和 [[开发团队 (Development Team)]] 会定期（通常占用 [[Sprint]] 中 5-10% 的时间）一起：

*   **评审和讨论** 即将到来的 PBI。
*   **澄清需求**，添加细节。
*   **拆分** 过大的 PBI（例如 [[史诗 (Epic)]] 分解为更小的[[用户研究/用户故事|用户故事]]）。
*   **估算** 新的或修改后的 PBI。
*   **重新排序** PBI。

这个活动确保了产品待办列表始终处于良好状态 (DEEP)，为后续的 [[Sprint 计划会]]做好准备。

## 产品待办列表与 [[Sprint 待办列表 (Sprint Backlog)]]

*   **产品待办列表 (Product Backlog)**: 包含**所有**已知的产品需求，是产品的长期需求池，由 [[产品负责人 (Product Owner)]] 负责。
*   **[[Sprint 待办列表 (Sprint Backlog)]]**: 包含为**当前 Sprint** 选定的 PBI 以及交付这些 PBI 所需的任务计划。它是 [[开发团队 (Development Team)]] 在一个 Sprint 内的工作计划，由 [[开发团队 (Development Team)]] 负责管理。

在 [[Sprint 计划会]]上，[[开发团队 (Development Team)]] 从产品待办列表的顶部选择最高优先级的 PBI，并将其放入 [[Sprint 待办列表 (Sprint Backlog)]] 中。

## 总结

产品待办列表是 [[Scrum]] 框架的核心，是连接[[基础概念/产品愿景|产品愿景]]与开发执行的桥梁。[[产品负责人 (Product Owner)]] 通过持续维护一个排序良好、细节适当、动态更新的产品待办列表，来指导 [[开发团队 (Development Team)]] 最大化产品价值的交付。

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

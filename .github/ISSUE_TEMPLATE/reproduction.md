---
name: '复现反馈或技术疑问 / Reproduction or question'
about: '说明做到哪一步、预期与实际差异，帮助定位伴读或统计口径问题。'
title: '[TA05] '
---

## 1. 我实际做到哪一步 / What I actually tried

- [ ] 只阅读教程或数据，没有运行 UE
- [ ] 打开在线伴读
- [ ] 下载 HTML 后离线打开
- [ ] 导出 CSV
- [ ] 用原始数据完成读数练习，未运行 UE / Completed the reading exercise without running UE
- [ ] 自己在 UE 中另做了实验（这是新实验，不是本仓库重新计时）

## 2. 我的问题 / Question or unexpected result

期望 / Expected:

实际看到 / Observed:

## 3. 最短复现步骤 / Minimal steps

1.
2.
3.

若涉及图表，请说明：透明阶段或整帧 GPU、均值或采样最大值、线性或对数、所选窗口及帧索引。截图可选，不需要上传整个工程。

For chart questions, include the metric, statistic, axis scale, selected window and frame index. A whole Unreal project is not needed.

读数练习可补这三项 / For the reading exercise

- 改了什么，哪些条件保持一致 / Changed variable and fixed conditions
- 比较的窗口、口径和毫秒数 / Compared windows, timing scope, statistic and values in ms
- 读数支持的结论，或卡在哪一步 / Supported conclusion or the step you got stuck on

## 4. 必要环境 / Relevant environment

浏览器与版本、电脑或手机；如果是自己的 UE 实验，再写 UE 版本、RHI、分辨率、GPU，以及与原文条件不同之处。不确定的项目写“未知”。

Browser/version and desktop/phone; for your own UE experiment, also note UE version, RHI, resolution, GPU and changed conditions. Unknown values can stay unknown.

## 5. 如果有数据差异 / If reporting a data mismatch

文件名、窗口或行号、期望值与实际值；原 CSV 保持不动，另附最小示例即可。

Keep the original CSV unchanged and identify the file, window/row and expected versus observed values.

提交前删去令牌、账号、私有路径和未获准公开的项目内容。请勿把只阅读写成实际运行；没有收到独立复现前，作者不会把这条记录称为优化效果或读者复现成功。

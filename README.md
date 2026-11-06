# TA05 · Niagara GPU Timing Companion

**77的技术美术实战｜把 UE 制作中的问题、工具与流程讲清楚。**

An offline, interactive teaching companion for reading **existing Unreal Engine Niagara rendering measurements**. It contains 12 measured windows and 40,353 sampled frames. This is a data-reading example, not a new benchmark, optimisation tool, Unreal plugin, or game.

**[Open the interactive companion / 直接打开交互伴读](https://qiqideqi.github.io/ta05-niagara-gpu-timing-companion/)**

![Interactive timing chart](docs/timing-companion.png)

## English measurement guide

Read the **[standalone illustrated guide](https://qiqideqi.github.io/ta05-niagara-gpu-timing-companion/measurement-notes.html)** for metric scopes, all 12 windows, window means versus sample maxima, and an eight-frame worked excerpt. It includes three figures and the measurement limits; no Chinese tutorial or Unreal installation is required to follow it. The existing interactive charts remain available above. Try the [English reading exercise](https://qiqideqi.github.io/ta05-niagara-gpu-timing-companion/measurement-notes.html#reading-exercise-en) to compare render-pass and whole-frame readings.

## Start / 开始使用

**[Try the online reading exercise / 直接做读数练习](https://qiqideqi.github.io/ta05-niagara-gpu-timing-companion/#reading-exercise)**

Choose one size or material comparison. Record the changed variable, timing scope, selected windows and measured values, then write what the readings support. You can do this in your browser without opening Unreal Engine.

选一组尺寸或材质对照，记下变量、计时口径、窗口和读数，再写一句结论。完成后可用[反馈模板](https://github.com/QIQIdeqi/ta05-niagara-gpu-timing-companion/issues/new?template=reproduction.md)记录结论或卡点。离线用法如下。

1. Download and extract the **[latest offline ZIP](https://github.com/QIQIdeqi/ta05-niagara-gpu-timing-companion/releases/latest)**. Open `index.html` or `measurement-notes.html` directly from the extracted folder.
2. Open `index.html` in a modern browser. The page is in Chinese; all chart data is embedded. No account, network, Unreal installation, CDN, or build step is required.
3. Switch **透明阶段** (GPU/Translucency) versus **整帧 GPU** (GPUTime), **均值** (mean) versus **采样最大值** (sample maximum), and linear versus logarithmic axes.
4. Choose a measured window and click **定位所选范围的首个采样最大值** to locate its first sampled maximum. The slider inspects individual sampled frames.
5. The two buttons at the bottom export the original per-window and per-frame CSV files, byte for byte. Narrow screens can scroll the charts horizontally.

完整免费方法及节点搭建说明见作者原教程：[Niagara性能排查：粒子数、Overdraw与GPU计时｜TA实践手记05](https://zhuanlan.zhihu.com/p/2097710842536113511)。本仓库独立提供图表、数据、条件和操作步骤，不以外跳或付费作为使用条件。

## What the comparison means / 怎样读对照

- A: sprite size 16 versus 80, with the same simple material.
- B: keep size 80 and the opacity outline fixed, then change material work.
- Reference: hide the effect's rendering; the background still has a cost.
- Each condition has three interleaved measured windows. A chart point represents one window, not an independent machine or an additional experiment.
- GPU/Translucency is a scene pass measurement, not one Niagara resource's exclusive GPU time. GPUTime covers the whole frame. Stage differences cannot be translated directly into a fixed FPS improvement.

图表、表格和逐帧读数分别保留统计口径。峰值是已采样窗口的最大值，不冒充完整技能生命周期峰值；三轮范围不是置信区间。Overdraw调试颜色没有换算为毫秒。

## Frozen measurement conditions / 真实采集条件

Windows · UE5.8.2 · D3D11/SM5 · RTX 4070 Laptop GPU · driver 560.94 · 1280×720 · FOV 50 · seed 77. CPU simulation advances 60 × 1/60 seconds and then pauses; GPU rendering continues. Each window has 5 seconds of warm-up and approximately 10 seconds of timing; three interleaved repetitions per condition. The three rendered cases recorded 88 active particles.

These are static rendering comparisons at approximately one second of system age. They do not establish GPU particle simulation cost, dynamic gameplay cost, exclusive hardware conditions, cross-machine behaviour, or a universal resource ranking.

## Files and verification

- `index.html`: single-file interactive reader, version 1.0.2, including the two original CSV exports; now with an optional English-guide link.
- `measurement-notes.html` and `docs/measurement/`: standalone English explanation with three checked figures; original measurements are unchanged.
- `data/逐轮统计.csv`: 12 window summaries.
- `data/逐帧关键列.csv`: all 40,353 key-frame rows.
- `data/实测汇总.json`: original measured summary.
- `data/provenance.json`: hashes, source scope and statistical limitations.

The original 12 CSV hashes were checked against frozen records. Means and sample maxima were recomputed from all key frames. Browser checks covered eight chart combinations, 24 peak-location cases and a 390px responsive viewport; the original CSV export bytes were checked. This does not establish an independent reader reproduction or a physical-phone test.

## Questions and reproduction / 疑问与复现反馈

If a chart, CSV export or explanation does not match what you expected, [open a focused issue](https://github.com/QIQIdeqi/ta05-niagara-gpu-timing-companion/issues/new?template=reproduction.md). State the step you reached, expected versus observed behaviour, selected metric/window/frame, and the relevant environment. Reading without running UE is welcome; mark it as reading rather than a reproduction.

有疑问可使用[复现反馈模板](https://github.com/QIQIdeqi/ta05-niagara-gpu-timing-companion/issues/new?template=reproduction.md)，留下最短步骤和实际差异。不要求上传整个工程；未知值保留未知，原CSV不要覆盖。自己的UE测试属于另一次实验，需单独记录条件，不能与这里的静态渲染数据混算。请先移除账号、令牌、私有路径与未获准公开的素材。

## Attribution and scope

Created for **77的技术美术实战**. AI assisted with code, wording and layout; numerical claims are grounded in the recorded CSV data and checks. No Unreal Engine binaries, third-party UE assets, private project files or paid Knowledge Planet packages are included. This repository does not change the original teaching project's licence; see [RIGHTS.md](RIGHTS.md).

Technical background: Epic Games, *Measuring Performance in Niagara* and *Viewport Modes*. This is an independent teaching resource, not an Epic Games product or endorsement.

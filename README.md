# XiaoShui Pretty PPT

一套面向 Codex / Claude Code 等 Coding Agent 的可复用 **HTML 网页 PPT 技能**。

它的目标不是生成普通网页，而是把笔记、文档、教程、复盘、汇报、演讲提纲和飞书文档内容，转成可以直接打开、展示、分享或部署的高完成度网页 PPT。

当前内置 12 套视觉模板，分为两个模块：

## Module A · 自媒体 / 个人展示 / 作品集

适合更活泼、更有记忆点、更适合对外分享的内容。

- **Pastel Blockfolio / 粉彩拼贴志**：教程、案例、流程复盘、自媒体选题说明。
- **Blush Editorial / 暖粉编辑志**：品牌内容页、推荐清单、工具目录、编辑感长页面。
- **Mono Curve Slides / 墨线白稿**：动态幻灯片、课程说明、产品更新、轻量演示页。
- **Ribbon Tab Brochure / 彩签页报**：项目资料册、产品说明、运营复盘、对外提案。
- **Blue Growth Deck / 蓝色增长稿**：AI 产品、运营增长、GEO 复盘、轻商务互动演示。
- **Garden Pop Landing / 花园跳色长页**：自媒体教程、课程产品、创作者产品发布、轻快产品长页。

## Module B · 行政政务 / 职场汇报 / 产品演讲

适合更实用、更正式、更偏工作交付的演示场景。

- **One Dot Cinnabar / 一点丹红**：年终总结、工作汇报、项目复盘、正式演讲。
- **Ivory Research Deck / 象牙研稿**：学术汇报、研究总结、职场简报、产品调研。
- **Cobalt Executive Deck / 钴蓝商策**：商务汇报、产品介绍、公司介绍、合作提案。
- **Coral Startup Deck / 珊瑚企简**：公司介绍、项目汇报、团队路演、工作计划。
- **Sapphire Defense Deck / 宝蓝答辩稿**：论文答辩、学术汇报、研究总结、正式项目复盘。
- **Vermilion Civic Deck / 红色汇报稿**：政务工作、行政汇报、党建材料、公共服务项目总结。

## Preview

### 01. Pastel Blockfolio / 粉彩拼贴志

适合把一个操作过程、案例复盘、前后对比教程做成有视觉记忆点的图文演示。

![Pastel Blockfolio preview](assets/previews/template-01-pastel-blockfolio.png)

### 02. Blush Editorial / 暖粉编辑志

适合品牌感、编辑感更强的内容页面，比如工具推荐、清单整理、内容目录、产品介绍。

![Blush Editorial preview](assets/previews/template-02-blush-editorial.png)

### 03. Mono Curve Slides / 墨线白稿

适合像 PPT 一样讲内容：上方可以做卡片预览，点开后进入独立幻灯片页面。

![Mono Curve Slides preview](assets/previews/template-03-mono-curve-slides.png)

### 04. One Dot Cinnabar / 一点丹红

适合正式场合的汇报页面，比如年终总结、项目复盘、领导汇报、部门工作汇报。

![One Dot Cinnabar preview](assets/previews/template-04-one-dot-cinnabar.png)

### 05. Ivory Research Deck / 象牙研稿

适合学术、研究和正式汇报场景：用象牙白纸面、浅蓝信息块、细线表格和时间轴承载高密度内容。

![Ivory Research Deck preview](assets/previews/template-05-ivory-research-deck.png)

### 06. Cobalt Executive Deck / 钴蓝商策

适合商务汇报、产品介绍、公司介绍和合作提案。

![Cobalt Executive Deck preview](assets/previews/template-06-cobalt-executive-deck.png)

### 07. Coral Startup Deck / 珊瑚企简

适合更温暖、更有亲和力的公司介绍、项目汇报、团队路演和工作计划。

![Coral Startup Deck preview](assets/previews/template-07-coral-startup-deck.png)

### 08. Ribbon Tab Brochure / 彩签页报

适合全屏项目资料册、产品说明、运营复盘和对外提案。

![Ribbon Tab Brochure preview](assets/previews/template-08-ribbon-tab-brochure.png)

### 09. Sapphire Defense Deck / 宝蓝答辩稿

适合论文答辩、研究汇报和正式项目复盘。

![Sapphire Defense Deck preview](assets/previews/template-09-sapphire-defense-deck.png)

### 10. Vermilion Civic Deck / 红色汇报稿

适合政务、行政、党建和公共服务类正式汇报。

![Vermilion Civic Deck preview](assets/previews/template-10-vermilion-civic-deck.png)

### 11. Blue Growth Deck / 蓝色增长稿

适合 AI 产品、运营增长、GEO 复盘和轻商务互动演示。

![Blue Growth Deck preview](assets/previews/template-11-blue-growth-deck.png)

### 12. Garden Pop Landing / 花园跳色长页

适合自媒体教程、课程产品、创作者发布和轻快产品长页。

![Garden Pop Landing preview](assets/previews/template-12-garden-pop-landing.png)

## What It Can Do

XiaoShui Pretty PPT 可以帮助 Coding Agent：

- 读取用户提供的文字、Markdown、飞书文档内容、图片、截图、视频素材。
- 在动手前判断 PPT 的使用场景、受众、内容密度和模板方向。
- 判断内容更适合哪一种 PPT 模板。
- 把长文档拆成 cover、agenda、chapter、data、process、comparison、image、summary、closing 等演示页。
- 生成可以直接打开的静态 HTML 网页 PPT，内置浏览器编辑模式。
- 保留每套模板自己的配色、字体层级、版式节奏和交互动效。
- 根据内容长度决定应该做成几页，而不是把所有内容硬塞进一屏。
- 默认内置浏览器编辑模式：按 `E` 直接改任何文字、替换图片/视频、插入新图片，保存到本机或导出修改后的 HTML。

## What Makes It Different

XiaoShui Pretty PPT 的独特之处：

- **模板驱动**：不是从零生成代码，而是从 12 套精心设计的视觉模板出发，保持每组配色、字体层级和交互动画的一致性。
- **先判断再动手**：在使用前会先了解场景、受众、内容密度和素材情况，再推荐最合适的模板方向。
- **渐进式交付**：清晰的工作流 — 判断模式 → 内容摄入 → 选择模板 → 规划页面 → 复制模板 → 填充内容 → 质量验收 → 交付。
- **可编辑交付物**：生成的 HTML PPT 默认内置编辑工具栏，按 `E` 即可编辑所有文字、替换图片/视频、插入新图片，按 `Cmd+S` 保存，点「导出 HTML」下载独立文件。
- **内容压缩**：不是把文档逐段贴进页面，而是将素材分类为"必须展示/可口头说明/可省略/需要可视化"再规划页面。

## Before Creating A PPT

如果用户只给一个主题，skill 会先判断几个维度：

| 维度 | 要判断什么 |
|---|---|
| 使用场景 | 现场演讲、对外分享、内部汇报、产品路演、课程教程、作品集展示 |
| 受众 | 领导、同事、客户、学生、公开观众、专业评审 |
| 内容密度 | 少字演讲型、图文均衡型、高密度报告型、教程走查型 |
| 素材状态 | 完整文档、粗略笔记、只有主题、截图/图片/旧 PPT 是否齐全 |
| 模板方向 | 自媒体/个人展示/作品集，还是行政政务/职场汇报/产品演讲 |

默认只问 3 个关键问题：

1. 这个 PPT 给谁看、用在什么场景？
2. 内容要少一点适合演讲，还是多一点适合阅读/汇报？
3. 你有文档、截图、图片、数据或旧 PPT 吗？

内容密度默认分四档：

| 密度 | 适合 | 页面规则 |
|---|---|---|
| Speaker Deck | 现场演讲、分享会、发布 | 一页一个观点，少字，强视觉 |
| Share Deck | 既演讲也发给别人看 | 3-5 个要点，图文均衡 |
| Report Deck | 行政、政务、职场、研究 | 可放表格/卡片/KPI，但必须分组，不堆长段落 |
| Tutorial / Portfolio | 教程、案例、作品集 | 以步骤、截图、案例前后对比为主 |

## How To Use

在 Codex 里可以这样调用：

```text
使用 $xiaoshui-pretty-ppt，把这份文档做成一个适合晚上分享的 HTML 网页 PPT。
请根据内容自动选择最合适的模板。
```

指定模板：

```text
使用 $xiaoshui-pretty-ppt 的 Cobalt Executive Deck / 钴蓝商策，
把这份产品介绍做成商务汇报型网页 PPT。
```

复制模板到本地输出目录（默认内置编辑工具栏）：

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force
open /tmp/shui-cobalt-demo/index.html
```

生成不带编辑工具栏的纯净版：

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force --no-edit
open /tmp/shui-cobalt-demo/index.html
```

给已有 HTML PPT 注入编辑模式：

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/inject_edit_mode.py /tmp/shui-cobalt-demo/index.html
```

打开后右上角会出现编辑工具栏：按 `E` 进入编辑模式，直接点任何文字即可修改；点图片/视频上的「替换图片」「替换视频」可换 URL 或上传本地文件；点「➕ 插入图片」可以往页面里新增图片；按 `Cmd+S` / `Ctrl+S` 保存到本机；点「导出 HTML」下载修改后的独立文件；点「重置」清除本地修改恢复模板内容。

验证输出：

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/validate_deck.py /tmp/shui-cobalt-demo
```

## Install

### Install from GitHub

推荐使用 `skills` CLI：

```bash
npx -y skills@latest add XshuiAi/xiaoshui-pretty-ppt \
  --skill xiaoshui-pretty-ppt \
  --agent codex \
  --global
```

如果希望复制文件而不是软链接：

```bash
npx -y skills@latest add XshuiAi/xiaoshui-pretty-ppt \
  --skill xiaoshui-pretty-ppt \
  --agent codex \
  --global \
  --copy \
  -y
```

### Manual install for Codex

复制 skill 目录到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R skills/xiaoshui-pretty-ppt ~/.codex/skills/xiaoshui-pretty-ppt
```

然后重启 Codex，让新 skill 生效。

### Verify Install

检查是否安装成功：

```bash
npx -y skills@latest list --global --agent codex --json
test -f ~/.agents/skills/xiaoshui-pretty-ppt/SKILL.md
```

## Repository Structure

```text
xiaoshui-pretty-ppt/
├── README.md
├── assets/
│   └── previews/                    # README preview images
└── skills/
    └── xiaoshui-pretty-ppt/         # Codex skill source
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        │   ├── intake-and-density.md
        │   ├── ppt-template-catalog.md
        │   ├── quality-checklist.md
        │   ├── editable-delivery.md
        │   ├── workflow-and-install.md
        │   ├── style-index.md
        │   └── *.md                 # detailed style specs
        ├── scripts/
        │   ├── copy_template.py
        │   ├── inject_edit_mode.py
        │   └── validate_deck.py
        └── assets/templates/        # reusable HTML PPT template sources
```

## Design Principle

- 每个模板都是独立可运行的完整 HTML 页面，复制即用，不需要从零开始生成。
- 模板之间有明确的视觉差异，确保每套 PPT 风格都有自己的辨识度。
- 所有生成逻辑都基于真实的模板源文件，保证产出质量稳定。

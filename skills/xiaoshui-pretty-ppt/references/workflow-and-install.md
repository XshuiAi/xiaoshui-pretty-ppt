# Workflow And Install Guide

This file explains how XiaoShui Pretty PPT is installed, updated, and validated.

## Install From GitHub

Recommended:

```bash
npx -y skills@latest add XshuiAi/xiaoshui-pretty-ppt \
  --skill xiaoshui-pretty-ppt \
  --agent codex \
  --global
```

Use `--copy` if symlinks are not desired:

```bash
npx -y skills@latest add XshuiAi/xiaoshui-pretty-ppt \
  --skill xiaoshui-pretty-ppt \
  --agent codex \
  --global \
  --copy \
  -y
```

## Manual Install

```bash
mkdir -p ~/.codex/skills
cp -R skills/xiaoshui-pretty-ppt ~/.codex/skills/xiaoshui-pretty-ppt
```

Then restart Codex if the skill list does not refresh.

## Verify Install

```bash
npx -y skills@latest list --global --agent codex --json
test -f ~/.agents/skills/xiaoshui-pretty-ppt/SKILL.md
```

If installed manually to `~/.codex/skills`, check:

```bash
test -f ~/.codex/skills/xiaoshui-pretty-ppt/SKILL.md
```

## Update Published Skill

After editing the repository:

```bash
git status --short
git add .
git commit -m "Improve XiaoShui Pretty PPT workflow"
git push
```

Then reinstall/update locally:

```bash
npx -y skills@latest add XshuiAi/xiaoshui-pretty-ppt \
  --skill xiaoshui-pretty-ppt \
  --agent codex \
  --global \
  --copy \
  -y
```

## Validate A Template Copy

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force
python3 skills/xiaoshui-pretty-ppt/scripts/validate_deck.py /tmp/shui-cobalt-demo
open /tmp/shui-cobalt-demo/index.html
```

## Create An Editable Deck

Browser edit mode is injected **by default** into every generated deck — no extra flag needed. The output includes a floating toolbar (edit, save, export, reset, insert image).

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force
open /tmp/shui-cobalt-demo/index.html
```

To generate a clean locked deck without the editing toolbar, use `--no-edit`:

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force --no-edit
open /tmp/shui-cobalt-demo/index.html
```

For an existing deck:

```bash
python3 skills/xiaoshui-pretty-ppt/scripts/inject_edit_mode.py /tmp/shui-cobalt-demo/index.html
```

Keyboard and toolbar behavior:

- Press `E` to enter or exit edit mode. All text elements become editable.
- Click any text directly to edit it.
- In edit mode, click the `替换图片` / `替换视频` badge on any image/video to replace its source (URL or local file upload).
- Click `➕ 插入图片` in the toolbar to insert a new image into the current page.
- Press `Cmd+S` / `Ctrl+S`, or click `保存`, to save changes to browser localStorage.
- Click `导出 HTML` to download a standalone edited HTML file.
- Click `重置` to clear local browser edits and restore original template content.
- Press `Esc` to exit edit mode.

## Prompt Examples

Use automatic selection:

```text
使用 $xiaoshui-pretty-ppt，把这份文档做成一个适合分享的 HTML 网页 PPT。
请先判断内容密度和模板方向，再开始生成。
```

Specify a module:

```text
使用 $xiaoshui-pretty-ppt，做一个偏行政汇报的网页 PPT。
内容密度可以高一点，但不要堆满文字。
```

Specify a template:

```text
使用 $xiaoshui-pretty-ppt 的 Garden Pop Landing / 花园跳色长页，
把这个课程介绍做成更适合自媒体发布的 PPT。
```

Editable handoff:

```text
使用 $xiaoshui-pretty-ppt，把这份飞书文档做成可直接演示的 HTML 网页 PPT。
请开启可编辑模式，这样我录视频时可以展示直接修改页面文字和导出 HTML。
```

# short-drama-comic-studio

中文文档：[`README.zh-CN.md`](README.zh-CN.md)

A Codex skill for building short drama / comic-drama projects end-to-end:

- Plan-mode-style interrogation (systematic intake questions)
- Script + episode outlines + storyboard schema
- Creative department review pass (director + DP + lighting + editing)
- Storyboard/keyframe image generation via `$imagegen`
- Xiaoyunque (剪映小云雀) API handoff + polling + downloading results

This repo is structured as a **skill folder** (root contains `SKILL.md`, plus `agents/`, `references/`, `scripts/`).

## What You Get

- `SKILL.md`: The main workflow and triggering description
- `references/`: Checklists and templates (intake questions, creative roles, pack schema, API notes)
- `scripts/`: Helper scripts (create a production pack; submit/poll/upload/download for Xiaoyunque)

## Requirements

- Python 3
- Xiaoyunque API access key in environment variable: `XYQ_ACCESS_KEY`

## Install

If you use the `skills` installer:

```bash
npx skills add https://github.com/FreddyJerich/short-drama-comic-studio.git -y -g
```

Or install manually by copying this folder into your Codex skills directory, for example on Windows:

- `C:\Users\<you>\.codex\skills\short-drama-comic-studio`

## Use In Chat

Invoke it explicitly:

```text
$short-drama-comic-studio
```

Example request:

```text
用 $short-drama-comic-studio 帮我做一个短漫剧：先系统追问立项，再出剧本、分镜、分镜图，最后走小云雀生成视频（优先 Seedance 2.0 Fast VIP）。
```

## Create A Local Production Pack

```bash
python scripts/init_production_pack.py --title "项目标题" --episodes 5 --style "3D, CG动画" --genre "男频逆袭"
```

This produces a folder with:

- `00_brief.md` / `01_story_bible.md` / `02_episode_script.md`
- `03_storyboard.json` (includes `camera`, `lighting`, `lighting_preset`, `edit_note`)
- `04_asset_bible.md`
- `05_xyq_request.md` (includes model preference)
- `06_director_review.md` (director/DP/lighting/edit checklists)
- `outputs/images/` and `outputs/video/`

## Xiaoyunque API

PowerShell:

```powershell
$env:XYQ_ACCESS_KEY = "<your-access-key>"
```

Submit:

```bash
python scripts/submit_run.py --message "用户最终确认的短剧生成需求（优先选择 Seedance 2.0 Fast VIP）"
```

Poll:

```bash
python scripts/get_thread.py --thread-id THREAD_ID --run-id RUN_ID --after-seq 0
```

Upload reference image/video:

```bash
python scripts/upload_file.py C:\absolute\path\to\reference.png
```

Download results:

```bash
python scripts/download_results.py --urls URL1 URL2 --output-dir ./outputs/video --prefix final
```

## Security

- Never commit real keys. Keep `XYQ_ACCESS_KEY` only in your environment.
- This repo intentionally uses placeholders in docs and scripts.


#!/usr/bin/env python3
"""Initialize a short-drama/comic-drama production pack."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "short-drama-project"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_pack(args: argparse.Namespace) -> Path:
    slug = args.slug or slugify(args.title)
    root = Path(args.output_dir).expanduser().resolve() / slug
    root.mkdir(parents=True, exist_ok=True)
    (root / "outputs" / "images").mkdir(parents=True, exist_ok=True)
    (root / "outputs" / "video").mkdir(parents=True, exist_ok=True)

    write(
        root / "00_brief.md",
        f"""# Brief

Title: {args.title}
Genre: {args.genre}
Format: {args.format}
Ratio: {args.ratio}
Episodes: {args.episodes}
Target duration: {args.duration}
Style: {args.style}
Xiaoyunque model preference: {args.xyq_model}

## User Constraints

- 

## Success Criteria

- 
""",
    )

    write(
        root / "01_story_bible.md",
        """# Story Bible

## Logline


## Core Hook


## World Rules


## Main Characters


## Reversal Mechanism


## Episode Arc

""",
    )

    episode_sections = []
    for episode in range(1, args.episodes + 1):
        episode_sections.append(
            f"""## 第{episode}集：待定标题

目标时长：{args.duration}
核心爽点：
卡点：

### {episode}-1 日 外/内 地点
角色：
道具：
画面：
对白/旁白：
音效：
转场：
"""
        )
    write(root / "02_episode_script.md", "# Episode Script\n\n" + "\n".join(episode_sections))

    storyboard = {
        "project": {
            "title": args.title,
            "ratio": args.ratio,
            "style": args.style,
            "xyq_model": args.xyq_model,
            "format": args.format,
            "episodes": args.episodes,
        },
        "clips": [],
    }
    write(root / "03_storyboard.json", json.dumps(storyboard, ensure_ascii=False, indent=2) + "\n")

    write(
        root / "04_asset_bible.md",
        """# Asset Bible

## Roles

| Name | Function | Visual Description | Voice | Continuity Notes |
| --- | --- | --- | --- | --- |

## Scenes

| Name | Visual Description | Lighting | Recurring Objects | Continuity Notes |
| --- | --- | --- | --- | --- |

## Props

| Name | Owner | Plot Function | Close-up Notes |
| --- | --- | --- | --- |
""",
    )

    write(
        root / "05_xyq_request.md",
        f"""# Xiaoyunque Request

请生成一部{args.format}。

标题：{args.title}
画面比例：{args.ratio}
视觉风格：{args.style}
类型：{args.genre}
集数：{args.episodes}
单集目标时长：{args.duration}
模型优先级：优先选择 {args.xyq_model} 生成视频；如果不可用，请先确认再切换其他模型。

请保持角色、场景、服装、声音和关键道具在全剧中一致。按分集输出，并在可以时合成全集。

## Attachments

Asset IDs:

## Final Approved Message

""",
    )

    write(
        root / "06_director_review.md",
        """# Director Review

Use this file to review the project before generating keyframes or submitting to Xiaoyunque.

## Short-Drama Director

- Dramatic intention:
- Performance action:
- Hook/card point:
- Required rewrite:

## Cinematographer / DP

- Shot language:
- Camera movement:
- Spatial relationship:
- 9:16 readability:

## Lighting Director

- Lighting preset:
- Light motivation:
- Contrast and color:
- Character readability:
- Continuity risk:

Reference presets: 逆光=英雄/神秘/浪漫；顶光=压迫/权威/神秘；丁达尔=史诗感/电影感；底光=诡异/黑化；侧光=紧张冲突/内心冲突；硬光=张力/压迫/攻击性；柔光=干净/温暖/亲情；蝴蝶光=精致贵气/主角感。

## Editing Director

- Rhythm:
- Cut points:
- Clip duration issues:
- Episode ending/card point:

## Approval

- Ready for $imagegen keyframes:
- Ready for Xiaoyunque submission:
""",
    )

    return root


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a standard short-drama/comic-drama production pack.")
    parser.add_argument("--title", required=True, help="Project title")
    parser.add_argument("--episodes", type=int, default=5, help="Episode count")
    parser.add_argument("--style", default="3D, CG动画", help="Visual style")
    parser.add_argument("--genre", default="短剧", help="Genre or audience lane")
    parser.add_argument("--format", default="短剧/短漫剧", help="Project format")
    parser.add_argument("--ratio", default="9:16", help="Aspect ratio")
    parser.add_argument("--duration", default="45-60s", help="Target duration per episode")
    parser.add_argument("--xyq-model", default="Seedance 2.0 Fast VIP", help="Preferred Xiaoyunque video model")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--slug", default="", help="Optional folder slug")
    args = parser.parse_args()

    if args.episodes < 1:
        raise SystemExit("--episodes must be >= 1")

    root = build_pack(args)
    print(root)


if __name__ == "__main__":
    main()

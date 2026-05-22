# short-drama-comic-studio（中文版）

这是一个 Codex Skill，用于把短剧/短漫剧项目从“立项到成片”跑通并标准化：

- 类 Plan 模式的系统追问（立项刨根问底）
- 剧本大纲、分集脚本、分镜/故事板结构化
- 创作部门审稿（短剧导演 + 摄影指导/DP + 灯光师 + 剪辑导演）
- 通过 `$imagegen` 生成分镜图/关键帧/角色图/场景图（raster 图片）
- 调用剪映小云雀（Xiaoyunque）API：提交任务、轮询进度、下载结果

本仓库按 **Skill 目录结构**组织（根目录包含 `SKILL.md`，并带 `agents/`、`references/`、`scripts/`）。

## 你会得到什么

- `SKILL.md`：技能触发描述 + 标准工作流（含追问模式、审稿模式、小云雀模型偏好）
- `references/`：问题库、审稿清单、制作包结构、API 说明等
- `scripts/`：生产工具脚本（初始化制作包；小云雀 submit/poll/upload/download）

## 环境要求

- Python 3
- 小云雀 API Key（环境变量）：`XYQ_ACCESS_KEY`

## 安装

如果你使用 `skills` 安装器：

```bash
npx skills add https://github.com/FreddyJerich/short-drama-comic-studio.git -y -g
```

或者手动安装：把整个目录复制到你的 Codex skills 目录（Windows 举例）：

- `C:\Users\<you>\.codex\skills\short-drama-comic-studio`

## 在对话中使用

显式调用：

```text
$short-drama-comic-studio
```

示例：

```text
用 $short-drama-comic-studio 帮我做一个短漫剧：先系统追问立项，再出剧本、分镜、分镜图，最后走小云雀生成视频（优先 Seedance 2.0 Fast VIP）。
```

## 初始化本地制作包（推荐）

```bash
python scripts/init_production_pack.py --title "项目标题" --episodes 5 --style "3D, CG动画" --genre "男频逆袭"
```

会生成一个标准目录，包含：

- `00_brief.md` / `01_story_bible.md` / `02_episode_script.md`
- `03_storyboard.json`（含 `camera`、`lighting`、`lighting_preset`、`edit_note`）
- `04_asset_bible.md`
- `05_xyq_request.md`（包含模型偏好）
- `06_director_review.md`（导演/摄影/灯光/剪辑审稿清单）
- `outputs/images/` 与 `outputs/video/`

## 小云雀 API（剪映小云雀）

PowerShell 设置 Key：

```powershell
$env:XYQ_ACCESS_KEY = "<your-access-key>"
```

提交任务（建议把模型偏好写进 message）：

```bash
python scripts/submit_run.py --message "用户最终确认的短剧生成需求（优先选择 Seedance 2.0 Fast VIP）"
```

轮询进度：

```bash
python scripts/get_thread.py --thread-id THREAD_ID --run-id RUN_ID --after-seq 0
```

上传参考图/视频：

```bash
python scripts/upload_file.py C:\absolute\path\to\reference.png
```

下载产物：

```bash
python scripts/download_results.py --urls URL1 URL2 --output-dir ./outputs/video --prefix final
```

## 安全说明

- 不要把真实 Key 写进文件或提交到仓库，`XYQ_ACCESS_KEY` 只放环境变量。
- 本仓库文档与脚本只使用占位符，不包含真实密钥。


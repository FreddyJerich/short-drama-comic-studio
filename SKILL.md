---
name: short-drama-comic-studio
description: "Build a standard short drama or comic-drama production workflow from idea to deliverables, starting each new project with a systematic Plan-mode-style interrogation before creating: concept audit, episode script, narration-style script, storyboard plan, director/DP/lighting/editor review, storyboard/keyframe image prompts, role and scene asset bible, image generation through $imagegen, Xiaoyunque/Pippit submission message, API polling, and final video download. Use when the user asks for 短剧, 漫剧, 短漫剧, 剧本, 分镜, 分镜图, 资产库, 旁白型剧本, 小云雀, xyq, Pippit, or a standard process that generates script, storyboard images, and final video."
---

# Short Drama Comic Studio

Use this skill to run a controlled short-drama/comic-drama pipeline before submitting to Xiaoyunque. Prefer it when the user wants a repeatable production process, editable scripts, storyboard/keyframe images, asset consistency, or a final API-generated video.

## Operating Modes

- **New project interrogation**: At the start of a new short-drama/comic-drama conversation or when the user's intent is vague, ask systematic follow-up questions before producing scripts, images, or video requests.
- **Production pack first**: Create local deliverables for review: brief, story bible, episode script, storyboard JSON, asset bible, keyframe prompts, and Xiaoyunque request.
- **Creative department pass**: Before finalizing scripts, storyboards, keyframes, or Xiaoyunque requests, review them through four roles: short-drama director, cinematographer/DP, lighting director, and editing director.
- **Generate visual references**: Create storyboard/keyframe images only after script and asset bible are stable. Use `$imagegen` for all raster image generation or editing, including character sheets, scene concepts, storyboard panels, and keyframes.
- **Submit to Xiaoyunque**: Send a consolidated request through the bundled `scripts/submit_run.py`, prioritizing `Seedance 2.0 Fast VIP` as the Xiaoyunque video model, then poll with `scripts/get_thread.py` and download results with `scripts/download_results.py`.
- **Direct handoff**: If the user explicitly wants Xiaoyunque to handle all creative planning, use the Xiaoyunque scripts with the user's original wording instead of rewriting it.

## New Project Interrogation

For every new project conversation, behave like a planning interviewer before creating. Do not jump straight into a script unless the user explicitly says to skip questioning.

Ask questions in batches, not as a single wall of text. Start with 8-12 essential questions covering:

- story seed, genre, target audience, and platform
- short drama vs comic-drama vs narrated comic
- desired emotion:爽感,反转,悬疑,虐恋,喜剧,治愈,恐怖, etc.
- protagonist, antagonist, relationship pressure, and core contradiction
- episode count, target duration, ratio, language, and subtitle needs
- visual style, reference works, forbidden styles, and content limits
- whether to create a local production pack, storyboard images with `$imagegen`, Xiaoyunque video, or all three
- deadline, quality bar, and whether credits/API calls may be consumed

After the user answers, ask a second round only for contradictions, missing constraints, or choices that change production cost. Then summarize the project plan and wait for confirmation before generating production deliverables or submitting to Xiaoyunque.

## Workflow

1. For a new project, run **New Project Interrogation** first. Infer defaults only after the user has answered or explicitly asks to skip: 9:16, 3-5 episodes, 35-75 seconds per episode, strong first-3-second hook, short vertical-video pacing.
2. If the user wants files, initialize a pack:

```bash
python {baseDir}/scripts/init_production_pack.py --title "项目标题" --episodes 5 --style "3D, CG动画" --genre "男频逆袭"
```

3. Produce the core text deliverables in this order:
   - logline and sellable premise
   - story bible and character stakes
   - episode outline
   - narration-style or dialogue-style script
   - storyboard plan with clip durations and card points
   - director/DP/lighting/editor review notes
   - asset bible for roles, scenes, props, voices, and visual continuity
4. Run the **Creative Department Pass** before image generation or video submission. The director checks dramatic intent and performance; the cinematographer checks framing and camera motion; the lighting director checks mood, space, and readability; the editing director checks rhythm, card points, and continuity.
5. For storyboard/keyframe images, make one stable visual prompt per important shot or clip. Keep character descriptors consistent with the asset bible. Include camera, lens/framing, lighting, and edit purpose in the prompt. When the user asks to generate those images, invoke `$imagegen` and keep final project-bound images under the pack's `outputs/images/` folder.
6. Before video submission, build a single Xiaoyunque request that includes style, ratio, episode list, asset requirements, storyboard intent, role-based creative notes, model preference `Seedance 2.0 Fast VIP`, and what must remain consistent.
7. Submit only after the user asks to generate or approves the pack. Do not hardcode access keys. Read `XYQ_ACCESS_KEY` from the environment.

## Xiaoyunque API

Use the bundled scripts:

```bash
python {baseDir}/scripts/submit_run.py --message "生成一部短剧..."
python {baseDir}/scripts/get_thread.py --thread-id THREAD_ID --run-id RUN_ID --after-seq 0
python {baseDir}/scripts/upload_file.py C:\path\to\reference.png
python {baseDir}/scripts/download_results.py --urls URL1 URL2 --output-dir ./outputs/video --prefix final
```

Default Xiaoyunque video model preference: `Seedance 2.0 Fast VIP`. Include this preference in the submitted message. If Xiaoyunque cannot use that model or asks for confirmation, pause and ask the user before choosing a fallback.

PowerShell session-only key setup:

```powershell
$env:XYQ_ACCESS_KEY = "<access-key>"
```

Never write real access keys into `SKILL.md`, references, project packs, source files, or logs.

## References

- Read `references/production_workflow.md` when building or reviewing the full process.
- Read `references/intake_questions.md` when starting a new project or when the user asks to be questioned systematically.
- Read `references/creative_roles.md` when writing, revising, or reviewing scripts, storyboards, keyframes, and Xiaoyunque requests.
- Read `references/pack_schema.md` when creating or validating a project pack.
- Read `references/xyq_api.md` when submitting, polling, uploading references, or downloading generated videos.

# Production Workflow

## Purpose

Use this workflow to turn a short-drama or comic-drama idea into a controlled production pack and, when requested, a Xiaoyunque video generation request.

## Stage 1 - Intake And Interrogation

At the start of every new short-drama/comic-drama project, run a planning interview before drafting. The goal is to surface the hidden production constraints that normally cause weak scripts, inconsistent assets, or wasted video-generation credits.

Use two rounds:

1. **Round 1: foundation questions** - ask for story, audience, format, style, duration, output path, and constraints.
2. **Round 2: pressure-test questions** - ask only about contradictions, missing stakes, unclear viewer payoff, visual consistency risks, or choices that change generation cost.

After both rounds, produce a concise project plan with assumptions and ask for confirmation before creating deliverables.

Capture or infer:

- title or working title
- genre and audience: male-frequency, female-frequency, comedy, suspense, romance, fantasy, workplace, family, etc.
- format: short drama, comic-drama, narrated comic, cinematic animation, live-action style, mixed media
- episode count and target duration
- aspect ratio, usually 9:16
- visual style: 3D CG, anime, manhua panel motion, cinematic realism, ink comic, etc.
- non-negotiables: characters, platform rules, references, IP restrictions, forbidden content

If the user provides only a seed idea, do not immediately create a default pack. Ask the interrogation questions first unless the user explicitly says to skip questioning. If the user skips, use 5 episodes, 45-60 seconds each, 4-8 clips per episode.

## Stage 2 - Story Engine

Write these before detailed scenes:

1. **Logline**: one sentence with protagonist, pressure, reversal, and payoff.
2. **Core hook**: what viewers understand in the first 3 seconds.
3. **Contradiction**: why the protagonist appears weak, wrong, poor, rejected, or doomed.
4. **Power/reversal mechanism**: system, hidden identity, skill, rebirth, secret, contract, social proof, or emotional truth.
5. **Escalation ladder**: each episode must raise stakes and end on a card point.
6. **Emotional promise**: revenge, protection, face-slapping, salvation, romance tension, comedy payoff, mystery reveal.

## Stage 3 - Script Format

Use one of two formats:

- **Narration-style script** for comic-drama or AI video: short descriptive lines, VO, on-screen captions, minimal dialogue.
- **Dialogue-style script** for dramatic acting: location, time, action, dialogue, sound, card point.

Episode block:

```markdown
## 第1集：标题

目标时长：45s
核心爽点：
卡点：

### 1-1 日 外 地点
角色：
道具：
画面：
对白/旁白：
音效：
转场：
```

## Stage 4 - Creative Department Pass

Before locking scripts, storyboards, keyframes, or Xiaoyunque requests, review them through four production roles. See `creative_roles.md` for detailed checklists.

- **Short-drama director**: clarify the episode's dramatic intention, hook, performance action, and emotional turn.
- **Cinematographer/DP**: specify framing, camera height, movement, shot size, lens feeling, and spatial relationship.
- **Lighting director**: specify key light motivation, contrast, color temperature, readability, atmosphere, and continuity.
- **Editing director**: specify clip duration, beat order, cut point, card point, rhythm, and what the viewer must understand before the next clip.

Add a concise note from each role to every major episode or clip. If a note does not change the shot, omit it rather than padding.

## Stage 5 - Asset Bible

Create assets before image or video generation:

- roles: name, function, age range, body, face, hair, outfit, symbolic item, emotional range, voice description
- scenes: name, era, geography, lighting, palette, recurring objects, danger level
- props: item, owner, plot function, visual close-up use
- continuity notes: what must never change across episodes

For Xiaoyunque-style asset libraries, align role and scene names with script references so they can be reused consistently.

## Stage 6 - Storyboard And Keyframes

For each clip, define:

- clip id, episode id, duration between 4 and 15 seconds
- scene reference
- role references, at most a few per clip
- action beat
- camera framing and movement
- emotion and expression
- lighting intent, preferably using the lighting vocabulary in `creative_roles.md`: 逆光, 顶光, 丁达尔光, 底光, 侧光, 硬光, 柔光, 蝴蝶光
- edit purpose and cut point
- dialogue or VO
- caption/card point
- keyframe prompt

Generate storyboard/keyframe images only after the asset bible is stable. Use one image per major clip unless the user requests a full panel board.

When images are requested, use `$imagegen` as the image generation/editing path. Do not substitute SVG, HTML/CSS, or ad hoc placeholders for role sheets, scene concepts, storyboard panels, or keyframes unless the user explicitly asks for non-raster output.

Default `$imagegen` image types:

- role sheet: full-body character reference on a clean background
- scene concept: reusable environment reference with stable lighting and layout
- storyboard panel: single shot with framing, action, and emotion
- keyframe: polished representative frame for Xiaoyunque video reference

Save project-bound image outputs into `outputs/images/` and keep filenames tied to the storyboard id, such as `ep01_clip03_keyframe.png`.

## Stage 7 - Xiaoyunque Request

Build a single request that says exactly what to generate:

- project type: short drama, comic-drama, narrated comic, etc.
- ratio, style, episode count, target duration
- title and story summary
- full episode scripts or storyboard summary
- asset consistency requirements
- director/DP/lighting/editor notes that should influence video generation
- model preference: prioritize `Seedance 2.0 Fast VIP`
- whether reference images/videos are attached by asset id
- output expectation: separate episode videos, full merged video, or both

Submit only after user approval when the request may consume credits. If `Seedance 2.0 Fast VIP` is unavailable or Xiaoyunque requests another model choice, ask the user before falling back.

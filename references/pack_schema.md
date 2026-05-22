# Production Pack Schema

Use this file to create or inspect a local production pack.

## Folder Layout

```text
project-slug/
  00_brief.md
  01_story_bible.md
  02_episode_script.md
  03_storyboard.json
  04_asset_bible.md
  05_xyq_request.md
  06_director_review.md
  outputs/
    images/
    video/
```

## Required Fields

`00_brief.md`

- title
- genre
- format
- ratio
- episode count
- target duration
- style
- user constraints

`01_story_bible.md`

- logline
- story premise
- world rules
- protagonist desire
- antagonist pressure
- reversal mechanism
- episode arc

`02_episode_script.md`

- one section per episode
- each episode has title, target duration, scenes, action, dialogue/VO, sound, card point

`03_storyboard.json`

```json
{
  "project": {
    "title": "",
    "ratio": "9:16",
    "style": "",
    "episodes": 5
  },
  "clips": [
    {
      "episode": 1,
      "clip": "1-1",
      "duration_seconds": 8,
      "scene": "",
      "roles": [],
      "action": "",
      "camera": "",
      "lighting": "",
      "lighting_preset": "",
      "edit_note": "",
      "dialogue_or_vo": "",
      "caption": "",
      "keyframe_prompt": ""
    }
  ]
}
```

`04_asset_bible.md`

- roles
- scenes
- props
- voice descriptions
- continuity constraints

`05_xyq_request.md`

- final message to submit to Xiaoyunque
- attached asset ids if any
- desired outputs and polling notes
- model preference: `Seedance 2.0 Fast VIP`

`06_director_review.md`

- short-drama director notes
- cinematographer/DP notes
- lighting director notes
- editing director notes
- blocking issues and required rewrites

`outputs/images/`

- store images generated through `$imagegen`
- use stable names such as `role-linxiao-front.png`, `scene-wasteland-street.png`, or `ep01_clip01_keyframe.png`
- do not leave project-bound generated images only in a default image cache path

## Quality Checks

- Every named role in storyboard appears in the asset bible.
- Every scene in storyboard appears in the asset bible.
- Clip durations stay between 4 and 15 seconds for Xiaoyunque-style video editing.
- Each episode has at least one card point.
- Any generated role, scene, storyboard, or keyframe image was produced through `$imagegen` unless the user explicitly selected another path.
- Major clips include camera, lighting, and edit-purpose notes.
- Lighting notes choose a purposeful preset when useful: 逆光, 顶光, 丁达尔光, 底光, 侧光, 硬光, 柔光, or 蝴蝶光.
- `06_director_review.md` confirms director/DP/lighting/editor review before Xiaoyunque submission.
- The Xiaoyunque request is a single coherent instruction, not many small prompts.

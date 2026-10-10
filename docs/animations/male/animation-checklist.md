# Man4 body animation checklist

Previews show original male UO body 400, facing down-left. Playback speed is illustrative. Static slots display a single pose; mounted previews show the rider without a mount, and weapon actions show the body without equipment.

Scope: the 35 classic human action slots used by our male body 400 target. All 35 have reference data in the installed client's anim.mul. This checklist does not cover creature bodies or later extended body-specific animation sets.

One slot is approved (unarmed run); 34 remain. Four slots are single poses (4, 7, 8, 25), so those can be built manually without finding a moving stock clip. Frame counts below were read from the installed client and match across all five stored directions.

Animation names and IDs: [ClassicUO PeopleAnimationGroup](https://github.com/ClassicUO/ClassicUO/blob/main/src/ClassicUO.Assets/AnimationsLoader.cs#L1593). IDs are action IDs, not direction-block offsets.

| ID | Body animation | UO frames per direction | Stock search phrase | Status | Down-left original UO preview |
|---:|---|---:|---|---|---|
| 0 | Walk, unarmed | 10 | in-place relaxed walk | To source or create  ![Action 0](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-00-down-left.gif>) |
| 1 | Walk, armed | 10 | walk carrying weapon | To source or create  ![Action 1](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-01-down-left.gif>) |
| 2 | Run, unarmed | 10 | in-place run | Approved: 90.0022% run fit  ![Action 2](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-02-down-left.gif>) |
| 3 | Run, armed | 10 | run carrying weapon | To source or create  ![Action 3](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-03-down-left.gif>) |
| 4 | Neutral standing pose | 1 | relaxed standing idle | To source or create  ![Action 4](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-04-down-left.gif>) |
| 5 | Idle fidget 1 | 5 | standing idle gesture | To source or create  ![Action 5](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-05-down-left.gif>) |
| 6 | Idle fidget 2 | 5 | standing idle gesture | To source or create  ![Action 6](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-06-down-left.gif>) |
| 7 | One-handed combat ready pose | 1 | one-handed weapon combat idle | To source or create  ![Action 7](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-07-down-left.gif>) |
| 8 | Two-handed combat ready pose | 1 | two-handed weapon combat idle | To source or create  ![Action 8](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-08-down-left.gif>) |
| 9 | One-handed attack | 7 | one-handed sword slash | To source or create  ![Action 9](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-09-down-left.gif>) |
| 10 | Unarmed attack 1 | 7 | unarmed punch variant 1 | To source or create  ![Action 10](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-10-down-left.gif>) |
| 11 | Unarmed attack 2 | 7 | unarmed punch variant 2 | To source or create  ![Action 11](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-11-down-left.gif>) |
| 12 | Two-handed downward attack | 7 | two-handed overhead chop | To source or create  ![Action 12](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-12-down-left.gif>) |
| 13 | Two-handed wide attack | 7 | two-handed horizontal swing | To source or create  ![Action 13](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-13-down-left.gif>) |
| 14 | Two-handed thrust | 7 | spear thrust | To source or create  ![Action 14](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-14-down-left.gif>) |
| 15 | Combat walk | 10 | combat walk weapon ready | To source or create  ![Action 15](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-15-down-left.gif>) |
| 16 | Directed spell cast | 7 | forward spell casting gesture | To source or create  ![Action 16](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-16-down-left.gif>) |
| 17 | Area spell cast | 7 | area spell casting gesture | To source or create  ![Action 17](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-17-down-left.gif>) |
| 18 | Bow attack | 7 | bow draw and release | To source or create  ![Action 18](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-18-down-left.gif>) |
| 19 | Crossbow attack | 7 | crossbow aim and fire | To source or create  ![Action 19](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-19-down-left.gif>) |
| 20 | Hit reaction | 5 | standing hit reaction | To source or create  ![Action 20](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-20-down-left.gif>) |
| 21 | Death 1 | 6 | falling death variant 1 | To source or create  ![Action 21](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-21-down-left.gif>) |
| 22 | Death 2 | 6 | falling death variant 2 | To source or create  ![Action 22](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-22-down-left.gif>) |
| 23 | Mounted slow riding | 5 | horse rider walk cycle | To source or create  ![Action 23](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-23-down-left.gif>) |
| 24 | Mounted fast riding | 5 | horse rider run cycle | To source or create  ![Action 24](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-24-down-left.gif>) |
| 25 | Mounted stationary pose | 1 | horse rider idle | To source or create  ![Action 25](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-25-down-left.gif>) |
| 26 | Mounted melee attack | 5 | horseback weapon attack | To source or create  ![Action 26](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-26-down-left.gif>) |
| 27 | Mounted bow attack | 5 | horseback bow shot | To source or create  ![Action 27](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-27-down-left.gif>) |
| 28 | Mounted crossbow attack | 7 | horseback crossbow shot | To source or create  ![Action 28](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-28-down-left.gif>) |
| 29 | Mounted slap / urge mount | 5 | rider urge horse gesture | To source or create  ![Action 29](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-29-down-left.gif>) |
| 30 | Turn gesture | 5 | standing turn gesture | To source or create  ![Action 30](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-30-down-left.gif>) |
| 31 | Unarmed attack while walking | 7 | moving unarmed attack | To source or create  ![Action 31](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-31-down-left.gif>) |
| 32 | Bow emote | 5 | standing respectful bow | To source or create  ![Action 32](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-32-down-left.gif>) |
| 33 | Salute emote | 5 | standing salute | To source or create  ![Action 33](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-33-down-left.gif>) |
| 34 | Idle fidget 3 | 5 | standing idle gesture | To source or create  ![Action 34](<C:/Users/jim/Documents/ChatGPT/UO Server/graphics/man4-animation-library-v01/previews/action-34-down-left.gif>) |

## Suggested work order

1. Neutral stand (4), unarmed walk (0), armed walk/run (1, 3), and combat walk (15).
2. Combat ready poses (7, 8); melee attacks (9–14, 31); bow/crossbow (18, 19).
3. Spell casting (16, 17), hit reaction (20), and both deaths (21, 22).
4. Mounted actions (23–29), using a consistent mount position for the rider.
5. Fidgets, turn, and emotes (5, 6, 30, 32–34).

## Choosing stock clips

A rough match in posture, hand use, and motion is enough to start. The stock clip does not need the exact UO frame count: we can retarget it to Man4, select or resample suitable poses, and compare against all five reference views. Prefer in-place locomotion clips, with consistent facing and no baked travel. Keep candidates separate so failed matches cannot overwrite the approved model.

Search phrases are starting points, not exact descriptions of the UO sprites. Inspect the original reference sequence before deciding which punch, death, fidget, or turn variant to use. Each numbered variant remains a separate target.

Mounted actions here describe the rider's body. Animating a new mount itself would be a separate creature project.

## Preserving the approved run

The approved model includes animation-dependent run corrective shape keys. When building a multi-action library, make these corrections action-specific; frame-number-only drivers must not apply the run's corrections to every new action. Preserve its existing rig, approved run, and anatomy in an immutable master and develop each new action in a copy.

The run's 90.0022% score applies only to its measured 50 views, not to this entire future library. Every newly fitted action needs its own comparison and silhouette review.

Approved master: `C:\Users\jim\Documents\ChatGPT\UO Server\graphics\man4-run-shape-optimization-v01\model\man4_uo_optimized.blend`

Track candidate paths and fitted results in animation_catalog.json. Only the approved run has an existing measured score.

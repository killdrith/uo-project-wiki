# Subversive axe client test

This private ClassicUO client and UO asset copy replaces the equipped War Axe
animation (644). Its original backpack, ground and paperdoll artwork remains.
The original UO installation, normal ClassicUO profile, server code and saves
were not modified. All War Axes seen through this test client share the reskin.

## Start and spawn

1. If Subversive is stopped, run `Start Subversive Server.cmd`. If it is already
   running, keep that existing instance; do not start a second server.
2. Run `Launch Axe Test.cmd`. This directly opens the separate ClassicUO client
   using this folder's `client/settings.json` and `uo-data`.
3. Log in with your existing owner account and a male human character.
4. Type `[add WarAxe` and click the ground to create the test weapon.
5. Type `[set Animation Slash1H` and target that War Axe. IMPORTANT: stock
   WarAxe uses Bash1H (action 11); our approved one-handed attack is Slash1H
   (action 9). This per-item property makes the server select the right motion.
6. Type `[set Hue 0` and target it, then equip it in your right hand.
   Optional: `[set Name Test Axe` and target it to label it.

The property overrides affect only the item you target; no weapon class or
server engine change is needed. Inventory and paperdoll still show the stock
War Axe intentionally. The in-world held axe should be our new model.

## On-foot test

Start without armor to inspect grip and occlusion, then try your usual outfit.
Check idle, all eight directions, walk/run, war-mode ready and combat walk,
and ordinary attacks. Test picking up, dragging, dropping and equipping.
Record animation/direction/frame and a screenshot for any alignment issue.

22 approved actions (17 on foot plus five mounted) are installed across five stored directions.
Movement slots 0 and 2 additionally alias our armed walk/run for clients that
request those slots while carrying a weapon. The remaining action entries are
stock. Female, elf and gargoyle use are outside this test.
The male-fit reskin occupies a shared equipment animation slot, so other
bodies may also display it, without having been fitted for those bodies.

The PNG's alpha is converted to binary UO transparency at 128; colors become
RGB555 with at most 256 colors per action/direction block. Cropped frames retain
the exact (128,168) anchor. GIF previews are decoded from installed MUL blocks,
not the pre-conversion PNGs. In-game clothing layering and playback still need
the live test; an offline decode does not establish those behaviors.

## Return to normal

Close this test client and reopen your usual ClassicUO launcher/profile. The
original data is untouched. The test item's Animation override can be restored
with `[set Animation Bash1H`, or the temporary item can be deleted.
Safely stop the server, if desired, with `[admin` -> Administer -> Server ->
Shutdown (With Save).

## Recorded checks

`metadata/verification.json` has the encoder/installed-block checks;
`metadata/patched-blocks.json` lists every changed index entry;
`metadata/source-client-manifest.json` records original client file hashes;
`metadata/baseline-anim.idx` preserves the pristine index.
The original bytes in anim.mul remain intact; new blocks were appended.
Re-running `scripts/build_client_test.py` rebuilds all on-foot and mounted actions from pristine source files.

## Mounted test (v02)

Close the v01 test client, leaving Subversive running, then launch this v02
client with `Launch Axe Test.cmd`. Log in with the same character and use the
existing test axe; its Slash1H property remains stored by the server.

All five supported mounted actions are replaced: stationary (25), slow riding
(23), fast riding (24), melee attack (26), and slap/urge mount (29).
Walk and run normally while mounted and rotate through all eight directions.
Attack an ordinary creature in melee range. Slash1H selects mounted action 26.
If Blessed prevents attacks, `[set Blessed false` targeting yourself allows
combat; restore `[set Blessed true` afterwards if desired.

For stationary attack previews without fighting, stand still while mounted:

    [animate 26 5 1 true false 0

For slap/urge mount:

    [animate 29 5 1 true false 0

The horse masking was calibrated for the gray horse, body 226 / mount item
0x3EA0 (16032). For a matching test horse, dismount; use `[set Body 226` and
`[set ItemID 16032`, targeting the horse each time; then remount. Change both
properties together so standing and mounted horse art agree. Record the old
values first if you want to restore a different horse variant later.

Only far-side head/mane overlap is removed, using the established side-view
horse regions intersected with the current original horse frame. Front/back
are unchanged. This is a test of those specific masks, not a universal horse
depth system; different mounts can require different cutouts. Review previews
compose the decoded axe over the original UO rider and horse.

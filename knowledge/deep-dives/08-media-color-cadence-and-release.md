# Media, color, cadence, dan release

Menghubungkan D03, D27, D28, D29, D38, D39 dan D40. FFmpeg examples below are reference commands, NOT_RUN in this build; no video deliverable is claimed.

## Delivery contract

Declare width/height, pixel aspect, display aspect, rational frame rate, frame count, first PTS, duration convention, audio sample rate/channels, color primaries/transfer/range, alpha requirement, codec/container and playback target. "MP4 1080p" leaves cadence, color, audio and compatibility ambiguous.

Frame n for rate p/q has t=nq/p. N frames nominally cover Nq/p under fixed-frame-duration convention; last sample time is (N−1)q/p. Distinguish tail display duration from sample timestamp. If brief needs endpoint visible, plan hold frames/evaluation policy.

## Source to encode

Frames must be complete and correctly ordered. Hash/list inputs before job; missing frame can produce partial output or timeline shift depending input method. Example reference command:

```bash
ffmpeg -framerate 60 -i frames/%06d.png -c:v libx264 -pix_fmt yuv420p output.mp4
```

Assumptions: numbered PNG sequence starts according FFmpeg defaults, encoder available, dimensions compatible with chosen pixel format, source color interpretation reviewed. This command alone does not preserve alpha or establish explicit HDR/color conversion. Actual installed FFmpeg/version and input metadata determine options required.

## Color and alpha

Track working space from image creation through composite to output. Alpha may be lost in an opaque codec; straight/premultiplied mix can create halos before encoding. Metadata tag is not pixel conversion. Linear-light arithmetic and output transfer should happen intentionally; avoid repeated decode/encode transfers at intermediate stages.

YUV chroma subsampling can soften colored text/edges, particularly with motion. Bit depth affects banding; compression artifacts vary with scene detail and dynamics. Evaluate fast motion, gradients, small typography and transparency requirements, not only static beauty frame.

## Audio alignment

Audio samples and video frames need shared timeline mapping. Encoder delay, trims, padding, resampling and container timebase can affect first event and drift. Equal stream duration does not prove aligned cues. Use known markers near beginning, middle and end and inspect decoded signals; perception is a separate question.

## Decode verification

Reference inspection:

```bash
ffprobe -v error -show_streams -show_format -of json output.mp4
ffprobe -v error -select_streams v:0 -show_frames -of json output.mp4
ffmpeg -v error -i output.mp4 -f null -
```

Metadata inspection checks declared properties; frame information checks PTS/count as supplied by tool; full decode reveals corrupt/undecodable content. They still do not verify subject/message/comfort. Actual playback on target can reveal unsupported codec, color mismatch or dropped presentation frames.

## Reproducible release

Retain scene/timeline configuration, source assets identity, fonts, renderer/encoder versions, render settings, output hash and review notes. Render farm job complete means work completed, not output accepted. Re-render only impacted stage when inputs unchanged and cache valid. Preview and final differences must be documented.

For deployed motion app, analogous checks concern production bundle, asset loading, feature fallback, focus/input lifecycle and device performance. Publishing stage must use actual target authorization; a repository of examples is not itself a deployed product.

## Final decision

Compare expected contract and actual output, classify defects by timeline, rendering, compositing, encoding, playback or human experience. Keep NOT_RUN properties visible. Python rational-cadence lab verifies timestamp arithmetic only; it does not execute these FFmpeg commands or verify audio/video sync.

# /compress-video — Compress video for Discord/sharing

Compress a video file to fit within a target size limit, optimized for Discord upload.

## Arguments

`$ARGUMENTS`

- First argument: path to the video file (required)
- Second argument: target size in MB (optional, default: 24)

## Instructions

1. **Probe the source file**:
   ```
   ffprobe -v quiet -print_format json -show_format -show_streams "<path>"
   ```
   Extract: duration, resolution, codec, file size. Print a one-line summary.

2. **Calculate target bitrate**:
   - Target size in bits = `target_MB * 8 * 1024 * 1024`
   - Audio budget = `96kbps * duration_seconds`
   - Video bitrate = `(target_bits - audio_budget) / duration_seconds`
   - If video bitrate < 500kbps, warn that quality will be very low

3. **Choose scale**:
   - If source width > 1920: scale to 1920:-2
   - If source width > 1280 and target < 10MB: scale to 1280:-2
   - Otherwise: keep original resolution

4. **Compress**:
   - Output path: same directory as source, filename `<original_name>_discord.mp4`
   - Use ffmpeg with unix-style `/c/` input path but write output to current working directory first, then move:
   ```
   ffmpeg -i "<input>" -vf "scale=<W>:-2" -c:v libx265 -b:v <bitrate>k -preset medium -c:a aac -b:a 96k -y "<output_name>"
   ```
   - Run in background with `run_in_background: true`

5. **After completion**: Report input size, output size, compression ratio, and the output file path.

## Path handling (Windows/MSYS2)

ffmpeg on Windows cannot write to `/c/` style paths. Always write output to the current working directory, then move if needed:
```bash
ffmpeg -i "/c/Users/..." -y "output_name.mp4"
# then if needed:
mv output_name.mp4 "/c/Users/atayl/Videos/"
```

## Examples

- `/compress-video C:\Users\atayl\Videos\recording.mp4` — compress to under 24MB
- `/compress-video C:\Users\atayl\Videos\recording.mp4 8` — compress to under 8MB
- `/compress-video C:\Users\atayl\Videos\recording.mp4 50` — compress to under 50MB (Nitro)

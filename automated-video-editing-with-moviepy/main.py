from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx, CompositeAudioClip

clip1 = VideoFileClip("video1.mp4").subclip(10, 15).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)
clip2 = VideoFileClip("video2.mp4").subclip(10, 15).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

clip3 = VideoFileClip("video2.mp4").subclip(5, 10).fx(vfx.colorx, 1.5).fx(vfx.lum_contrast, 0, 50, 128)

audio = AudioFileClip("audio1.mp3").subclip(1, 15).fx(afx.audio_fadein, 1).fx(afx.volumex, 0.2)

combined = concatenate_videoclips([clip1, clip2, clip3])
combined.audio = CompositeAudioClip([audio])

combined.write_videofile("combined.mp4")
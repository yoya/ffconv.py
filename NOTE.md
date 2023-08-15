 -start_frame 215 <= -start 215
 -end_frame 215 <= -end 215
 -vf trim=start_frame=299:end_frame=600
 -ss 0:0:215 <= -start 215s
 -end_frame 215 <= -end 215s
 -i frame-%05d.jpg

 -vf "setpts=PTS*2"  -af "atempo=0.5" <= -speeddown 2
 -vf "setpts=PTS/2"  -af "atempo=2"  <= -speedup 2  [0.5...2.0]
 -r <= -rate

 -vcodec libx264 -pix_fmt yuv420p <= slow.mp4

 -vf crop="w=620:h=424:x=0:y=3" <= -crop 620x424+0+3

 -vf colorchannelmixer=.7:.4:.1:0:.2:.8:.1:0:.1:.3:.5 <= -color-matrix=".7 .4 . 0 .2 .8 .1 0 .1 .3 .5"
 -vf colorchannelmixer=.7:.4:.1:0:.2:.8:.1:0:.1:.3:.5,vignette <= -aged

 -an <= -an -no-audio help
 -vn <= -vn -no-video help
 -vf split[a][b];[a]palettegen[pal];[b][pal]paletteuse <= -palette

 -vf transpose=3 <= -rotate 270

 -vf scale="640:480" -sws_flags bilinear  <= -scale 640x480
 -intra <= -keyframe
 -vf "scale=iw*2:ih"  <= -scale 200%x100%!
 -vf scale=1920x1080:flags=bicubic:param0=.33:param1=.33 <= -resize ...
 -vf scale=100x100:flags=lanczos:param0=3 <= -resize 100x100

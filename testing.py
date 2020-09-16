"""
from moviepy.editor import VideoFileClip, ImageClip

#clip = VideoFileClip("/Users/noah/Downloads/box-elder-county/out.mp4")
clip = VideoFileClip("/Users/noah/Dropbox/code/cropcircles/assets/video-sample-sw42.286577541476696,-113.90409924217032ne42.340476458523305,-113.80691475782969.mp4")
fps= 3.0 # take one frame per second
nframes = clip.duration*fps # total number of frames used
total_image = sum(clip.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image.save_frame("average_test2.png")
"""

VIDEO_WIDTH = int(3840/2)
VIDEO_HEIGHT = int(VIDEO_WIDTH / 2.33)

MARGIN = int(VIDEO_HEIGHT / 10)

from moviepy.editor import *

#print(TextClip.list('font'))
clip = VideoFileClip("/Users/noah/Downloads/box-elder-county/out.mp4").subclip(0,2)

title_font_size = MARGIN
txt_clip = TextClip("Center\nPivot\nIrrigation",fontsize=title_font_size,color='white',font='OpticianSans',align='west',interline=-title_font_size/4)
txt_clip = txt_clip.set_position((MARGIN,MARGIN)).set_duration(2)
txt_clip2 = TextClip("#001",fontsize=title_font_size,color='lightgray',font='OpticianSans',align='west')
txt_clip2 = txt_clip2.set_position((MARGIN,MARGIN+title_font_size*2)).set_duration(2)
video = CompositeVideoClip([clip, txt_clip, txt_clip2])
color_clip = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(20, 20, 20)).set_duration(2)  # size needs to be int tuple
test_clip = CompositeVideoClip([color_clip, txt_clip])

import glob
cpi_field_images = glob.glob("test/*.jpg")
cpi_fields = concatenate_videoclips([ImageClip(f).set_duration(1/3).resize((VIDEO_WIDTH, VIDEO_HEIGHT)) for f in cpi_field_images])
fps = 3
nframes = cpi_fields.duration*fps # total number of frames used
total_image = sum(cpi_fields.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image = average_image.set_duration(2)
average_image.save_frame("average_test3.png")


video = concatenate_videoclips([average_image, cpi_fields, video, test_clip])
video.write_videofile("test.mp4",fps=24)

# TODO title background: avg?

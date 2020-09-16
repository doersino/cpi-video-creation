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

MARGIN = int(VIDEO_HEIGHT / 16)

title_font_size = MARGIN * 1.5

from moviepy.editor import *

#print(TextClip.list('font'))
#clip = VideoFileClip("/Users/noah/Downloads/box-elder-county/out.mp4").subclip(0,2)

def compute_nonmoving_texts_size(clips):
    """TODO comment. really, compositevideoclip should do this automatically, but it doesn't"""

    size = [0,0]
    for clip in clips:
        s = clip.size
        p = clip.mask.pos(0)  # doesn't work for animations
        x = s[0] + int(abs(p[0]))
        y = s[1] + int(abs(p[1]))
        if x > size[0]:
            size[0] = x
        if y > size[1]:
            size[1] = y
    return tuple(size)

s = None

def draw_logo(no):
    txt_clip = TextClip("Center\nPivot\nIrrigation",fontsize=title_font_size,color='white',font='OpticianSans',align='west',interline=-title_font_size/4)
    txt_clip = txt_clip.set_position((0,0-title_font_size*0.1))
    txt_clip2 = TextClip("#" + no,fontsize=title_font_size,color='lightgray',font='OpticianSans',align='west')
    txt_clip2 = txt_clip2.set_position((0,0-title_font_size*0.1+title_font_size*2))
    logo = [txt_clip, txt_clip2]
    global s
    s = compute_nonmoving_texts_size(logo)

    return CompositeVideoClip(logo, size=s)

# font size is relative to height for thumbnail purposes!
txt_clip1 = draw_logo("001").set_position((MARGIN,MARGIN))
clip1 = ColorClip(s, color=(200, 0, 0)).set_position((MARGIN,MARGIN))
txt_clip3 = TextClip("Box Elder County",fontsize=title_font_size*1.2,color='white',font='OpticianSans')
txt_clip3 = txt_clip3.set_position(('center',VIDEO_HEIGHT-title_font_size*3))
txt_clip4 = TextClip("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",fontsize=title_font_size*0.5,color='white',font='SourceSerifPro',align='west',size=(VIDEO_WIDTH/2,None),method='caption')
txt_clip4 = txt_clip4.set_position(('center',MARGIN))
#video = CompositeVideoClip([clip, txt_clip, txt_clip2])
color_clip = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(20, 20, 20))  # size needs to be int tuple
titles = [color_clip, clip1, txt_clip1, txt_clip3, txt_clip4]
test_clip = CompositeVideoClip([clip.set_duration(4) for clip in titles])
test_clip = test_clip.fadein(1)
test_clip = test_clip.fadeout(1)
test_clip.write_videofile("test.mp4",fps=3)

"""
import glob
cpi_field_images = glob.glob("test/*.jpg")
cpi_fields = concatenate_videoclips([ImageClip(f).set_duration(1/3).resize((VIDEO_WIDTH, VIDEO_HEIGHT)) for f in cpi_field_images])
fps = 3
nframes = cpi_fields.duration*fps # total number of frames used
total_image = sum(cpi_fields.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image = average_image.set_duration(2)
average_image.save_frame("average_test3.png")
"""


#video = concatenate_videoclips([video, test_clip])
#video.write_videofile("test.mp4",fps=24)

# TODO title background: avg?

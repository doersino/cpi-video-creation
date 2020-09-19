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

MARGIN = int(VIDEO_HEIGHT / 14)

from moviepy.editor import *

#print(TextClip.list('font'))
#clip = VideoFileClip("/Users/noah/Downloads/box-elder-county/out.mp4").subclip(0,2)

def compute_nonmoving_texts_size(clips):
    """TODO comment. for non-positioned (so at 0,0) non-moving text clips. really, compositevideoclip should do this automatically, but it doesn't"""

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

import subprocess

def trim_text_clip(clip):
    """Trims a clip, i.e. removes all transparent pixels from the edges. TODO better"""

    f = "trim_text_tmp.png"
    clip.save_frame(f)
    # TODO use same imagemagick path as moviepy, somehow
    subprocess.run(["mogrify", "-trim", f])
    return ImageClip(f)

def draw_logo(no):
    logo_font_size = MARGIN * 1.2
    cpi = TextClip("Center\nPivot\nIrrigation",fontsize=logo_font_size,color='white',font='OpticianSans',align='west',interline=-logo_font_size*0.3)
    no = TextClip("#" + no,fontsize=logo_font_size,color='lightgray',font='OpticianSans',align='west')
    no = no.set_position((0,logo_font_size*1.9))
    logo = [cpi, no]
    logo = CompositeVideoClip(logo, size=compute_nonmoving_texts_size(logo))
    return trim_text_clip(logo)

def draw_title(main, sub):
    title_font_size = MARGIN * 2
    main = TextClip(main,fontsize=title_font_size,color='white',font='OpticianSans',align='center',interline=-title_font_size*0.3)
    sub = TextClip(sub,fontsize=title_font_size*0.67,color='white',font='OpticianSans',align='center')
    sub = sub.set_position((main.size[0]/2-sub.size[0]/2,title_font_size))
    title = [main, sub]
    title = CompositeVideoClip(title, size=compute_nonmoving_texts_size(title))
    return trim_text_clip(title)

# TODO pretty-print latlon from filenames

# font size is relative to height for thumbnail purposes!

import glob
cpi_field_images = glob.glob("test/*.jpg")
cpi_fields = concatenate_videoclips([ImageClip(f).set_duration(1/3).resize((VIDEO_WIDTH, VIDEO_HEIGHT)) for f in cpi_field_images])
fps = 3
nframes = cpi_fields.duration*fps # total number of frames used
total_image = sum(cpi_fields.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image.save_frame("average_test3.png")

logo = draw_logo("001")
logo = logo.set_position((MARGIN,VIDEO_HEIGHT-MARGIN-logo.size[1]))
title = draw_title("Box Elder County", "Utah, USA")
#title = title.set_position(lambda t: ('center', 2*MARGIN+10*t))
title = title.set_position(('center', 3*MARGIN))

titles = [average_image, logo, title]
titles = [clip.set_duration(5) for clip in titles]

titles[1] = titles[1].set_start(1.5,change_end=False)
titles[2] = titles[2].set_start(2.5,change_end=False)

titles = CompositeVideoClip(titles)

titles = titles.fadein(1)
titles = titles.fadeout(1)

################################################################################

last_image = ImageClip(cpi_field_images[-1]).set_duration(2).resize((VIDEO_WIDTH, VIDEO_HEIGHT)).fadeout(1)

black = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(0, 0, 0))

end_font_size = MARGIN*0.33
text = TextClip("""
This has been all center pivot irrigation fields located or partially located in Box Elder County, Utah, USA at the time the aerial imagery was captured.

The imagery is courtesy of Google Maps. It has been downloaded using ærialbot, see github.com/doersino/aerialbot, and cropped using Crop Cricles, see github.com/doersinog/cropcircles, and assembled into a video using custom Python tooling available at github.com/doersino/cpi-video-creation.

The soundtrack was “Grey Shadow” by Adrián Berenguer, available at adrianberenguer.bandcamp.com/track/grey-shadow and used in accordance with its CC BY-NC-SA license, see creativecommons.org/licenses/by-nc-sa/3.0/. As per the conditions of the license, this video is licensed the same.

The fonts used are Optician Sans, see TODO, and Source Serif Pro, see TODO, both used in accordance with their SIL OFL licenses.
    """,
    fontsize=end_font_size,color='white',font='SourceSerifPro',align='west',size=(VIDEO_WIDTH/2,None),method='caption')
text = trim_text_clip(text)
text = text.set_position((MARGIN,VIDEO_HEIGHT-MARGIN-text.size[1]))

endcard = [black, logo.set_position((MARGIN,MARGIN)), text]
endcard = [clip.set_duration(8) for clip in endcard]
endcard = CompositeVideoClip(endcard)
endcard = endcard.fadein(1)
endcard = endcard.fadeout(1)

################################################################################

video = concatenate_videoclips([black.set_duration(1), titles, cpi_fields, last_image, endcard, black.set_duration(2)])

video.write_videofile("test.mp4",fps=24)




#txt_clip4 = TextClip("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",fontsize=title_font_size*0.5,color='white',font='SourceSerifPro',align='west',size=(VIDEO_WIDTH/2,None),method='caption')
#txt_clip4 = txt_clip4.set_position(('center',MARGIN))
#video = CompositeVideoClip([clip, txt_clip, txt_clip2])

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

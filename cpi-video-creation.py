##########
# CONFIG #
##########

NO = "002"
LOCATION = "Box Elder County"
LOCATION_SUBTITLE = "Utah, USA"

ENDCARD_INTRO = """
That's all center pivot irrigation fields located in Box Elder County, Utah, USA
— at least the {image_count} that were discernible at the time the aerial
imagery was captured.
"""

ENDCARD_REST = """
The soundtrack was a variant of "Grey Shadow" by Adrián Berenguer where parts of
the work were repeated to reach the required length. The original is available
at adrianberenguer.bandcamp.com/track/grey-shadow, it has been used in
accordance with its CC BY-NC-SA license, see
creativecommons.org/licenses/by-nc-sa/3.0/. As per the conditions of the
license, this video is licensed under the same terms.

The aerial imagery is courtesy of Google Maps. It has been downloaded with
ærialbot, see github.com/doersino/aerialbot, then cropped using Crop Cricles,
see github.com/doersino/cropcircles, and finally assembled into a video using
custom MoviePy-based tooling available at
github.com/doersino/cpi-video-creation. The title screen background is the
average of all images shown.

The typeface used for the title screen, the coordinates of each field, and the
link in the bottom left here is Optician Sans, see optician-sans.com. This
colophon is set in Source Serif Pro, see
github.com/adobe-fonts/source-serif-pro. Both typefaces are licensed under the
SIL Open Font License, see opensource.org/licenses/OFL-1.1. Any kerning issues
you may have noticed are caused by the video production process, the typefaces
themselves are fine.
"""

LICENSE = ["by", "nc", "sa"]

IMAGES_DIR = "/Users/noah/Downloads/box-elder-county"
IMAGES_LIMIT = 5  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840 / 2
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # TODO determine based on imgs?

MUSIC_FILE = "/Users/noah/Desktop/greyshadow.wav"
BPM = 100
TIME_BEFORE_FIRST_BEAT = 0.85

VIDEO_PATH = "result.mp4"
FPS = 24

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = "result-thumbnail.png"

################################################################################

import glob
import math
import re
import subprocess

import moviepy.config
from moviepy.editor import *

################################################################################

# TODO make sure these are even?
VIDEO_WIDTH = int(VIDEO_WIDTH)
VIDEO_HEIGHT = int(VIDEO_HEIGHT)

MARGIN = int(VIDEO_HEIGHT / 14)

ENDCARD_INTRO = "\n\n".join(map(lambda l: " ".join(l.strip().split("\n")), ENDCARD_INTRO.split("\n\n")))
ENDCARD_REST = "\n\n".join(map(lambda l: " ".join(l.strip().split("\n")), ENDCARD_REST.split("\n\n")))

MAGICK = moviepy.config.IMAGEMAGICK_BINARY


def compute_static_clips_size(clips):
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

def trim_text_clip(clip):
    """Trims a clip, i.e. removes all transparent pixels from the edges. TODO better"""

    f = "temp/trim_text_clip_tmp.png"
    f_result = "temp/trim_text_clip_tmp_result.png"
    clip.save_frame(f)
    subprocess.run([MAGICK, f, "-trim", f_result])
    return ImageClip(f_result)

def normalize_image_clip(clip):
    f = "temp/normalize_image_clip_tmp.png"
    f_result = "temp/normalize_image_clip_tmp_result.png"
    clip.save_frame(f)
    subprocess.run([MAGICK, f, "-contrast-stretch", "0", "-modulate", "110,80", f_result])
    return ImageClip(f_result)

def draw_logo(no):
    logo_font_size = MARGIN * 1.2
    cpi = TextClip("Center\nPivot\nIrrigation",fontsize=logo_font_size,color='white',font='OpticianSans',align='west',interline=-logo_font_size*0.3)
    no = TextClip("#" + no,fontsize=logo_font_size,color='white',font='OpticianSans',align='west')
    no = no.set_position((0,logo_font_size*1.86))
    no = no.set_opacity(0.85)
    logo = [cpi, no]
    logo = CompositeVideoClip(logo, size=compute_static_clips_size(logo))
    return trim_text_clip(logo)

def draw_title(main, sub):
    title_font_size = MARGIN * 2
    main = TextClip(main,fontsize=title_font_size,color='white',font='OpticianSans',align='center',interline=-title_font_size*0.3)
    title = [main]
    if sub:
        sub = TextClip(sub,fontsize=title_font_size*0.67,color='white',font='OpticianSans',align='center')
        sub = sub.set_position((main.size[0]/2-sub.size[0]/2,title_font_size))
        title = [main, sub]
    title = CompositeVideoClip(title, size=compute_static_clips_size(title))
    return trim_text_clip(title)

# font size is relative to height for thumbnail purposes!

def generate_thumbnail(background, logo, title):
    vid_aspect = VIDEO_WIDTH / VIDEO_HEIGHT
    thumb_aspect = THUMBNAIL_WIDTH / THUMBNAIL_HEIGHT

    thumbnail = None
    # TODO check if these work for all situations
    if (vid_aspect > thumb_aspect):  # video wider
        thumbnail = background.crop(x1=VIDEO_WIDTH/2-(VIDEO_HEIGHT/THUMBNAIL_HEIGHT)*THUMBNAIL_WIDTH/2, width=THUMBNAIL_WIDTH*(VIDEO_HEIGHT/THUMBNAIL_HEIGHT))
    else:
        # TODO fix
        thumbnail = background.crop(y1=VIDEO_HEIGHT/2-(VIDEO_WIDTH/THUMBNAIL_WIDTH)*THUMBNAIL_HEIGHT/2, height=THUMBNAIL_HEIGHT*(VIDEO_WIDTH/THUMBNAIL_WIDTH))

    #logo = logo.set_position((MARGIN, VIDEO_HEIGHT-MARGIN-logo.size[1]))
    #title = title.set_position(('center', 5*MARGIN))
    CompositeVideoClip([thumbnail, logo, title]).resize((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT)).save_frame(THUMBNAIL_PATH)

black = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(0, 0, 0))

cpi_field_images = glob.glob(IMAGES_DIR + "/*.jpg")
cpi_field_images.sort()
if (IMAGES_LIMIT):
    cpi_field_images = cpi_field_images[:IMAGES_LIMIT]

cpi_field_clips = [ImageClip(f).set_duration(60 / BPM).resize((VIDEO_WIDTH, VIDEO_HEIGHT)) for f in cpi_field_images]

cpi_fields = concatenate_videoclips(cpi_field_clips)
fps = BPM / 60
nframes = cpi_fields.duration*fps # total number of frames used
total_image = sum(cpi_fields.iter_frames(fps,dtype=float,logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image = normalize_image_clip(average_image)
#average_image.save_frame("average_test3.png")

logo = draw_logo(NO)
logo = logo.set_position((MARGIN, VIDEO_HEIGHT-MARGIN-logo.size[1]))
title = draw_title(LOCATION, LOCATION_SUBTITLE)
title = title.set_position(('center', 5*MARGIN))

titles = [black, average_image.set_opacity(0.9), logo, title]
generate_thumbnail(average_image, logo, title)
titles = [clip.set_duration(5) for clip in titles]

titles[2] = titles[2].set_start(1.5,change_end=False)
titles[3] = titles[3].set_start(2.5,change_end=False)

snd = AudioFileClip("assets/beep.wav").set_start(1.49)  # no idea why the delay has to be set here too
snd2 = AudioFileClip("assets/boop.wav").set_start(2.49)
titles[2] = titles[2].set_audio(snd)
titles[3] = titles[3].set_audio(snd2)

titles = CompositeVideoClip(titles)
titles = titles.fadein(1).fadeout(1)

################################################################################

song = AudioFileClip(MUSIC_FILE)

def fancy(lat, lon):
    """Stringifies a point in a rather fancy way, e.g. "44°35'27.6"N
    100°21'53.1"W", i.e. with minutes and seconds."""

    # helper function as both latitude and longitude are stringified
    # basically the same way
    def fancy_coord(coord, pos, neg):
        coord_dir = pos if coord > 0 else neg
        coord_tmp = abs(coord)
        coord_deg = math.floor(coord_tmp)
        coord_tmp = (coord_tmp - math.floor(coord_tmp)) * 60
        coord_min = math.floor(coord_tmp)
        coord_sec = round((coord_tmp - math.floor(coord_tmp)) * 600) / 10
        coord = f"{coord_deg}°{coord_min}'{coord_sec}\"{coord_dir}"
        return coord

    lat = fancy_coord(lat, "N", "S")
    lon = fancy_coord(lon, "E", "W")

    return f"{lat} {lon}"

def overlay_geocoords_if_available(filename, imageclip):
    coords = re.search(r'(-?\d+.\d+),(-?\d+.\d+)', filename)
    if (not coords):
        return imageclip
    coords = [float(coords.group(1)), float(coords.group(2))]

    coords_font_size = MARGIN * 0.4
    coords = TextClip(fancy(coords[0], coords[1]),fontsize=coords_font_size,color='white',font='OpticianSans',align='west')
    coords = trim_text_clip(coords)
    coords = coords.set_position((VIDEO_WIDTH-MARGIN-coords.size[0],VIDEO_HEIGHT-MARGIN-coords.size[1])).set_duration(60/BPM)  # TODO 60/BPM into a const

    return CompositeVideoClip([imageclip, coords])

fields = [overlay_geocoords_if_available(f, clip) for f, clip in zip(cpi_field_images, cpi_field_clips)]
last_image = fields[-1]
fields = concatenate_videoclips(fields)
fields = concatenate_videoclips([black.set_duration(TIME_BEFORE_FIRST_BEAT), fields])
fields = fields.set_audio(song)

# TODO ugh
last_image = concatenate_videoclips([last_image, last_image, last_image, last_image, last_image, last_image, last_image]).set_duration(2).fadeout(2)

################################################################################

end_font_size = MARGIN*0.3
end_intro_font_size = end_font_size * 1.3

intro = TextClip(ENDCARD_INTRO.format(image_count=len(cpi_field_images)),fontsize=end_intro_font_size,color='white',font='SourceSerifPro',align='west',size=(VIDEO_WIDTH*0.55,None),method='caption')
intro = trim_text_clip(intro)

text = TextClip(ENDCARD_REST, fontsize=end_font_size,color='white',font='SourceSerifPro',align='west',size=(VIDEO_WIDTH*0.55,None),method='caption')
text = trim_text_clip(text)

intro = intro.set_position((MARGIN,VIDEO_HEIGHT-MARGIN-text.size[1]-intro.size[1]-MARGIN))
text = text.set_position((MARGIN,VIDEO_HEIGHT-MARGIN-text.size[1]))

link = TextClip("noahdoersing.com",fontsize=end_font_size * 1.4,color='white',font='OpticianSans',align='west')
link = trim_text_clip(link)
link = link.set_position((VIDEO_WIDTH-MARGIN-link.size[0],VIDEO_HEIGHT-MARGIN-link.size[1]))

license_codes = ["cc", *LICENSE]
license_icons = list(map(lambda l: ImageClip("assets/cc/" + l + ".png"), license_codes))
for i in range(len(license_icons)):
    icon = license_icons[i]
    icon = icon.resize((end_font_size*1.4, end_font_size*1.4))
    icon = icon.set_position((i*1.8*end_font_size, 0))
    license_icons[i] = icon
license_icons = CompositeVideoClip(license_icons, size=compute_static_clips_size(license_icons))  # TODO rename that function
license_icons = license_icons.set_position((VIDEO_WIDTH-MARGIN-license_icons.size[0],VIDEO_HEIGHT-MARGIN-link.size[1]-2*license_icons.size[1]))

endcard = [black, average_image.set_opacity(0.15), logo.set_position((MARGIN,MARGIN)), intro, text, link, license_icons]
endcard = CompositeVideoClip([clip.set_duration(20) for clip in endcard])
endcard = endcard.fadein(1).fadeout(1)

################################################################################

video = concatenate_videoclips([
    black.set_duration(1),
    titles,
    black.set_duration(0.5),
    fields,
    last_image,
    endcard,
    black.set_duration(1)
    ])

video.write_videofile(VIDEO_PATH, fps=FPS, temp_audiofile="temp/temp_audio.mp3")







# TODO alrighty, then cleanup!
# TODO add default outputs to gitignore
# TODO keep versions of this file for old videos in archive folder in repo?



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

#print(TextClip.list('font'))
#clip = VideoFileClip("/Users/noah/Downloads/box-elder-county/out.mp4").subclip(0,2)

#title = title.set_position(lambda t: ('center', 2*MARGIN+10*t))
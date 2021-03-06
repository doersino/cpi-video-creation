##########
# CONFIG #
##########

'''
NO = "001"
LOCATION = "Prologue"
LOCATION_SUBTITLE = ""
LOCATION_KERNING = 0.33

TITLECARD_DURATION = 5  # includes fadeinout

ENDCARD_INTRO = """
This has been a selection of 94 center pivot irrigation fields located around
the world – there will be a number of follow-up videos, most with a more
regional focus, sometimes exhaustively covering all fields in an area. Stay
tuned.
"""
ENDCARD_REST = """
The soundtrack was a variant of "Continent" by Adrián Berenguer, slowed down
from 149 to 120 BPM. The original is available at
adrianberenguer.bandcamp.com/track/grey-shadow, it has been used in accordance
with its CC BY-NC-SA license, see
creativecommons.org/licenses/by-nc-sa/3.0/. As per the conditions of the
license, this video is licensed under the same terms.

The aerial imagery is courtesy of Google Maps. It has been downloaded with
ærialbot, see github.com/doersino/aerialbot, then cropped using Crop Circles,
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
LICENSE = ["by", "nc", "sa"]  # set to None for no license icons
ENDCARD_DURATION = 20  # includes fadeinout

# all *.jpg files from this dir will be shown in the result video
IMAGES_DIR = "/Users/noah/Documents/cpi-video-stuff/001-prologue/sequence"
IMAGES_LIMIT = None  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # should be based on aspect ratio of inputs

MUSIC_FILE = "/Users/noah/Documents/cpi-video-stuff/001-prologue/soundtrack/continent.wav"
BPM = 120 * 2
TIME_BEFORE_FIRST_BEAT = 0.62  # screen will be black until that time

LAST_IMAGE_ADDITIONAL_DURATION = 0.5  # time the last image will be shown (on top of the normal time), sometimes best set to 0
LAST_IMAGE_FADEOUT_DURATION = 2.0  # a good default is 1.5

VIDEO_PATH = "001-prologue.mp4"
FPS = 30

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = "001-prologue-thumbnail.jpg"
'''

'''
NO = "002"
LOCATION = "Box Elder County"
LOCATION_SUBTITLE = "Utah, USA"
LOCATION_KERNING = 0

TITLECARD_DURATION = 5  # includes fadeinout

ENDCARD_INTRO = """
That's all {image_count} center pivot irrigation fields located in Box Elder
County, Utah, USA — at least the ones that were visible from space at the time
the aerial imagery was captured.
"""
ENDCARD_REST = """
The soundtrack was a variant of "Grey Shadow" by Adrián Berenguer where parts of
the work were repeated to reach the required length. The original is available
at adrianberenguer.bandcamp.com/track/grey-shadow, it has been used in
accordance with its CC BY-NC-SA license, see
creativecommons.org/licenses/by-nc-sa/3.0/. As per the conditions of the
license, this video is licensed under the same terms.

The aerial imagery is courtesy of Google Maps. It has been downloaded with
ærialbot, see github.com/doersino/aerialbot, then cropped using Crop Circles,
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
LICENSE = ["by", "nc", "sa"]  # set to None for no license icons
ENDCARD_DURATION = 20

# all *.jpg files from this dir will be shown in the result video
IMAGES_DIR = "/Users/noah/Documents/cpi-video-stuff/002-box-elder-county/sequence"
IMAGES_LIMIT = None  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # should be based on aspect ratio of inputs

MUSIC_FILE = "/Users/noah/Documents/cpi-video-stuff/002-box-elder-county/soundtrack/greyshadow.wav"
BPM = 100
TIME_BEFORE_FIRST_BEAT = 0.85  # screen will be black until that time

LAST_IMAGE_ADDITIONAL_DURATION = 0.2  # time the last image will be shown (on top of the normal time), sometimes best set to 0
LAST_IMAGE_FADEOUT_DURATION = 1.5  # a good default is 1.5

VIDEO_PATH = "002-box-elder-county.mp4"
FPS = 30

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = "002-box-elder-county-thumbnail.jpg"
'''

'''
NO = "003"
LOCATION = "Selwyn District"
LOCATION_SUBTITLE = "Canterbury, New Zealand"  # must render narrower than the main location; you can make the location wider by adjusting the kerning
LOCATION_KERNING = 0.06

TITLECARD_DURATION = 5  # includes fadeinout

ENDCARD_INTRO = """
This has been a selection of {image_count} center pivot irrigation fields
located in Selwyn District, Canterbury, New Zealand — there are quite a bit
more, but they aren't large enough to show up clearly in publicly available
aerial imagery.
"""
ENDCARD_REST = """
The soundtrack was a variant of "Continent" by Adrián Berenguer, shortened and
slowed down from 149 to 110 BPM. The original is available at
adrianberenguer.bandcamp.com/track/grey-shadow, it has been used in accordance
with its CC BY-NC-SA license, see
creativecommons.org/licenses/by-nc-sa/3.0/. As per the conditions of the
license, this video is licensed under the same terms.

The aerial imagery is courtesy of Google Maps. It has been downloaded with
ærialbot, see github.com/doersino/aerialbot, then cropped using Crop Circles,
see github.com/doersino/cropcircles, partially color-balanced using Adobe
Photoshop CS6, and finally assembled into a video using custom MoviePy-based
tooling available at github.com/doersino/cpi-video-creation. The title screen
background is the average of all images shown.

The typeface used for the title screen, the coordinates of each field, and the
link in the bottom left here is Optician Sans, see optician-sans.com. This
colophon is set in Source Serif Pro, see
github.com/adobe-fonts/source-serif-pro. Both typefaces are licensed under the
SIL Open Font License, see opensource.org/licenses/OFL-1.1. Any kerning issues
you may have noticed are caused by the video production process, the typefaces
themselves are fine.
"""
LICENSE = ["by", "nc", "sa"]  # set to None for no license icons
ENDCARD_DURATION = 20  # includes fadeinout

# all *.jpg files from this dir will be shown in the result video
IMAGES_DIR = "/Users/noah/Documents/cpi-video-stuff/003-selwyn-district/sequence"
IMAGES_LIMIT = None  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # should be based on aspect ratio of inputs

MUSIC_FILE = "/Users/noah/Documents/cpi-video-stuff/003-selwyn-district/soundtrack/continent.wav"
BPM = 110
TIME_BEFORE_FIRST_BEAT = 0.35  # screen will be black until that time

LAST_IMAGE_ADDITIONAL_DURATION = 0.3  # time the last image will be shown (on top of the normal time), sometimes best set to 0
LAST_IMAGE_FADEOUT_DURATION = 1.5  # a good default is 1.5

VIDEO_PATH = NO + "-selwyn-district.mp4"
FPS = 30

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = NO + "-selwyn-district-thumbnail.jpg"
'''

NO = "004"
LOCATION = "San Juan County"
LOCATION_SUBTITLE = "New Mexico, USA"  # must render narrower than the main location; you can make the location wider by adjusting the kerning
LOCATION_KERNING = 0

TITLECARD_DURATION = 5  # includes fadeinout

ENDCARD_INTRO = """
That's all {image_count} center pivot irrigation fields located in San Juan
County, New Mexico, USA — at least the ones that were visible from space at the
time the aerial imagery was captured.
"""
ENDCARD_REST = """
The soundtrack was a variant of "Explore, be curious" by Cloudkicker that's been
cut apart and reassembled to match the length of this video. The original is
available at cloudkicker.bandcamp.com/track/explore-be-curious, it has been used
in accordance with its CC BY license, see creativecommons.org/licenses/by/3.0/.
This video is also licensed under a CC license, specifically the slightly more
restrictive CC BY-NC-SA license, see creativecommons.org/licenses/by-nc-sa/3.0/.

The aerial imagery is courtesy of Google Maps. It has been downloaded with
ærialbot, see github.com/doersino/aerialbot, then cropped using Crop Circles,
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
LICENSE = ["by", "nc", "sa"]  # set to None for no license icons
ENDCARD_DURATION = 20  # includes fadeinout

# all *.jpg files from this dir will be shown in the result video
IMAGES_DIR = "/Users/noah/Documents/cpi-video-stuff/004-san-juan-county/sequence"
IMAGES_LIMIT = None  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # should be based on aspect ratio of inputs

MUSIC_FILE = "/Users/noah/Documents/cpi-video-stuff/004-san-juan-county/soundtrack/explorebecurious.wav"
BPM = 138
TIME_BEFORE_FIRST_BEAT = 0.28  # screen will be black until that time

LAST_IMAGE_ADDITIONAL_DURATION = 0.3  # time the last image will be shown (on top of the normal time), sometimes best set to 0
LAST_IMAGE_FADEOUT_DURATION = 1.5  # a good default is 1.5

VIDEO_PATH = NO + "-san-juan-county.mp4"
FPS = 30

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = NO + "-san-juan-county-thumbnail.jpg"


################################################################################

import glob
import math
import os
import re
import subprocess

import moviepy.config
from moviepy.editor import *

################################################################################

# make sure they are integer-valued and even (required by H.264, apparently)
VIDEO_WIDTH = int(VIDEO_WIDTH/2)*2
VIDEO_HEIGHT = int(VIDEO_HEIGHT/2)*2

MARGIN = int(VIDEO_HEIGHT / 16)

# font size is relative to height for thumbnail purposes
BASE_FONT_SIZE = VIDEO_HEIGHT / 14

# prepare end card texts
ENDCARD_INTRO = "\n\n".join(map(lambda l: " ".join(l.strip().split("\n")), ENDCARD_INTRO.split("\n\n")))
ENDCARD_REST = "\n\n".join(map(lambda l: " ".join(l.strip().split("\n")), ENDCARD_REST.split("\n\n")))

MAGICK = moviepy.config.IMAGEMAGICK_BINARY

def status(message):
    print("\033[1m" + message + "\033[0m")

def compute_static_clips_size(clips):
    """
    Computes the total size of a list of non-positioned (at 0,0), non-moving
    (where mask.pos is constant with time) clips. The constructor of
    CompositeVideoClip should do this automatically, but it seemingly doesn't,
    so we need to do it manually.
    """

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

def trim_text_clip(clip, width=None, align='west'):
    """Trims a clip, i.e. removes all transparent pixels from the edges."""

    f = "temp/trim_text_clip_tmp.png"
    f_result = "temp/trim_text_clip_tmp_result.png"
    f_result_padded = "temp/trim_text_clip_tmp_result_padded.png"
    clip.save_frame(f)
    subprocess.run([MAGICK, f, "-trim", f_result])
    clip_result = ImageClip(f_result)
    if width:
        extent = f"{width}x{clip_result.size[1]}"
        subprocess.run([MAGICK, f_result, "-background", "transparent", "-gravity", align, "-extent", extent, f_result_padded])
        clip_result = ImageClip(f_result_padded)
    return clip_result

def normalize_image_clip(clip):
    """
    Normalizes an image, i.e. makes sure it covers the whole brightness range,
    thus making it more vibrant.
    """

    f = "temp/normalize_image_clip_tmp.png"
    f_result = "temp/normalize_image_clip_tmp_result.png"
    clip.save_frame(f)
    subprocess.run([MAGICK, f, "-contrast-stretch", "0", "-modulate", "105,80", f_result])
    return ImageClip(f_result)

def draw_logo(no):
    logo_font_size = BASE_FONT_SIZE * 1.35
    cpi = TextClip(
        "Center\nPivot\nIrrigation",
        fontsize=logo_font_size,
        color='white',
        font='OpticianSans',
        align='west',
        interline=-logo_font_size*0.29
        )
    no = TextClip(
        "#" + no,
        fontsize=logo_font_size,
        color='white',
        font='OpticianSans',
        align='west'
        )
    no = no.set_position((0, logo_font_size*1.84))
    no = no.set_opacity(0.87)

    logo = [cpi, no]
    logo = CompositeVideoClip(logo, size=compute_static_clips_size(logo))
    return trim_text_clip(logo)

def draw_title(main, sub):
    title_font_size = BASE_FONT_SIZE * 2.4
    main = TextClip(
        main,
        fontsize=title_font_size,
        color='white',
        font='OpticianSans',
        align='center',
        interline=-title_font_size*0.2,
        kerning=LOCATION_KERNING*title_font_size
        )
    main = trim_text_clip(main)
    title = [main]

    if sub:
        sub = TextClip(
            sub,
            fontsize=title_font_size*(2/3),
            color='white',
            font='OpticianSans',
            align='center'
            )
        sub = trim_text_clip(sub)
        sub = sub.set_position((main.size[0]/2-sub.size[0]/2,
                                main.size[1]+title_font_size*0.4))
        title = [main, sub]

    title = CompositeVideoClip(title, size=compute_static_clips_size(title))
    return trim_text_clip(title)

def generate_thumbnail(background, logo, title):
    vid_aspect = VIDEO_WIDTH / VIDEO_HEIGHT
    thumb_aspect = THUMBNAIL_WIDTH / THUMBNAIL_HEIGHT

    thumbnail = None
    if vid_aspect > thumb_aspect:  # video wider
        height_factor = VIDEO_HEIGHT / THUMBNAIL_HEIGHT
        thumbnail = background.crop(
            x1=VIDEO_WIDTH/2-height_factor*THUMBNAIL_WIDTH/2,
            width=THUMBNAIL_WIDTH*height_factor
            )
    else:
        width_factor = VIDEO_WIDTH / THUMBNAIL_WIDTH
        thumbnail = background.crop(
            y1=VIDEO_HEIGHT/2-width_factor*THUMBNAIL_HEIGHT/2,
            height=THUMBNAIL_HEIGHT*width_factor
            )

    # positioning is the same as for the title card, so nothing needs to be done here

    thumbnail = CompositeVideoClip([thumbnail, logo, title])

    thumbnail = thumbnail.resize((THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT))
    thumbnail.save_frame(THUMBNAIL_PATH, withmask=False)

def fancy(lat, lon):
    """Stringifies a point in a rather fancy way, e.g. "44°35'27.6"N
    100°21'53.1"W", i.e. with arc minutes and seconds."""

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

"""
def overlay_geocoords_if_available(filename, imageclip):
    coords = re.search(r'(-?\d+.\d+),(-?\d+.\d+)', filename)
    if not coords:
        return imageclip
    coords = [float(coords.group(1)), float(coords.group(2))]

    coords_font_size = BASE_FONT_SIZE * 0.4
    coords = TextClip(
        fancy(coords[0], coords[1]),
        fontsize=coords_font_size,
        color='white',
        font='OpticianSans',
        align='west'
        )
    coords = trim_text_clip(coords)
    coords = coords.set_position((VIDEO_WIDTH-MARGIN-coords.size[0],
                                  VIDEO_HEIGHT-MARGIN-coords.size[1]))
    coords = coords.set_duration(60/BPM)  # same as images

    return CompositeVideoClip([imageclip, coords])
"""

# the variant above leads to what appears to be a memory leak – it seems as
# though CompositeVideoClip([imageclip, coords]) needs to load the image into
# memory and keep it there until the video has been rendered instead of doing
# things in a streaming manner. the fix is to instead make a concatenated clip
# of overlays with the same timing as the images, then composite that on top of
# a concatenation of the images. yes, that's basically the same, just stupider
# – with the notable advantage that it doesn't gobble up ram like there's no
# tomorrow. additionally, you might wonder why the text is set to "not actually
# visible" and then hidden via .set_opacity(0) if there are no coords – it would
# be easier to just return a tiny empty image or something, but the resulting
# size difference would confudse concatenate_videoclips() to no end.
# tl;dr: computers were a mistake and my life has been cut noticeably shorter by
# all of this nonsense
def generate_geocoords_overlay_if_available(filename):
    coords_font_size = BASE_FONT_SIZE * 0.4

    # the leading "-?" prevents things like the dash in
    # "cropcircles-[lat],[lon]" from flipping everything south
    coords = re.search(r'-?(-?\d+.\d+),(-?\d+.\d+)', filename)
    text = "not actually visible"
    if coords:
        text = fancy(float(coords.group(1)), float(coords.group(2)))

    coords_clip = TextClip(
        text,
        fontsize=coords_font_size,
        color='white',
        font='OpticianSans',
        align='east'
        )

    # trim, but make it right-aligned in the process (VIDEO_WIDTH/2 is a safe
    # upper bound of the maximum width the text can possibly have)
    coords_clip = trim_text_clip(coords_clip, width=VIDEO_WIDTH/2, align='east')
    coords_clip = coords_clip.set_duration(60/BPM)  # same as images

    if not coords:
        coords_clip = coords_clip.set_opacity(0)

    return coords_clip

################################################################################

black = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(0, 0, 0))

status("Finding images...")
cpi_field_images = glob.glob(IMAGES_DIR + "/*.jpg")
cpi_field_images.sort()  # gotta make sure they're sorted
if IMAGES_LIMIT:
    cpi_field_images = cpi_field_images[:IMAGES_LIMIT]

"""
# not required: moviepy resizes without using much ram, after all
status("Resizing images...")
cpi_field_images_resized = []
os.mkdir("temp/images/")
for i, f in enumerate(cpi_field_images):
    print(f"{i+1}/{len(cpi_field_images)}: " + os.path.basename(f))
    f_result = "temp/images/" + os.path.basename(f)
    # could actually skip conversion if a file with that name, filesize and maybe resolution already exists
    subprocess.run([MAGICK, f, "-resize", str(VIDEO_WIDTH) + "x" + str(VIDEO_HEIGHT) + "!", "-quality", "95%", f_result])
    cpi_field_images_resized.append(f_result)
cpi_field_images = cpi_field_images_resized
"""

status("Loading images...")
cpi_field_clips = []
for i, f in enumerate(cpi_field_images):
    print(f"{i+1}/{len(cpi_field_images)}: " + os.path.basename(f))
    #clip = ImageClip(f).set_duration(60 / BPM)
    clip = ImageClip(f).set_duration(60 / BPM).resize((VIDEO_WIDTH, VIDEO_HEIGHT))
    cpi_field_clips.append(clip)

status("Turning them into a video sequence...")
cpi_fields = concatenate_videoclips(cpi_field_clips)

status("Computing average image...")
fields_per_second = BPM / 60
nframes = cpi_fields.duration*fields_per_second # total number of frames used
total_image = sum(cpi_fields.iter_frames(fields_per_second, dtype=float, logger='bar'))
average_image = ImageClip(total_image/ nframes)
average_image = normalize_image_clip(average_image)

status("Preparing logo and title...")
logo = draw_logo(NO)
logo = logo.set_position((MARGIN, VIDEO_HEIGHT-MARGIN-logo.size[1]))

title = draw_title(LOCATION, LOCATION_SUBTITLE)
title_y = MARGIN + 1/2 * (VIDEO_HEIGHT - 2*MARGIN - logo.size[1]) - title.size[1] / 2
title = title.set_position(('center', title_y))

status("Generating thumbnail...")
generate_thumbnail(average_image, logo, title)

status("Drawing title card...")
titles = [
    black,
    average_image.set_opacity(0.9),
    logo,
    title
    ]
titles = [clip.set_duration(TITLECARD_DURATION) for clip in titles]

titles[2] = titles[2].set_start(1.5, change_end=False)
titles[3] = titles[3].set_start(2.5, change_end=False)

# no idea why the delay has to be set here too – other seemingly-sensible
# approaches didn't seem to produce the desired results
beep = AudioFileClip("assets/beep.wav").set_start(1.49)
boop = AudioFileClip("assets/boop.wav").set_start(2.49)
titles[2] = titles[2].set_audio(beep)
titles[3] = titles[3].set_audio(boop)

titles = CompositeVideoClip(titles)
titles = titles.fadein(1).fadeout(1)

################################################################################

status("Overlaying geo coordinates over image sequence...")
overlays = []
for i, f in enumerate(cpi_field_images):
    print(f"{i+1}/{len(cpi_field_images)}: " + os.path.basename(f))
    overlays.append(generate_geocoords_overlay_if_available(f))
overlays = concatenate_videoclips(overlays)
overlays = overlays.set_position((VIDEO_WIDTH-MARGIN-overlays.size[0],
                                  VIDEO_HEIGHT-MARGIN-overlays.size[1]))
fields = CompositeVideoClip([cpi_fields, overlays])

# keep the last image on screen for a bit longer, then fade it out
fields = fields.fx(
    vfx.freeze,
    t='end',
    freeze_duration=LAST_IMAGE_ADDITIONAL_DURATION+LAST_IMAGE_FADEOUT_DURATION,
    padding_end=0.1)
fields = fields.fadeout(LAST_IMAGE_FADEOUT_DURATION)

fields = concatenate_videoclips([black.set_duration(TIME_BEFORE_FIRST_BEAT), fields])

status("Loading and incorporating music...")
song = AudioFileClip(MUSIC_FILE)
fields = fields.set_audio(song)

################################################################################

status("Preparing end card...")
end_font_size = BASE_FONT_SIZE * 0.3
end_intro_font_size = end_font_size * 1.3

end_text_width = VIDEO_WIDTH*0.55

intro = TextClip(
    ENDCARD_INTRO.format(image_count=len(cpi_field_images)),
    fontsize=end_intro_font_size,
    color='white',
    font='SourceSerifPro',
    align='west',
    size=(end_text_width,None),
    method='caption'
    )
intro = trim_text_clip(intro)

text = TextClip(
    ENDCARD_REST,
    fontsize=end_font_size,
    color='white',
    font='SourceSerifPro',
    align='west',
    size=(end_text_width, None),
    method='caption'
    )
text = trim_text_clip(text)

intro = intro.set_position((MARGIN, VIDEO_HEIGHT-MARGIN-text.size[1]-intro.size[1]-end_font_size*3))
text = text.set_position((MARGIN, VIDEO_HEIGHT-MARGIN-text.size[1]))

link = TextClip(
    "noahdoersing.com",
    fontsize=end_font_size*1.5,
    color='white',
    font='OpticianSans',
    align='east'
    )
link = trim_text_clip(link)
link = link.set_position((VIDEO_WIDTH-MARGIN-link.size[0],
                          VIDEO_HEIGHT-MARGIN-link.size[1]))

license_icons = TextClip("a more diligent programmer would do this elegantly").set_opacity(0.0)
if LICENSE:
    status("Loading license icons...")
    license_codes = ["cc", *LICENSE]
    license_icons = list(map(lambda l: ImageClip("assets/cc/" + l + ".png"), license_codes))
    for i in range(len(license_icons)):
        icon = license_icons[i]
        icon_size = end_font_size * 1.5
        icon = icon.resize((icon_size, icon_size))
        icon = icon.set_position((i * 2.0 * end_font_size, 0))  # stagger them horizontally
        license_icons[i] = icon
    license_icons = CompositeVideoClip(license_icons, size=compute_static_clips_size(license_icons))
    license_icons = license_icons.set_position((
        VIDEO_WIDTH-MARGIN-license_icons.size[0],
        VIDEO_HEIGHT-MARGIN-link.size[1]-2*license_icons.size[1]
        ))

status("Drawing end card...")
endcard = [
    black,
    average_image.fx(vfx.blackwhite).set_opacity(0.2),
    logo.set_position((MARGIN,MARGIN)),
    intro,
    text,
    link,
    license_icons
    ]
endcard = CompositeVideoClip([clip.set_duration(ENDCARD_DURATION) for clip in endcard])
endcard = endcard.fadein(1).fadeout(1)

################################################################################

status("Putting everything together...")
video = concatenate_videoclips([
    black.set_duration(1),
    titles,
    black.set_duration(1 - TIME_BEFORE_FIRST_BEAT if TIME_BEFORE_FIRST_BEAT < 1 else 0),
    fields,
    black.set_duration(1),
    endcard,
    black.set_duration(1)
    ])

status("Writing – first audio, then video...")
video.write_videofile(VIDEO_PATH, fps=FPS, temp_audiofile="temp/temp_audio.mp3")

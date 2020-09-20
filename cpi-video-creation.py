##########
# CONFIG #
##########

NO = "002"
LOCATION = "Box Elder County"
LOCATION_SUBTITLE = "Utah, USA"
TITLECARD_DURATION = 5

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
LICENSE = ["by", "nc", "sa"]  # set to None for no license icons
ENDCARD_DURATION = 20

# all *.jpg files from this dir will be shown in the result video
IMAGES_DIR = "/Users/noah/Downloads/box-elder-county"
IMAGES_LIMIT = None  # handy for testing, set to None otherwise

VIDEO_WIDTH = 3840 / 2
VIDEO_HEIGHT = VIDEO_WIDTH / 2.33  # should be based on aspect ratio of inputs

MUSIC_FILE = "/Users/noah/Desktop/greyshadow.wav"
BPM = 100
TIME_BEFORE_FIRST_BEAT = 0.85

VIDEO_PATH = "result.mp4"
FPS = 30

THUMBNAIL_WIDTH = 1920
THUMBNAIL_HEIGHT = 1080
THUMBNAIL_PATH = "result-thumbnail.jpg"

################################################################################

import glob
import math
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

def trim_text_clip(clip):
    """Trims a clip, i.e. removes all transparent pixels from the edges."""

    f = "temp/trim_text_clip_tmp.png"
    f_result = "temp/trim_text_clip_tmp_result.png"
    clip.save_frame(f)
    subprocess.run([MAGICK, f, "-trim", f_result])
    return ImageClip(f_result)

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
    logo_font_size = BASE_FONT_SIZE * 1.3
    cpi = TextClip(
        "Center\nPivot\nIrrigation",
        fontsize=logo_font_size,
        color='white',
        font='OpticianSans',
        align='west',
        interline=-logo_font_size*0.3
        )
    no = TextClip(
        "#" + no,
        fontsize=logo_font_size,
        color='white',
        font='OpticianSans',
        align='west'
        )
    no = no.set_position((0, logo_font_size*1.87))
    no = no.set_opacity(0.87)

    logo = [cpi, no]
    logo = CompositeVideoClip(logo, size=compute_static_clips_size(logo))
    return trim_text_clip(logo)

def draw_title(main, sub):
    title_font_size = BASE_FONT_SIZE * 2.3
    main = TextClip(
        main,
        fontsize=title_font_size,
        color='white',
        font='OpticianSans',
        align='center',
        interline=-title_font_size*0.2
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
    # TODO check if these work for all situations
    if (vid_aspect > thumb_aspect):  # video wider
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

def overlay_geocoords_if_available(filename, imageclip):
    coords = re.search(r'(-?\d+.\d+),(-?\d+.\d+)', filename)
    if (not coords):
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

################################################################################

black = ColorClip((VIDEO_WIDTH,VIDEO_HEIGHT), color=(0, 0, 0))

status("Loading images...")
cpi_field_images = glob.glob(IMAGES_DIR + "/*.jpg")
cpi_field_images.sort()  # gotta make sure they're sorted
if IMAGES_LIMIT:
    cpi_field_images = cpi_field_images[:IMAGES_LIMIT]

cpi_field_clips = []
for i, f in enumerate(cpi_field_images):
    print(f"{i}/{len(cpi_field_images)}: " + f)
    clip = ImageClip(f).set_duration(60 / BPM).resize((VIDEO_WIDTH, VIDEO_HEIGHT))
    cpi_field_clips.append(clip)

status("Computing average image...")
cpi_fields = concatenate_videoclips(cpi_field_clips)
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

status("Overlaying geo coordinates over images...")
fields = []
for i, (f, clip) in enumerate(zip(cpi_field_images, cpi_field_clips)):
    print(f"{i}/{len(cpi_field_images)}: " + f)
    fields.append(overlay_geocoords_if_available(f, clip))
last_image = fields[-1]

status("Concatenating images, thus creating video...")
fields = concatenate_videoclips(fields)
fields = concatenate_videoclips([black.set_duration(TIME_BEFORE_FIRST_BEAT), fields])

# keep the last image on screen for a bit longer, then fade it out
last_image = concatenate_videoclips([last_image for i in range(10)]).set_duration(1.5).fadeout(1.5)

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
    align='west'
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
    average_image.set_opacity(0.2),
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
    last_image,
    black.set_duration(1),
    endcard,
    black.set_duration(1)
    ])

status("Writing – first audio, then video...")
video.write_videofile(VIDEO_PATH, fps=FPS, temp_audiofile="temp/temp_audio.mp3")

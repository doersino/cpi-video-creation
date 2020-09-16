font stuff:

moviepy uses imagemagick for text rendering. imagemagick comes with its own list of fonts that references the fonts preinstalled on every mac, but not custom ones. this list can be seen with

TextClip.list('font')

or, directly with im, with

convert -list font

at the top of the output of that command is the font list used (supposedly it will use ~/.magick/type.xml if exists, but it doesn't, instead it's something like /usr/local/Cellar/imagemagick/7.0.10-28/etc/ImageMagick-7/type-apple.xml). need to edit that file and add an entry for any font i wanna use, with correct path etc:

TODO additional entries here

  <type
     format="ttf"
     name="Iosevka"
     fullname="Iosevka"
     family="Iosevka"
     glyphs="/Users/noah/Library/Fonts/iosevka-regular.ttf"
     />
  <type
     format="otf"
     name="OpticianSans"
     fullname="OpticianSans"
     family="OpticianSans"
     glyphs="/Users/noah/Library/Fonts/Optician-Sans.otf"
     />

need to do this each time im is updated

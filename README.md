# cpi-video-creation

A quickly-thrown-together tool for making videos like [this one](TODO), intended for use with aerial imagery downloaded by [ærialbot](https://github.com/doersino/aerialbot) and cropped using [Crop Circles](https://github.com/doersino/cropcircles).

*This repository is probably not very interesting to you unless you're planning on using [MoviePy](https://zulko.github.io/moviepy/) yourself and are looking for an example project before you dive in.*

Each video created by this tool consists of three segments: a title card, a sequence of images (the average of which is used as the title card background) with a soundtrack, and an end card with further information.

![](assets/examples/1.jpg)

![](assets/examples/2.jpg)

![](assets/examples/3.jpg)


## Setup

Take a look at the [setup instructions for MoviePy](https://zulko.github.io/moviepy/) and check if there's anything special to be done on your system. On mine, setting up MoviePy entails installing [ImageMagick](https://www.imagemagick.org) and *patching* it in order to force it to recognize the required typefaces (which are located in `assets/fonts/`).


### Patching ImageMagick's font list

MoviePy uses ImageMagick for text rendering, which is terrible in many ways but just shy of terrible enough for me to consider building an alternative. Besides the completely-missing support for proper kerning and ligatures and text formatting and I don't even know what else, the [Homebrew](https://brew.sh)-provided distribution of ImageMagick comes with its own list of fonts that references the fonts preinstalled on every macOS system, but not custom ones. (With other ImageMagick distributions or on a different operating system, things might work a bit differently, I don't know.) This list can be pretty-printed (in Python/MoviePy) with

```python
TextClip.list('font')
```

or, directly with ImageMagick, with:

```
$ convert -list font
```

At the top of the output of that command is the path of the font list – on my system, as of September 2020, that's `/usr/local/Cellar/imagemagick/7.0.10-28/etc/ImageMagick-7/type-apple.xml`. (Supposedly, ImageMagick will instead use `~/.magick/type.xml` if that exists, but it just kinda doesn't. ¯\\\_(ツ)\_/¯) You will need to edit that file and add an entry for each of the two typefaces this tool uses, with whatever paths are correct on your system. The following Works On My Machine™:

```xml
  <type
     format="otf"
     name="OpticianSans"
     fullname="OpticianSans"
     family="OpticianSans"
     glyphs="/Users/noah/Library/Fonts/Optician-Sans.otf"
     />
  <type
     format="ttf"
     name="SourceSerifPro"
     fullname="SourceSerifPro"
     family="SourceSerifPro"
     glyphs="/Users/noah/Library/Fonts/SourceSerifPro-Regular.ttf"
     />
```

You might need to repeat this process each time you update ImageMagick.


### And the rest

Assuming things have gone smoothly so far, let's proceed – I suggest using the `venv` module (which is conveniently included in your Python installation) to avoid dependency hell. Run the following commands to get the tool installed on your system:

```bash
$ git clone https://github.com/doersino/cpi-video-creation
$ python3 -m venv cpi-video-creation
$ cd cpi-video-creation
$ source bin/activate
$ pip3 install -r requirements.txt
```

(To deactivate the virtual environment, run `deactivate`.)


## Configuration & Usage

Open `cpi-video-creation.py` and modify the variables at the top of the file, then (after making sure the virtual environment is active):

```
$ python3 cpi-video-creation.py
```


## License

You may use this repository's contents under the terms of the *MIT License*, see `LICENSE`.

However, the subdirectory `assets/fonts/` contains third-party fonts licensed under the *SIL Open Font License Version 1.1*, a copy of which is included with each of them.

Further, the subdirectory `assets/cc/` contains Creative Commons License icons, which appear to be licensed under the *Attribution 4.0 International License*, see [here](https://creativecommons.org/licenses/by/4.0/).

Finally, the two files `assets/beep.wav` and `assets/boop.wav` are recordings of my phone being bumped against my stove's power knobs. Since it took literally seconds to create them, you may use them as you like.

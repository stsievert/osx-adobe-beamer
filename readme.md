
## Motivation
Beamer has nice features:

* videos
* notes
* (also, it's a *great* presentation tool)

Adobe has some great features to display a PDF:

* transitions
* video/animation
* hyperlinks

but I couldn't find a way to include presenter notes when displaying a PDF full
screen (i.e., Beamer presentation). I couldn't find any other software that
included all the niceties of Adobe *and* had note support so I created a
wrapper for Adobe.

This wrapper allows presentations in Adobe but also allows you to view the
notes you write with `\note{}`.

![](speaker_view.jpg)

It does this by creating two PDFs and mapping your keypresses (arrows/etc) to
*both* open Acrobat windows.

This is not a big application; it only maps your keystrokes to both of Adobe
Readers windows. If it fails during a presentation, you can still survive! You
can still operate Adobe as normal and still have a presentation, but then the
notes will be out of sync.

## Latex compiling directions
I have provided a package so your presentation and notes have the same number
of slides.

0. Download this repo and copy `osx-adobe-beamer.sty` into the folder your
   presentation is in.
1. Include the line `\usepackage{osx-adobe-beamer}` before `\begin{document}`.
2. Compile your docuement with `\usepackage[notes]{osx-adobe-beamer}` and `\usepackage[slides]{osx-adobe-beamer}`.
(I'm fairly certain this file must be included after beamer options (I did it
   before `\begin{document}` and was fine)
3. Copy the PDFs so you can open them both at once.

## Presentation directions
0. Download this repo.
1. Open up `notes.pdf` and `presentation.pdf` in Adobe Reader.
2. Run the command `python /path/to/present.py` in your terminal
3. Make the window that opens up active/in front.
4. Certain keys are now mapped to Adobe Reader! (arrows/space/return)

## Requirements
* A LaTeX install, probably MacTex
* the `applescript` package, installable with `pip install py-applescript`
* an OSX machine (because this package runs an Applescript to map your
  keypresses)

## Similar software
* [PDFslide](http://sourceforge.net/projects/pdfslide/)
* [PDF Presenter](http://pdfpresenter.sourceforge.net/)
* [Présentation.app](http://iihm.imag.fr/blanch/software/osx-presentation/)
* [Skim](http://tex.stackexchange.com/a/21857/29873)
* [SplitShow](https://github.com/mpflanzer/splitshow)
* [PDF to Keynote](http://www.cs.hmc.edu/~oneill/freesoftware/pdftokeynote.html)
* [pympress](http://pympress.org/)
* [pdf-presenter](https://github.com/thefranke/pdf-presenter)

I didn't find any of these that could easily be installed on OSX, supported
video/animation playback *and* gave a "presenter" view.

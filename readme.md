
## Motivation
Beamer has nice features:

* videos
* notes
* (also, it's a *great* presentation tool)

but I haven't found a good viewer that supports both these options. Adobe
Reader supports videos and there are many options to support notes.

I wrapped Adobe Reader so it could show the notes on a separate screen: see the
screenshot below!

![](speaker_view.jpg)

This is not a big application; it only maps your keystrokes to both of Adobe
Readers windows. If it fails during a presentation, you can still survive!

## Presentation directions
0. Download this repo.
1. Open up `notes.pdf` and `presentation.pdf` in Adobe Reader.
2. Run the command `python /path/to/present.py` in your terminal
3. Make the window that opens up active/in front.
4. Certain keys are now mapped to Adobe Reader! (arrows/space/return)

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


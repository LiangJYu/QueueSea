Demo of offline standalone plotting tool for replacing LG QC webapp

Read in plant readouts and calculate additional parameters; load everything for plotting.

Basic usage video: https://youtu.be/n3I0svB3TFY

Usage:

python gui.py

Note:

.ui has to be pyuic'd before usage

TODO:

Make clear button do something

Add unit tests

Add per-y-axis controls for marker type, color, linewidth, etc...

Add filtering x-axis by time

Add database to more efficiently track and accumulate data (vs independently managed Excel or csv)

Enable compilation to an execuatable

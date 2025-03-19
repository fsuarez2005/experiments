#!/bin/zsh

OUTNAME=texput

tex \\relax


if [ -f "$OUTNAME.dvi" ]; then

	dvipdf "$OUTNAME.dvi" && open "$OUTNAME.pdf"
	
fi


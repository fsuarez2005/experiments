temp = resume.dvi resume.pdf resume.log
#resumecomponents = header.tex education.tex projects.tex workexperience.tex
#resumecomponents = 

all: resume.pdf




resume.pdf: resume.dvi
	dvipdf resume.dvi


resume.dvi: resume.tex
	tex resume.tex
	
clean:
	rm $(temp)

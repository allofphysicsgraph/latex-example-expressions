IMAGENAME=latex-examples

help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"

# on linux
docker:
	sudo service docker start
	sudo docker build -t $(IMAGENAME) .
	sudo docker run -it --rm $(IMAGENAME) /bin/bash

# for Mac
docmac:
	docker build -t $(IMAGENAME) .
	docker run -it --rm -v `pwd`:/scratch $(IMAGENAME) /bin/bash

pythonmac:
	docker run -it --rm --workdir /scratch -v `pwd`:/scratch $(IMAGENAME) python3 /scratch/generate_pdf_from_latex_files.py


clean:
	rm -rf *.aux *.log *.tex *.pdf *.dvi
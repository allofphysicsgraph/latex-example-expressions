help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"

docker:
	sudo service docker start
	sudo docker build -t latex-examples .
	sudo docker run -it --rm latex-examples /bin/bash

docmac:
	docker build -t latex-examples .
	docker run -it --rm latex-examples /bin/bash


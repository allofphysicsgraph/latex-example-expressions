help:
	@echo "make docker"
	@echo "         for linux"
	@echo "  "
	@echo "make docmac"
	@echo "         for Mac"

docker:
	sudo service docker start
	sudo docker build -t msg_sympy .
	sudo docker run -it --rm msg_sympy /bin/bash

docmac:
	docker build -t msg_sympy .
	docker run -it --rm msg_sympy /bin/bash


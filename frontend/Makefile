###########
# Site
frontend-run:
	$(info Start site)
	yarn start

# Build image of site for
frontend-build-image: IMAGE_TAG := zifter/byprice24-site:test
frontend-build-image:
	$(info Build docker image)
	docker build . -t $(IMAGE_TAG)

frontend-run-image: IMAGE_TAG := zifter/byprice24-site:test
frontend-run-image:
	$(info Build docker image)
	docker run -p 3000:3000 -t $(IMAGE_TAG)

###########
# Site
run:
	$(info Start site)
	yarn start

# Build image of site for
build-image: IMAGE_TAG := zifter/byprice24-site:test
build-image:
	$(info Build docker image)
	docker build . -t $(IMAGE_TAG)

run-image: IMAGE_TAG := zifter/byprice24-site:test
run-image:
	$(info Build docker image)
	docker run -p 3000:3000 -t $(IMAGE_TAG)

###########
# Site
setup:
	npm install

run:
	$(info Start site)
	yarn start

# Build image of site for
image-build: IMAGE_TAG := test
image-build:
	$(info Build docker image)
	docker build . -t zifter/byprice24-site:$(IMAGE_TAG)

run-image: IMAGE_TAG := test
run-image:
	$(info Build docker image)
	docker run -p 3000:3000 -t zifter/byprice24-site:$(IMAGE_TAG)

lint:
	npm run eslint

lint-fix:
	npm run eslint-fix

test:
	npm run test

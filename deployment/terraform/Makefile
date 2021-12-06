install:
	sudo tfenv install 0.13.7
	sudo tfenv use 0.13.7

login:
	terraform login

refresh:
	$(info Execute terraform refresh)
	terraform refresh -var-file="local.tfvars"

init:
	$(info Execute terraform init)
	terraform init

.SILENT:
output: NAME=""
output:
	$(info Execute terraform refresh)
	terraform output $(NAME)

plan:
	$(info Execute terraform refresh)
	terraform plan -var-file="local.tfvars"

apply:
	$(info Execute terraform plan)
	terraform apply -var-file="local.tfvars"

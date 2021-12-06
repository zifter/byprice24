install:
	sudo tfenv install 0.13.7
	sudo tfenv use 0.13.7

login:
	terraform login

refresh:
	$(info Execute terraform refresh)
	terraform refresh -var-file="local.auto.tfvars"

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
	terraform plan -var-file="local.auto.tfvars"

apply:
	$(info Execute terraform plan)
	terraform apply


s3_bucket=sam-artifacts-dev
stack_name ?= juni-fondo
sam_template_base=sam
sam_template=$(sam_template_base).yml
sam_output=$(sam_template_base)-new.yml


build:
	juni build

package:
	sam package \
	    --s3-bucket $(s3_bucket) \
	    --template-file $(sam_template) \
	    --output-template-file ./dist/$(sam_output) \
	    --profile $(profile)

deploy: build package
	sam deploy \
	    --template-file ./dist/$(sam_output) \
	    --stack-name $(stack_name) \
	    --capabilities CAPABILITY_IAM \
	    --region us-east-1 \
	    --profile $(profile)

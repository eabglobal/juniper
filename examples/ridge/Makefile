s3_bucket=temp-awsdev
stack_name ?= juni-ridge
sam_template_base=sam
sam_template=$(sam_template_base).yml
sam_output=$(sam_template_base)-new.yml


build:
	docker build -t juniper/xmlsec -f docker/Dockerfile.xmlsec .
	juni build

package:
	sam package \
	    --s3-bucket $(s3_bucket) \
	    --template-file $(sam_template) \
	    --output-template-file ./dist/$(sam_output) \
	    --profile $(profile)

deploy: package
	sam deploy \
	    --template-file ./dist/$(sam_output) \
	    --stack-name $(stack_name) \
	    --capabilities CAPABILITY_IAM \
	    --region us-east-1 \
	    --profile $(profile)

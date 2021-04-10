install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,W1203,E1101 mlib predict utilscli app; 
	docker run --rm -i hadolint/hadolint:latest < Dockerfile; 
	cd aws-lambda-sam/stroke-application/stroke_app/; \
		pylint --disable=R,C,W1203,E1101 mlib predict app; \
		docker run --rm -i hadolint/hadolint:latest hadolint --ignore DL3045 --ignore DL3013 - < Dockerfile
	
ecr:
	aws ecr create-repository --repository-name stroke-prediction-app --image-tag-mutability IMMUTABLE --image-scanning-configuration scanOnPush=true
		
deploy:
	cd aws-lambda-sam/stroke-application/stroke_app; \
		pylint --disable=R,C,W1203,E1101 mlib predict app; \
		docker run --rm -i hadolint/hadolint:latest hadolint --ignore DL3045 --ignore DL3013 - < Dockerfile; \
	cd ..; \
		sam build; \
		sam deploy --config-file samconfig.toml --no-confirm-changeset
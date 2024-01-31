rm -rf ./dest/
rm requirements.txt

poetry export --without-hashes --format=requirements.txt > requirements.txt

docker run -it --rm -v C:/Users/kirin/Desktop/AI/aws-lambda-youtubetranscriptapi/aws_lambda_youtubetranscriptapi/:/tmp python:3.11 bash -c "pip install -r tmp/requirements.txt -t tmp/dest/; exit"

cp -r ./src/ ./dest/
cp lambda_function.py ./dest/

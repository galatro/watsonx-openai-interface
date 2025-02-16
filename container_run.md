source ./.env
podman run -d -p 8080:8000 --name watsonxai-endpoint \
-e IBM_API_KEY=${IBM_API_KEY} \
-e WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID} \
-e WATSONX_REGION=${WATSONX_REGION} \

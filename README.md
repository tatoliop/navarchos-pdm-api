# navarchos-pdm-api
API for the PdM module

## Deployment

Build the docker image with `docker build -t navarchos-pdm:0.0.1 .`

Run the docker image with `docker run -d --name navarchos -p 8080:8080 navarchos-pdm:0.0.1`

OR

Using the `docker-compose.yml` file, e.g., `docker-compose up` will build the image (if not present) and run the service.

Examples on the API requests are available in the Swagger docs after deployment using `localhost:8080/swagger`

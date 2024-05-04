# Order Processing System

## Description

The system should handle order processing, including stock validation, payment processing (integrated with a mock payment gateway), and sending order confirmation emails to customers.

**Technologies**: Python, Flask, Mongodb, Docker and render.

## Features
Stock Management: Implement functionality to validate the availability of products in the store's inventory when
placing an order. Ensure that the system updates the stock count accordingly after each successful order.
2. Payment Processing: Integrate with a mock payment gateway to simulate payment processing. Upon successful payment, mark the order as paid and proceed with order fulfillment.
3. Order Confirmation Emails: Develop a feature to send order confirmation emails to customers after a successful purchase. The email should include details such as the order ID, purchased items, and total amount.
4. Error Handling: Implement error handling to gracefully manage any issues that may occur during the order processing flow, such as stock unavailability or payment failures.
5. Documentation: Provide clear and concise documentation on how to set up and run the Order Processing System on (swagger)
6. Containerization: Dockerize the Order Processing System by creating a Dockerfile to package the application into a container. Ensure that the Dockerfile is included in the repository.
7. Repository Integration: Push the built Docker image to a container registry/repository on Docker Hub
Docker Hub).

## Documentation

- Deployed on render [here](https://appgaintask.onrender.com/api/docs)

## Getting Started

1. pull Docker image.
- Docker image on Docker Hub [here](https://hub.docker.com/repository/docker/mohmed123/python-appgain/general)

2. Run a command
```bash
$ docker run -d -p 4000:4000 mohmed123/python-appgain
```

3. **Contribution**: Contributions are welcome! If you find any issues or would like to add new features, feel free to open a pull request.


### if dont want use docker then follow this commands
```bash
$ py -m venv .venv

$ .venv\Scripts\Activate

$ pip install -r requirements.txt

$ flask run
```

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to the NestJS team for providing an excellent framework for building web applications.
- Special thanks to the contributors of libraries and tools used in this project.

## Full Stack Application with Monitoring and Logging

This project sets up the infrastructure for the Boss application using Docker Compose, Traefik, and AWS Route53. The setup includes a frontend, backend, database, and monitoring services with Traefik managing SSL certificates and path-based routing.

## Project Structure

The project is organized into the following structure:

- `application/`: Contains the application stack, including frontend, backend, and database services. Also contains configuration files for monitoring services such as Prometheus, Grafana, Loki, and Promtail.
- `frontend/`: Contains the source code for the frontend.
- `backend/`: Contains the source code for the backend.
- `traefik/`: Contains configuration files for the Traefik proxy.

## Features

1. **Traefik Proxy**:
   - Handles path-based routing for all services.
   - Automatically issues SSL certificates via Let's Encrypt.

2. **Route53 Domains**:
   - Two A records are set up for the domain:
     - `www.boss.kapilkumaria.com`
     - `boss.kapilkumaria.com`

3. **Monitoring**:
   - Prometheus, Grafana, Loki, and Promtail for application monitoring and logging.

## Prerequisites

1. Ensure Docker and Docker Compose are installed.
2. Set up the following A records in AWS Route53:
   - `www.boss.kapilkumaria.com`
   - `boss.kapilkumaria.com`
3. Point the A records to your server's IP address.

## Setup

### Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-folder>
```
## Configure Environment Variables

    Adjust database credentials in the backend/.env file.
    Configure Traefik with the domain names in the docker-compose.yml file.

## Run the Application

Run the application stack and monitoring stack using Docker Compose:
```
docker compose up -d
```

## Access the Services

- Frontend: https://boss.kapilkumaria.com
- Backend API: https://boss.kapilkumaria.com/api
- Backend Docs: https://boss.kapilkumaria.com/docs
- Prometheus: https://boss.kapilkumaria.com/prometheus
- Grafana: https://boss.kapilkumaria.com/grafana
- Database Admin: https://boss.kapilkumaria.com/adminer

## Traefik Configuration

- SSL certificates for boss.kapilkumaria.com are automatically issued via Let's Encrypt.
- HTTP to HTTPS redirection and www to non-www redirection are handled by Traefik.

## Monitoring Setup

After all applications are successfully accessible through the custom domain, configure Grafana for visualizing metrics and logs:
Login to Grafana

## Access Grafana and login using the default credentials:

      Username: admin
      Password: admin

## Set Up Data Sources

### Prometheus:

- Add a new data source with the URL: http://prometheus:9090/prometheus

### Loki:

- Add a new data source with the URL: http://loki:3100

### Import Pre-Built Dashboard

- Import the Container Metrics dashboard using ID: 19792

## Create Custom Dashboard

    Create a new dashboard and configure the following variables in Settings:
        Variable 1:
            Name: container
            Display Name: Container
            Type: Query
            Label Value: container_name
        Variable 2:
            Name: container_search
            Display Name: Search
            Type: Textbox
        Variable 3:
            Name: severity
            Display Name: Severity
            Type: Custom
            Custom Values: info, warn, error
        Variable 4:
            Name: NodeLogs
            Display Name: Node Logs
            Type: Query
            Label Value: filename
        Variable 5:
            Name: varlog_search
            Display Name: NodeLog Filter
            Type: Textbox

- Create a new visualization for Container Logs with the following query:
```
{container_name="$container"} |~ `$container_search` | logfmt level | (level =~ `$severity` or level= "")

Create a new visualization for Node Logs with the following query:

    {job="varlogs"} |~ `$varlog_search`
```

## Functionality

**Container Logs**:
        Search container logs using container_search.
        Filter logs by severity (info, warn, error).

**Node Logs**:
        Search node logs using varlog_search.
        Apply filters for efficient log analysis.

## Verifications

1. Verify that all services are running and accessible via the defined paths.
2. Test HTTP to HTTPS redirection.
3. Test www to non-www redirection.

## Future Enhancements

- Add more services as required with Traefik managing the routing.
- Integrate additional monitoring tools if necessary.

## Troubleshooting

- **SSL Issues**:
        Ensure the domain A records are correctly pointing to your server.
        Check Traefik logs for any SSL certificate errors.

- **Service Connectivity**:
        Verify container logs for errors.
        Ensure environment variables are correctly configured.

---
---

## How to Use This Repository

Follow the steps below to set up and deploy the services defined in this repository:

### Step 1: Clone the Repository

Clone this repository to your server to access the application and configuration files.
```
git clone https://github.com/kapilkumaria/cv-challenge01.git
```
### Step 2: Navigate to the Application Directory

Move into the application folder where the main docker-compose.yml file is located.
```
cd cv-challenge01/application
```
### Step 3: Create a Docker Network

Create a Docker network named app_network. This network ensures seamless communication between the containers.
```
docker network create app_network
```
## Step 4: Secure the ACME Configuration

Ensure that the acme.json file (used by Traefik for Let's Encrypt certificates) has the correct permissions for security.
```
chmod 600 cv-challenge01/traefik/letsencrypt/acme.json
```
    Note: Incorrect permissions may prevent Traefik from functioning properly and could expose sensitive certificate data.

### Step 5: Configure DNS Settings

Add the following A records in your AWS Route 53 hosted zone (or equivalent DNS management service) to point to your server's public IP address:
```
    www.boss.kapilkumaria.com
    boss.kapilkumaria.com
```
    Tip: Ensure that your DNS changes propagate correctly by verifying them with tools like nslookup or dig.

### Step 6: Deploy Services with Docker Compose

Use Docker Compose to build and deploy the services defined in the docker-compose.yml file. The -d flag runs the containers in detached mode.
```
docker compose up -d --build
```
    Best Practice: Always review the logs after deployment using docker compose logs to ensure all services are running as expected.

### Step 7: Access the Application

Once the services are running, access the deployed application through the following URLs:

Main Application: https://www.boss.kapilkumaria.com

Adminer (Database Management): https://www.boss.kapilkumaria.com/adminer

API Documentation (Swagger UI): https://www.boss.kapilkumaria.com/docs

API Documentation (ReDoc): https://www.boss.kapilkumaria.com/redoc

Monitoring (Prometheus): https://www.boss.kapilkumaria.com/prometheus

Dashboard (Grafana): https://www.boss.kapilkumaria.com/grafana

## Additional Notes

**Scalability**: This repository is designed to scale across environments with minor modifications to docker-compose.yml or Traefik configurations.

**Security**: Ensure you follow best practices for securing access, including using strong passwords and restricting access via firewall or security groups.

## Troubleshooting:
- Check Traefik logs: docker logs traefik
- Validate DNS resolution using tools like nslookup or dig.

For further information or contributions, feel free to open an issue or submit a pull request.
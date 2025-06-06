# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /opt/dagster/app

# Copy the setup files and install dependencies
COPY setup.py pyproject.toml README.md /opt/dagster/app/
COPY dagster_multi_etl /opt/dagster/app/dagster_multi_etl
COPY dagster_multi_etl_tests /opt/dagster/app/dagster_multi_etl_tests

# Install Dagster and project dependencies
# Ensure .[dev] extras are installed for dagster-webserver
RUN pip install --upgrade pip &&     pip install -e ".[dev]"

# Copy the workspace file
COPY workspace.yaml /opt/dagster/app/

# Create DAGSTER_HOME directory and set permissions
RUN mkdir -p /opt/dagster/dagster_home &&     chown -R 1001:0 /opt/dagster/dagster_home ||     (echo "Failed to chown DAGSTER_HOME, perhaps running as non-root or user/group 1001:0 does not exist. Continuing..." && true)

# Expose the port Dagster UI runs on
EXPOSE 3000

# Command to run Dagster Dagit (webserver)
# This will be overridden by docker-compose for the daemon
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000", "-w", "workspace.yaml"]

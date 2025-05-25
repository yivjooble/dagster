# dagster_multi_etl

This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/guides/build/projects/creating-a-new-project).

## Getting started

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `dagster_multi_etl/assets.py`. The assets are automatically loaded into the Dagster code location as you define them.

## Running with Docker Compose

This project can be run using Docker Compose, which simplifies the setup of the Dagster webserver and daemon.

**Prerequisites:**
- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: Usually included with Docker Desktop. If not, [Install Docker Compose](https://docs.docker.com/compose/install/).

**Steps:**

1.  **Build and run the containers:**
    Navigate to the `dagster_multi_etl` project directory (where the `docker-compose.yml` file is located) and run:
    ```bash
    docker-compose up --build
    ```
    The `--build` flag ensures the Docker image is built the first time or when `Dockerfile` changes. Subsequent runs can omit `--build` if no changes to the Docker environment are made.

2.  **Access Dagster UI:**
    Open http://localhost:3000 in your browser to see the Dagster UI.

3.  **Stopping the services:**
    To stop the Docker Compose services, press `Ctrl+C` in the terminal where `docker-compose up` is running, or run:
    ```bash
    docker-compose down
    ```
    This will stop and remove the containers.

## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

Tests are in the `dagster_multi_etl_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_multi_etl_tests
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/guides/automate/schedules/) or [Sensors](https://docs.dagster.io/guides/automate/sensors/) for your jobs, the [Dagster Daemon](https://docs.dagster.io/guides/deploy/execution/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.

## Deploy on Dagster+

The easiest way to deploy your Dagster project is to use Dagster+.

Check out the [Dagster+ documentation](https://docs.dagster.io/dagster-plus/) to learn more.

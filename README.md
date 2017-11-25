# LAMP on Docker - Hello world

Simple example of a LAMP stack using Docker.

# Start the LAMP stack

## Using Python Invoke
 
- `virtualenv .ve` - Create a virtual Python environment
- `. .ve/bin/activate` - Activate the virtual environment
- `pip install -r requirements.txt`
- `inv -l` - List available tasks
- `inv up` - Start basic LAMP stack using Docker Compose.
- Navigate to `localhost:8080`

## Using Docker Compose

- `up.sh` - Start basic LAMP stack using Docker Compose.
- Navigate to `localhost:8080`
- `down.sh` - Stop all containers.

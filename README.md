# python-web-api-flask-oracle-simple

## Description
Creates an api of `dog` table in default namespace `FREEPDB1`.
Has the ability to query by parameters.

Remotely tested with *testify*.

## Tech stack
- python
  - flask
  - oracle
  - testify
  - requests

## Docker stack
- python:latest
- gvenzl/oracle-free:latest

## To run
`sudo ./install.sh -u`
- Get all routes: http://localhost/help

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- [Oracle docker image](https://hub.docker.com/r/gvenzl/oracle-free)
- [All routes for flask app](https://github.com/pallets/flask/blob/2.1.2/src/flask/cli.py#L931)
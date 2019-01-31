#!/bin/bash
set -e

export PATH=$PATH:/home/flaskuser/.local/bin
exec "$@"

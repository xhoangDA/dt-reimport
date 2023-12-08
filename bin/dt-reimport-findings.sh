#!/bin/sh
export PYTHONPATH="${PYTHONPATH}:/usr/local/dt-reimport"
python -m dt_reimport.dt_reimport_findings

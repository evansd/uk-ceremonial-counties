#!/bin/bash
set -eo pipefail
./merge_and_label_counties.py source-geojson/*.geojson \
  | node_modules/mapshaper/bin/mapshaper - \
  -format=geojson \
  -dissolve county sum-fields=area \
  -o - > uk-ceremonial-counties.geojson

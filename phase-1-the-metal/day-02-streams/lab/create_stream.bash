#!/bin/bash
mkdir -p ./archive

(while true; do
  echo "$(($RANDOM%255)).0.0.1 - - [$(date +%d/%b/%Y:%H:%M:%S)] \"GET /api/v1/data HTTP/1.1\" 200"
  # Let's speed it up to see the 'metal' move
  sleep 0.01
done) | \
# pv shows the rate of lines passing through
pv -l -N "Raw Stream" | \
grep -v --line-buffered "healthcheck" | \
# pv shows the rate after filtering
pv -l -N "Filtered" | \
tee >(gzip --fast > ./archive/access_$(date +%F).log.gz) | \
awk '{print "DB Load ->", $1}'
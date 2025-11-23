#!/bin/bash

echo "Last update: $(date)" > activity.log
git add activity.log
git commit -m "Daily update on $(date)"
git push


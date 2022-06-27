#!/bin/bash

POST=$(curl -X POST http://localhost:5000/api/timeline_post -d "name=luke&email=luke@luke.com&content=test")
GET=$(curl http://localhost:5000/api/timeline_post)

if [[ "$POST" == *"$GET"* ]] || [[ "$GET" != "" ]]; then
	echo "Passed"
    exit 0
else
	echo "Failed"
    exit 1
fi
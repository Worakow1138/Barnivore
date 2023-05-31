#!/bin/bash

# Ensure that GOOGLE_APPLICATION_CREDENTIALS is set as an ENV variable in Cloud Run Job
gcloud auth activate-service-account --key-file GOOGLE_APPLICATION_CREDENTIALS
moonrise $@
export TZ="America/New_York"
current_date_time=$(date '+%Y-%m-%d_%H:%M:%S')
gsutil -m cp -r reports gs://barnivore_test_reports/reports_$current_date_time
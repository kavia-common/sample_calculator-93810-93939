#!/bin/bash
cd /home/kavia/workspace/code-generation/sample_calculator-93810-93939/Sample_calculatorBackend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi


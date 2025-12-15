#! /usr/bin/env bash

source flamapyenv/bin/activate

# Which variability model to analyze?
CATALOGUE="${1:-catalogue.uvl}"
echo "Analyzing ${CATALOGUE}"

echo "## Model Structure"

# Satisfiability
echo "Is the catalogue satisfiable?"
flamapy satisfiable $CATALOGUE 

# False optional features
echo "Identify false optional features"
flamapy false_optional_features $CATALOGUE 

# Dead features
echo "Identify dead features"
flamapy dead_features $CATALOGUE 

echo "## Model usage"

# Configuration set cardinality
echo "How many different possible configurations?"
numfmt --grouping $(flamapy configurations_number $CATALOGUE)

echo "How many decisions from the user?"
flamapy count_leafs $CATALOGUE 



#!/bin/bash

# Pink Morsels Test Suite Runner
# This script automates running the test suite for CI/CD pipelines

set -e

echo "=========================================="
echo "  Pink Morsels Test Suite Runner"
echo "=========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if virtual environment exists, create if not
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Creating virtual environment...${NC}"
    python3 -m venv venv
fi

# Activate virtual environment
echo -e "${YELLOW}Activating virtual environment...${NC}"
source venv/bin/activate

# Install dependencies
echo -e "${YELLOW}Installing dependencies...${NC}"
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

# Run the test suite
echo -e "${YELLOW}Running test suite...${NC}"
echo ""

# Run pytest and capture exit code
if pytest test_app.py -v --tb=short; then
    echo ""
    echo -e "${GREEN}=========================================="
    echo -e "  ✅ ALL TESTS PASSED!"
    echo -e "==========================================${NC}"
    exit 0
else
    echo ""
    echo -e "${RED}=========================================="
    echo -e "  ❌ SOME TESTS FAILED!"
    echo -e "==========================================${NC}"
    exit 1
fi

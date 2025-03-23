#!/bin/bash

# Path to test programs
TEST_DIR="test_programs"
my_output="my_output.txt"
ref_output="ref_output.txt"

# Check if test directory exists
if [ ! -d "$TEST_DIR" ]; then
    echo "Error: Test directory '$TEST_DIR' not found!"
    exit 1
fi

# Function to compare outputs
compare_outputs() {
    if diff -w "$1" "$2" > /dev/null; then
        return 0  # Match
    else
        return 1  # Different
    fi
}

# Print header
echo "================================================"
echo "      VERIFICATION CONDITION GENERATOR TESTER    "
echo "================================================"
echo

# Get all test files
test_files=("$TEST_DIR"/test*.vcg)
total=${#test_files[@]}
matches=0
mismatches=0

# Process each test file
for test_file in "${test_files[@]}"; do
    filename=$(basename "$test_file")
    echo -n "Testing $filename... "
    
    # Run your implementation
    python3 VCG.py "$test_file" > "$my_output" 2>/dev/null
    
    # Run reference implementation
    java -jar VCG18.jar "$test_file" > "$ref_output" 2>/dev/null
    
    # Compare outputs
    if compare_outputs "$my_output" "$ref_output"; then
        echo "✅ MATCH"
        ((matches++))
    else
        echo "❌ MISMATCH"
        echo "   Differences:"
        diff -w "$my_output" "$ref_output" | sed 's/^/   /'
        echo
        ((mismatches++))
    fi
done

# Print summary
echo
echo "================================================"
echo "                   SUMMARY                      "
echo "================================================"
echo "Total tests:  $total"
echo "Matches:      $matches"
echo "Mismatches:   $mismatches"

if [ "$mismatches" -eq 0 ]; then
    echo -e "\n🎉 ALL TESTS PASSED! 🎉"
else
    echo -e "\n⚠️  SOME TESTS FAILED! ⚠️"
fi

# Clean up
rm -f "$my_output" "$ref_output"
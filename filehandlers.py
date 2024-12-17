# Function to calculate the weighted grade
def calculate_weighted_grade(marks_weights):
    total_marks = 0
    total_weight = 0
    for mark, weight in marks_weights:
        total_marks += mark * (weight / 100)
        total_weight += weight
    if total_weight != 100:
        raise ValueError("Total weight must add up to 100.")
    return total_marks
# Function to process the input and write to output
def process_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        outfile.write("Name, Mark, Grade\n")  # Write the header
        while True:
            name = infile.readline().strip()  # Read the student's name
            if not name:
                break
            marks_weights = []
            for _ in range(3):  # Read 3 units for each student
                line = infile.readline().strip()
                unit, mark, weight = line.split(", ")
                marks_weights.append((float(mark), float(weight)))
            final_mark = calculate_weighted_grade(marks_weights)
            # Assign grade based on final mark
            if final_mark >= 70:
                grade = "Distinction"
            elif final_mark >= 60:
                grade = "Merit"
            elif final_mark >= 50:
                grade = "Pass"
            else:
                grade = "Fail"
            outfile.write(f"{name}, {final_mark:.2f}, {grade}\n")  # Write result to file
# Main program
if __name__ == "__main__":
    input_file = "input.txt"   # Input file name
    output_file = "output.txt"  # Output file name
    process_file(input_file, output_file)
    print("Results have been written to", output_file)

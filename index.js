const dfd = require('danfojs-node');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
const { spawnSync } = require('child_process');

// Function to prompt user for input
function promptInput(question) {
    return new Promise((resolve) => {
        readline.question(question, (answer) => {
            resolve(answer);
        });
    });
}

// Main function to collect input, create a DataFrame, and send data to Python
async function main() {
    // Prompt the user for input
    const age = await promptInput('Enter your age: ');
    const gender = await promptInput('Enter your gender: ');
    const income = await promptInput('Enter your income: ');

    // Create a dictionary from the input
    const data = {
        Age: [parseInt(age)], // Convert age to a number
        Gender: [gender],
        Income: [parseFloat(income)] // Convert income to a number
    };

    // Create a single-row DataFrame from the dictionary
    const df = new dfd.DataFrame(data);

    // // Print the DataFrame
    // console.log('\nSingle-Row DataFrame:');
    // df.print();

    // Convert the DataFrame to JSON
    const jsonData = JSON.stringify(df.toJSON());

    // Send the JSON data to Python
    const pythonProcess = spawnSync('python', ['node.py', jsonData], {
        encoding: 'utf-8'
    });

    // Check for errors
    if (pythonProcess.error) {
        console.error('Error executing Python script:', pythonProcess.error);
        return;
    }

    // Capture and log the output
    const output = pythonProcess.stdout;
    // const response = JSON.parse(output);
    console.log('Python Output:', output);

    // Close the readline interface
    readline.close();
}

// Run the main function
main();
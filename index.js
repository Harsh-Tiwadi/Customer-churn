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

// [
//     'gender', 'under_30', 'senior_citizen', 'dependents', 'married', 'phone_service',
//     'internet_service', 'online_security', 'online_backup', 'device_protection',
//     'premium_tech_support', 'streaming_tv', 'streaming_movies', 'streaming_music',
//     'internet_type', 'contract', 'paperless_billing', 'payment_method', 'monthly_ charges',
//     'avg_monthly_long_distance_charges', 'total_charges', 'total_long_distance_charges',
//     'total_revenue', 'tenure', 'multiple_lines', 'avg_monthly_gb_download', 'unlimited_data',
//     'offer', 'satisfaction_score', 'cltv', 'churn_label', 'extra_data_charges', 'referrals'
// ]

// Main function to collect input, create a DataFrame, and send data to Python
async function main() {
    // Prompt the user for input
    const gender = await promptInput('Enter your gender {"1":Male, "2":Female}: ');
    const under_30 = await promptInput('Is your age under_30 {"1":yes, "0":no}: ');
    const senior_citizen = await promptInput('Is your age above_65 {"1":yes, "0":no}: ');
    const dependents = await promptInput('Any dependents {"1":yes, "0":no}: ');
    const married = await promptInput('married {"1":yes, "0":no}: ');
    const phone_service = await promptInput('using phone_service? {"1":yes, "0":no}: ');
    const internet_service = await promptInput('using internet_service? {"1":yes, "0":no}: ');
    const online_security = await promptInput('online_security {"1":yes, "0":no}: ');
    const online_backup = await promptInput('online_backup {"1":yes, "0":no}: ');
    const device_protection = await promptInput('device_protection {"1":yes, "0":no}: ');
    const premium_tech_support = await promptInput('premium_tech_support {"1":yes, "0":no}: ');
    const streaming_tv = await promptInput('streaming_tv {"1":yes, "0":no}: ');
    const streaming_movies = await promptInput('streaming_movies {"1":yes, "0":no}: ');
    const streaming_music = await promptInput('streaming_music {"1":yes, "0":no}: ');
    const internet_type = await promptInput('internet_type {"1": "Fiber Optic", "2": "DSL", "3": "Cable"}: ');
    const contract = await promptInput('contract period {"1": "Month-Month", "2": "Two year", "3": "One year"}: ');
    const paperless_billing = await promptInput('paperless_billing {"1":yes, "0":no}: ');
    const payment_method = await promptInput('payment method {"1": "Electronic check", "2": "Mailed check", "3": "bank transfer(automatic)", "4": "credit card(automatic)"}: ');
    const monthly_charges = await promptInput('monthly_charges: ');
    const avg_monthly_long_distance_charges = await promptInput('avg_monthly_long_distance_charges: ');
    const total_charges = await promptInput('total_charges: ');
    const total_long_distance_charges = await promptInput('total_long_distance_charges: ');
    const total_revenue = await promptInput('total_revenue: ');
    const tenure = await promptInput('tenure: ');
    const multiple_lines = await promptInput('multiple_lines {"1":yes, "0":no}: ');
    const avg_monthly_gb_download = await promptInput('avg_monthly_gb_download: ');
    const unlimited_data = await promptInput('unlimited_data {"1":yes, "0":no}: ');
    const offer = await promptInput('offer {"1":offer B, "2":offer E, "3":offer D, "4":offer A, "5":offer C}: ');
    const satisfaction_score = await promptInput('satisfaction_score {1,2,3,4,5}: ');
    const cltv = await promptInput('cltv: ');
    const extra_data_charges = await promptInput('extra_data_charges {"1":yes, "0":no}: ');
    const referrals = await promptInput('referrals {"0":no, "1":less than 5 times, "2": more than 5 times}: ');

    // Create a dictionary from the input
    const data = {
        gender: [parseInt(gender)],
        under_30: [parseInt(under_30)],
        senior_citizen: [parseInt(senior_citizen)],
        dependents: [parseInt(dependents)],
        married: [parseInt(married)],
        phone_service: [parseInt(phone_service)],
        internet_service: [parseInt(internet_service)],
        online_security: [parseInt(online_security)],
        online_backup: [parseInt(online_backup)],
        device_protection: [parseInt(device_protection)],
        premium_tech_support: [parseInt(premium_tech_support)],
        streaming_tv: [parseInt(streaming_tv)],
        streaming_movies: [parseInt(streaming_movies)],
        streaming_music: [parseInt(streaming_music)],
        internet_type: [parseInt(internet_type)],
        contract: [parseInt(contract)],
        paperless_billing: [parseInt(paperless_billing)],
        payment_method: [parseInt(payment_method)],
        avg_monthly_long_distance_charges: [parseFloat(avg_monthly_long_distance_charges)],
        total_charges: [parseFloat(total_charges)],
        total_long_distance_charges: [parseFloat(total_long_distance_charges)],
        total_revenue: [parseFloat(total_revenue)],
        tenure: [parseFloat(tenure)],
        multiple_lines: [parseInt(multiple_lines)],
        avg_monthly_gb_download: [parseFloat(avg_monthly_gb_download)],
        unlimited_data: [parseInt(unlimited_data)],
        offer: [parseInt(offer)],
        satisfaction_score: [parseInt(satisfaction_score)],
        cltv: [parseFloat(cltv)],
        extra_data_charges: [parseInt(extra_data_charges)],
        referrals: [parseInt(referrals)],
        monthly_charges: [parseFloat(monthly_charges)]
    };

    // Create a single-row DataFrame from the dictionary
    // const df = new dfd.DataFrame(data);
    const df = await dfd.readCSV("model"); // Path to your CSV file

    // // Print the DataFrame
    // console.log('\nSingle-Row DataFrame:');
    // df.print();

    // Convert the DataFrame to JSON
    const jsonData = JSON.stringify(df.toJSON());

    // Send the JSON data to Python
    const pythonProcess = spawnSync('python', ['model/model.py', jsonData], {
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
    res = output.toString()
    if (output==1){
        console.log('churned');
    }
    else{
        console.log('not churn')
    }

    // Close the readline interface
    readline.close();
}

// Run the main function
main();
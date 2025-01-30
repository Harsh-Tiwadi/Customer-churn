const dfd = require('danfojs-node');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});
const { spawnSync } = require('child_process');


async function promptInput(prompt, defaultValue) {
  return new Promise((resolve) => {
    readline.question(`${prompt} (default: ${defaultValue}): `, (input) => {
      resolve(input.trim() || defaultValue); // Trim whitespace and use default if empty
    });
  });
}

async function main() {
  const defaults = {
    gender: [1],
    under_30: [1],
    senior_citizen: [0],
    dependents: [0],
    married: [0],
    phone_service: [1],
    internet_service: [1],
    online_security: [0],
    online_backup: [0],
    device_protection: [0],
    premium_tech_support: [0],
    streaming_tv: [1],
    streaming_movies: [1],
    streaming_music: [1],
    internet_type: [1],
    contract: [1],
    paperless_billing: [1],
    payment_method: [3],
    avg_monthly_long_distance_charges: [12],
    total_charges: [234],
    total_long_distance_charges: [12],
    total_revenue: [2343],
    tenure: [1],
    multiple_lines: [0],
    avg_monthly_gb_download: [80],
    unlimited_data: [1],
    offer: [3],
    satisfaction_score: [3],
    cltv: [1800],
    extra_data_charges:[0],
    referrals: [1],
    monthly_charges: [35],
  };

  const useDefaults = await promptInput("Use default values for all inputs? (yes/no): ", "yes");

  let data = {};

  if (useDefaults.toLowerCase() === 'yes' || useDefaults === '') { //If user press enter or type yes
    data = defaults; // Use default values
    // Close the readline interface
    readline.close();
    console.log("Using default values.");
    // console.log("Data collected:", data);
  } else {
    console.log("Prompting for individual inputs.");
    data = { // Prompt for individual inputs
      gender: [parseInt( await promptInput('Enter your gender {"1":Male, "2":Female}: ', defaults.gender))],
      under_30: [parseInt( await promptInput('Is your age under_30 {"1":yes, "0":no}: ', defaults.under_30))],
      senior_citizen: [parseInt( await promptInput('Is your age above_65 {"1":yes, "0":no}: ', defaults.senior_citizen))],
      dependents: [parseInt( await promptInput('Any dependents {"1":yes, "0":no}: ', defaults.dependents))],
      married: [parseInt( await promptInput('married {"1":yes, "0":no}: ', defaults.married))],
      phone_service: [parseInt( await promptInput('using phone_service? {"1":yes, "0":no}: ', defaults.phone_service))],
      internet_service: [parseInt( await promptInput('using internet_service? {"1":yes, "0":no}: ', defaults.internet_service))],
      online_security: [parseInt( await promptInput('online_security {"1":yes, "0":no}: ', defaults.online_security))],
      online_backup: [parseInt( await promptInput('online_backup {"1":yes, "0":no}: ', defaults.online_backup))],
      device_protection: [parseInt( await promptInput('device_protection {"1":yes, "0":no}: ', defaults.device_protection))],
      premium_tech_support: [parseInt( await promptInput('premium_tech_support {"1":yes, "0":no}: ', defaults.premium_tech_support))],
      streaming_tv: [parseInt( await promptInput('streaming_tv {"1":yes, "0":no}: ', defaults.streaming_tv))],
      streaming_movies: [parseInt( await promptInput('streaming_movies {"1":yes, "0":no}: ', defaults.streaming_movies))],
      streaming_music: [parseInt( await promptInput('streaming_music {"1":yes, "0":no}: ', defaults.streaming_music))],
      internet_type: [parseInt( await promptInput('internet_type {"1": "Fiber Optic", "2": "DSL", "3": "Cable"}: ', defaults.internet_type))],
      contract: [parseInt( await promptInput('contract period {"1": "Month-Month", "2": "Two year", "3": "One year"}: ', defaults.contract))],
      paperless_billing: [parseInt( await promptInput('paperless_billing {"1":yes, "0":no}: ', defaults.paperless_billing))],
      payment_method: [parseInt( await promptInput('payment method {"1": "Electronic check", "2": "Mailed check", "3": "bank transfer(automatic)", "4": "credit card(automatic)"}: ', defaults.payment_method))],
      avg_monthly_long_distance_charges: [parseFloat( await promptInput('avg_monthly_long_distance_charges: ', defaults.avg_monthly_long_distance_charges))],
      total_charges: [parseFloat( await promptInput('total_charges: ', defaults.total_charges))],
      total_long_distance_charges: [parseFloat( await promptInput('total_long_distance_charges: ', defaults.total_long_distance_charges))],
      total_revenue: [parseFloat( await promptInput('total_revenue: ', defaults.total_revenue))],
      tenure: [parseFloat( await promptInput('tenure: ', defaults.tenure))],
      multiple_lines: [parseInt( await promptInput('multiple_lines {"1":yes, "0":no}: ', defaults.multiple_lines))],
      avg_monthly_gb_download: [parseFloat( await promptInput('avg_monthly_gb_download: ', defaults.avg_monthly_gb_download))],
      unlimited_data: [parseInt( await promptInput('unlimited_data {"1":yes, "0":no}: ', defaults.unlimited_data))],
      offer: [parseInt( await promptInput('offer {"1":offer B, "2":offer E, "3":offer D, "4":offer A, "5":offer C}: ', defaults.offer))],
      satisfaction_score: [parseInt( await promptInput('satisfaction_score {1,2,3,4,5}: ', defaults.satisfaction_score))],
      cltv: [parseFloat( await promptInput('cltv: ', defaults.cltv))],
      extra_data_charges: [parseInt( await promptInput('extra_data_charges {"1":yes, "0":no}: ', defaults.extra_data_charges))],
      referrals: [parseInt( await promptInput('referrals {"0":no, "1":less than 5 times, "2": more than 5 times}: ', defaults.referrals))],
      monthly_charges: [parseInt( await promptInput('monthly_charges: ', defaults.monthly_charges))],
    };
    // Close the readline interface
    readline.close();
  }

    console.log(data)

  // // Function to prompt user for input
  // function promptInput(question) {
    //     return new Promise((resolve) => {
        //         readline.question(question, (answer) => {
            //             resolve(answer);
            //         });
            //     });
            // }

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


    // Create a single-row DataFrame from the dictionary
    const df = new dfd.DataFrame(data);

    // Print the DataFrame
    console.log('\nSingle-Row DataFrame:');
    df.print();

    // Convert the DataFrame to JSON
    const jsonData = JSON.stringify(dfd.toJSON(df));

    // Send the JSON data to Python
    // const df_path = "data/model_data/test_data.csv"; // Path to your CSV file
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

    // store the value:
    response = JSON.parse(output.toString())
    churnValue = response.result
    console.log(typeof churnValue)

    // compare and return
    if (churnValue === 1) { // Correct comparison
        console.log('prediction: churned');
    } else if (churnValue === 0) {
    console.log('prediction: not churn');
    } else {
    console.log('Python script returned an unexpected value:', churnValue);
    }

};
// Run the main function
main();
// python();
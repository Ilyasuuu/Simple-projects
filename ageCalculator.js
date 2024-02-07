const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


function calculateAge(birthdate) {
    // Convert birthdate to Date object and get current date
    const birthDate = new Date(birthdate);
    const today = new Date();
    
    // Calculate age
    let age = today.getFullYear() - birthDate.getFullYear();
    
    // Adjust for case where this year's birthday has not occurred yet
    const monthDifference = today.getMonth() - birthDate.getMonth();
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    
    }
    
    return age;
}
// Example usage
rl.question('Please enter your birthdate (YYYY-MM-DD): ', (birthdate) => {
    console.log(`Your age is ${calculateAge(birthdate)}`);
    rl.close();
}); // 


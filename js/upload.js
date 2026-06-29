const fs = require('fs');

fs.readFile('tweets.json', 'utf8', (err, jsonString) => {
    if (err) {
        console.log("Error reading file:", err);
        return;
    }
    let data = JSON.parse(jsonString);

    console.log(data);  
});
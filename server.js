// Server. js
const express = require('express')
const app= express()
const port = 3000
//fs= file system
const fs = require('fs');
const {parse} = require("csv-parse");

// Serve static files:
const path = require('path')
app.use(express.static('public'))

// needed for post methods
app.use(express.urlencoded())

// needed for time stamp
const moment = require('moment');
// Read CSV file into an array
const data =[];

fs.createReadStream("public/data/people.csv")
  .pipe(parse({
  delimiter: ",",
  columns: true,
  ltrim: true }))
  .on("data", function (row) {
    data.push(row);
  })
  .on("error", function (error) {
    console.log(error.message);
  })
  .on("end", function () {
    console.log("finished");
  });

app.get('/', (req,res)=> {
    console.log(__dirname)
        res.sendFile(path.join(__dirname, 'public/RegisterForm.html'));
    });
     

    app.post('/addcsvuser', (req, res) => {
        let user = req.body;
        let IDExists = data.find((u) => u.name === user.name);
        let timestamp = moment().format('YYYY/MM/DD HH:mm:ss');
      
        if (!IDExists) {
          // User is being registered for the first time
          user.updated_at = timestamp;
          data.unshift(user); // Add user to the beginning of the data array
        } else {
          user.updated_at = timestamp;
          res.send(`Thank you for updating your profile ${IDExists.name}`);
          IDExists.sex = user.sex;
          IDExists.age = user.age;
          IDExists.body_type = user.body_type;
          IDExists.diet = user.diet;
          IDExists.drinks = user.drinks;
          IDExists.drugs = user.drugs;
          IDExists.height = user.height;
          IDExists.pets = user.pets;
          IDExists.religion = user.religion;
          IDExists.smokes = user.smokes;
          IDExists.preferred_min_age = user.preferred_min_age;
          IDExists.preferred_max_age = user.preferred_max_age;
          IDExists.preferred_body_type = user.preferred_body_type;
          IDExists.preferred_diet = user.preferred_diet;
          IDExists.preferred_drinks = user.preferred_drinks;
          IDExists.preferred_drugs = user.preferred_drugs;
          IDExists.preferred_height = user.preferred_height;
          IDExists.preferred_pets = user.preferred_pets;
          IDExists.preferred_religion = user.preferred_religion;
          IDExists.preferred_smokes = user.preferred_smokes;
      
          // Move the existing user's data to the beginning of the data array
          data.splice(data.indexOf(IDExists), 1);
          data.unshift(IDExists);
        }
      
        // Write to CSV file
        const csvString = `${Object.keys(data[0]).join(',')}\n${data
          .map((row) => Object.values(row).join(','))
          .join('\n')}`;
      
        fs.writeFile('public/data/people.csv', csvString, (err) => {
          if (err) {
            console.log('Error writing to CSV file:', err);
            res.send('Error writing to CSV file');
          } else {
            console.log('Data added to CSV file');
            res.send('User added: ' + JSON.stringify(user));
          }
        });
      });
      

    
app.listen(port, ()=> {
    console.log(`Example app listening at http://localhost:${port}`)
})

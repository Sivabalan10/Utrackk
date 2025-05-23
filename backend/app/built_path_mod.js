const path = require('node:path');
console.log(__filename);
console.log(__dirname);

console.log(path.basename(__filename));
console.log(path.extname(__filename))

console.log(path.parse(__filename));
console.log(path.join(__dirname, 'custom_modules', 'add.js'));
console.log(path.isAbsolute(__filename));
console.log(path.isAbsolute('./custom_modules/add.js'));
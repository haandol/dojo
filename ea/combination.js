const _ = require('lodash');

function generateCombinations(sidePosition) {
    const helper = (substring, path) => {
        if (path) res.add(path);
        if (!substring) return;

        for (const j of _.range(substring.length)) {
            helper(substring.slice(j+1), path+substring[j]);
        }
    };

    const res = new Set();
    helper(sidePosition, '');
    return res;
}

console.log(generateCombinations('DFFM'));
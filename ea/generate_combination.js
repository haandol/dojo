const _ = require('lodash');

function generateCombinations(sidePosition) {
  const helper = (s, i, path, res) => {
    if (i == s.length) return res.push(_.sortBy(path));

    helper(s, i+1, _.concat(path, s[i]), res);
    for (const j of _.range(0, path.length)) {
      helper(s, i+1, _.concat(_.slice(path, 0, j), path[j]+s[i], ..._.slice(path, j+1)), res);
    }
  };

  res = new Set();
  helper(sidePosition, 1, [sidePosition[0]], res)
  return _.sortBy(res);
}

console.log(generateCombinations('DDFM'));
const _ = require('lodash');

const AVAILABLE_POSITIONS = [
    'DFFM'      // 2 DF
];

function generatePotisions(playerPositions) {
    /**
        map = {
            'D': ['FFM', 'FMM', 'DFM'],
            'DD': ['FM'],
            'DDF': ['FM'],
            'DDFM': [],
            'DDM': ['FM'],
            'DF': ['FM', 'MM', 'DM'],
            'DFF': ['M'],
            'DFFM': [],
            'DFM': ['F', 'M', 'D'],
            'DFMM': [],
            'DM': ['FF', 'FM', 'DF'],
            'DMM': ['F'],
            'F': ['DFM', 'DMM', 'DDM'],
            'FF': ['DM'],
            'FM': ['DF', 'DM', 'DD'],
            'M': ['DF', 'DM', 'DD'],
            'MM': ['DF']
        };
    */
   result = _.clone(AVAILABLE_POSITIONS);
   for (const formation of playerPositions) {
       for (const i of _.range(0, result.length)) {
           if (!result[i]) break;

           if (-1 == _.indexOf(result[i], formation)) { 
               result[i] = null;
           } else {
               result[i] = result[i].replace(formation, '');
           }
       }
   }
   return _.filter(result, (formation) => { return formation; });
}

function helper(arr, r, path) {
    if (r == path.length) {
      console.log(path);
      return;
    }

  for (const i in _.range(0, arr.length)) {
    helper(_.slice(arr, i+1), r, _.concat(path, arr[i]));
  }
};

function combination(data, r) {
  for (const item of data) {
    helper(item.split(''), r, []);
  }
}


console.log(generatePotisions('D'));
console.log(combination(generatePotisions('D'), 3));
console.log(combination(generatePotisions('D'), 2));
console.log(combination(generatePotisions('D'), 1));
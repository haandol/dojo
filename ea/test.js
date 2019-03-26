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


function combination(s) {
  helper = (substring, path) => {
    if (0 === substring.length) {
      res.push(_.clone(path));
      return;
    }

    for (const length of _.range(1, substring.length+1)) {
      helper(substring.slice(length), _.concat(path, [substring.slice(0, length)]));
    }
  };

  const res = [];
  helper(s, []);
  return res;
}


console.log(generatePotisions('D'));
console.log(combination(generatePotisions('D')[0]));
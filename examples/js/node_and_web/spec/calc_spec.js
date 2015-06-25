var c = require('../calc');

describe("Calculator has a", function() {
    it("version", function() {
        expect(c.Calc.version).toEqual(0.01);
    });
});

describe("Calculator can", function() {
    it("add numbers", function() {
        expect(c.Calc.add(2, 7)).toEqual(9);
    });
    it("divide numbers", function() {
        expect(c.Calc.div(15, 3)).toEqual(5);
    });
});

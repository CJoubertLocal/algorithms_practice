import pytest
from karatsuba import karastuba_multiplication, not_able_to_convert_into_an_integer_exception


# Test cases from: https://github.com/beaunus/stanford-algs/tree/master/testCases/course1/assignment1Multiplication
class TestClass:
    def test_one(self):
        assert karastuba_multiplication(1, 2) == 2, "karatsuba multiplication fails on 1-digit multiplication"

    def test_two(self):
        assert karastuba_multiplication(10, 20) == 200, "karatsuba multiplication fails on 2-digit multiplication"

    def test_two1(self):
        assert karastuba_multiplication(10, 200) == 10*200, "karatsuba multiplication fails on 2-digit multiplication"
    
    def test_two2(self):
        assert karastuba_multiplication(100, 20) == 100*20, "karatsuba multiplication fails on 2-digit multiplication"
    
    def test_two3(self):
        assert karastuba_multiplication(100, 200) == 100*200, "karatsuba multiplication fails on 2-digit multiplication"
    
    def test_two4(self):
        assert karastuba_multiplication(100, 2000) == 100*2000, "karatsuba multiplication fails on 2-digit multiplication"
        
    def test_three(self):
        assert karastuba_multiplication(66729899957367990709339108031112, 32340867005124202389268050080611) == 2158102819786481370385134761940486771461182643704842409095969432, "karatsuba multiplication fails on 32-digit multiplication"
        
    def test_four(self):
        assert karastuba_multiplication(-10, 20) == -200, "karatsuba multiplication fails when the first integer is negative"
        
    def test_five(self):
        assert karastuba_multiplication(10, -20) == -200, "karatsuba multiplication fails when the second integer is negative"
        
    def test_six(self):
        assert karastuba_multiplication(-10, -20) == 200, "karatsuba multiplication fails both integers are negative"

    def test_seven(self):
        karastuba_multiplication(78624642046507710938888309775009441060368035479983368921194424236729498279818304768532971365125084366714124105458846627616155684, 57579173234021428356201222308669471930637687238795395560984306955384912395268850754122737444531250516797690870019557285179017458) == 4527141884858792569703012943690376879588033499441823212561236223396968611098565612973869852611827681292580539090160200871263453645942301937640563473106936130137478841069949884085208733024887924764700977723693142997968462661561226948749754204074730281931272, "karatsuba multiplication fails when multiplying two 128-digit integers"

    def test_eight(self):
        with pytest.raises(Exception) as not_able_to_convert_into_an_integer_exception:
            karastuba_multiplication("1a", 1)
    
    def test_nine(self):
        assert karastuba_multiplication(-1, 20) == -20, "karatsuba multiplication fails with a 1-digit negative number"

        
    def test_ten(self):
        assert karastuba_multiplication(10, -200) == -2000, "karatsuba multiplication fails with a 3-digit negative number"
    
    def test_eleven(self):
        assert karastuba_multiplication(1234, 1234) == 1234**2, "karatsuba multiplication fails when multiplying 1234 by itself"
    
    def test_twelve(self):
        assert karastuba_multiplication(7878064237045606, 7349065192669285) == 57896407670084570194037420411710, "karatsuba multiplication fails when multiplying positive 16-digit integers"
    
    def test_thirteen(self):
        assert karastuba_multiplication(90109928, 95084501) == 8568057539025928, "karatsuba multiplication fails when multiplying positive 8-digit integers"
        assert karastuba_multiplication(1234, 5678) == 1234*5678, "karatsuba multiplication fails when multiplying positive 8-digit integers"
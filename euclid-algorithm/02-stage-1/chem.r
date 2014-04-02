 : : 0 in A1, A1p, B1, B1p, begin01
beginModule01 1		: M01FN00 3 	: 1000 	Go signal for module 1 function 0
 : : 0
 : : 0 MODULE 01 FUNCTION 00
M01FN00 4			: M01FN00 3		: 1000 limit growth of M01FN00
M01FN00 1 A1 1 B1 1 		: B1pp 1 M01FN00 1	: 1000 Make B1pp using up A1 and B1
M01FN00 1 B1ab 1 A1s 1 		: B1ab 1 M01FN00 1	: 1000 Destroy A1s if both A1 and B1 are not zero
B1ab 1 A1sab 1 M01FN00 1	: B1ab 1 A1sab 1	: 1000 END FUNCTION M01FN00
B1ab 1 A1sab 1 			: M01FN01 3 B1ab 1 A1sab 1	: 1 CALL FUNCTION M01FN01
 : : 0
 : : 0 MODULE 01 FUNCTION 01 store A1s changed value in A1s
M01FN01 4			: M01FN01 3		: 1000 limit growth of M01FN01
M01FN01 1 B1pp 1		: B1 1 M01FN01 1	: 1000 change B1pp to B1
M01FN01 1 A1 1 			: A1pp 1 A1s 1 M01FN01 1: 1000 copy A1 to A1s
A1ab 1 B1ppab 1 M01FN01 1	: A1ab 1 B1ppab 1	: 1000 END FUNCTION M01FN01
A1ab 1 B1ppab 1 		: M01FN02 3 A1ab 1 B1ppab 1	: 1 CALL FUNCTION M01FN02
 : : 0
 : : 0 MODULE 01 FUNCTION 02 Restore A1 to origninal value (the value held by A1p)
M01FN02 4			: M01FN02 3		: 1000 limit growth of M01FN01
M01FN02 1 A1pp 1		: A1 1 M01FN02 1	: 1000 copy
A1ppab 1 M01FN02 1		: A1ppab 1		: 1000 END FUNCTION M01FN02
A1ppab 1			: M01FN00 3		: 1 CALL FUCTION M01FN00
 : : 0
 : : 0 BEGIN ABSENCE INDICATORS
: A1ab 1 : 1
A1ab 2 : A1ab 1 : 1000
A1 1 A1ab 1 : A1 1: 10000
: A1sab 1 : 1
A1sab 2 : A1sab 1 : 1000
A1s 1 A1sab 1 : A1s 1: 1000000
: A1ppab 1 : 1
A1ppab 2 : A1ppab 1 : 1000
A1pp 1 A1ppab 1 : A1pp 1: 1000000
: B1ab 1 : 1
B1ab 2 : B1ab 1 : 1000
B1 1 B1ab 1 : B1 1: 10000000
: B1ppab 1 : 1
B1ppab 2 : B1ppab 1 : 1000
B1pp 1 B1ppab 1 : B1pp 1: 10000

/*
:name: function_void_return
:description: void function return value test
:should_fail: 1
:tags: 13.4.1
*/
module top();

function void add(int a, int b);
	$display("%d+%d=", a, b);
	return a + b;
endfunction

initial
	$display("%d", add(45, 90));

endmodule
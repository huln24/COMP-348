
compile-main:
	clang main_q3.c aggregate.c -o build/main_q3
	clang main_q4.c aggregate.c -o build/main_q4
	clang linked_list.c -o build/linked_list
	clang main_q7.c aggregate.c -o build/main_q7

run-main:
	./build/main_q3
	./build/main_q4
	./build/main_q7

bnr: compile-main run-main


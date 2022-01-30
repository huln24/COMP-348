
compile-main:
	clang main.c aggregate.c -o build/main
	clang main1.c aggregate.c -o build/main1
	clang linked_list.c -o build/linked_list

run-main:
	./build/main
	./build/main1

bnr: compile-main run-main


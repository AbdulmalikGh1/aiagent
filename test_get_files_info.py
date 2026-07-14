from functions.get_files_info import get_files_info



def print_result(title: str, result: str, indent: str = "  ") -> None:
	print(title)
	for line in result.splitlines():
		print(f"{indent}{line}")


print_result("Result for current directory:", get_files_info("calculator", "."))
print_result("Result for 'pkg' directory:", get_files_info("calculator", "pkg"))
print_result("Result for '/bin' directory:", get_files_info("calculator", "/bin"), indent="    ")
print_result("Result for '../' directory:", get_files_info("calculator", "../"), indent="    ")
from functions.get_file_content import get_file_content


def print_result(title: str, result: str) -> None:
	print(title)
	print(result)


result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

print_result(
	"Result for 'main.py' file:",
	get_file_content("calculator", "main.py"),
)

print_result(
	"Result for 'pkg/calculator.py' file:",
	get_file_content("calculator", "pkg/calculator.py"),
)

print_result(
	"Result for '/bin/cat' file:",
	get_file_content("calculator", "/bin/cat"),
)

print_result(
	"Result for 'pkg/does_not_exist.py' file:",
	get_file_content("calculator", "pkg/does_not_exist.py"),
)

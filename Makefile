#запускать из корня
build:
	uv build

#запускать из корня
install:
	uv sync
	
#запускать из корня
package-install:
	uv tool install dist/*.whl
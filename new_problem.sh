if [ $# -eq 0 ]; then
    >&2 echo "No arguments provided"
    exit 1
fi

mkdir "$1"
cd "$1"
touch "$1.py"
touch input
code .

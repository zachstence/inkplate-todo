$port = $args[0]

if (!$port) {
    Write-Error "Missing port"
    exit 1
}

# Run main.py on the Inkplate
python .\Inkplate-micropython\pyboard.py --device $port .\inkplate-todo\main.py

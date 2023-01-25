$port = $args[0]

if (!$port) {
    Write-Error "Missing port"
    exit 1
}

function Upload {
    param (
        [bool]$Retry = $true
    )

    try {
        Push-Location .\inkplate-todo
        
        python ..\Inkplate-micropython\pyboard.py --device $port -f cp main.py :main.py
        python ..\Inkplate-micropython\pyboard.py --device $port -f mkdir secret
        python ..\Inkplate-micropython\pyboard.py --device $port -f cp secret/network.json :secret/network.json
        
    } finally {
        Pop-Location
    }

    $IsRetryable = $output -contains "could not enter raw repl"
    if ($IsRetryable -and $Retry) {
        Copy-Lib-Files -Retry $false
    } else {
        Write-Output $output
    }
}


#####


Upload

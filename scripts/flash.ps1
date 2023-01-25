$port = $args[0]

if (!$port) {
    Write-Error "Missing port"
    exit 1
}

function Write-Banner {
    param (
        [string]$Content
    )

    Write-Output ""
    Write-Output "##############################"
    Write-Output "# $Content"
    Write-Output "##############################"
}

function Clear-Flash {
    Write-Banner -Content "Erasing flash"
    esptool.py --port $port erase_flash 
}

function Write-Flash {
    Write-Banner -Content "Writing firmware to flash"
    esptool.py --chip esp32 --port $port write_flash -z 0x1000 .\Inkplate-micropython\esp32spiram-20220117-v1.18.bin
}

function Copy-Lib-Files {
    param (
        [bool]$Retry = $true
    )

    if ($Retry) {
        Write-Banner -Content "Copying library files"
    }

    try {
        Push-Location .\Inkplate-micropython
        
        $output = python pyboard.py --device $port -f cp `
            inkplate6_COLOR.py                 `
            gfx.py                             `
            gfx_standard_font_01.py            `
            PCAL6416A.py                       `
            image.py                           `
            shapes.py                          `
            :
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


##########


Clear-Flash
Write-Flash
Copy-Lib-Files

Write-Output "`nDone!"
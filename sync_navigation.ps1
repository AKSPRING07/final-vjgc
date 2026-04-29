# Master Synchronization Script for VJS Website Navigation
# Source of Truth: index-2.html

$sourcePath = "c:\Users\Admin\vjs-website-\public\index-2.html"
$targetDir = "c:\Users\Admin\vjs-website-\public"

if (-not (Test-Path $sourcePath)) {
    Write-Error "Source file $sourcePath not found."
    exit
}

$sourceContent = Get-Content $sourcePath -Raw

# 1. Extract the Master Header
$headerRegex = '(?si)<header.*?</header>'
$headerMatch = [regex]::Match($sourceContent, $headerRegex)
if (-not $headerMatch.Success) {
    Write-Error "Could not find <header> block in source."
    exit
}
$masterHeader = $headerMatch.Value

# 2. Extract the Sustainability JS injection (at the bottom)
$jsRegex = '(?si)<script src="js/mega-dropdown.js"></script>'
$jsMatch = [regex]::Match($sourceContent, $jsRegex)
$masterJS = if ($jsMatch.Success) { $jsMatch.Value } else { '<script src="js/mega-dropdown.js"></script>' }

# 3. Get all HTML files
$htmlFiles = Get-ChildItem -Path $targetDir -Filter "*.html"

foreach ($file in $htmlFiles) {
    # Skip some files if necessary, but generally we want all
    $content = Get-Content $file.FullName -Raw
    $modified = $false

    # A. Inject CSS links if missing
    if ($content -notlike "*navbar-vjs.css*") {
        $content = $content -replace '</head>', "`t<link rel=`"stylesheet`" type=`"text/css`" href=`"css/navbar-vjs.css`" media=`"all`">`n</head>"
        $modified = $true
    }
    if ($content -notlike "*custom.css*") {
        $content = $content -replace '</head>', "`t<link rel=`"stylesheet`" type=`"text/css`" href=`"css/custom.css`" media=`"all`">`n</head>"
        $modified = $true
    }

    # B. Replace Header
    if ($content -match $headerRegex) {
        $content = [regex]::Replace($content, $headerRegex, $masterHeader)
        $modified = $true
    }

    # C. Inject JS if missing (before </body>)
    if ($content -notlike "*mega-dropdown.js*") {
        $content = $content -replace '</body>', "`t$masterJS`n</body>"
        $modified = $true
    }

    if ($modified) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Synchronized: $($file.Name)"
    }
}

Write-Host "Master Synchronization Complete."

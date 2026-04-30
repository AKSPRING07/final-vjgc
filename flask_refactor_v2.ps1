# flask_refactor_v2.ps1
$templateDir = "c:\Users\Admin\vjs-website-\templates"

$assetDirs = @("css", "js", "images", "fonts", "videos", "vendor", "webfonts")
# Handle both single and double quotes
$assetRegex = "(href|src)=['`"]((?:$(($assetDirs -join "|")))/[^'`"]+)['`"]"

$htmlFiles = Get-ChildItem -Path $templateDir -Filter "*.html"

foreach ($file in $htmlFiles) {
    Write-Host "Refactoring $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # 1. Update Asset Links
    $newContent = [regex]::Replace($content, $assetRegex, {
        param($m)
        $attr = $m.Groups[1].Value
        $path = $m.Groups[2].Value
        # Remove existing url_for if present to avoid double wrapping
        if ($path -like "*url_for*") { return $m.Value }
        return "$attr=`"{{ url_for('static', filename='$path') }}?v=1.1`""
    })
    
    # 2. Update Internal Page Links
    $pageRegex = "href=['`"]((?![#|http|https|mailto|tel])[^'`"]+\.html)['`"]"
    $newContent = [regex]::Replace($newContent, $pageRegex, {
        param($m)
        $page = $m.Groups[1].Value
        if ($page -like "*url_for*") { return $m.Value }
        
        # Special case for index-2.html -> home
        if ($page -eq "index-2.html" -or $page -eq "index.html") {
            return "href=`"{{ url_for('home') }}?v=1.1`""
        }
        return "href=`"{{ url_for('catch_all', filename='$page') }}?v=1.1`""
    })

    Set-Content $file.FullName $newContent -NoNewline
}

Write-Host "Flask refactoring v2 complete."

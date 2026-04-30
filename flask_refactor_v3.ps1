# flask_refactor_v3.ps1
$templateDir = "c:\Users\Admin\vjs-website-\templates"

$htmlFiles = Get-ChildItem -Path $templateDir -Filter "*.html"

foreach ($file in $htmlFiles) {
    Write-Host "Aggressive Refactoring $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # 1. Assets (href/src/content)
    $assetDirs = @("css", "js", "images", "fonts", "videos", "vendor", "webfonts")
    $dirsPattern = ($assetDirs -join "|")
    
    # Target: attr="dir/path" or attr='dir/path'
    $assetRegex = "(href|src|content|data-src)=(['`"])($dirsPattern)/([^'`"]+)(['`"])"
    $content = [regex]::Replace($content, $assetRegex, {
        param($m)
        $attr = $m.Groups[1].Value
        $quote = $m.Groups[2].Value
        $dir = $m.Groups[3].Value
        $path = $m.Groups[4].Value
        if ($path -like "*url_for*") { return $m.Value }
        return "$attr=$quote{{ url_for('static', filename='$dir/$path') }}?v=1.2$quote"
    })
    
    # 2. Pages (href="page.html")
    $pageRegex = "href=(['`"])((?![#|http|https|mailto|tel])[^'`"]+\.html)(['`"])"
    $content = [regex]::Replace($content, $pageRegex, {
        param($m)
        $quote = $m.Groups[1].Value
        $page = $m.Groups[2].Value
        if ($page -like "*url_for*") { return $m.Value }
        
        if ($page -eq "index-2.html" -or $page -eq "index.html") {
            return "href=$quote{{ url_for('home') }}?v=1.2$quote"
        }
        return "href=$quote{{ url_for('catch_all', filename='$page') }}?v=1.2$quote"
    })

    Set-Content $file.FullName $content -NoNewline
}

Write-Host "Flask refactoring v3 complete."

# flask_refactor_v5.ps1
$templateDir = "c:\Users\Admin\vjs-website-\templates"
$htmlFiles = Get-ChildItem -Path $templateDir -Filter "*.html"

foreach ($file in $htmlFiles) {
    Write-Host "Refactoring $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # 1. Page links - match href="anypage.html" or href='anypage.html'
    # Use a broader regex
    $pageRegex = "href=(['`"])([^'`"]+?\.html)(['`"])"
    $content = [regex]::Replace($content, $pageRegex, {
        param($m)
        $quote = $m.Groups[1].Value
        $page = $m.Groups[2].Value
        
        # Skip if already refactored
        if ($page -like "*url_for*") { return $m.Value }
        # Skip external
        if ($page -like "http*" -or $page -like "//*" -or $page -like "#*") { return $m.Value }
        
        if ($page -eq "index-2.html" -or $page -eq "index.html") {
            return "href=$quote{{ url_for('home') }}$quote"
        }
        return "href=$quote{{ url_for('catch_all', filename='$page') }}$quote"
    })
    
    # 2. Asset links - more aggressive
    $assetRegex = "(href|src|content|data-src)=(['`"])(css|js|images|fonts|videos|vendor|webfonts)/([^'`"]+?)(['`"])"
    $content = [regex]::Replace($content, $assetRegex, {
        param($m)
        $attr = $m.Groups[1].Value
        $quote = $m.Groups[2].Value
        $dir = $m.Groups[3].Value
        $path = $m.Groups[4].Value
        if ($path -like "*url_for*") { return $m.Value }
        return "$attr=$quote{{ url_for('static', filename='$dir/$path') }}$quote"
    })

    Set-Content $file.FullName $content -NoNewline
}

Write-Host "Flask refactoring v5 complete."

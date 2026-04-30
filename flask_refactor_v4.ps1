# flask_refactor_v4.ps1
$templateDir = "c:\Users\Admin\vjs-website-\templates"
$htmlFiles = Get-ChildItem -Path $templateDir -Filter "*.html"

$assetDirs = @("css", "js", "images", "fonts", "videos", "vendor", "webfonts")

foreach ($file in $htmlFiles) {
    Write-Host "Refactoring $($file.Name)..."
    $content = Get-Content $file.FullName -Raw
    
    # 1. Assets
    foreach ($dir in $assetDirs) {
        # Replace href="dir/ and href='dir/
        $content = $content -replace "href=(['`"])$dir/", "href=$1{{ url_for('static', filename='$dir/') }}"
        $content = $content -replace "src=(['`"])$dir/", "src=$1{{ url_for('static', filename='$dir/') }}"
        $content = $content -replace "content=(['`"])$dir/", "content=$1{{ url_for('static', filename='$dir/') }}"
        $content = $content -replace "data-src=(['`"])$dir/", "data-src=$1{{ url_for('static', filename='$dir/') }}"
    }
    
    # 2. Fix the closing quotes for static url_for
    # We need to find the next quote and close the url_for
    # This is hard with -replace if it's not a regex.
    
    # Let's use a better regex for assets
    $assetRegex = "(href|src|content|data-src)=(['`"])((?:css|js|images|fonts|videos|vendor|webfonts)/[^'`"]+)(['`"])"
    $content = [regex]::Replace($content, $assetRegex, {
        param($m)
        $attr = $m.Groups[1].Value
        $quote = $m.Groups[2].Value
        $path = $m.Groups[3].Value
        if ($path -like "*url_for*") { return $m.Value }
        return "$attr=$quote{{ url_for('static', filename='$path') }}$quote"
    })

    # 3. Pages
    $pageRegex = "href=(['`"])((?![#|http|https|mailto|tel|/])[^'`"]+\.html)(['`"])"
    $content = [regex]::Replace($content, $pageRegex, {
        param($m)
        $quote = $m.Groups[1].Value
        $page = $m.Groups[2].Value
        if ($page -like "*url_for*") { return $m.Value }
        
        if ($page -eq "index-2.html" -or $page -eq "index.html") {
            return "href=$quote{{ url_for('home') }}$quote"
        }
        return "href=$quote{{ url_for('catch_all', filename='$page') }}$quote"
    })

    Set-Content $file.FullName $content -NoNewline
}

Write-Host "Flask refactoring v4 complete."

$templatesDir = "templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html" -Recurse

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    
    # Replace {{ url_for('catch_all', filename='page.html') }} with {{ url_for('dynamic_route', path='page') }}
    # Also handle single quotes and double quotes
    $newContent = $content -replace '\{\{\s*url_for\s*\(\s*''catch_all''\s*,\s*filename\s*=\s*''([^'']+)\.html''\s*\)\s*\}\}', '{{ url_for(''dynamic_route'', path=''$1'') }}'
    $newContent = $newContent -replace '\{\{\s*url_for\s*\(\s*"catch_all"\s*,\s*filename\s*=\s*"([^"]+)\.html"\s*\)\s*\}\}', '{{ url_for("dynamic_route", path="$1") }}'
    
    if ($content -ne $newContent) {
        $newContent | Set-Content -Path $file.FullName -Encoding UTF8
        Write-Host "Updated links in $($file.Name)"
    }
}

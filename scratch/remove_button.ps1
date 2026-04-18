$path = Get-ChildItem -Path "public/*.html"
foreach ($file in $path) {
    Write-Host "Processing $($file.FullName)"
    $content = Get-Content $file.FullName -Raw
    
    # Remove Mobile "Get in Touch" li
    $newContent = [regex]::Replace($content, '(?s)<li class="d-md-none[^>]*>.*?Get in Touch.*?</li>', '')

    # Remove Desktop "right-widget" containing "Get in Touch"
    $newContent = [regex]::Replace($newContent, '(?s)<div class="right-widget[^>]*>.*?Get in Touch.*?</div>\s*<!--/\.right-widget-->', '')

    if ($content -ne $newContent) {
        $newContent | Set-Content $file.FullName
        Write-Host "Updated $($file.Name)"
    }
}

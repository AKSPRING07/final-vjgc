$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

foreach ($file in $files) {
    Write-Host "Processing $($file.Name)..."
    try {
        # Read file as Windows-1252 (which handles 0x97, 0x93 etc)
        $content = Get-Content -Path $file.FullName -Encoding Default
        # Save as UTF-8 without BOM
        [System.IO.File]::WriteAllLines($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
    } catch {
        Write-Error "Failed to process $($file.Name): $($_.Exception.Message)"
    }
}
Write-Host "All templates converted to UTF-8."

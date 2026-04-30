$templatesDir = "c:\Users\Admin\vjs-website-\templates"
$files = Get-ChildItem -Path $templatesDir -Filter "*.html"

foreach ($file in $files) {
    $content = [System.IO.File]::ReadAllText($file.FullName)
    
    # Matches background-image: url('images/...') or url(images/...)
    # and converts them to background-image: url('{{ url_for('static', filename='images/...') }}')
    $regex = 'background-image:\s*url\(([''"]?)(images/.*?)\1\)'
    
    if ($content -match $regex) {
        Write-Host "Fixing image paths in $($file.Name)..."
        $newContent = [System.Text.RegularExpressions.Regex]::Replace($content, $regex, {
            param($match)
            $path = $match.Groups[2].Value
            return "background-image: url('{{ url_for(''static'', filename=''$path'') }}')"
        })
        
        $newContent = $newContent.Replace("''", "'")
        [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding($false)))
    }
}

Write-Host "Global image path fix complete."

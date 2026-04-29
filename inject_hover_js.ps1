
$publicPath = "$PSScriptRoot\public"
$scriptTag = "`n`t`t<!-- Navbar Hover Animation -->`n`t`t<script src=`"js/navbar-hover.js`"></script>"
$themeJs = '<script src="js/theme.js"></script>'

# For all pages EXCEPT index-2.html — inject after theme.js
$files = Get-ChildItem -Path "$publicPath\*.html" | Where-Object { $_.Name -ne 'index-2.html' }

$count = 0
foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    
    # Only inject if not already there
    if ($content -notmatch 'navbar-hover\.js') {
        if ($content -match [regex]::Escape($themeJs)) {
            $content = $content.Replace($themeJs, $themeJs + $scriptTag)
            [System.IO.File]::WriteAllText($f.FullName, $content, [System.Text.Encoding]::UTF8)
            Write-Host "Injected: $($f.Name)"
            $count++
        } else {
            Write-Host "No theme.js found: $($f.Name)"
        }
    } else {
        Write-Host "Already has it: $($f.Name)"
    }
}

Write-Host ""
Write-Host "==================================="
Write-Host "Done! Injected into $count pages"
Write-Host "==================================="
